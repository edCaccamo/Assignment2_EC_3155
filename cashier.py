class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        try:
            num_large_dollar = int(input("how many large dollar coins?: "))
            num_half_dollar = int(input("how many half dollar coins?: "))
            num_quarters = int(input("how many quarters?: "))
            num_nickels = int(input("how many nickels?: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            return 0

        total = (num_large_dollar * 1.0) + (num_half_dollar * 0.5) + (num_quarters * 0.25) + (num_nickels * 0.05)
        total = round(total, 2)
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False
