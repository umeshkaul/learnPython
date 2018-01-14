class Employee:
	def __init__ (self,first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * 1.04)



emp_1 = Employee('one','kaul',1000)
emp_2 = Employee('Two','Paul',2000)


#print emp_1.first,emp_1.last
#print ('{} {}'.format(emp_1.first, emp_1.last))
#print(emp_1.fullname())
print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))
#print emp_1.fullname()
