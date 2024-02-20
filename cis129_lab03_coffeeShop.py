""" This is a basic register script for a coffee shop,
This script will calcluate your subtotal, tax, and total, and will print a reciept.
These first 5  lines will set the variables as a constant number. """

PRICECOFFEE = 5
PRICEMUFFIN = 4
PRICESCONES = 4.5
PRICECREPES = 6.75
TAX = .06

#These next 11 Lines will prompt the user to select how many items they would like to purchase. using the input statement.

print('***************************************')
print('My Coffee And Muffin Shop')
print('Number of Coffees Bought $',PRICECOFFEE, "Each")
numOfCoffees = int(input(": "))
print('Number of Muffins Bought $',PRICEMUFFIN, "Each")
numOfMuffins = int(input(": "))
print('Number of Scones Bought $',PRICESCONES, "Each")
numOfScones = int(input(": "))
print('Number of Crepes Bought $',PRICECREPES, "Each")
numOfCrepes = int(input(": "))
print('***************************************')

print('***************************************')
print('My Coffee and Muffin Shop Reciept')

#These next 7 lines will calculate and set the subtotal, tax, and total variables of each item based on the amount purchased. 

coffeeSubtotal = numOfCoffees * PRICECOFFEE
muffinSubtotal = numOfMuffins * PRICEMUFFIN
sconeSubtotal = numOfScones * PRICESCONES
crepeSubtotal = numOfCrepes * PRICECREPES
Subtotal = coffeeSubtotal + muffinSubtotal + sconeSubtotal + crepeSubtotal
TaxofSubtotal = Subtotal * TAX
GrandTotal = Subtotal + TaxofSubtotal

"""The final lines will print the calculated subtotal, tax and total.
 I was having an issue with the tax printing out a very large decimal number so i added the formatted print
 which will only print the first two numbers of the decimal."""

print('Subtotal: $', Subtotal)
print('Tax at 6% $', f'{TaxofSubtotal:.2f}')
print('Total: $', GrandTotal)
print('***************************************')

# :)
