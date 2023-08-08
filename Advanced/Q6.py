"""Create the custom Python classes which have methods and
attributes and implement single inheritance, multiple inheritance,
and multilevel inheritance
"""

# Single Inheritance


class Company:
	def name(self):
		print("The name is ABC Corp.")

class Employee(Company):
	def role(self):
		print("The role of the employee is HR.")


object = Employee()
object.name()
object.role()


# Multiple Inheritance

class Mammal:
    def mammal_info(self):
        print("\nMammals can give direct birth.")

class Pets:
    def pet_info(self):
        print("Pet animals can be used for companionship.")

class Dog(Mammal, Pets):
    def dog_info(self):
	    print("Dogs are loyal to master")

obj = Dog()
obj.mammal_info()
obj.pet_info()
obj.dog_info()


# Multilevel Inheritance 

class Manager:
	def final_review(self):
		print("\nFinal Review and Client Management")

class Team_lead(Manager):
	def review(self):
		print("Reviews and approves...")

class Developer(Team_lead):
	def writes(self):
		print("Writes the code")

obj_ = Developer()
obj_.final_review()
obj_.review()
obj_.writes()