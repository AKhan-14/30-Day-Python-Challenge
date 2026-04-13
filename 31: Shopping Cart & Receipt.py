# The Challenge: Create a program that allows a user to input multiple items
# and their corresponding prices.

# --- SECTION 1: INITIALIZATION ---
# 1. Create an empty container to hold all items (What structure did we use on Day 6?)
shopping_cart = {}

# --- SECTION 2: THE DATA ENTRY LOOP ---
# 2. Start a loop that runs until the user is finished.
while True:
    # 3. Ask for the Item Name.
    item = input("What is the items name? (Or type 'done' to summarise) ").strip().lower()
    # 4. Check if the user typed "done". 
    # (Hint: use .lower() to handle "DONE" or "Done").
    # If they did, exit the loop.
    if item == "done":
        break
    # 5. Start a sub-loop or a check to get a VALID price.
    # (Why use a loop here? So if they type "abc", you can ask for the price AGAIN 
    # without losing the Item Name).
    while True:
        price = input("What is the price of the item? £")
        # 6. Try to convert the input to a float.
        # 7. If successful, save it and break this sub-loop.
        # 8. If it fails (ValueError), print an error message and let the loop repeat.
        try:
            price = float(price)
            break
        except ValueError:
            print("That is not a number. Try again")

    # 9. "Glue" the Name and the Price together into a Dictionary.
    # 10. Add that dictionary to your main container from Section 1.
    shopping_cart[item] = price
    print("New item added successfully! ")
    # print(shopping_cart)

# --- SECTION 3: THE RECEIPT GENERATOR ---
# 11. Create a variable to keep track of the Total Cost (start at 0).
total_cost = 0
item_number = 1
# 12. Print a nice Header (e.g., "--- YOUR RECEIPT ---").
print("\n")
print("--- YOUR RECEIPT ---")
# 13. Loop through your container of items.
for item, price in shopping_cart.items():
    # 14. For each item, print the name and the price.
    # (Hint: Use f-string formatting :.2f to show 2 decimal places).
    print(f"{item_number}. {item.upper()} : £{price:.2f}")
    # 15. Add the current item's price to the Total Cost variable.
    total_cost += price
    item_number += 1
# 16. Print a footer with the final Total Cost.
print("--------------------")
print(f"Total: {total_cost:.2f}")
print("\n")