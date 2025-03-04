# Define prices
coffee_price = 5.00

muffin_price = 4.00

bagel_price = 4.00

tax_rate = 0.06

# Get the number of coffees, muffins, and bagels bought from the user
num_coffees = int(input("Number of coffees bought?\n"))
num_muffins = int(input("Number of muffins bought?\n"))
num_bagels = int(input("Number of bagels bought?\n"))

num_coffees = bought = 1
num_muffins = bought = 2
# Calculate subtotal for coffees, muffins, and bagels
coffee_total = num_coffees * coffee_price
muffin_total = num_muffins * muffin_price
bagel_total = num_bagels * bagel_price

# Calculate tax and total
subtotal = coffee_total + muffin_total + bagel_total
tax = subtotal * tax_rate
total = subtotal + tax

# Display the receipt
print("\n" + "*" * 40 + "\n")
print("My Coffee and Muffin Shop Receipt")
print(f"{num_coffees} Coffee at ${coffee_price:.2f} each: $ {coffee_total:.2f}")
print(f"{num_muffins} Muffins at ${muffin_price:.2f} each: $ {muffin_total:.2f}")
print(f"{num_bagels} Bagels at ${bagel_price:.2f} each: $ {bagel_total:.2f}")
print(f"6% tax: $ {tax:.2f}")
print("---------")
print(f"Total: $ {total:.2f}")

