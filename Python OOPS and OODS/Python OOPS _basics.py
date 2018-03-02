

https://www.cs.colorado.edu/~kena/classes/5448/f12/presentation-materials/li.pdf

Python supports multiple programming paradigms,
primarily but not limited to object-oriented, imperative
and, to a lesser extent, functional programming styles.

• It features a fully dynamic type system and automatic
memory management


**********


class Person:
	name = '123'
	raise_amt = 1.4

	def __init__(self, name):
		self.name name
		self.__private_name = 'Private var'   # this is a private var now

	def printName(self):
		print '{} {}'.format(self.name, self.__private_name)

	def printHi(self):
		print "%s says Hi ",self.name
		print self.__private_name # private var accisble inside class

	def speak(self):
		print 'I can speak'

	def accisble(self):  # Define public function
		print 'I am accisble public func'

	def __inaccisible(self): # Define private function
		print 'I m private function bcz of wrong name format'

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount

	@classmethod  # work as alternative constructor
	def from_string(cls, semp_str):
		name = emp_str
		return cls(name)

	@staticmethod #  if a method don't need any of the class name or instance name as param
	def _is_work_day(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

	# dunder method: all methods which start with double underscore __
	def __repr__(): # __str__() use __repr__ as fallbak so its good to implement __repr__ atleast
		return "Employee('{}', '{}', '{}').format(self.first, elf.last, self.email)"
	def __str__():
		return '{} - {}'.foramt(self.fullName(), self.email)
	def __add__(self, other): # emp1 + emp2  print combine saleary of both emp
		return self.pay + other.pay
	def __len__(self): # in order to make len(emp1) work for our case, we have to implement __len__() for our class
		return len(self.fullname())
	def __del__(self):
		self.name = None


	@property # property decorator allow us to use function like a variable. emp1.email() and emp1.email both will run this function.old impl won't break after this
	def email(self):
		return '{}.{}@eamil.com'.format(self.first, self.last)

	@fullname.setter # emp1.fullname = 'Corey Anderson'
	def fullname(self, name):
		fisrt, last = name.split(' ')
		self.fisrt = fisrt

	@fullname.deleter # del emp1.fullname
	def fullname(self):
		print 'delete name!'
		self.first = None
		self.last = None


class Man(Person):
	def __init__(self, name, height=None): # #pass None as default to list. Never pass a mutable type lke list or dictionary as default type
		super().__init__(name)   # or Employee.__init__(self, first,last,pay) other way of calling.,helpful in multi inheritance where U want to name the parent class to call
		self.height = height

	def wear(Self):
		print 'I wear shirt'

class Woman(Person):
	def wear(self):
		print 'I wear skirt'

class Human(Man, Woman):
	def wear(self):
		print 'I wear skirt'


class TestHuman:
	def printName(self,human):
		human.wear()
	def GotoSleep(self, human):
		human.wear()
	def makeNose(Self, human):
		human.wear()

per = Person('qwert')
Person.printName(emp1)
print per.__dict__   # printing whtever thatinstancehas direct accesss to.. and not htouf=gh class chain
Person.__dict__  # print for class

Person.set_raise_amt(1.5) # # 1.5  earler it was 1.4 by default as set in class itself
per.set_raise_amt(1.5) # class method can also be called from instances

per = Person.from_string('name') # will return class instance



person = Person("Ashish")

person.printHi()
person.name
Person().name
person.__private_name # error stating no var called __B in class..

# Actually, the private accessibility method is just a rule,not the limitation of compiler.
# Its fact is to change name of private name like __variable or __function() to _ClassName__variable or _ClassName__function(). So we can’t access them because of wrong names.
Person().accisble()
Person().__inaccisible  # throw error..Can’t access private function .. but
Person()._Person__inaccisible() # ..prints correct..Access private function via changed name

man = Man()
man.wear()   .. iwear shirt
man.speak()  -- i can speak



human  = TestHuman()
man = Man()
woman = Woman()
hum = Human()

TestHuman.printName(dog)   # i m dog
TestHuman.GotoSleep(dog)  # sleep

# isinstance() and issubclass method
print isinstance(emp_1, Employee)  true
print isinstance(mgr_1, Employee)  true as Employee is a super class of Manager
print issubclass(Mnaager, Developer)  false
print issubclass(Mnaager, Employee)  true




**********



class Person:
	def __init__(self, name):
		self.name name
	def __del__(self):
		self.name = None
	def printHi(self):
		print "%s says Hi ",self.name

A = Person("Ashish")
A.printHi()
A.name

This example includes
class definition, constructor function, destructor function,
attributes and methods definition and object definition.


Class definition syntax:
class subclass[(superclass)]:
	[attributes and methods]


Object instantiation syntax:
object = class()


Attributes Name Description
__dict__ Dict variable of class name space
__doc__ Document reference string of class
__name__ Class name
__module__ Module name consisting of class
__bases__ The tuple including all the superclasses




Form and Object for Class

class A:
	i = 123
	def __init__(self):
		self.i = 12345

print A.i --> invoke form: just invoke data or method in the class ..i =123
print A().i   --> invoke obejct: initialize obejct forst and then invoke i on it.. i = 12345






Inheritance
Inheritance in Python is simple,
Just like JAVA, subclass can invoke
Attributes and methods in superclass.


From the example, Class Man inherits
Class Person, and invoke speak() method
In Class Person


Inherit Syntax:
class subclass(superclass):



class Person:
	def speak(self):
		print 'I can speak'


class Man(Person):
	def wear(Self):
		print 'I wear shirt'

class Woman(Person):
	def wear(self):
		print 'I wear skirt'

man = Man()
man.wear()   .. iwear shirt
man.speak()  -- i can speak





Multiple Inheritance
Python supports a limited form of multiple inheritance.



class DerivedClass(Base1, Base2, Base3 …)
	<statement-1>
	<statement-2>


resolution rule used for class attribute references. This is
depth-first, left-to-right. Thus, if an attribute is not found in
DerivedClass, it is searched in Base1, then recursively in the
classes of Base1, and only if it is not found there, it is searched
in Base2, and so on.



class A:
	def A(self):
		print 'i am A'

class B:
	def A(self):
		print 'I AM a'
	def B(self):
		print 'I  am B'

class C(A, B):
	def C(self):
		print 'I am C'

C = C()
C.A() -- bcz of left to right rule first search will be in A..so A.A() gets print
C.B() -- since class A dosen't have B(), so then search will be in B..and B.B() gets print
C.C() -- C() is present in class C..so C.C() gets print




“Self”
“Self” in Python is like the pointer “this” in C++. In
Python, functions in class access data via “self”.




Encapsulation – Accessibility (1)

In Python, there is no keywords like ‘public’, ‘protected’
and ‘private’ to define the accessibility. In other words, In
Python, it acquiesce that all attributes are public.


But there is a method in Python to define Private:
Add “__” in front of the variable and function name
can hide them when accessing them from out of
class.


class Person:
	def __init__(self):
		self.A = 'public var'
		self.__B = 'Private var'   # this is a private var now

	def print(self):
		print self.__B   # private var accisble inside class

P = Person()

P.A  #print public var
P.__B   # error stating no var called __B in class..
P.print()   ..print __B


Actually, the private accessibility method is just a rule,
not the limitation of compiler.
• Its fact is to change name of private name like __variable
or __function() to _ClassName__variable or
_ClassName__function(). So we can’t access them
because of wrong names.


class C:
	def accisble(self):  Define public function
		print 'I am accisble public func'

	def __inaccisible(self):  Define private function
		print 'I m private function bcz of wrong name format'

C().accisble()  # pritn correct
C().__inaccisible  # throw error..Can’t access private function .. but
C()._C__inaccisible() ..prints correct..Access private function via changed name





Polymorphism


 traditional polymorphism exist

class Animal:
	def Name(self):
		pass
	def Sleep(self):
		print 'sleep'
	def MakeNoise(self):
		pass

class Dog(Animal):
	def Name(self):
		print 'I m dog'
	def MakeNoise(self):
		print ' i bark'

class Cat(Animal):
	def Name(self):
		print 'i m cat'
	def MakeNosie(self):
		print 'meow'

class Lion(Animal):
	def Name(Self):
		print 'i m lion'
	def MakeNoise(self):
		print 'roar'

class TestAnimals:
	def printName(self,animal):
		animal.Name()
	def GotoSleep(self, animal):
		printanimal.gotoSleep()
	def makeNose(Self, animal):
		animal.makeNoise()




testAnimal  = TestAnimals()
dog = Dog()
cat = Cat()
lion = Lion()

TestAnimals.printName(dog)   # i m dog
TestAnimals.GotoSleep(dog)  # sleep
TestAnimals.MakeNosie(dog)  # bark
TestAnimals.printName(cat)  # i m cat
TestAnimals.MaleNosie(lion)  # roar




Everywhere is polymorphism in Python (1)


Since Python is a dynamic programming language, it
means Python is strongly typed as the interpreter keeps
track of all variables types. It reflects the polymorphism
character in Python.

Not only
integer but also string, list, tuple and dictionary can
realize their relative ‘add’ operation.

>> 1+2
3
>> 'key' + 'board'
keyboard
>> [1,2,3,4] + [5,6,7,8]
[1,2,3,4,5,6,7,8]
>> (1,2,3,4) + (5,6,7,8)
(1,2,3,4,5,6,7,8)
>> {A:a, B:b} + {C:c, D;d}
{A:a, B:b, C:c, D:d}



repr()
For ‘repr’ method, it can transfer any kinds of data to
string type.

a= 123
>> b =repr(a)
>> b
'123'
>> b+ 'string'
123string




Avoid Destroying Polymorphism!

The only way to destroy polymorphism is check types by
using functions like ‘type’, ‘isinstance’ and ‘issubclass’ etc.








Two ways to call a function insid a class

class Employee:
	def __init__(self, name, email):
	 self.anme = name
	 self.email = email

	def printName(self):
		print '{} {}'.format(self.name, self.email)


emp1 = Employee('assh', 'aks@g.com')

2 ways to call afunction
1. emp1.printName()

2. Employee.printName(emp1)   # here we are passing emp1 as self argument for the function

in general whereever you are using self ,it can be replaced with tthe class name itsedl..even indisde the clas function



CLass varibale and instance veriables:

will be same for all instances and will not chnage per instance

e.g raise_amt . which will besame for each employee instances



To print namespace of the class instance
i.e printing whtever thatinstancehas direct accesss to.. and not htouf=gh class chain

print emp1.__dict__
{'name':sdsds, email:sjdnsdj}

to print for class
Employee.__dict__

if we do emp1.raise_amt = 1.4 .. this will only change raose amt fot the sigle instance and all other instance iwll have class raise_amt



class Employee:

	raise_amt = 1.5
	num_of)emp = 0

	def __init__(self, name, email):
	 self.anme = name
	 self.email = email

	 Employee.num_of_emp+=1     # here we don't want ot put self.num_of_emp bcz we don't want to chnage number of employee fr any instance..this shud be same for all emloyee instance..

	def printName(self):
		print '{} {}'.format(self.name, self.email)

	def apply_Raise(Self):
		self.pay = int(self.pay * self.raise_amt)





