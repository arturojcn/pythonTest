from http import HTTPStatus

class UserExistException(Exception):
    def __init__(self, msg):
        self.data = dict(status=HTTPStatus.OK, msg=msg)