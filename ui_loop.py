import sqlite3
from member import Member
from teacher import Teacher

class UI():

    def __init__(self):
        self.active_user = None

    def login_page(self):
        member = Member()
        username = input('Username: ')
        while (member.user_syntax_auth(username)):
            username = input('Username: ')

        password = input('Password: ')
        while (member.password_syntax_auth(password)):
            password = input('Password: ')
        return member.get_teacher_id()

    def sign_in(self):

        return
    
    def main_page():
        return
    def prompt():
        return



if __name__ == "__main__":
    ui = UI()
    ui.login_page()