classmethods and staticmethods :

class method works on class varibales and takes class as first parma

reular methods takes self as first param




class Employee:

	raise_amt = 1.4
	num_of)emp = 0

	def __init__(self, name, email):
	 self.anme = name
	 self.email = email

	 Employee.num_of_emp+=1     # here we don't want ot put self.num_of_emp bcz we don't want to chnage number of employee fr any instance..this shud be same for all emloyee instance..

	def printName(self):
		print '{} {}'.format(self.name, self.email)

	def apply_Raise(Self):
		self.pay = int(self.pay * self.raise_amt)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount


Employee.set_raise_amt(1.5)

print Employee.raise_amt  # 1.5  earler it was 1.4 by default as set in class itself
print emp1.raise_amt   # 1.5
print emp2 raise_amt   # 1.5



class method can also be called from instances
emp1.set_raise_amt(1.5) and this will also change the class variabe;


now classmethods are also used as alternative xontructor where tou want to do some cleaning/preprocessing before creating instances

like you are sending as tinf of info which eed to be paresed and taken out required info to pass to constructor

we can provide a class method to do thos cleasning and call constructor interally anretyunr thr object


	@classmethod
	def from_string(cls, semp_str):
		name, email = emp_str.split('-')
		return cls(name, email)

emp_str = 'asg-aks123@g.com'
new_emp = Employee.from_string(emp_str)


