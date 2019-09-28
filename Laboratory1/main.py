from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel
from cassandra.query import SimpleStatement

cl = Cluster()
session = cl.connect('workspace')

# 9 insert
s = """	insert into student JSON '{"university": "KPI", "faculty": "FPM", "group": "KM-61", "student_id": 1, 
"student_data": {"name":"eugene", "surname": "patrushev", "second_name": "null", "birthday": "1999-01-20"}, "data_enrollment": "2016-06-01", 
"count_of_study_students": 3}';"""
session.execute(s, (), ConsistencyLevel.TWO)

s = """insert into Student JSON '{"university": "KPI", "faculty": "FPM", "group": "KM-61", "student_id": 2, 
"student_data": {"name": "vova", "surname": "pasko", "second_name": "null", "birthday": "1999-04-13"}, "data_enrollment": "2016-06-01", 
"count_of_study_students": 3}';"""
session.execute(s, (), ConsistencyLevel.THREE)

s = """insert into Student JSON '{"university": "KPI", "faculty": "FPM", "group": "KM-62", "student_id": 3, 
"student_data": {"name": "denis", "surname": "vradii", "second_name": "null", "birthday": "1999-05-02"}, "data_enrollment": "2017-06-01", 
"count_of_study_students": 3}'"""
session.execute(s, (), ConsistencyLevel.ALL)

s = "SELECT * from Student;"
print('student table: ')
for row in session.execute(s):
	print('name', row.student_data.name, '; surname', row.student_data.surname, '; birthday', row.student_data.birthday)
print()

s = """
insert into Discipline 
JSON '{"university": "KPI", "faculty": "FPM", "discipline_name": "DB", "hours_for_semester": 120, "exam": "true"}';"""
session.execute(s, (), ConsistencyLevel.TWO)

s = """
insert into Discipline
JSON '{"university": "KPI", "faculty": "FPM", "discipline_name": "ML", "hours_for_semester": 100, "exam": "false"}';"""
session.execute(s, (), ConsistencyLevel.THREE)


s = """
insert into Discipline
JSON '{"university": "KPI", "faculty": "FPM", "discipline_name": "English1", "hours_for_semester": 60, "exam": "false"}';"""
session.execute(s, (), ConsistencyLevel.ALL)


s = "SELECT * from Discipline;"
print('Discipline table: ')
for row in session.execute(s):
	print('name', row.discipline_name, '; hours_for_semester', row.hours_for_semester, '; exam', row.exam)
print()

s = """
insert into Professor 
JSON '{"university": "KPI", "department": "FPM", "professor_id": 1, "professor_data": {"name":"Volodimir", "surname": "Malchikov", "second_name": "null", "birthday": "1967-01-01"}, "data_enrollment": "1994-06-01"}';"""
session.execute(s, (), ConsistencyLevel.TWO)

s = """
insert into Professor 
JSON '{"university": "KPI", "department": "FPM", "professor_id": 2, "professor_data": {"name":"Lilia", "surname": "Vovk", "second_name": "null", "birthday": "1975-01-01"}, "data_enrollment": "1999-06-01"}';"""
session.execute(s, (), ConsistencyLevel.THREE)

s = """
insert into Professor 
JSON '{"university": "KPI", "department": "ISAS", "professor_id": 4, "professor_data": {"name":"Anastasia", "surname": "Adamuk", "second_name": "null", "birthday": "1990-01-01"}, "data_enrollment": "2014-06-01"}';"""
session.execute(s, (), ConsistencyLevel.ALL)

s = "SELECT * from Professor;"
print('Professor table: ')
for row in session.execute(s):
	print('name', row.professor_data.name, '; surname', row.professor_data.surname, '; birthday', row.professor_data.birthday)
print()


