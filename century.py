year = '2154'

f = int(year)//100 + 1
if f < 20:
    l = 'th'
elif f % 10 == 1:
    l = 'st'
elif f % 10 == 2:
    l = 'nd'
elif f % 10 == 3:
    l = 'st'
else:
    l = 'th'
century = f'{f}{l}'
print(century)
