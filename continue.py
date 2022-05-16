x=1
y=20
while x<y:
    x+=1
    if x%2!=0:
        continue
    #The continue statement skips the remainder of the current iteration
    print(x)