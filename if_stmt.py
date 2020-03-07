price=1000000

is_good_credit=True

if is_good_credit:
    down_paymnt=0.1*price
else:
    down_paymnt=0.2*price

print(f"Down payment will be {down_paymnt}")
