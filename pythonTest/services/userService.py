import logging

from ..exceptions.handlerExceptions import UserExistException
from ..interfaces.userInterface import UserInterface
from ..models.models import User
from ..utils.security import (hash_password, check_password)


log = logging.getLogger(__name__)

class UserService(object):

    def __init__(self, dbsession):
        self.dbsession = dbsession

    def get_user(self, user):
        log.info('Into get_user method')
        user_entity = self.dbsession.query(User).filter(User.email == user['email']).first()
        if user_entity:
            user_dic = User.get_dic(user_entity)

            if check_password(user['password'], user_dic['password']):
                return user_dic
         

    def save_user(self, user):
        log.info('into save_user method')

        user_validate = self.dbsession.query(User).filter(User.email==user['email']).first()

        if user_validate:
            raise UserExistException("Email %s already exist"%(user['email']))
        
        pwd = hash_password(user['password'])
        new_user = User(document=user['document'], name=user['name'], last_name=user['last_name'], email=user['email'], password=pwd, status=True)
        
        del user['password']
        self.dbsession.add(new_user)

        return user