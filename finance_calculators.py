import math

# Ask user whether they require the investment or bond calculator and transpose input to lowercase.
calc_type = input("Choose either 'investment' or 'bond' from the menu below to proceed:\n"
"___________________________________________________________________________________\n"
"\n"
"investment   - to calculate the amount of interest you will earn on your investment \n"
"bond         - to calculate the amount you will have to pay on a home loan\n"
"Choice: ").lower()


# If user requests INVESTMENT, ask for : Deposit value / Interest rate / Repayment span (years) / Interest type required.
if calc_type == "investment":
    deposit = float(input("Enter the value of your deposit: "))
    rate = float(input("Enter your interest rate (exclude the % symbol): "))
    years = float(input("How many years do you plan on investing?: "))
    interest = input("Would you prefer simple or compound interest?: ").lower()


# If interest = simple: utilise simple interest formula to calculate earnings total and print total to user.
    if interest == "simple":
        total = deposit*(1 + (rate/100) * years)
        print(f"After {years} years your investment will be worth: £{round(total,2)}")


# If interest = compound: utilise compound interest formula to calculate earnings total and print total to user.
    else:
        total = deposit * math.pow((1 + (rate/100)), years)
        print(f"After {years} years your investment will be worth: £{round(total,2)}")

        
# If user requests BOND: ask for : House value / Interest rate / Repayment span (months).
elif calc_type == "bond":
    house = float(input("What is the current value of your house?: "))
    rate = float(input("Enter your interest rate (exclude the % symbol): "))
    months = float(input("How many months do you intend to pay your bond over?: "))

    
# utilise bond formula to calculate total monthly repayments and print total to user.
    monthly_interest = (rate/100)/12
    total = (monthly_interest * house) / ( 1 - (math.pow((1 + monthly_interest), -months)))
    print(f"Each month you will pay £{round(total,2)}")


# If neither investment or bond is chosen, prompt user to re-enter their choice.
else:
    print("Something went wrong. Please enter your choice from the given menu items.")