#Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. 
#By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

#In this problem, we will not be dealing with a minimum monthly payment rate.




monthlyInterest = annualInterestRate/12
fixedPayment = 10
new = balance


while balacne >= fixedPayment:
    balance = new
    for i in range(12):
        unpaid_balance = new - fixedPayment
        new = unpaid_balance + monthlyInterest * unpaid_balance

        if new <= 0:
            print(round(fixedPayment, 2))
        
        else:
            fixedPayment += 10
            balance = new
            
print("Lowest Payment:", fixedPayment)
