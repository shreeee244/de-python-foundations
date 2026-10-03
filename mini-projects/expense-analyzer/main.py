import csv

total = 0
category_totals = {}

highest_expense = 0
highest_category = ""

with open("expenses.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        amount = float(row["amount"])
        category = row["category"]

        total = total + amount

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

        if amount > highest_expense:
            highest_expense = amount
            highest_category = category

print("Total spending:", total)
print(category_totals)
print("Highest expense:", highest_expense)
print("Category:", highest_category)