prices = [105, 110, 108, 112, 115, 116, 114]

print("3-day rolling averages:")

for i in range(len(prices) - 2):
    total = sum(prices[i:i+3])
    average = total / 3
    print(round(average, 2))
