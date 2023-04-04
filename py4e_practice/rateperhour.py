inp = input('Enter Hours:')
hrs = int(inp)
h = float(hrs)

rate = input('Enter Rate:')
rt = float(rate)

ot_rate = rt * 1.5

if h <= 40:
    pay = h * rt
elif h > 40:
    ot_hours = h - 40
    pay = (ot_hours * ot_rate) + (10.50 * 40)
print(pay)
