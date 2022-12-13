import itertools
class Student():
    instance_id = itertools.count()
    def __init__(self, firstname, lastname, student_id, tc):
        self.id = 'S' + str(next(self.instance_id))
        self.firstname = firstname
        self.lastname = lastname
        self.student_id = student_id
        self.tc = tc
        self.course_list = {}
    def add_course(self, course):
        self.course_list[course.id] = course
