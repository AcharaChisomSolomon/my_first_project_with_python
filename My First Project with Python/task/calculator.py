print('''Earned amount:
Bubblegum: $202
Toffee: $118
Ice cream: $2250
Milk chocolate: $1680
Doughnut: $1075
Pancake: $80
''')
print('Income: $5405')

revenue = 5405
print('Staff expenses:')
s_expense = int(input())
print('Other expenses:')
o_expense = int(input())

print('Net Income: $' + str(revenue - s_expense - o_expense))
