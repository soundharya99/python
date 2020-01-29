def printPascal(n):
    for line in range(1,n+1): 
        j = 1
        for i in range(1,line+1): 
            print (j)
            j = j * (line - i) / i 
        print ("\t\n\t")
n = 5
printPascal(n)
