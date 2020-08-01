import logging

from pyramid.view import (view_defaults, view_config)
from pyramid.response import Response

from . import HTTPStatus
log = logging.getLogger(__name__)


@view_defaults(accept='application/json', renderer='json')
class TransactionView():

    def __init__(self, request):
        self.request = request

    @view_config(route_name='transation', request_method='POST')
    def transaction(self):
        pass
    
    @view_config(route_name='getTransations', request_method='GET')
    def get_transactions(self):
        pass

    @view_config(route_name='getTransactionsByAddress', request_method='GET')
    def get_transactions_by_addres(self):
        return Response(json_body={'status':HTTPStatus.OK, 'message':'asdsad'})
