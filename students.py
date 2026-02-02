class Student:

    valid_courses = set([
        'Computer Science', 
        'Software Engineering', 
        'Networks and Security', 
        'Cybersecurity', 
        'Data Science', 
        'Computing'
        ])
    
    def __init__(self, up_number, course, placement=False):
        self._up_number = up_number
        if course in self.valid_courses:
            self._course = course
        else:
            self._course = 'Computer Science'
        self._year = 3 if placement else 1

    @property
    def up_number(self):
        return self._up_number
    
    @property
    def course(self):
        return self._course
    
    @course.setter
    def course(self, new_course):
        if new_course in self.valid_courses:
            self._course = new_course
            return f"Course changed to {self._course}"

    @property
    def year(self):
        return self._year
    
    def progress(self):
        if self._year < 4:
            self._year += 1

    def __str__(self):
        output = f"Student up{self.up_number} studying {self.course} in year {self.year}"
        return output


class PlacementStudent(Student):
    
    def __init__(self, up_number, course, company):
        super().__init__(up_number, course, placement=True)
        self._company = company

    @property
    def company(self):
        return self._company
    
    def __str__(self):
        output = f"Placement student up{self.up_number} working at {self.company}"
        return output


def test_student():
    student = Student(2511688, 'Cybersecurity')
    student.progress()
    placement_student = PlacementStudent(111111, 'Cybersecurity', 'Apple')
    student2 = Student(2501901, 'Maths')
    print(f"{student}\n")
    print(f"Student Year {student.year}")
    print(f"Student UP Number: {student.up_number}\n")
    student.progress()
    student.progress()
    student.progress()
    student.progress() #shouldnt progress past year 4
    print(f"{student}\n")
    print('------------------------------------------')
    print(f"{student2}\n")
    print('------------------------------------------')
    print(f"{placement_student}\n")
    print(f"Student Company: {placement_student.company}")
    print(f"Student Year: {placement_student.year}")

test_student()