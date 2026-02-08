#time and hours 
#hour = int(input("enter the hour : "))
for hour in range(0,25):
    if hour == 0:
        print("12 AM - midnight")
    elif 0 < hour < 12 :
        print(f"{hour} AM ")
    elif hour == 12 :
        print("12 PM - noon")
    elif hour>=12 :
        print(f"{hour-12} PM ")
