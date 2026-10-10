# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

# Number of stocks
n = int(input("Enter number of stocks: "))

# Take stock details from user
for i in range(n):
    stock = input("\nEnter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        price = stock_prices[stock]
        investment = price * quantity
        total_investment += investment

        print("Stock Price:", price)
        print("Investment:", investment)
    else:
        print("Stock not available!")

# Display total investment
print("\n===== Portfolio Summary =====")
print("Total Investment Value: $", total_investment)

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("===== Stock Portfolio Summary =====\n")
    file.write("Total Investment Value: $" + str(total_investment))

print("\nPortfolio result saved to portfolio.txt")