# Author: Llobrera, John Aaron B.
    # Affiliation: BS Statistics, Institute of Statistics, University of the Philippines Los Baños
    # E-Mail: jbllobrera@up.edu.ph

# Code Description:
    # This program is a simple cake ordering system called SILVERLOCK.
    # It allows users to choose cakes, apply discount coupons, compute the total price with additional charges and discounts,
    # and finally, pay for the order.

# Function to display the main menu options
def main_menu():
    print("\nWELCOME TO SILVERLOCK!")
    print("Main Menu:")
    print("[1] Choose cake")
    print("[2] Enter discount coupon")
    print("[3] Compute total and pay")
    print("[0] Exit")

# Display the available cake menu items and return the total price of selected items
def choose_cake():
    menu = {
        1: ("Black Forest Cake", 804.00),
        2: ("Luscious Mocha", 689.00),
        3: ("Royal Fudge Cake", 756.00),
        4: ("Chocolate Caramel", 529.00)
    }

    total_price = 0
    while True:
        print("\nCake Menu:")
        for item_num, (cake_name, price) in menu.items():
            print(f"[{item_num}] {cake_name}: P{price:.2f}")
        print("[0] Back to main menu")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 0:
                print(f"\nTotal Price: P{total_price:.2f}")
                return total_price
            elif choice in menu:
                total_price += menu[choice][1]
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Ask the user for a discount coupon and return the corresponding discount amount.
def enter_discount_coupon(total_price):
    coupon_codes = {
        "PAYDAY15": 0.15,
        "PICKUP10": 0.10
    }
    
    coupon = input("\nEnter discount coupon (case-sensitive): ")
    if coupon in coupon_codes:
        discount = coupon_codes[coupon] * total_price
        print("Your current price to pay is: P{:.2f}".format(total_price - discount))
        return discount  # Return the discount amount
    else:
        print("Coupon not found. No discount applied.")
        return 0  # Return 0 only when coupon is not found

# Compute the total price with additional charges and discounts.
def compute_total_and_pay(total_price, discount):
    delivery_charge = 0.07 * total_price
    total_with_delivery = total_price + delivery_charge

    # Apply discount from the voucher
    total_with_discount = total_price - discount

    # Ensure the total price doesn't go negative
    total_with_discount = max(0, total_with_discount)

    total_with_discount_and_delivery = total_with_discount * 1.07

    has_pwd_or_senior_id = input("\nDo you have a PWD ID or Senior Citizen ID? (y/n): ").lower()
    if has_pwd_or_senior_id == 'y':
        total_with_discount_and_delivery *= 0.8

    print("Total price with 7% delivery charge: P{:.2f}".format(total_with_discount_and_delivery))

    amount_paid = float(input("Enter the amount you want to pay: "))
    change = amount_paid - total_with_discount_and_delivery
    if change >= 0:
        print("Change: P{:.2f}".format(change))
        print('\nThank you for shopping!')
    else:
        print("Insufficient payment. Add: P{:.2f}".format(change*-1))

# Main function to run the program
def main():
    total_price = 0
    discount = 0  # Initialize discount outside the loop
    
    while True:
        main_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 0:
                print("Thank you for availing our service!")
                break
            elif choice == 1:
                total_price = choose_cake()
            elif choice == 2:
                if total_price != 0:
                    discount = enter_discount_coupon(total_price)
                else:
                    print("Please select a cake first.")
            elif choice == 3:
                if total_price != 0:
                    compute_total_and_pay(total_price, discount)
                else:
                    print("Please select a cake first.")
            else:
                print("Invalid choice. Please enter a number from the menu.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Execution
if __name__ == "__main__":
    main()
