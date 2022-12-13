import itertools
class Course():
    instance_id = itertools.count()
    def __init__(self, name, teacherid, description, start_date, end_date, total_lesson_count):
        self.id = 'C' + str(next(self.instance_id))
        self.name = name
        self.teacherid = teacherid
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.total_lesson_count = total_lesson_count

    