class Checkbook:
    """
    Class Description:
        This class represents a simple checkbook allowing deposits, withdrawals,
        and balance inquiries.

    Attributes:
        balance (float): The current account balance, initialized to 0.0.
    """

    def __init__(self):
        """Initializes the balance to 0.0"""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits an amount into the account.

        Parameters:
            amount (float): The amount to deposit.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited: ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws an amount from the account if sufficient funds exist.

        Parameters:
            amount (float): The amount to withdraw.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew: ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Displays the current account balance.

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function for user interaction.
    Handles commands: deposit, withdraw, balance, exit.
    Uses error handling to prevent crashes from invalid input.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            print("Goodbye!")
            break
        elif action.lower() in ('deposit', 'withdraw'):
            try:
                amount = float(input("Enter the amount: $"))
                if amount < 0:
                    print("Amount cannot be negative.")
                    continue
                if action.lower() == 'deposit':
                    cb.deposit(amount)
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input! Please enter a number.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