s = """
insert into Student_record_book
JSON '{"university": "KPI", "faculty": "FPM", "group": "KM-61", "student_id": 1, "discipline_name": "English1", "professor_data": {"professor_id": 4, "department": "ISAS"}, "semester_mark": 45,  "final_mark": 75, "data_passed": "2019-12-16"}'"""
session.execute(s, (), ConsistencyLevel.ALL)

s = """
insert into Professor_record_book_index
JSON '{"university": "KPI", "department": "ISAS", "professor_id": 4, "year": 2019, "semester": 1, "marks": [{"discipline_name": "English1", "student_id": 1, "semester_mark": 45, "final_mark": 75}]}';"""
session.execute(s, (), ConsistencyLevel.ALL)



# 3 update
s = """
update Student
set student_data = {name:'eugene',
					surname: 'patrushev', 
					second_name: 'Vladislavovich', 
					birthday: '1999-01-20'}
where university = 'KPI' and faculty='FPM' and group = 'KM-61' and student_id = 1
"""
session.execute(s, (), ConsistencyLevel.TWO)

print('student')
for row in session.execute("select * from Student;"):
	print(row)
print()

s = """
update Professor
set count_of_professors_work = 2
where university = 'KPI' and department = 'FPM'
"""
session.execute(s, (), ConsistencyLevel.ALL)

print('professor')
for row in session.execute("select * from Professor;"):
	print(row)
print()

s = """
update Discipline
set hours_for_semester = 125
where university = 'KPI' and faculty='FPM' and discipline_name = 'DB'
"""
session.execute(s, (), ConsistencyLevel.ONE)

print("Discipline")
for row in session.execute("select * from Discipline;"):
	print(row)
print()

# 4 select

s = """
Select professor_data, discipline_name, final_mark from student_record_book where student_id = 1 
and group = 'KM-61' and university = 'KPI' and faculty = 'FPM'
"""
print('student_record_book')
for row in session.execute(s, (), ConsistencyLevel.ONE):
	print(row.professor_data, row.discipline_name, row.final_mark)
print()


s = """
Select marks from Professor_record_book_index where university = 'KPI' and professor_id = 4 and 
department = 'ISAS' and semester = 1 and year = 2019
"""
print('Professor_record_book_index')
for row in session.execute(s, (), ConsistencyLevel.ONE):
	print(row.marks)
print()


s = """
Select professor_data.surname from Professor where university = 'KPI' and department = 'FPM' 
and professor_id = 1;
"""
print('Professor')
for row in session.execute(s, (), ConsistencyLevel.TWO):
	print(row[0])
print()

s = """
Select student_data.surname from Student where university = 'KPI' and group = 'KM-61' 
and faculty = 'FPM'
"""
print('Student')
for row in session.execute(s, (), ConsistencyLevel.ALL):
	print(row[0])
print()

# 3 delete


s = "delete from Student where university = 'KPI' and faculty = 'FPM' and group = 'KM-61' and student_id = 1"
session.execute(s)
s = "delete from Student where university = 'KPI' and faculty = 'FPM' and group = 'KM-61' and student_id = 2"
session.execute(s)
s = "delete from Student where university = 'KPI' and faculty = 'FPM' and group = 'KM-61' and student_id = 3"
session.execute(s)

s = "delete from Professor where university = 'KPI' and department = 'FPM' and professor_id = 1"
session.execute(s)
s = "delete from Professor where university = 'KPI' and department = 'FPM' and professor_id = 2"
session.execute(s)
s = "delete from Professor where university = 'KPI' and department = 'FPM' and professor_id = 3"
session.execute(s)

s = "delete from Discipline where university = 'KPI' and faculty = 'FPM' and discipline_name = 'ML'"
session.execute(s)
s = "delete from Discipline where university = 'KPI' and faculty = 'FPM' and discipline_name = 'DB'"
session.execute(s)
s = "delete from Discipline where university = 'KPI' and faculty = 'FPM' and discipline_name = 'English1'"
session.execute(s)

session.execute("TRUNCATE Student_record_book")
session.execute("TRUNCATE Professor_record_book_index")
