from pyramid.config import Configurator

from pyramid.authorization import ACLAuthorizationPolicy

from .interfaces import (UserInterface, WalletInterface)
from .services import (UserService, WalletService)

def user_factory(context, request):
    dbsession = request.dbsession
    svc = UserService(dbsession)
    return svc

def wallet_factory(context, request):
    dbsession = request.dbsession
    svc = WalletService(dbsession)
    return svc

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('.models')
    config.include('.routes')
    config.include('pyramid_services')
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.include('pyramid_jwt')    
    config.set_jwt_authentication_policy('$2b$12$NJ/nSM2JPCQDqPyImbiiaOMAeXmZ4/uGEFNVNI5GTw1oX4j/41GLm', auth_type='Bearer')

    config.register_service_factory(user_factory, UserInterface)
    config.register_service_factory(wallet_factory, WalletInterface)

    
    config.scan()
    return config.make_wsgi_app()