print new_emp.email



STATIC METHODS
it dosen't pass nayhtng as first param
if you fucntion dosen;t need any of the class name or instance name self, it could be a static method


	@staticmethod
	def _is_work_day(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return false
		return true

import datetime
my_date = datetime.date(2015, 7, 10)
Employee.is_work_day(my_date)   # false bcz 10th is sunday

my_date = datetime.date(2015, 7, 11)
Employee.is_work_day(my_date)   # true bcz 11th is monday



Tutorial 4: Inheritance - Creating Subclasses

print  help(Developer)  will give object resoltion order for subclass Developer


class Developer(Employee):
	raise_amt = 1.10

	def __init__(self, first,last,pay,prog_lang):  # it has one extra attrib prog_lang
		super().__init__(first, last, apy)   # or Employee.__init__(self, first,last,pay) other way of calling.,helpful in multi inheritance where U want to name the parent class to call
		self.prog_lang = prog_lang



you shoud never pass a mutable type lke list or dictionary as default type. so pass None as default to function

class Manager(Employee):

	def __init__(self, first, last, apy, employees = None):   #pass None as default to list
		super().__init__(self, first, last, pay)
		if emplyees is None:
			self.employees = []
		else:
			self.employes = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.emplyees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.emplyees.remove(emp)




isinstance() and issubclass method

print isinstance(emp_1, Employee)  true
print isinstance(mgr_1, Employee)  true as Employee is a super class of Manager
print isinstance(mgr_1, Developer)  false



print issubclass(Mnaager, Developer)  false
print issubclass(Mnaager, Employee)  true



Tutorial 5: Special (Magic/Dunder) Methods


dunder method : all methods which start with double underscore __

__init__()
__repr__()
__str__()
__add__()   # int.__add__(), str.__add__()
__len__()   # len('string') uses this ..'string'.__len__()

__str__() used repr as fallbak so its good to implement repr atleast
moreover repr is user for defveloper repr, mor eof a debugging ,etc and str is for user readability

def __repr__():
	return "Employee('{}', '{}', '{}').format(self.first, elf.last, self.email)"

now whe we print emp_1 we will se Employee('corey', 'anderson', 'c@g.com')

we can call __str__() and __repr__() separatly also print __str__(emp_!)

def __str__():
	return '{} - {}'.foramt(self.fullName(), self.email)



__add__()

print 1+2  gives 3
print a+b gives ab
now str and int has its own __add__() dender methods

print int.__add__(1,2)
print str.__add__('a','b')

we can customize our own add for our class

adding two employee

def __add__(self, other):
	return self.pay + other.pay

print emp1 + emp2  print combine saleary of both emp



similarly len('string') uses __len__() as dunder emthod

so in order to make len work for our case, we have to implement __len__() for our clas

def __len__(self):
	return len(self.fullname())







Property Decorators - Getters, Setters, and Deleters

property decorator llow us to use function like a variable


in our case we are creating employee email using first and lat naem, which means everytime someone chages there fist name or last name we have to modify there asciated emil.
surrent email is getting crated inside constructor.

so we need to have a way to over come this without breakingthe existing fucnt for those already using it..

i.e to provide a way to update email

@property
def email(self):
	return '{}.{}@eamil.com'.format(self.first, self.last)

what this oropert will do is it will aloowe to acces  a method like a attribute
i.e emp1.email() and emp1.email both will run this function.so existing duntionaly is not broken

so when  someone from old impl try to print emp1.email like before. but now we are not setting emial insde the __init__() method , still emp1.email will retunr them corect emial using the proerty fucntion for emial.



setters: we can use them to set attribute values

@fullname.setter
def fullname(Self, name):
	fisrt, last = name.split(' ')
	self.fisrt = fisrt ..

@fullname.deleter
def fullname(self):
	print 'delete name!'
	self.first = None
	self.last = None


emp1.fullname = 'Corey Anderson'
del emp1.fullname





****************************************************************************************



Working with String

print '{} {}'.format('asasasas',asasasas) ====
print f'{asasasa} {asasasa}'. Welcon


print f'{asasasa} {asasasa.toupper}'. Welcon

name = 'Aahiasa'
print dir(name)
give s info about wht all mehtods are available to this strng

print help(str.lower)
will give all info about this .lower function on string class


****************************************************************************************



num = 3
print type(num)    int/float


float divistion

a // b ..double dicide sign

print abs(-2)

print round(3.75) ..4

print round(3.74,1) ..3.8


num1 = int(num1)





****************************************************************************************

Lists, Tuples, and Sets

courses = []
lne(courses)


courses.append('art') at end

courses.insert(0, 'art') ..at specfic nsdex

extend # to insert multiple /list as individual item

couses2 = []
cousses.extend(course2)

courses.remove('Art') ..will remove specfic name art..

courses.pop()  #return the value it remove and efault the last item..helpful in stack and queue


courses.reverse()

cousese.sort()

courses.sort(reverse =True) ..inpace sorting/reversing

to get soted version of actual list

sorted_course = sorted(courses)

num ] []
print min(num)

