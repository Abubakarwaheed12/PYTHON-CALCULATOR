# CALCULATOR  USING PYTHON PROGRAMMING LANGUAGE

print("SELECT AN OPERATION TO PERFORM  . . . ")
print("1:  ADD")
print("2:  MULTIPLY")
print("3:  DIVIDE")
print("4:  SUBSTRACTION")

operation=int(input())
if operation==1:
    num1=int(input("ENTER FIRST NUMBER ?"))
    num2=int(input("ENTER SECOND NUMBER ?"))
    num3=num1+num2
    print(f"THE SUM IS :  {num3}")
elif operation==2:
    num1=int(input("ENTER FIRST NUMBER ?"))
    num2=int(input("ENTER SECOND NUMBER ?"))
    num3=num1*num2
    print(f"THE MULTIPLY IS :  {num3}")
elif operation==3:
    num1=int(input("ENTER FIRST NUMBER ?"))
    num2=int(input("ENTER SECOND NUMBER ?"))
    num3=num1/num2
    print(f"THE DIVISION IS :  {num3}")
elif operation==4:
    num1=int(input("ENTER FIRST NUMBER ?"))
    num2=int(input("ENTER SECOND NUMBER ?"))
    num3=num1-num2
    print(f"THE SUBSTRACTION IS :  {num3}")
else:
    print("INVALID INPUT")