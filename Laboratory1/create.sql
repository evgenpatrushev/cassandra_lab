CREATE KEYSPACE workspace WITH REPLICATION = {'class':'SimpleStrategy', 'replication_factor':3};

use workspace;

CREATE TYPE IF NOT EXISTS human_record(
	name varchar,
	surname varchar,
	second_name varchar,
	birthday date,
	city_of_birth varchar
);

CREATE TYPE IF NOT EXISTS professor_record(
	department varchar,
	professor_id int
);

CREATE TYPE IF NOT EXISTS student_record_mark(
	discipline_name varchar,
	student_id int,
	semester_mark int,
	final_mark int
);

CREATE TABLE Student(
	university varchar,
	faculty varchar,
	group varchar,
	student_id int,
	student_data frozen<human_record>,
	data_enrollment date,
	data_expelled date,
	count_of_study_students int STATIC,
	PRIMARY KEY ((university, faculty), group, student_id)
);

CREATE TABLE Discipline(
	university varchar,
	faculty varchar,
	discipline_name varchar,
	hours_for_semester int,
	exam Boolean,
	PRIMARY KEY ((university, faculty), discipline_name)
);

CREATE TABLE Professor(
	university varchar,
	department varchar,
	professor_id int,
	professor_data frozen<human_record>,
	data_enrollment date,
	data_expelled date,
	degree varchar,
	count_of_professors_work int STATIC,
	PRIMARY KEY ((university, department), professor_id)
);


CREATE TABLE Student_record_book(
	university varchar,
	faculty varchar,
	group varchar,
	student_id int,
	discipline_name varchar,
	professor_data frozen<professor_record>,
	semester_mark int,
	final_mark int,
	data_passed date,
	PRIMARY KEY ((university, faculty), group, student_id, discipline_name)
);

CREATE TABLE Professor_record_book_index(
	university varchar,
	department varchar,
	professor_id int,
	year int,
	semester int,
	marks List<frozen<student_record_mark>>,
	PRIMARY KEY ((university, department), professor_id, year, semester)
);