# Se importan las clases Student, Teacher y Course 
from student import Student
from teacher import Teacher
from course import Course

# Creación de instancias de estudiantes, profesores y cursos
student1 = Student("Esteban", 43, "B30754")
student2 = Student("Maria", 28, "B50854")

teacher1 = Teacher("Jorge Romero", 65, "12345")
teacher2 = Teacher("Profesor X", 53, "72490")

course1 = Course("IE0217", "DSA")
course2 = Course("IE0320", "CD1")

# Inscripción a cursos y asignación de cursos
student1.enroll_course(course1.course_code)
student1.enroll_course(course2.course_code)

teacher1.assign_course(course1.course_code)
teacher2.assign_course(course2.course_code)

# Mostrar información de estudiante, profesor y curso
student1.display_info()
teacher1.display_info()
course1.display_info()