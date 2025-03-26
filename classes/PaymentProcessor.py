class PaymentProcessor:
    def top_up_account(user, amount):
        user.update_balance(amount)
        print(f"Account topped up by {amount}. New balance: {user.balance}")
        

    def process_payment(user, amount):
        if user.balance >= amount:
            user.update_balance(-amount)
            print(f"Payment of {amount} processed. New balance: {user.balance}")
        else:
            print(f"Insufficient balance to process payment of {amount}.")
        
