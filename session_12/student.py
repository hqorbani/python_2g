from person import person
class student(person):
    def __init__(self, name, family , std_number) -> None:
        super().__init__(name, family)
        self.std_number = std_number

    def tell_student_number(self):
        return self.std_number
