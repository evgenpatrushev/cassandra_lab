insert into student 
JSON '{"university": "KPI", "faculty": "FPM", "group": "KM-61", "student_id": 1, "student_data": {"name":"eugene", "surname": "patrushev", "second_name": "null", "birthday": "1999-01-20"}, "data_enrollment": "2016-06-01", "count_of_study_students": 3}';

insert into Student
JSON '{"university": "KPI", "faculty": "FPM", "group": "KM-61", "student_id": 2, "student_data": {"name": "vova", "surname": "pasko", "second_name": "null", "birthday": "1999-04-13"}, "data_enrollment": "2016-06-01", "count_of_study_students": 3}';

insert into Student
JSON '{"university": "KPI", "faculty": "FPM", "group": "KM-62", "student_id": 3, "student_data": {"name": "denis", "surname": "vradii", "second_name": "null", "birthday": "1999-05-02"}, "data_enrollment": "2017-06-01", "count_of_study_students": 3}';

SELECT * from Student;

insert into Discipline 
JSON '{"university": "KPI", "faculty": "FPM", "discipline_name": "DB", "hours_for_semester": 120, "exam": "true"}';

insert into Discipline
JSON '{"university": "KPI", "faculty": "FPM", "discipline_name": "ML", "hours_for_semester": 100, "exam": "false"}';

insert into Discipline
JSON '{"university": "KPI", "faculty": "FPM", "discipline_name": "English1", "hours_for_semester": 60, "exam": "false"}';

SELECT * from Discipline;

insert into Professor 
JSON '{"university": "KPI", "department": "FPM", "professor_id": 1, "professor_data": {"name":"Volodimir", "surname": "Malchikov", "second_name": "null", "birthday": "1967-01-01"}, "data_enrollment": "1994-06-01"}';

insert into Professor 
JSON '{"university": "KPI", "department": "FPM", "professor_id": 2, "professor_data": {"name":"Lilia", "surname": "Vovk", "second_name": "null", "birthday": "1975-01-01"}, "data_enrollment": "1999-06-01"}';

insert into Professor 
JSON '{"university": "KPI", "department": "ISAS", "professor_id": 4, "professor_data": {"name":"Anastasia", "surname": "Adamuk", "second_name": "null", "birthday": "1990-01-01"}, "data_enrollment": "2014-06-01"}';

SELECT * from Professor;

insert into Student_record_book
JSON '{"university": "KPI", "faculty": "FPM", "group": "KM-61", "student_id": 1, "discipline_name": "English1", "professor_data": {"professor_id": 4, "department": "ISAS"}, "semester_mark": 45,  "final_mark": 75, "data_passed": "2019-12-16"}'

insert into Professor_record_book_index
JSON '{"university": "KPI", "department": "ISAS", "professor_id": 4, "year": 2019, "semester": 1, "marks": [{"discipline_name": "English1", "student_id": 1, "semester_mark": 45, "final_mark": 75}]}';


update Student
set student_data = {name:'eugene',
					surname: 'patrushev', 
					second_name: 'Vladislavovich', 
					birthday: '1999-01-20'}
where university = 'KPI' and faculty='FPM' and group = 'KM-61' and student_id = 1;

select * from Student;

update Professor
set count_of_professors_work = 2
where university = 'KPI' and department = 'FPM';

select * from Professor;

update Discipline
set hours_for_semester = 125
where university = 'KPI' and faculty='FPM' and discipline_name = 'DB';

select * from Discipline;


Select professor_data, discipline_name, final_mark from student_record_book where student_id = 1 
and group = 'KM-61' and university = 'KPI' and faculty = 'FPM' ;

Select marks from Professor_record_book_index where university = 'KPI' and professor_id = 4 and 
department = 'ISAS' and semester = 1 and year = 2019;

Select professor_data.surname from Professor where university = 'KPI' and department = 'FPM' 
and professor_id = 1;

Select student_data.surname from Student where university = 'KPI' and group = 'KM-61' 
and faculty = 'FPM';


delete from Student
where university = 'KPI' and faculty = 'FPM' and group = 'KM-61' and student_id = 1;
delete from Student
where university = 'KPI' and faculty = 'FPM' and group = 'KM-61' and student_id = 2;
delete from Student
where university = 'KPI' and faculty = 'FPM' and group = 'KM-61' and student_id = 3;

delete from Professor
where university = 'KPI' and department = 'FPM' and professor_id = 1;
delete from Professor
where university = 'KPI' and department = 'FPM' and professor_id = 2;
delete from Professor
where university = 'KPI' and department = 'FPM' and professor_id = 4;

delete from Discipline
where university = 'KPI' and faculty = 'FPM' and discipline_name = 'ML';
delete from Discipline
where university = 'KPI' and faculty = 'FPM' and discipline_name = 'DB';
delete from Discipline
where university = 'KPI' and faculty = 'FPM' and discipline_name = 'English1';