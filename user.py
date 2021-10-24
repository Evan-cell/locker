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