from cassandra.cluster import Cluster
from cassandra.query import BatchStatement
from cassandra.query import SimpleStatement

cl = Cluster()
session = cl.connect('workspace')

semester_m, final_m = 50, 80
index_or_record = 0

batch = BatchStatement()
batch.add( SimpleStatement("""Update Student_record_book set semester_mark= %s, final_mark= %s 
	WHERE university = 'KPI' and faculty = 'FPM' and group = 'KM-61' and student_id = 1 and discipline_name = 'English1'"""), (semester_m, final_m))
batch.add(SimpleStatement("""Update Professor_record_book_index set marks[%s] = 
	{discipline_name: 'English1', student_id: 1, semester_mark: %s, final_mark: %s} 
	WHERE university = 'KPI' and professor_id = 4 and department = 'ISAS' and semester = 1 and year = 2019"""), (index_or_record, semester_m, final_m))
session.execute(batch)
