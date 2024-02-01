class SalaryNotInRange(Exception):
    def __init__(self, salary, message="Salary is not in (5000,15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)


salary = int(input("Ingrese el salario: "))
if not 5000<salary<15000:
    raise SalaryNotInRange(salary)
