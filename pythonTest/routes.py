def includeme(config):
    config.add_route('home', '/')

    config.add_route('signup', '/api/v01/user/signup')
    config.add_route('login', '/api/v01/user/signin')

    config.add_route('createWallet', '/api/v01/wallet')
    config.add_route('getWallets', '/api/v01/wallets')
    config.add_route('getWallet', '/api/v01/wallet/{address}')

    config.add_route('transation',  '/api/v01/transation/{address}')
    config.add_route('getTransations', '/api/v01/transations')
    config.add_route('getTransactionsByAddress', '/api/v01/wallets/{address}/transactions')
    