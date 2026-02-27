def sip_calculator(monthly_sip, annual_return, years):
    monthly_rate = annual_return / 12 / 100
    total_months = years * 12

    invested_amount = monthly_sip * total_months
    final_value = 0

    for m in range(total_months):
        months_remaining = total_months - m
        final_value += monthly_sip * ((1 + monthly_rate) ** months_remaining)

    profit = final_value - invested_amount

    return invested_amount, round(final_value, 2), round(profit, 2)


# -------- User Input --------
monthly_sip = float(input("Enter monthly SIP amount (₹): "))
annual_return = float(input("Enter expected annual return (%): "))
years = int(input("Enter SIP duration (in years): "))

invested, value, profit = sip_calculator(monthly_sip, annual_return, years)

print("\n----- SIP RESULT -----")
print("Total Invested Amount: ₹", invested)
print("Final Value: ₹", value)
print("Total Profit: ₹", profit)