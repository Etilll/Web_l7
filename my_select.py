
from seed import Base, session, Mark, Student, Subject, Teacher, Group
from sqlalchemy import desc, func


def select_1():
    print(f"\033[92m{'-'*20} REQUEST 1\033[0m\n")
    print(session.query(func.avg(Mark.value).label('average'), Student.name).join(Student).group_by(Student.id).order_by(desc('average')).limit(5))
    print(f"\033[92m{'-'*20} REQUEST 1 END\033[0m\n")

def select_2():
    print(f"\033[92m{'-'*20} REQUEST 2\033[0m\n")
    print(session.query(func.avg(Mark.value).label('average'), Student.name, Subject.name.label('Subject')).join(Student).join(Subject).where(Mark.subject_id == 4).group_by(Student.id, Subject.name).order_by(desc('average')).limit(1))
    print(f"\033[92m{'-'*20} REQUEST 2 END\033[0m\n")

def select_3():
    print(f"\033[92m{'-'*20} REQUEST 3\033[0m\n")
    print(session.query(func.avg(Mark.value).label('average'), Subject.name.label('Subject'), Student.group_id.label('Group')).join(Student).join(Subject).where(Mark.subject_id == 4).group_by(Student.group_id, Subject.name).order_by(desc('average')))
    print(f"\033[92m{'-'*20} REQUEST 3 END\033[0m\n")

def select_4():
    print(f"\033[92m{'-'*20} REQUEST 4\033[0m\n")
    print(session.query(func.avg(Mark.value).label('average')))
    print(f"\033[92m{'-'*20} REQUEST 4 END\033[0m\n")

def select_5():
    print(f"\033[92m{'-'*20} REQUEST 5\033[0m\n")
    print(session.query(Subject.name.label('Subject')).where(Subject.teacher_id == 5))
    print(f"\033[92m{'-'*20} REQUEST 5 END\033[0m\n")

def select_6():
    print(f"\033[92m{'-'*20} REQUEST 6\033[0m\n")
    print(session.query(Student.name.label('Student')).where(Student.group_id == 2))
    print(f"\033[92m{'-'*20} REQUEST 6 END\033[0m\n")

def select_7():
    print(f"\033[92m{'-'*20} REQUEST 7\033[0m\n")
    print(session.query(Mark.value.label('Marks'), Student.group_id.label('Group')).join(Student).where(Mark.subject_id == 4, Student.group_id == 3).group_by(Student.group_id, Mark.value))
    print(f"\033[92m{'-'*20} REQUEST 7 END\033[0m\n")

def select_8():
    print(f"\033[92m{'-'*20} REQUEST 8\033[0m\n")
    print(session.query(func.avg(Mark.value).label('average'), Subject.name.label('Subject')).join(Subject).where(Subject.teacher_id == 2).group_by(Subject.teacher_id, Subject.name).order_by(desc('average')))
    print(f"\033[92m{'-'*20} REQUEST 8 END\033[0m\n")

def select_9():
    print(f"\033[92m{'-'*20} REQUEST 9\033[0m\n")
    print(session.query(Mark.student_id.label('Student'), Subject.name.label('Subject')).join(Subject).where(Mark.student_id == 5).group_by(Subject.name, Mark.student_id))
    print(f"\033[92m{'-'*20} REQUEST 9 END\033[0m\n")

def select_10():
    print(f"\033[92m{'-'*20} REQUEST 10\033[0m\n")
    print(session.query(Mark.student_id.label('Student'), Subject.id, Subject.teacher_id, Subject.name.label('Subject')).select_from(Mark).join(Subject).where(Mark.student_id == 5, Subject.teacher_id == 5).group_by(Subject.name, Subject.id, Mark.student_id, Subject.teacher_id))
    print(f"\033[92m{'-'*20} REQUEST 10 END\033[0m\n")

    
if __name__ == '__main__':
    select_1()
    select_2()
    select_3()
    select_4()
    select_5()
    select_6()
    select_7()
    select_8()
    select_9()
    select_10()
