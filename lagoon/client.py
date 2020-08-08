import json
import socket
import logging
import os

from lagoon import exceptions
from lagoon.utils import is_socket_closed

logger = logging.getLogger(__name__)


class LagoonClient:

    MAX_ID = 2 << 16
    BUFF = 4096

    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self._host, self._port))
        self._rpc_id = 1

    def reconnect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self._host, self._port))

    def _invoke(self, id_value, method_name, *params):
        payload = {
            "jsonrpc": "2.0",
            "id": id_value % self.MAX_ID,
            "method": method_name,
            "params": list(params),
        }
        str_data = json.dumps(payload) + "\n"
        self.sock.send(str_data.encode("utf-8"))

    def _recieve(self):
        data = self.sock.recv(self.BUFF)
        str_data = data.decode("utf-8")
        result = json.loads(str_data[:-1])
        if "error" in result:
            raise exceptions.JSONRPCException(
                result["error"]["message"], result["error"]["code"]
            )
        return result["result"]

    def invoke(self, id_value, method_name, *params):
        if is_socket_closed(self.sock):
            self.reconnect()
        self._invoke(id_value, method_name, *params)

    def recieve(self):
        if is_socket_closed(self.sock):
            self.reconnect()
        return self._recieve()

    def create_collection(self, collection_name: str) -> bool:
        """
        Returns bool
        :param collection_name: name of the collection to create
        """
        self.invoke(self._rpc_id, "createCollection", collection_name)
        data = self.recieve()
        self._rpc_id += 1
        return data

    def has_key(self, collection: str, key: str) -> bool:
        """
        Returns bool
        :param collection: name of the collection
        :param key: name of the key to check if exist
        """
        self.invoke(self._rpc_id, "hasKey", collection, key)
        data = self.recieve()
        self._rpc_id += 1
        return data

    def set_key(self, collection: str, key: str) -> bool:
        """
        Returns bool
        :param collection: name of the collection
        :param key: name of the key to set
        """
        self.invoke(self._rpc_id, "setKey", collection, key)
        data = self.recieve()
        self._rpc_id += 1
        return data

    def delete_collection(self, collection_name: str) -> bool:
        """
        Returns bool
        :param collection: name of the collection to delete
        """
        self.invoke(self._rpc_id, "deleteCollection", collection_name)
        data = self.recieve()
        self._rpc_id += 1
        return data