from person import Person # Se importa la clase Person del modulo person

# Definición de la clase Teacher, que hereda de la clase Person
class Teacher(Person):
    # Constructor de la clase Teacher
    def __init__(self, name, age, employee_id):
        # Llamada del constructor de la clase Person usando super()
        super().__init__(name, age)
        self.employee_id = employee_id
        self.courses_taught = []

    # Metodo para asignar un curso
    def assign_course(self, course):
        # Agregar el curso a la lista
        self.courses_taught.append(course)

    # Método que muestra la información del profesor
    def display_info(self):
        # Llama al método display_info de la clase Person utilizando super()
        super().display_info()
        print(f"Employee ID: {self.employee_id}\
              \nCourses taught: {', '.join(self.courses_taught)}\n")