print course.index('Art') ..give index of art in ist

print 'Art' in curses

for item in courses:
	print item

for course in enumerate(courses):
	print index, course


for course in enumerate(courses, strart = 1):  now 1st vaklue will have index 1
	print index, course

comma seaprated list values
course_str = ', '.join(courses)

Taples: immutab;e

pribalem with lst is is mutable and anu assingment store the am referecne..like call by reference

list1 =[sdsd,sdsd,sdsd,sdsd]
list2  = lsut1

list1[0] = sdsdsd
now list 2 0th elem will also get mdfed
to overcome this we use tuples


tuple1 = (sdsd,sdsd,sdsd,sdsd)
tuple 2 = tuple1

tuple1[0] = asaas  #not allowed opearion..imutae


Sets:

cscouses = {sdsas,asas,asas,asasa}
pritn course # it odent prevent insertion order..its random

if Mth in couses:
	faste than lsit and tuple

cs_courses.intersection(art_Courses)

.difference()
.union()


emptylist = []
emptylist = list()

emptytuple = ()
emptytuple = tuple()

emptysets = {}  # wrong .this will create a dict..this a gotcha
emptyset = set()

****************************************************************************************


Dictionary

dict = {}

dict['keyexists'] ..print value
dict['nonexistkey'] ..throw error

