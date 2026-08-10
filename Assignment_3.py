"""
Experiment 3: Design Patterns in Python
Configurable Payment Processing System using the Strategy Pattern - Menu Driven Version
"""

from abc import ABC, abstractmethod


# ---------------- Strategy Interface ----------------
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# ---------------- Concrete Strategies ----------------
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        masked = self.card_number[-4:].rjust(len(self.card_number), "*")
        print(f"Paid Rs.{amount} using Credit Card (Card No: {masked})")


# om kutwal sy-12 roll no. 70
class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paid Rs.{amount} using PayPal (Account: {self.email})")


class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_id):
        self.wallet_id = wallet_id

    def pay(self, amount):
        print(f"Paid Rs.{amount} using Bitcoin (Wallet: {self.wallet_id})")


# ---------------- Context Class ----------------
class PaymentProcessor:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        if self.strategy is None:
            print("No payment method selected yet.")
            return
        self.strategy.pay(amount)


def print_menu():
    print("\n===== PAYMENT PROCESSING SYSTEM =====")
    print("1. Select Credit Card as payment method")
    print("2. Select PayPal as payment method")
    print("3. Select Bitcoin as payment method")
    print("4. Process a payment")
    print("5. Show currently selected strategy")
    print("6. Exit")
    print("=======================================")


def main():
    processor = PaymentProcessor()

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            card_number = input("Enter credit card number: ").strip()
            processor.set_strategy(CreditCardPayment(card_number))
            print("Payment method set to Credit Card.")

        elif choice == "2":
            email = input("Enter PayPal email: ").strip()
            processor.set_strategy(PayPalPayment(email))
            print("Payment method set to PayPal.")

        elif choice == "3":
            wallet_id = input("Enter Bitcoin wallet ID: ").strip()
            processor.set_strategy(BitcoinPayment(wallet_id))
            print("Payment method set to Bitcoin.")

        elif choice == "4":
            if processor.strategy is None:
                print("Please select a payment method first (option 1, 2, or 3).")
                continue
            amount = input("Enter amount to pay: ").strip()
            try:
                amount = float(amount)
                processor.process_payment(amount)
            except ValueError:
                print("Invalid amount entered.")

        elif choice == "5":
            if processor.strategy is None:
                print("No payment method selected yet.")
            else:
                print(f"Currently selected strategy: {type(processor.strategy).__name__}")

        elif choice == "6":
            print("Exiting the Payment Processing System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
