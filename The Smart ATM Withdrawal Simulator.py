
bank_balance =1000.00
print(f"Your available balance is :R{bank_balance}")
withdraw_Money = float(input("How much money do you want to withdraw: "))

if withdraw_Money <= bank_balance:
    bank_balance -= withdraw_Money
    print(f"Withdrawal successful! Remaining balance: R{round(bank_balance,2)}")
elif withdraw_Money <=0:
     print("Invalid amount. You must withdraw more than R0")   
else:
    print("Declined. Insufficient funds")   
