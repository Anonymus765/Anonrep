from student import Student

import datetime
date = datetime.date.today().year

stud1 = Student(name='Pasha', birth=2011)

print(f' - Student №1 - \n{stud1}')
print(Student.get_age(stud1))