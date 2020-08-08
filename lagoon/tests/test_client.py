import os
import sys

import lagoon


try:
    from unittest.case import TestCase
except ImportError:
    from unittest import TestCase


def connect_debug():
    try:
        host = os.environ["LAGOON_HOST"]
        port = int(os.environ["LAGOON_PORT"])
    except KeyError:
        print(
            "To run the tests the LAGOON_HOST and LAGOON_PORT variables "
            "need to be available. \n"
            "Please create a pull request if you are an external "
            "contributor, because these variables are automatically added "
            "by Travis."
        )
        sys.exit(1)

    return lagoon.connect(host, port)


client = connect_debug()


class ClientTest(TestCase):
    def setUp(self):
        client.create_collection("collection1")
        client.set_key("collection1", "key1")

    def test_collection_create(self):
        result = client.create_collection("collection2")
        self.assertEqual(result, True)

    def test_key_not_exist(self):
        result = client.has_key("collection1", "key2")
        self.assertEqual(result, False)

    def test_key_exist(self):
        result = client.has_key("collection1", "key1")
        self.assertEqual(result, True)

    def test_delete_collection(self):
        result = client.delete_collection("collection2")
        self.assertEqual(result, True)

    def tearDown(self):
        client.delete_collection("collection1")