# simple phone number format

phoneNumber = str(input("Please input the phone number: "))

digit = []

for i in phoneNumber:
    digit.append(i)

#print(digit)

numberString = "(" + digit[0] + digit[1] + digit [2] + ") " + digit[3] + digit[4] + digit[5] \
    + "-" + digit[6] + digit[7] + digit[8] + digit[9]

print(numberString)

