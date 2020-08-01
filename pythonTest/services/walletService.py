import logging, pip._vendor.requests as requests

from bitcoinaddress import Address, Key
from ..models.models import Wallet

log = logging.getLogger(__name__)
WALLET_BY_USERS = 10
BTC_SATOSHI = 100000000
class WalletService():

    def __init__(self, dbsession):
        self.dbsession = dbsession
    
    def generate_wallet(self, user_id):
        log.info('generating wallet')

        quantity = self.dbsession.query(Wallet).filter(Wallet.user_id == user_id).count()
        log.debug("quantity of wallets %s to user_id %d" %(quantity, user_id))
        if quantity < WALLET_BY_USERS:
            key = Key()
            key_dict = key.generate()

            address = Address(key)
            address_dict = address.generate()

            new_wallet = Wallet(_hex=key_dict['hex'], wif=key_dict['wif'], wifc=key_dict['wifc'], 
                pubkey=address_dict['pubkey'], pubkeyc=address_dict['pubkeyc'], pubaddr1=address_dict['pubaddr1'], 
                pubaddr3=address_dict['pubaddr3'], pubaddrbc1_p2wsh=address_dict['pubaddrbc1_p2wsh'], pubaddrbc1_p2wpkh=address_dict['pubaddrbc1_p2wpkh'],
                user_id=user_id, status=True)
            self.dbsession.add(new_wallet)
            
            return new_wallet.get_dic()
    
    def get_wallets(self, user_id):
        log.info('getting wallets')
        result =[]
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
        rate = float(r['bpi'].get('USD').get('rate').replace(',',''))
        log.debug(rate)
        
        for wallet in self.dbsession.query(Wallet).filter(Wallet.user_id==user_id).all():
            w = Wallet.get_dic(wallet)
            w['satoshis'] = w['balances'] * BTC_SATOSHI
            w['usd'] = w['balances'] * rate
            result.append(w)
        log.debug(result)
        
        return result



