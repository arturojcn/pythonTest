from pyramid.view import (view_config, view_defaults)

from pyramid.response import Response

from sqlalchemy.exc import DBAPIError

from http import HTTPStatus
from ..models import models

from ..interfaces.userInterface import UserInterface

import logging

log = logging.getLogger(__name__)

@view_defaults(accept='application/json', renderer='json')
class UserView():

    def __init__(self, request):
        self.request = request

    @view_config(route_name='home', request_method='POST')
    def my_view(self):
        msg = 'you need to sign in'
        if self.request.authenticated_userid:
            msg = 'Welcome to the btc wallet'
        

        return Response(json_body={'status': HTTPStatus.OK, 'message': msg})


    @view_config(route_name='signup', request_method='POST')
    def signup(self):
        user = self.request.json_body

        sl = self.request.find_service(UserInterface)
        new_user = sl.save_user(user)

        return Response(json_body=new_user, content_type='application/json', status=HTTPStatus.CREATED)


    @view_config(route_name='login', request_method='POST', renderer='json')
    def login(self):
        log.info('Into login view')
        data_rs = dict(status=HTTPStatus.OK)
        user = self.request.json_body

        sl = self.request.find_service(UserInterface)
        user_rs = sl.get_user(user)

        if user_rs:
            data_rs['token'] = self.request.create_jwt_token(dict(id=user_rs['id']), 180)
        else:
            data_rs['errorMessage'] = 'Credentials wasn\'t wrong, please check it and try again!'

        return Response(json_body=data_rs)