to overcome this
use .get()  it reyrn None for non exxite key vaues

dict.get('nonecuxtkey')  #print None
dict.get('nonexustkey', 'Not Found')..print Not found if key dosent exist


dict.update({asas:asas,asas:asas})..multile upate at once

del dict.age


age = dict.pop('age')

dict.keys()
dict.values()..print values of dict
dict.items() ..bit key ad values

for k,v in dict.items():
KEY,VALUE

****************************************************************************************


A = [ASAS,ASAS,ASAS]
b = [ASAS,ASAS,ASAS]

print a == b  .true..content same
print a is b # false bcz both are doff pbecy location in memory

to see location..print id(A) and id(b)..both diff now

but b = A
pritn b is a ..true as not both referecen same memory location

print id(A) and id(b)..both same now

a is b == id(A) ==id(b)


what corespnd to flase:
False
None
0 evel to false
'', {}, (), []

all else evel to true



****************************************************************************************



function

def f(*args, **kwargs)  # name could be anything but tis the convention

args accept all the positional arg like single passed parame without any leys
and kwargs acdept all teh lista dn dict or key value paitr passed

f('math', 'art',name = 'ase', age =33)
args = math, art
kwargs = anme:jphn, age:33

now if we create cousese=  [ssa,asas]
map = {name:asas, asas:dsds}

 and pass to function f(couse, amp)
 args = [asas,asasa], {ass:Asas,asas:erer}
 kwargs = {}

 but this is not what we thought, so in oder to unoack them we use * and ** before them tot ell compier to unoack them asn pass to args and kwargs

 func(*courses, **map)
now args = asas,asasa
kwargs = asas:asas,asas:wewe




****************************************************************************************


LEGB : local, enclosing,globel, build-in # thisis the order of resolution


x = 'gloabl_x'

def test():
	gloabl x

	 .. we are telling ytho than the x inside ths fucnton will be making chnages to gloabl x an no local copy will be created to override the gloabl x... if not provided than any oteh x declaion will be local copy of this fucn an global will remin intact
	 this line alos makes any var refreced after it as gloabl even toogu it may not exist in glbalscope...like if we comment gloabl x at top and write gloabl x inide fcuntion, then any var name x insde the fucntion will become gloabl

	 x= 'ssa'


