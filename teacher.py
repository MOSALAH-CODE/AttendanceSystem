from course import Course
import itertools

class Teacher():
    instance_id = itertools.count()
    def __init__(self, firstname, lastname, tc):
        self.id = 'T' + str(next(self.instance_id))
        self.firstname = firstname
        self.lastname = lastname
        self.tc = tc
        self.course_list = {}
    def input_attr(self):

        firstname = input('Enter your first name: ')
        lastname = input('Enter your last name: ')
        tc = input('Enter your tc: ')
        while len(tc) != 13 or tc.isdigit() is not True:
            tc = input('Enter your tc: ')
    def init_course(self, name, description):
        new_course = Course(name, id, description)
        self.course_list[new_course.id] = new_course

