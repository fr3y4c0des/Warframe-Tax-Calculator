def calculate_trade_tax(platinum_amount, clan_tax_percentage):
    base_credit_per_platinum = 500
    tax_multiplier = 1 + clan_tax_percentage / 100
    total_credit_per_platinum = base_credit_per_platinum * tax_multiplier
    total_credits = platinum_amount * total_credit_per_platinum
    return total_credits


platinum_amount = float(input("Enter the amount of platinum: "))
clan_tax_percentage = float(input("Enter the clan tax percentage: "))


result = calculate_trade_tax(platinum_amount, clan_tax_percentage)
print(f"Total credits with {clan_tax_percentage}% clan tax for {platinum_amount} platinum: {result} credits")
