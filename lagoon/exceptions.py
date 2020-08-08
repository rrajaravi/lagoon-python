class LagoonApiException(Exception):
    def __init__(self, error_message, status_code=None):
        Exception.__init__(self, error_message)
        self.detail = error_message
        if status_code is not None:
            self.status_code = status_code

    code = 1

    def __repr__(self):
        return "%s (%s)" % (self.__class__.__name__, self.detail)

    def __unicode__(self):
        return "%s (%s)" % (self.__class__.__name__, self.detail)


class JSONRPCException(LagoonApiException):
    def __init__(self, error_message, status_code):
        self.error_message = error_message
        self.status_code = status_code
        super(JSONRPCException, self).__init__(error_message)
