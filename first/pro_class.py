# class User:
#     def __init__(self, name):
#         self._name = name
#
#     def set_name(self, new_name):
#         self._name = new_name
#
# user_1 = User("John")
# user_1.set_name = "Артур "

# class Cat:
#     def __init__(self,name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
# cats = Cat(name="Барсик")
# name = cats.name
# print(name)


class Student:
    def __init__(self, name, course):
        self._name = name
        self._course = course

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        return self._name

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value):
        self._course = value


student = Student(name="Вася", course="Степик")
name = student.name
course = student.course

student.name = "Миха"
student.course = 1

print(name)
print(course)

print(student.name)
print(student.course )

