def bin_to_dec():
    bin=int(input("Enter a binary number : "))
    dec=0
    i=0
    while bin!=0:
        dec+=(bin%10)*(2**i)
        i+=1
        bin//=10
    print("Decimal Equivalent is : ",dec)


def oct_to_hex():
    oct=int(input("Enter an octal number : "))
    dec=0
    i=0
    while oct!=0:
        dec+=(oct%10)*(8**i)
        i+=1
        oct//=10
    hex =""
    while dec!=0:
        rem=dec%16
        if rem<10:
            hex+=str(rem)
        else:
            hex+= chr(ord('A')+rem-10)
        dec//=16
    hex=hex[::-1]
    print("Hexadecimal Equivalent is : ", hex)


print("BINARY TO DECIMAL CONVERSION")
bin_to_dec()
print("\n\nOCTAL TO HEXADECIMAL CONVERSION")
oct_to_hex()