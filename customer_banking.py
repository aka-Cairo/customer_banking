# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("Enter the initial savings account balance: "))
    interest_rate = float(input("Enter the APR interest rate for the savings account: "))
    months = int(input("Enter the length of months to determine the amount of interest: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, interest_rate, months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Updated savings account balance: ${updated_savings_balance}")
    print(f"Interest earned: ${interest_earned}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("\nEnter the initial CD account balance: "))
    cd_interest_rate = float(input("Enter the APR interest rate for the CD account: "))
    cd_months = int(input("Enter the length of months for the CD: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"\nUpdated CD account balance: ${updated_cd_balance}")
    print(f"Interest earned: ${cd_interest_earned}")

if __name__ == "__main__":
    # Call the main function.
    main()