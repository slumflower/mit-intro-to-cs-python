balance = 3329
annualInterestRate = 0.2

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
