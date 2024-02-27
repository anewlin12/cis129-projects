#Made by Anthony Newlin, 02/23/24
#This script will calculate the monthly sales bonus as well as the individual employee bonus,
# based on monthly sales and sales increase using if elif statments.


monthlySales = (0) #monthly sales amount
storeAmount = (0) #store bonus amount
empAmount = (0) #employee bonus amount
salesIncrease = (0) #percent of sales increase
prompt = ('Enter the monthly sales: $')

#aquire monthly sales
monthlySales = float(input(prompt))

if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

# this code gets the percent of increase in sales.
salesIncrease = float(input('Enter percent of sales increase: '))
salesIncrease = salesIncrease / 100

# this code will determine the bonus to employees
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0

#This code will print the bonus info
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)
if (storeAmount == 6000) and (empAmount == 75):
    print('Congrats! You have reached the highest bonus amounts possible! ')