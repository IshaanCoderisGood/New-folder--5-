def power4(userinput):
    if userinput <= 0:
        return False
    else:
       return  userinput & (userinput - 1 ) == 0 and userinput & 0x55555555 != 0

userinput = int(input("Enter number: "))

if power4(userinput):
    print("It is power of 4")
else: 
    print("It is not power of 4")