def calculate(inputVal,listVal):

    while len(listVal) > 1:
        mid = int(len(listVal)/2)
        midVal = listVal[mid-1]
        print(midVal)
        if inputVal > midVal:
            listVal = listVal[mid :]
            print(listVal)
        else:
            listVal = listVal[: mid]
            print(listVal)

listVal = [7,10,12,14,16,20,29,37]
print('Data : ',listVal)
i = 1
while i != '0' :
    inputVal = input("Enter the number you want to find : ")
    if int(inputVal) in listVal:
        calculate(int(inputVal),listVal)
        i = input("Enter 0 to end / 1 to continue : ")
    else:
        print("-"*45)
        print("\n!!!This number doesn't exist in the list !!!\n")
        print("-"*45,"\n")
