import random
import string
class User:
    """
    Class that generates new instances of users
    """
    userslist=[]
    def __init__(self,firstname,lastname,username,password):
        """
        __init__ method that helps us define properties for our objectsself.
        
        """
        self.firstname=firstname
        self.lastname=lastname
        self.username=username
        self.password=password
    def save_user(self):
            """
            save_user method saves user info into user userslist
            """
            User.userslist.append(self)  
        
    def delete_user(self):
        """
        delete_user method deletes a saved user from the userslist
        """
        User.userslist.remove(self)
    @classmethod
    def display_users(cls):
        """
        method that returns  info from the userlist
        """
        return cls.userslist       
                