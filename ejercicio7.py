def pasosRobot(n):
    if n==1 or n==2:
        return n
    elif n==3:
        return n+1
    else:
        return pasosRobot(n-3)+pasosRobot(n-2)+ pasosRobot(n-1)
print(pasosRobot(4))

