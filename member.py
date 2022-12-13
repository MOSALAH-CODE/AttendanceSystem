class Member():
    def __init__(self):
        self.username = None
        self.password = None

    def user_syntax_auth(self, username):
        excluded_character_list = [' ']
        if len(username) > 8 and len(username) < 32:
            print('Length')
            return False
        for char in excluded_character_list:
            if char in username:
                print('Excluded')
                return False
        print('Accepted')
        self.username = username
        return True
    def password_syntax_auth(self, password):
        excluded_character_list = [' ']
        if len(password) > 8 and len(password) < 32:
            print('Length')
            return False
        for char in excluded_character_list:
            if char in password:
                print('Excluded')
                return False
        print('Accepted')
        self.username = password
        return True
    def get_teacher_id(self, c):
        c.execute('''SELECT userID FROM member_login
                    WHERE username=:username 
                    AND password=:password''',
                    {'username': self.username,
                    'password': self.password})
        return c.fetchall()


