import logging

from pyramid.view import (view_defaults, view_config)
from pyramid.httpexceptions import HTTPForbidden
from pyramid.response import Response
from bitcoinaddress import Address, Key

from . import HTTPStatus
from ..interfaces import WalletInterface
from ..exceptions.handlerExceptions import *

log = logging.getLogger(__name__)

@view_defaults(renderer='json', accept='Application/json')
class WalletView():

    def __init__(self, request):
        self.request = request

    @view_config(route_name='createWallet', request_method='POST')
    def create_wallet(self):

        if self.request.authenticated_userid is None:
            raise HTTPForbidden()

        log.info('into create_wallet view')
        rs_fail = dict(status=HTTPStatus.OK, message="You only cant get 10 btc wallets")

        user_id = self.request.jwt_claims['sub']['id']

        sl = self.request.find_service(WalletInterface)
        wallet_rs = sl.generate_wallet(user_id)

        
        return Response(json_body=wallet_rs or rs_fail, status=HTTPStatus.OK)


    @view_config(route_name='getWallets', request_method='GET')
    def get_wallets(self):
        if self.request.authenticated_userid is None:
            raise HTTPForbidden()

        log.info('into get wallets views')
        rs_fail = 'At the moment you\'ve not created any wallet'
        user_id = self.request.jwt_claims['sub']['id']

        sl = self.request.find_service(WalletInterface)
        wallet_rs = sl.get_wallets(user_id)
        
        return Response(json_body={'status':HTTPStatus.OK, 'message': wallet_rs or rs_fail}, status=HTTPStatus.OK)
