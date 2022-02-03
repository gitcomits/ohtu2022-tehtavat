from entities.user import User
import re
import sys, pdb

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass

class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
    #    if len(username) < 3:
    #        raise AuthenticationError("Username 3 sign minimum")

    #    if not re.match("^[a-z]+$", username):
    #        raise AuthenticationError("Username contains invalid characters")
    
    
        if len(username) >= 3:
            if re.match("!^[a-z]+$", username):
                raise AuthenticationError("Username contains invalid characters")
        else:
            raise AuthenticationError("Username 3 sign minimum")
        
        if username == self._user_repository.find_by_username(username):
            raise AuthenticationError("Username already taken")
#        pdb.Pdb(stdout=sys.__stdout__).set_trace()
        if len(password) >=8:
            if re.match("!^[a-z]", password):
                raise AuthenticationError("Password can contain only letters")
        else:
            raise AuthenticationError("Password length atleast 8")
        
        #    raise AuthenticationError("Password length atleast 8")
        return["Registration OK"]
         
