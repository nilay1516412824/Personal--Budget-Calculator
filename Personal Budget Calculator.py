income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

remaining = income - expenses

print("\n--- Budget Summary ---")
print(f"Income: {income:.2f}")
print(f"Expenses: {expenses:.2f}")
print(f"Remaining: {remaining:.2f}")

if remaining < 0:
    advice = "You are overspending!"
elif remaining < income * 0.2:
    advice = "Try to save at least 20 percent of your income."
else:
    advice = "Good! You're saving well."

print("Advice:", advice)

# Save results to a text file
with open("budget_report.txt", "w") as file:
    file.write("--- Budget Summary ---\n")
    file.write(f"Income: {income:.2f}\n")
    file.write(f"Expenses: {expenses:.2f}\n")
    file.write(f"Remaining: {remaining:.2f}\n")
    file.write(f"Advice: {advice}\n")

print("\nBudget report saved to 'budget_report.txt'")