import builtins

min, max..make sure we not overwrite this be writng our own def min()...


enclosing fuc

def outer():
	x = 'outerx'

	def inner():
		print x     ...looks for inclsoing x insde first..LEGB..local,enclosing fucn, then gloabl
	inner()
	print x

to work with enclosing local vale
def outer():
	x = 'outerx'

	def inner():
		nonlocal x .. will change enclsng x
		print x     ...looks for inclsoing x insde first..LEGB..local,enclosing fucn, then gloabl
	inner()
	print x

****************************************************************************************



Virtual env:

pip install virtualenv

virtualenv prog_1_env

source project1_env/bin/activate

which python,pip

pip list

pip freeze --local > requirements.txt     # --local tell to mdfy local packages obly and no global

deactivate

rm -rf prog_1_env   ..renove the env


virtualenv -p /usr/bin.python2.6 proj_1_env ..will use python 2.6 for tis virtual env

****************************************************************************************

exit()

comprehensions

nums = [1,2,3,4,5,6,7,8,9,10]

# I want 'n' for each 'n' in nums
my_list = []
for n in nums:
  my_list.append(n)
print my_list

print [n for n in nums]


# Using a map + lambda
# map runs for all the item in list passed
my_list = map(lambda n: n*n, nums)
print my_list

# Using a filter + lambda
# filter works same as lambda
my_list = filter(lambda n: n%2 == 0, nums)
print my_list


# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list = []
for letter in 'abcd':
  for num in range(4):
    my_list.append((letter,num))
print my_list

# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
print zip(names, heros)  # zip makes both list 1-1 mapping od names and values

# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print my_dict


# Set Comprehensions
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = set()
for n in nums:
    my_set.add(n)
print my_set

Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
        yield n*n   # do not hold in memory anything except the first referece to first item

my_gen = gen_func(nums)

for i in my_gen:
    print i

****************************************************************************************


Sorting Lists, Tuples, and Objects

li = [8,1,9,2,7,3,5]

s_li = sorted(li)
s_li = sorted(li, reverese = True)

li = [-8,1,9,-2,7,-3,5]

s_li = sorted(li, key = abs)

in-place sorting
s_li.sort()
s_li.sort(reverese = True)


tuple = (9,1,8,2,7,3,6,4,5)
s_yup = sorted(tup)


di = {'name': 'corey', 'job': 'programmng', 'age':None, 'os':'Mac'}
s_di = sorted(di)  ... sort keys ['age,'job','name','os']


class Employee:
	def __init__(self, name, age, salary):
		sef.name = name
		self.age= age
		self.salary = salary

	def __repr__(self):
		return '{},{},${}'.format(self.name,self.age, self.salary)

e1 = Employee('Carl',34, 70000)
e1 = Employee('Sarah',32, 67000)
e1 = Employee('John',44, 50000)

employees = [e1,e2,e3]

s_employees = sorted(employees)     # throws error don't know how to sort e1 < e2

def e_sort(emp):
	return emp.name            ..emp.salary

s_employees = sorted(employees, key = e_sort)
s_employees = sorted(employees, key = lambda e: e.name, reverse = True)

from operator import attrgetter
s_employees = sorted(employees, key = attrgetter('age'))



****************************************************************************************


String Formatting - Advanced Operations for Dicts, Lists, Numbers, and Dates


person = {'name': 'Jenn', 'age': 23}

sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print(sentence)


sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
print(sentence)


sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
print(sentence)


tag = 'h1'
text = 'This is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag, text)


class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jack', '33')

sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)

sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='30')

person = {'name': 'Jenn', 'age': 23}
sentence = 'My name is {name} and I am {age} years old.'.format(**person)    # unpacking dictionary


for i in range(1, 11):
    sentence = 'The value is {}'.format(i)

for i in range(1, 11):
    sentence = 'The value is {:02}'.format(i)     # will print 2 places 01,02,03,04,05

pi = 3.14159265
sentence = 'Pi is equal to {:.2f}'.format(pi)

sentence = '1 MB is equal to {} bytes'.format(1000**2)
sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)    # 1,000,000.00 bytes



import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
# March 01, 2016

