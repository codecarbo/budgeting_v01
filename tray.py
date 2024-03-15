def print_sum(data):
    amounts = data["Betrag"].to_list()
    amounts = [float(amount.replace(",", ".")) for amount in amounts]

    income_list = [amount for amount in amounts if amount > 0]
    expense_list = [amount for amount in amounts if amount < 0]

    income = sum(income_list)
    expenses = sum(expense_list)
    total = income + expenses

    print(f"Einnahmen: {income}")
    print(f"Ausgaben: {expenses}")
    print(f"Summe: {"{:.2f}".format(total)}")