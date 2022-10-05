income = int(input())
if income >= 132407:
    tax = 28
elif income >= 42708:
    tax = 25
elif income >= 15528:
    tax = 15
else:
    tax = 0
calculated_tax = income * (tax / 100)
print("The tax for {} is {}%. That is {} dollars!".format(income, tax, round(calculated_tax)))
