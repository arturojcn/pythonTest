from zope.interface import Interface

class UserInterface(Interface):
    def get_user(user):
        pass
    def save_user(user):
        pass