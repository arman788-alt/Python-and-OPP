# Use multiple classes to create a school project

class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.id = id
        self.current_class = current_class

    def __repr__(self) -> str:
        return f'Student with name: {self.name}, class: {self.current_class}, id:{self.id}'


class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher: {self.name}, subject: {self.subject}'

class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)
    
    def enroll(self, name, fee):
        if fee < 6500:
            return 'not enough fee'
        else:
            id = len(self.students) + 1
            student = Student(name, 'C', id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'

    def __repr__(self) -> str:
        print('welcome to', self.name)
        print('--------OUR Teachers--------')
        for teacher in self.teachers:
            print(teacher)
        print('--------OUR STUDENTS--------')
        for student in self.students:
            print(student)
        return 'All Done for now'

# alia = Student('Alia Torkari', 9, 1)
# ranbeer = Teacher('Douran beer', 'Algorithm', 101)
# print(alia)
# print(ranbeer)

phitron = School('Phitron')
phitron.enroll('alia', 5200)
phitron.enroll('rani', 8000)
phitron.enroll('aishwaraiya', 7000)
phitron.enroll('vaijaan', 90000)

phitron.add_teacher('Tom Cruise', 'Algo')
phitron.add_teacher('Decap', 'DS')
phitron.add_teacher('AJ', 'Database')

print(phitron)

# st = Student('arman', 12, 101)
# print(st)



#Explain Code::
# মডিউল ৫-৭ঃ মাল্টিপল ক্লাস ব্যবহার করে স্কুল ক্রিয়েট করা
# এই মডিউল এ আমরা মাল্টিপল ক্লাস ইউস করে ছোট একটা স্কুল প্রজেক্ট তৈরি করব 

# শুরুতেই Stdudent এবং টিচার এর জন্য ২ টা আলাদা ক্লাস বানিয়ে নেয়।


# class Student:
#     def __init__(self, name, current_class, id):
#         self.name = name
#         self.id = id
#         self.current_class = current_class

#     def __repr__(self) -> str:
#         return f'Student with name: {self.name}, class: {self.current_class}, id:{self.id}'


# class Teacher:
#     def __init__(self, name, subject, id) -> None:
#         self.name = name
#         self.subject = subject
#         self.id = id

#     def __repr__(self) -> str:
#         return f'Teacher: {self.name}, subject: {self.subject}'
    
# এখানে ২ টা ক্লাস এর মধ্যেই যেই __repr__ মেথড ব্যবহার করা হয়েছে এটা ক্লাস অবজেক্ট এর স্ট্রিং রিপ্রেজেন্টেশন দিবে 
# অর্থাৎ আমরা যদি Teacher ক্লাস এর অবজেক্ট এর প্রিন্ট করি তাহলে এটা এই মেথড এর মধ্যে যেই স্ট্রিংটা রিটার্ন করা হচ্ছে সেই অনুযায়ী আউটপুট প্রিন্ট করবে 

# এবার আমরা School নামে একটা ক্লাস তৈরি করি


# class School:
#     def __init__(self, name) -> None:
#         self.name = name
#         self.teachers = []
#         self.students = []

#     def add_teacher(self, name, subject):
#         id = len(self.teachers) + 101
#         teacher = Teacher(name, subject, id)
#         self.teachers.append(teacher)
    
#     def enroll(self, name, fee):
#         if fee < 6500:
#             return 'not enough fee'
#         else:
#             id = len(self.students) + 1
#             student = Student(name, 'C', id)
#             self.students.append(student)
#             return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'

#     def __repr__(self) -> str:
#         print('welcome to', self.name)
#         print('--------OUR Teachers--------')
#         for teacher in self.teachers:
#             print(teacher)
#         print('--------OUR STUDENTS--------')
#         for student in self.students:
#             print(student)
#         return 'All Done for now'
    
# এখানে শুরুতে আমরা name, teacher এবং students নামে তিনটা ইন্সট্যান্স এট্রিবিউট ডিক্লেয়ার করে নিয়েছি। তারপর মেথড তৈরি করেছি

# add_teacher()
# এই মেথডের মধ্যে আমরা টিচার এর আইডি হিসিবে টিচার লিস্ট এর লেন্থ এর সাথে ১০১ যোগ করে দিছি আইডিটাকে ইউনিক রাখার জন্য তারপরে এই মেথডের মধ্যে টিচার ক্লাস এর একটা ইন্সট্যান্স তৈরি করা হয়েছে teacher নামে তারপর এই ইন্সট্যান্সটাকে স্কুল ক্লাস এর টিচার লিস্টের মধ্যে এপেন্ড করে দেওয়া হয়েছে।

# enroll()
# এই মেথডের মধ্যে শুরুতে চেক করা হচ্ছে ফি টা ৬৫০০ এর থেকে কম আছে কিনা যদি থাকে তাহলে সেই অনুযায়ী একটা মেসেজ রিটার্ন করবে

# এবং যদি ফি ঠিক থাকে তাহলে টিচার এর মতোই স্টুডেন্ট এর একটা আইডি সেট করে দেওয়া হচ্ছে তারপর স্টুডেন্ট ক্লাস এর একটা ইন্সট্যান্স তৈরি করে সেটাকে Student ক্লাস এর students নামে যেই লিস্ট টা ডিফাইন করা হয়েছে সেখানে এপেন্ড করে দেওয়া হয়েছে।

# __repr__()
# এটা হচ্ছে আমরা যদি School ক্লাস এর একটা অবজেক্ট তৈরি করি এইভাবে


# school = School("XYZ Govt School")
# print(school)

# তাহলে এই school অবজেক্টটা এই এই __repr__() মেথডে যেভাবে ডিফাইন করা হয়েছে সেই অনুযায়ী প্রিন্ট করবে

# এখন আমরা সম্পূর্ণ কোডটাকে এইভাবে টেস্ট করে দেখতে পারি 


# phitron = School('Phitron')
# phitron.enroll('alia', 5200)
# phitron.enroll('rani', 8000)
# phitron.enroll('aishwaraiya', 7000)
# phitron.enroll('vaijaan', 90000)

# phitron.add_teacher('Tom Cruise', 'Algo')
# phitron.add_teacher('Decap', 'DS')
# phitron.add_teacher('AJ', 'Database')

# print(phitron)


# তাহলে এরকম আউটপুট পাবো

# welcome to Phitron
# --------OUR Teachers--------
# Teacher: Tom Cruise, subject: Algo
# Teacher: Decap, subject: DS
# Teacher: AJ, subject: Database
# --------OUR STUDENTS--------
# Student with name: rani, class: C, id:1
# Student with name: aishwaraiya, class: C, id:2
# Student with name: vaijaan, class: C, id:3
# All Done for now