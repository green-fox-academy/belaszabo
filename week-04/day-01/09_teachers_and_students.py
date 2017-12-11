class Student(object):
    def learn(self):
        return "The student is learning"
    
    def question(self, teacher):
        return teacher.answer()

class Teacher(object):
    def teach(self, student):
        return student.learn()
    
    def answer(self):
        return "The teacher answeres a question"

student = Student()
teacher = Teacher()

print(student.question(teacher))
