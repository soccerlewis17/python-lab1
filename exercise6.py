
# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

month = input('Enter the month of the year (Jan - Dec): ').lower().capitalize()
day = int(input('Enter the day of the month: '))

if month == 'Jan' or month == 'Feb':
    print(f'{month} {day} is in winter.')
elif month == 'Mar' and day <= 19:
    print(f'{month} {day} is in winter.')
elif month == 'Mar' and day >= 20:
    print(f'{month} {day} is in spring.')
elif month == 'Apr' or month == 'May':
    print(f'{month} {day} is in spring.')
elif month == 'Jun' and day <= 20:
    print(f'{month} {day} is in spring.')
elif month == 'Jun' and day >= 20:
    print(f'{month} {day} is in summer.')
elif month == 'Jul' or month == 'Aug':
    print(f'{month} {day} is in summer.')
elif month == 'Sep' and day <= 21:
    print(f'{month} {day} is in summer.')
elif month == 'Sep' and day >= 21:
    print(f'{month} {day} is in fall.')
elif month == 'Oct' or month == 'Nov':
    print(f'{month} {day} is in fall.')
elif month == 'Dec' and day <= 20:
    print(f'{month} {day} is in fall.')
elif month == 'Dec' and day >= 21:
    print(f'{month} {day} is in winter.')