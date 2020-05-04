from study.Person import Person


class Employee(Person):
    def __init__(self, name, age, gender, salary):
        super().__init__(name, age, gender)
        self.salary = salary

    def do_work(self):
        print("working hard")

    def about_me(self):
        super().about_me()
        print("my salary is ", self.salary)
