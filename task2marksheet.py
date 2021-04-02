choice = input("\t\t\t\tdo you want to view marksheet")
if choice == 'y' and 'y':
    count = int(input("enter how many students"))
    student = []
    for_top = 0
    top_student = ''
    top_marks = 0
    for student_name in range(count):
        name = input("enter student name")
        student.append(name)
    subject = ['math', 'science', 'computer', 'hp', 'programming']
    subjects = {}
    names = {} # to store names and marks subjectwise
    for person in student:

        print(f"{person}\'s marks")

        for i in subject:
            marks = int(input(f"\t\t\t\tenter {i} marks:  "))
            if marks < 100:
                subjects[i] = marks
            else:
                print("\t\t\t\tmarks should be less than 100")
        for i in student:
            names[i] = subjects
        # print(names['as']['math']) prints math marks
        # print(names)
        """{'firstName': {'math': 11, 'science': 22, 'computer': 22, 'hp': 22, 'programming': 22}, 'anoName': {'math': 11, 'science': 22, 'com
puter': 22, 'hp': 22, 'programming': 22}}
"""
#determining total marks ,top marks and top student
    for k in student:
        marks = 0
        total_marks = 0
        print(f"{k}\'s student details")
        for i in subject:
            total_marks += names[k][i]
            if top_marks < names[k][i]:
                top_marks = names[k][i]
            if for_top < total_marks:
                top_student = k

        print(f"\t\t\t\ttotal marks = {total_marks}")
        percentage = total_marks * 100 / 500
        if percentage < 35:
            print("\t\t\t\tfail")
        else:
            if (percentage >= 35 and percentage < 45):
                print("\t\t\t\tpass")
            elif (percentage >= 45 and percentage < 60):
                print("\t\t\t\tgrade c ypu need improvement")
            elif (percentage >= 60 and percentage < 70):
                print("\t\t\t\tgrade b")
            elif (percentage >= 70 and percentage < 80):
                print("\t\t\t\tgrade a")
            else:
                print("\t\t\t\tdistinction")
print(f"top student is{top_student}")
print(f"top marks is{top_marks}")

# name=['p','q','r']
# subject = ['math', 'science', 'computer', 'hp', 'programming']
# marks={}
# for i in name:
#     sub={}
#     for j in subject:
#         mark=0
#         sub[j]=mark
#     marks[i]=sub
# print(marks)