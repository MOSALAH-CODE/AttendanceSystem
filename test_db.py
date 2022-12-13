import sqlite3
from teacher import Teacher
conn = sqlite3.connect(':memory:')
c = conn.cursor()

class DatabaseManager():

    def __init__(self):
        # self.conn = sqlite3.connect(':memory:')
        # self.c = self.conn.cursor()
        return
    def insert_into(self, table_name: str, value_dict : dict):
        value_placeholder = '('
        for count, key in enumerate(value_dict):
            if count < len(value_dict) - 1:
                value_placeholder = value_placeholder + ':' + key + ','
            else:
                value_placeholder = value_placeholder + ':' + key + ')'
        query_string = 'INSERT INTO ' + table_name + ' VALUES' + value_placeholder
        
        c.execute(query_string, value_dict)
        return c.fetchall()

def create_login_table():
    with conn:
        c.execute('''CREATE TABLE IF NOT EXISTS member_login 
                        (username TEXT NOT NULL, 
                        password TEXT NOT NULL, 
                        userID TEXT NOT NULL,
                        CONSTRAINT login_pk PRIMARY KEY (username))''')
def insert_login_table(username, password, userID):
    with conn:
        c.execute('''INSERT INTO member_login VALUES
                            (:username, 
                            :password, 
                            :userID)''', 
                            {'username': username, 
                            'password': password, 
                            'userID': userID})
def get_teacher_id(username, password):
    c.execute('''SELECT userID FROM member_login
                WHERE username=:username 
                AND password=:password''',
                {'username': username,
                'password': password})
    return c.fetchall()

def create_teacher_table():
    with conn:
        c.execute('''CREATE TABLE IF NOT EXISTS teacher 
                        (id TEXT NOT NULL,
                        firstname TEXT NOT NULL, 
                        lastname TEXT NOT NULL, 
                        tc TEXT NOT NULL,
                        CONSTRAINT teacher_pk PRIMARY KEY (id))''')
def insert_teacher_table(teacher: Teacher):
    with conn:
        c.execute('''INSERT INTO teacher VALUES
                            (:id, 
                            :firstname, 
                            :lastname,
                            :tc)''', 
                            {'id': teacher.id, 
                            'firstname': teacher.firstname, 
                            'lastname': teacher.lastname,
                            'tc': teacher.tc})
def get_teacher_from_login(userID):
    c.execute('''SELECT * FROM teacher
                WHERE id=:userID''',
                {'userID': userID})
    return c.fetchall()
def get_all_teachers():
    c.execute('''SELECT * FROM teacher''')
    return c.fetchall()


def create_course_table():
    with conn:
        c.execute('''CREATE TABLE IF NOT EXISTS course 
                        (id TEXT NOT NULL, 
                        name TEXT NOT NULL, 
                        teacherid TEXT NOT NULL, 
                        description TEXT,
                        start_date DATE NOT NULL,
                        end_date DATE NOT NULL,
                        CONSTRAINT course_pk PRIMARY KEY (id))''')
def insert_course_table(course):
    with conn:
        c.execute('''INSERT INTO course VALUES
                            (:id, 
                            :name, 
                            :teacherid,
                            :description,
                            :start_date,
                            :end_date)''', 
                            {'id': course.id, 
                            'name': course.name,
                            'teacherid': course.teacherid, 
                            'description': course.description,
                            'start_date': course.start_date,
                            'end_date': course.end_date})
def get_course_teacher(teacherid):
    c.execute('''SELECT * FROM course 
                WHERE teacherid=:teacherid''', 
                {'teacherid': teacherid})
    return c.fetchall()

def create_student_table():
    with conn:
        c.execute('''CREATE TABLE IF NOT EXISTS student 
                        (id TEXT NOT NULL, 
                        firstname TEXT NOT NULL, 
                        lastname TEXT NOT NULL, 
                        studentid TEXT NOT NULL,
                        tc TEXT NOT NULL,
                        CONSTRAINT student_pk PRIMARY KEY (id))''')
def insert_student_table(student):
    with conn:
        c.execute('''INSERT INTO student VALUES
                            (:id, 
                            :firstname, 
                            :lastname,
                            :studentid,
                            :tc)''', 
                            {'id': student.id, 
                            'firstname': student.firstname,
                            'lastname': student.lastname, 
                            'studentid': student.studentid,
                            'tc': student.tc})
def get_student_from_tc(tc):
    c.execute('''SELECT * FROM student 
                WHERE tc=:tc''', 
                {'tc': tc})
    return c.fetchall()

def create_lesson_table():
    with conn:
        c.execute('''CREATE TABLE IF NOT EXISTS lesson
                        (id TEXT NOT NULL, 
                        date DATE NOT NULL, 
                        courseid TEXT NOT NULL,
                        CONSTRAINT lesson_pk PRIMARY KEY (id), 
                        CONSTRAINT lesson_course_fk FOREIGN KEY(courseid)
                            REFERENCES course(id))''')
def insert_lesson_table(lesson):
    with conn:
        c.execute('''INSERT INTO lesson VALUES
                            (:id, 
                            :date, 
                            :courseid)''', 
                            {'id': lesson.id, 
                            'date': lesson.date,
                            'courseid': lesson.courseid})


def create_attendance_table():
    with conn:
        c.execute('''CREATE TABLE IF NOT EXISTS attendance
                        (id TEXT NOT NULL, 
                        lessonid TEXT NOT NULL, 
                        studentid TEXT NOT NULL,
                        CONSTRAINT attendance_pk PRIMARY KEY (id),
                        CONSTRAINT attendance_lesson_fk FOREIGN KEY(lessonid)
                            REFERENCES lesson(id),
                        CONSTRAINT attendance_student_fk FOREIGN KEY(studentid)
                            REFERENCES student(id))''')
def insert_attendance_table(attendance):
    with conn:
        c.execute('''INSERT INTO lesson VALUES
                            (:id, 
                            :lessonid, 
                            :studentid)''', 
                            {'id': attendance.id, 
                            'lessonid': attendance.lessonid,
                            'studentid': attendance.studentid})
def get_attendances_from_lesson(lessonid):
    c.execute('''SELECT * FROM attendance 
                WHERE lessonid=:lessonid''', 
                {'lessonid': lessonid})
    return c.fetchall()

create_login_table()
create_teacher_table()
create_course_table()
create_lesson_table()
create_student_table()
create_attendance_table()

insert_login_table('ali', 'lol','T099')
print(get_teacher_id('ali', 'lol'))
t = Teacher('teacher1', 'teacher1lastname','999513255')
t2 = Teacher('teacher2', 'teacher2lastname','999513343435')
insert_teacher_table(t)
insert_teacher_table(t2)
print(get_all_teachers())
t3 = Teacher('something', 'sfsfs', 'sfsfsfs')
db = DatabaseManager()
print(db.insert_into('teacher', vars(t3)))
conn.close()
