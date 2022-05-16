# x=range(30)
# for y in x:
#     if y%3==0:
#         print(f"{y} is divisible by 3")
#     elif y%5==0:
#         print(f"{y} is divisible by 5")
#     elif y%7==0:
#         print(f"{y} is divisible by 7")
#     else:
#         print(f"{y} is not divisible by 3,5 or 7")
        # . Write a program to accept percentage from the user and display the grade according to the following criteria:

        #  Marks                                    Grade
        #  > 90                                         A
        #  > 80 and <= 90                       B
        #  >= 60 and <= 80                       C
        #  below 60         
        #         D

x=(input("Percentage of student: "))
if x>90:
        print("A")
elif x>80 and x<=90:
        print("B")
elif x >= 60 and x<= 80:
        print("c")

else: 
        print("D")