sentence = '{:%B %d, %Y}'.format(my_date)

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
# March 01, 2016 fell on a Tuesday and was the 061 day of the year.
# added (0:) bcz we are passing single date instance to 3 place holders.so all will take the 0th only after adding 0:


****************************************************************************************

Generators in python


def square_numbers(nums):
    for i in nums:
        yield (i*i)

my_nums = square_numbers([1,2,3,4,5])

# comprehension notation
# to create set we uyse () and not []
my_nums = (x*x for x in [1,2,3,4,5])

# same perforce as not using generators
print list(my_nums) # [1, 4, 9, 16, 25]

for num in my_nums:
    print num



import mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print 'Memory (Before): {}Mb'.format(mem_profile.memory_usage_psutil())

def people_list(num_people):
    result = []
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in xrange(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person

t1 = time.clock()
people = people_list(1000000)
t2 = time.clock()
print 'Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil())  # 15 MB memory
print 'Took {} Seconds'.format(t2-t1) #399 MB memory

# bcz of generator it dosen't store anything in memory so memory cunsoption is not there.high performance
t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()
print 'Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil()) # 15 MB memory
print 'Took {} Seconds'.format(t2-t1) # 15 MB memory

# if we convert genretor retured referece to a lsit it is back t same old back erformce as list
t1 = time.clock()
people = list(people_list(1000000))		#list(gen_referecne)
t2 = time.clock()
print 'Memory (After) : {}Mb'.format(mem_profile.memory_usage_psutil())  # 15 MB memory
print 'Took {} Seconds'.format(t2-t1) #399 MB memory




****************************************************************************************

if __name__ == '__main__'


It basically mensa if you are runing this file directly or from some import

if you are runnng this current file then __name__ will be __main__ else it will be name of the file..the

so this check is required in some cases where you want certain modulr/function t run only if this file is run direty andno through import

module1.py

def main():
	print 'Run directly'

def main2():
	print 'run indirectly thorugh imports'

if __name__ == __main__:
	main()
else:
	main2()


module2.py

import module1

print 'run this file whcih will invoke method 2 on mymodule.py bcz that module is not directl run '







****************************************************************************************


For-else

else will run if no break stteet occumr in for loop

for letter in heystack:
	if needel == etter:
		print 'Found'
		break
else:  # will run if no break statement occure in for-loop
	print 'not Found'







****************************************************************************************

Better way to opena nd close a file

# best way
with open('file.txt') as f:
	for line in f:
		print line

no need to opena n lcose file ,its taken care of



# slightly better way
f = open('file.txt')
for line in f:
	print line
f.close()

#bad way
f = open('file.txt')
text = f.read()
for line in text.split('\n'):
	print line
f.close()



****************************************************************************************

try-except-else to handle failure and program crash

try:
	print int('x')   # wil throw error as x canot be cnverted to int
except:
	print 'conversion failed'
else: # if no-except
	print 'conversion successful'
finally:
	print 'Done'

benifut of finally
it will run regardless of what happend in try ctch,,even if error occures

try:
	print int('x')
finally:
	print 'do some cleanup even if error is thrown'





****************************************************************************************
Python Decorators
https://www.youtube.com/watch?v=nYDKH9fvlBY

Decorators solve two issues
1. code duplication
2. cluttering main  logic of function with additional functionality (i.e timing in our example, logging)

def time_it(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print(func.__name__ +' took '+ str((end-start)*1000) + ' mill sec')
		return result
	return wrapper

@time_it
def cal_square(numbers):
	# logic for square

@time_it
def cal_cube(numbers):
	# logic for cube


****************************************************************************************

raise AttributeError("Object is missing _auto_lock")








****************************************************************************************










****************************************************************************************










****************************************************************************************










****************************************************************************************










****************************************************************************************










****************************************************************************************










****************************************************************************************










****************************************************************************************










****************************************************************************************










****************************************************************************************










****************************************************************************************










****************************************************************************************










****************************************************************************************










****************************************************************************************










****************************************************************************************










****************************************************************************************










****************************************************************************************










****************************************************************************************










****************************************************************************************










****************************************************************************************










****************************************************************************************










****************************************************************************************










****************************************************************************************










****************************************************************************************










****************************************************************************************










****************************************************************************************






































