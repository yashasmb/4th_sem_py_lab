import re

#Without using Regular Expression:

def isphonenumber(number):
    if len(number) != 12:
        return False
    if number[3] != '-' or number[7] != '-':
        return False
    for i in range(12):
        if i == 3 or i == 7:
            continue
        if not number[i].isdigit():
            return False
    return True

#using RegExpr

def isphonenumber_reg(number):
    pattern = r"\d{3}-\d{3}-\d{4}"
    match = re.fullmatch(pattern, number)
    return match is not None

#main function
ph_num=str(input('enter the phone number in ddd-ddd-dddd format to validate'))
print('enter your choice')
print('Press 1.without RegExpression \t 2. using RegExpression')
choice=int(input())
if choice==1:
    res=isphonenumber(ph_num)
    if res==True:
        print('The phone No.'+str(ph_num)+' is valid')
    else:
        print('The Phone No.' + str(ph_num) + ' is invalid')
elif choice==2:
    res = isphonenumber_reg(ph_num)
    if res == True:
        print('The phone No.' + str(ph_num) + ' is valid')
    else:
        print('The Phone No.' + str(ph_num) + ' is invalid')
else:
    print('enter the correct option')
    exit(0)