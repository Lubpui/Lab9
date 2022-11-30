def calculate(inputVal,listVal):
    for i in range(len(listVal)):
        if inputVal == listVal[i]:
            print("-"*30)
            print("Your Value : ",listVal[i],'in index ',i)
            print("-"*30)

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

