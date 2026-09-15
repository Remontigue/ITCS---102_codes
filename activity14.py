# age (integer)
# is_employed (boolean)
# credit_score (integer)
# annual_income (float)
# has_collateral (boolean)

age = int(input("Enter your age    --> "))
is_employed = bool(input("Are your currently employed ---> "))
credit_score = float(input("Credit Score    --> "))
annual_income = float(input("What is your annual salary --> "))
has_collateral - bool(input("Do you have any collateral (True / False ) ---> "))


base_rate = 0.0 #default value

if age >= 21 and is_employed == True:
    print("Accepted Baseline Criteria")
    if credit_score >= 750: #tier1
        print("You have a high credit score")
        if annual_income >= 100000:
            print("You have a high annual salary")
            base_rate = 4.5
            print("Your base rate is ", base_rate)
        else:
            base_rate = 5.0
            print("Your base rate is ", base_rate)
    elif credit_score >= 600 and credit_score < 750: #tier2
        print("Your credit score is less than 750")
        if has_collateral == True:
            print("you have a collateral ")
            base_rate = 7.0
            print("Your base rate is ", base_rate)
        elif annual_income <= 40000:
            print("Low annual income")
            base_rate = 9.0
            print("Your base rate is ", base_rate)
        else:
            base_rate = 8.0
            print("Your base rate is ", base_rate)
    elif credit_score <= 600: #tier3
        print("Rejected: Credit score too low")
else:
    print("Invalid details")