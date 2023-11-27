#Challenge2.

#Ask the user: "Insert your first number#
number1 = int (input("Inser your first number : "))

#Ask the user: "Insert your second number#
number2 = int (input("Iner your second number : "))

#Ask the user: "Insert the operation#
operation = input("Insert the operation : ")

if operation == "+":
    print ("result is ", number1 + number2)
elif operation == "-":
    print ("result is ",number1 - number2)
elif operation == "*":
    print ("result is",number1 * number2)
#If the user enter another operations#
else:
    print ("We don't support this operation")
    
#print "Thanks for using our software"#
print ("Thanks for using our software.")

