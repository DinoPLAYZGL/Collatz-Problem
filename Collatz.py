Bool = False
AllDigits = []

Even = 0
Odd = 0

def SumList(ListVal):
    Total = 0
    for i in ListVal:
        Total =  Total + i
    return Total

def MaxVal(ListVal):
    max_Val = ListVal[0]
    for i in range(len(ListVal)):
        if ListVal[i] > max_Val:
            max_Val = ListVal[i]
    return max_Val

def FullList (ListVal):
    ListMaxVal = 0
    for i in range(len(ListVal)):
        ListMaxVal+=1
    return ListMaxVal


while True:

    Even = 0
    Odd = 0 
    AllDigits = []
    
    Digit = input("INPUT - ")

    x = int(Digit)
    while True:
        
        AllDigits.append(x)
        #print( "FIRST INTIGER - " + str(x))
        
        if x == 1:

            print( "----------------------------------\n")
            print( "=====================================")
            print( "FIRST INP   - " + str(AllDigits[0]))
            print( "FINALOUTPUT - " + str(x))
            print( "LIST MAX    - " + str(FullList(AllDigits)-1))
            print( "=====================================")  
            print( "ALL VALUES  - " + str(AllDigits))
            print( "=====================================")
            print( "SUM VALUES  - " + str(SumList(AllDigits)))
            print( "MAX VALUE   - " + str(MaxVal(AllDigits)))
            print( "EVEN OUTPT  - " + str(Even))
            print( "ODD OUTPT   - " + str(Odd))
            print( "=====================================")
            break
        elif x == 0:
            print("Null - INFINITY VALUE OUTPUT")
            break
        else:
            if x%2 == 0:
                Bool = True
                Even+=1
            else:
                Bool = False
                Odd+=1
                
            if Bool:
                #print( "EVEN OUTPUT SECTION VAL - " + str(x))
                x = x/2
            else:
                #print( "ODD OUTPUT SECTION VAL - " + str(x))
                x = 3 * x + 1

            #print( "Answer OUTPUT - " + str(x))
            #print( "----------------------------------")

    
            
        
        
