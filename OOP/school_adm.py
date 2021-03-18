import csv

def to_csv(l):
    with open("Student_info.csv","a",newline='') as file:
        writer = csv.writer(file)
        writer.writerow(l)

def assign_roll():
    f=open("student_info.csv","r")
    c=0
    for line in f:
        c += 1
    return c

c = True

while c:
    if(assign_roll()==0):
        to_csv(["SI","Name","Age","Contact","Email"])
    student_data=input("Enter student information in the format (Name,Age,Contact,Email): ")
    list=student_data.split(" ")
    print("Name:{}\nAge:{}\nContact:{}\nEmail:{}".format(list[0],list[1],list[2],list[3]))
    check=input("Confirm the Details(yes/no): ")

    if check=="yes":
        list.insert(0,assign_roll())
        to_csv(list)
        choice=input("Enter another students details?(yes/no): ")
        if choice=="yes":
            c=True
        elif choice=="no":
            c=False
    elif check=="no":
        print("Try Again:(")
    