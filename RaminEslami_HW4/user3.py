import uuid, hashlib
from extra3 import save, get_object, delete


class User:
    def __init__(self, username: str, password: str, phone_number: str = None, id: str = None) -> None:
        """
        this is initializer for User class
        :param username: input username
        :param password: input password
        :param phone_number: input phone number
        :param id: generated auto id
        """
        if id is None:
            self.id = str(uuid.uuid4())
        else:
            self.id = id
        self.username = username
        self.phone_number = phone_number
        self.__password = password

    @staticmethod
    def validate_pass(password: str) -> None:
        """
        this method validate password
        :param password: password for check
        :return: None if password was correct. or rais error if not valid
        """
        if len(password) == 0:
            raise ValueError('\n--- your password was empty! you must set password ---\n')
        elif len(password) < 4:
            raise ValueError('\n--- The length of the password must be more than 4 characters! ---\n')
        return None

    @staticmethod
    def validate_username(username: str) -> None:
        if len(username) == 0:
            raise ValueError('\n--- your username was empty! you must set password ---\n')
        return None

    @staticmethod
    def build_pass(password: str) -> str:
        password = password.encode()
        p_hash = hashlib.sha256()
        p_hash.update(password)
        password = p_hash.hexdigest()
        return password

    @classmethod
    def authenticated(cls, username: str) -> object | None:
        user = get_object(username)
        if user is not None:
            user = cls(user['username'], user['_User__password'], user['phone_number'])
            return user
        else:
            return None

    @classmethod
    def create_user(cls, username: str, password: str, phone_number:str =None, id:str =None) -> None:

        if User.validate_pass(password):
            return cls.validate_pass(password)
        elif User.validate_username(username):
            return cls.validate_username(username)
        elif User.authenticated(username) is None:
            password = cls.build_pass(password)
            user = User(username, password, phone_number, id)
            save(vars(user))
        else:
            raise ValueError('\n--- Registration failed , This username already exist! ---\n')

    @classmethod
    def login(cls, username: str, password: str) -> object:
        hashed_password = cls.build_pass(password)
        user = User.authenticated(username)
        if user:
            if user._User__password == hashed_password:
                return user
            else:
                raise ValueError('--- incorrect password ---')
        else:
            raise ValueError(f" --- There is no account with this username : {username} ---\n"
                             f" --- Please register and try again. ---")

    @classmethod
    def change_info(cls, username: str, new_username: str, new_phone_number: str) -> object:
        if cls.validate_username(new_username):
            return cls.validate_username(new_username)
        user = get_object(username)
        delete(username)
        user = cls(new_username, user['_User__password'], new_phone_number, user['id'])
        save(vars(user))
        return user

    def change_password(self, old: str, new: str, confirm_new: str) -> object:
        old = self.build_pass(old)
        if old == self._User__password:
            if self.match_pass(new, confirm_new):
                if self.validate_pass(new) is None:
                    new = self.build_pass(new)
                    delete(self.username)
                    user = User(self.username, new, self.phone_number, self.id)
                    save(vars(user))
                    return user
                return self.validate_pass(new)
            else:
                raise ValueError('--- new password and confirm password not mach ---')
        else:
            raise ValueError('--- your old is invalid ---')

    @staticmethod
    def match_pass(p1: str, p2: str) -> bool:
        if p1 == p2:
            return True
        return False

    def __str__(self) -> str:
        id, username, phone_number = self.id, self.username, self.phone_number
        return f'\nid = {id}\n' \
               f'username = {username}\n' \
               f'phone_number = {phone_number}'


