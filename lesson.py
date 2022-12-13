import itertools
class Lesson():
    instance_id = itertools.count()
    def __init__(self, date, courseid):
        self.id = 'L' + str(next(self.instance_id))
        self.date = date
        self.courseid = courseid
        return