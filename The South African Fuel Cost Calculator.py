

kilometers_drive = float(input('how many kilometers they want to drive.'))
Current_petrol_price = float(input('What is the current petrol price per lite'))

#    car uses exactly 1 liter of fuel for every 10 kilometers driven.
liters_needed  = kilometers_drive/10
total_cost = liters_needed * Current_petrol_price
print(f'The liter need is: {round(liters_needed,2)}')
print(f'The total cost is: {round(total_cost,2)}')

age = input('how many kilometers they want to drive.')