__author__ = 'Administrator'
from Student import Student

print "please input student name:"
name=raw_input()
print "please input student datebirth(YYYY-MM-DD):"
birth=raw_input()
print "please input student phone:"
phone=raw_input()
print "please input student email(wwww@xx.com):"
email=raw_input()
stu=Student(name,birth,phone,email)

print stu.name,stu.birthday,stu.phone,stu.email
