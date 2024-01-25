from student import Student
from teacher import Teacher
from course import Course

student1 = Student("Esteban", 43, "B30754")
student2 = Student("Maria", 28, "B50854")


teacher1 = Teacher("Jorge Romero", 65, "12345")
teacher2 = Teacher("Profesor X", 53, "72490")

course1 = Course("IE0217", "DSA")
course2 = Course("IE0320", "CD1")


student1.enroll_course(course1.course_code)
student1.enroll_course(course2.course_code)

teacher1.assign_course(course1.course_code)
teacher2.assign_course(course2.course_code)


student1.display_info()

teacher1.display_info()

course1.display_info()