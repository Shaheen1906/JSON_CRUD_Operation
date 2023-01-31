from student_module import Student, read_data

#creating object here
stu1 = Student('C:/Users/shahe/OneDrive/Desktop/Projects/project/students.json')

#creating new record
stu1.create(
    id = len(read_data())+1,
    name= "Anu",
    rollno= 21,
    age= 24
)

#read all records
# stu1.read()

#read single record by id
# stu1.read_single(1)

#update record by id
# stu1.update(1,"bhargav",2,23)

#delete single record by id
# stu1.delete(1)

#exporting file
# stu1.export_json()