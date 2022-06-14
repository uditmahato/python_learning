#dictionary student name and marks
from pickletools import markobject


student_marks = {'Mary': 93, 'Bob': 87, 'John': 80, 'Tom': 60,'Bharat':50,'raju':40,'siva':30,'krishna':98}
std_name=input('Enter the name of students to check their marks: ')
mark=student_marks[std_name]
if mark>=80:
    print('Congratulations! You have passed with distinction getting {} marks'.format(mark))
elif mark>=70 and mark<80:
    print('Congratulations .You have passed with First division getting {} marks'.format(mark))
elif mark>=60 and mark<70:
    print('Congratulations .You have passed with Second division getting {} marks'.format(mark))
else:
    print('Sorry! You have failed getting {} marks'.format(mark))
    