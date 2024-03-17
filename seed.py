from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, desc, func
from random import randint
from faker.providers import job


engine = create_engine("postgresql+psycopg2://postgres:92192834@localhost/postgres")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(50))
    age = Column(Integer())
    gender = Column(String(20))
    group_id = Column(Integer(), ForeignKey('groups.id'))
    #articles = relationship('Article', back_populates='author')

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(50))
    age = Column(Integer())
    gender = Column(String(20))

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(255))
    #author = relationship('User', back_populates='articles')

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(255))
    teacher_id = Column(Integer(), ForeignKey('teachers.id'))

class Mark(Base):
    __tablename__ = 'marks'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    value = Column(Integer())
    student_id = Column(Integer(), ForeignKey('students.id'))
    subject_id = Column(Integer(), ForeignKey('subjects.id'))
    created_at = Column(DateTime, default=func.now())

def set_skeleton():
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine   

def fill_base():
    from faker import Faker
    fake = Faker()
    for i in range(3):
        record = Group(name=f'Group {i + 1}')
        session.add(record)
        session.commit()

    students = randint(30,50)
    for i in range(students):
        record = Student(name=fake.name(), age=randint(17,54), gender='binary', group_id=randint(1,3))
        session.add(record)
        session.commit()

    teachers = randint(3,5)
    for i in range(teachers):
        record = Teacher(name=fake.name(), age=randint(25,90), gender='binary')
        session.add(record)
        session.commit()
        
    subjects = randint(5,8)
    for i in range(subjects):
        fake.add_provider(job)
        record = Subject(name=fake.job(), teacher_id=randint(1, teachers))
        session.add(record)
        session.commit()

    for curr_stud in range(1, students + 1):
        for i in range(randint(1,20)):
            record = Mark(value=randint(1,12), student_id=curr_stud, subject_id=randint(1, subjects))
            session.add(record)
            session.commit()

def select_1():
    print(session.query(func.avg(Mark.value).label('average'), Student.name).join(Student).group_by(Student.id).order_by(desc('average')).limit(5))

def select_2():
    print(session.query(func.avg(Mark.value).label('average'), Student.name, Subject.name.label('Subject')).join(Student).join(Subject).where(Mark.subject_id == 4).group_by(Student.id, Subject.name).order_by(desc('average')).limit(1))

def select_3():
    print(session.query(func.avg(Mark.value).label('average'), Subject.name.label('Subject'), Student.group_id.label('Group')).join(Student).join(Subject).where(Mark.subject_id == 4).group_by(Student.group_id, Subject.name).order_by(desc('average')))

def select_4():
    print(session.query(func.avg(Mark.value).label('average')))

def select_5():
    print(session.query(Subject.name.label('Subject')).where(Subject.teacher_id == 5))

def select_6():
    print(session.query(Student.name.label('Student')).where(Student.group_id == 2))

def select_7():
    print(session.query(Mark.value.label('Marks'), Student.group_id.label('Group')).join(Student).where(Mark.subject_id == 4, Student.group_id == 3).group_by(Student.group_id, Mark.value))

def select_8():
    print(session.query(func.avg(Mark.value).label('average'), Subject.name.label('Subject')).join(Subject).where(Subject.teacher_id == 2).group_by(Subject.teacher_id, Subject.name).order_by(desc('average')))

def select_9():
    print(session.query(Mark.student_id.label('Student'), Subject.name.label('Subject')).join(Subject).where(Mark.student_id == 5).group_by(Subject.name, Mark.student_id))

def select_10():
    print(session.query(Mark.student_id.label('Student'), Subject.id, Subject.teacher_id, Subject.name.label('Subject')).select_from(Mark).join(Subject).where(Mark.student_id == 5, Subject.teacher_id == 5).group_by(Subject.name, Subject.id, Mark.student_id, Subject.teacher_id))


if __name__ == '__main__':
    set_skeleton()
    fill_base()