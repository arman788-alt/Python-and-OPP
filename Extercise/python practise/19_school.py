class student:
    def __init__(self, name, cls, id ):
        self.name = name
        self.cls = cls
        self.id = id

    def __repr__(self):
        return f"{self.name}, cls: {self.cls}, wiht id: {self.id}"


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        
    
    def __repr__(self):
        return f"{self.name}, subject:  {self.subject}"


class school:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
    
    def addteacher(self, name, subject):
        teacher = Teacher(name, subject)
        self.teachers.append(teacher)
    
    
    def enroll(self, name,fee):
        if fee < 6500:
            print("Low amount ,cannot enroll")
        else:
            id = len(self.students) + 1
            Student = student(name, 'c', id)
            self.students.append(Student)
    

    def __repr__(self):

        print(f"-----Welcome to {self.name}")
        print(f"----All Teachers:----")
        for teacher in self.teachers:
            print(teacher)
        
        print("----ALL students:----- ")
        for student in self.students:
            print(student)
        return 'all done'
    

phitron = school('Phitron')
phitron.enroll('alia', 5200)
phitron.enroll('rani', 8000)
phitron.enroll('aishwaraiya', 7000)
phitron.enroll('vaijaan', 90000)

phitron.addteacher('Tom Cruise', 'Algo')
phitron.addteacher('Decap', 'DS')
phitron.addteacher('AJ', 'Database')

print(phitron)

        




