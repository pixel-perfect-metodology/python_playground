print('\n\nday 12\n\n')

print('# Classes and Objects')


class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

p1.age = 40
print('p1.age', p1.age)

del p1.age
# print('p1.age', p1.age)  # AttributeError
# AttributeError: 'Person' object has no attribute 'age'

del p1
# print('p1.age', p1.age)  # NameError: name 'p1' is not defined


class Person:
  pass



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


class Student(Person):
  pass


x = Student("Mike", "Olsen")
x.printname()


class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)


x = Student("Mike", "Olsen")
x.printname()


class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)


x = Student("Mike", "Olsen")
x.printname()


class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year


x = Student("Mike", "Olsen", 2019)
print(x)


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student("Mike", "Olsen", 2019)
x.welcome()

print(vars(x), type(vars(x)))
print(dir(x), type(dir(x)))
print(x.__dict__)
