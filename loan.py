loan_amount = float(input("Enter the loan amount? "))
year = int(input("Enter year to pay? "))
month = year * 5
principal = loan_amount / month
remain_bal = loan_amount
#loan_int = pass
#monthly_loan = pass

#for loop
print("S.No\t|\tMonthly Payment\t|\tInterest\t|\tPrincipal\t|\tRemaining Balance\t|")
for count in range(1, month + 1):
    remain_bal -= principal
    loan_int = remain_bal * 0.00256
    monthly_pay = loan_int + principal
    #print(x ,monthly_pay, loan_int, round(principal, 2 ) , round(remain_bal, 2))
    print(f"|{count}\t|\t{round(monthly_pay,2)}\t\t|\t {round(loan_int, 2)}\t\t|\t{round(principal,2)}\t\t|\t {round(remain_bal,2)}\t\t|")


