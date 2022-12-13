import itertools
class Attendace():
    instance_id = itertools.count()
    def __init__(self, lessonid, studentid):
        self.id = 'A' + str(next(self.instance_id))
        self.lessonid = lessonid
        self.studentid = studentid
