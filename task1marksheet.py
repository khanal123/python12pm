print("====================marksheet===================")
print("do you want marksheet \n press y or Y if yes ")
choice=input("Enter your choice")
if (choice == 'y' or choice=='Y'):
    print("Enter subject marks:")
    marks1 = int(input("Enter marks in nepali:"))
    marks2 = int(input("Enter marks in english:"))
    marks3 = int(input("Enter marks in math:"))
    marks4 = int(input("Enter marks in science:"))
    marks5 = int(input("Enter marks in population:"))
    total_marks_obtained = marks1 + marks2 + marks3 + marks4 + marks5
    full_marks = 500
    if marks1 > 100 or marks2 > 100 or marks3 > 100 or marks4 > 100 or marks5 > 100:
        print("Invalid!!! Enter Data Again")
    else:
        percentage = total_marks_obtained / full_marks * 100
        if percentage < 35:
            print("fail")
        else:
            if percentage >= 35 and percentage <= 45:
                print("pass")
            elif percentage > 45 and percentage <= 60:
                print("second")
            elif percentage > 60 and percentage <= 75:
                print("first")
            else:
                print("top")