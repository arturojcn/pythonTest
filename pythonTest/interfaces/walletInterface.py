from zope.interface import Interface

class WalletInterface(Interface):
    def generate_wallet(user_id):
        pass
    def get_wallet(user_id, address):
        pass