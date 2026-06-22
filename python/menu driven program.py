# menu driven program :
stack = []
while True :
    print("\n 1. insert")
    print("2 . delete")
    print("3 . display")
    print("4 . exit")
    n = int(input("Enter your choice  : "))
    if n == 1 :
        i = int(input("Enter the value : "))
        stack.append(i)
    elif n == 2:
        if len(stack)==0:
            print("empty list")
        else :
            stack.pop(0)
    elif n == 3:
        if len(stack) == 0:
            print("Empty list")
        else :
            print(stack)
    elif n == 4:
        print("Exiting group")
        break
    else :
        print("Invalid choice")
            

