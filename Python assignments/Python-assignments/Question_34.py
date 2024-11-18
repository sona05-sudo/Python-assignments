"""Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
¡
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500"""

def compute_net_amount():
    net_amount = 0
    print("Enter transaction log (D for deposit, W for withdrawal, enter 'done' to finish):")
    
    while True:
        transaction = input()
        if transaction.lower() == 'done':  # Check for the end of input
            break
        
        # Split the transaction into type and amount
        action, amount = transaction.split()
        amount = int(amount)  # Convert amount to integer
        
        # Update net amount based on the action
        if action.upper() == 'D':
            net_amount += amount  # Deposit
        elif action.upper() == 'W':
            net_amount -= amount  # Withdrawal

    # Print the final net amount
    print("Net Amount:", net_amount)

# Call the function to execute the program
compute_net_amount()
