from person import Person # Se importa la clase Person del modulo person

# Definición de la clase Student, que hereda de la clase Person
class Student(Person):
    # Constructor de la clase Student
    def __init__(self, name, age, student_id):
        # constructor de la clase person utilzando super()
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    # Metodo para inscribirse en un curso
    def enroll_course(self, course):
        # Agrega el curso a la lista de cursos
        self.courses.append(course)

    # Método que muestra la información del estudiante
    def display_info(self):
        # Llama al método display_info de la clase Person utilizando super()
        super().display_info()
        print(f"Student ID: {self.student_id}\
              \nCourses: {', '.join(self.courses)}\n")
