# Program to input a number upto 5 digits and print it in words
number = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
nty = ["", "", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninty"]
tens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

array_decimal = []
d = [0, 0, 0, 0, 0, 0, 0, 0]
i = 0
point = ""
n = str(input("Enter a number with decimal:- "))
split = n.split(".")
n = int(split[0])
deci = int(split[1])
dec = split[1]

while deci != 0:
    array_decimal.append(deci % 10)
    deci = deci // 10

while n > 0:
    d[i] = n % 10
    i += 1
    n = n // 10

if n > 99999999:
    print("Cant solve for more than 5 digits")
else:

    num = ""
    if d[7] != 0:
        num += number[d[7]] + " Crore "
    if d[6] != 0:
        if (d[6] == 1):
            num += tens[d[5]] + " Lakh "
        else:
            num += nty[d[6]] + " " + number[d[5]] + " Lakh "
    else:
        if d[5] != 0:
            num += number[d[5]] + " Lakh "
    if d[4] != 0:
        if (d[4] == 1):
            num += tens[d[3]] + " Thousand "
        else:
            num += nty[d[4]] + " " + number[d[3]] + " Thousand "
    else:
        if d[3] != 0:
            num += number[d[3]] + " Thousand "
    if d[2] != 0:
        num += number[d[2]] + " Hundred and "
    if d[2] == 0:
        num += " and "
    if d[1] != 0:
        if (d[1] == 1):
            num += tens[d[0]]
        else:
            num += nty[d[1]] + " " + number[d[0]]
    else:
        if d[0] != 0:
            num += number[d[0]]

if len(array_decimal) == 1:
    point = "  " + dec + "/10"
elif len(array_decimal) == 2:
    point = "  " + dec + "/100"
elif len(array_decimal) == 3:
    point = "  " + dec + "/1000"
elif len(array_decimal) == 4:
    point = "  " + dec + "/10000"

print("Rs " + num + point + " Only")
