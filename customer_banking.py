from cd_account import create_cd_account
from savings_account import create_savings_account

# Function to check if the input is can be converted into float
def is_floatable(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    while True:
        savings_balance = input("Enter the initial savings account balance: ")
        if is_floatable(savings_balance):
            savings_balance = float(savings_balance)
            break
        else:
            print("Invalid input. Please enter a valid number.")

    while True:
        interest_rate = input("Enter the APR interest rate for the savings account: ")
        if is_floatable(interest_rate):
            interest_rate = float(interest_rate)
            break
        else:
            print("Invalid input. Please enter a valid number.")

    while True:
        months = input("Enter the length of months to determine the amount of interest: ")
        if months.isdigit():
            months = int(months)
            break
        else:
            print("Invalid input. Please enter a valid number of whole months. (No decimals!)")

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, interest_rate, months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print("__________________________________")
    print(f"\nInterest earned on savings: ${interest_earned:,.2f}")
    print(f"Updated savings account balance: ${updated_savings_balance:,.3f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    while True:
        cd_balance = input("\nEnter the initial CD account balance: ")
        if is_floatable(cd_balance):
            cd_balance = float(cd_balance)
            break
        else:
            print("Invalid input. Please enter a valid number.")

    while True:
        cd_interest_rate = input("Enter the APR interest rate for the CD account: ")
        if is_floatable(cd_interest_rate):
            cd_interest_rate = float(cd_interest_rate)
            break
        else:
            print("Invalid input. Please enter a valid number.")

    while True:
        cd_months = input("Enter the length of (whole) months for the CD: ")
        if cd_months.isdigit():
            cd_months = int(cd_months)
            break
        else:
            print("Invalid input. Please enter a valid number of whole months. (No decimals!)")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print("__________________________________")
    print(f"\nInterest earned on your CD: ${cd_interest_earned:,.2f}")
    print(f"Updated CD account balance: ${updated_cd_balance:,.3f}")

if __name__ == "__main__":1
    # Call the main function.
main()