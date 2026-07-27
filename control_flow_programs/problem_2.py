'''calculate the electricity bill'''

'''First 100 units → $0
Next 100 units → $5 per unit
Above 200 → $10 per unit'''

def bill(units):
    if units<=100:
        return units*0
    elif units<=200:
        return units*5
    else :
        return units*10
print(f'the amount of current bill for 105 units is {bill(201)}')     