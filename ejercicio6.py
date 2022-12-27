def pasosRobot(n):
    if n==1 or n==2:
        numPasos= n
    else:
        numPasos=pasosRobot(n-1)+pasosRobot(n-2)
    return numPasos
print(pasosRobot(5))
