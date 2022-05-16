#  Write a program to accept a number from 1 to 7 and display 
#  the name of the day like 1 for Sunday , 2 for Monday and so on.
# x=range(1,7)
x=(input("Insert a number: "))
if x==1:   
    print("Monday")
elif x==2:
    print("Tuesday")
elif x==3:
    print("Wednesday")
elif x==4:
    print("Thursday")
elif x==5:
    print("Friday")
elif x==6:
    print("Saturdsy")
else:
    print("num")    