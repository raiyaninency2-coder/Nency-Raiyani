# print element of list in single line 
students = ["nency","niyati","dev"]
marks = [98,97,92,36.50,37.75,35.50]
def l(list):
    for item in list:
        print(item,end="")
    return item
l(students)
l(marks)