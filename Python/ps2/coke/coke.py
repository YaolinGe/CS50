due = 50
coins = [5, 10, 25]
remaining = due
while remaining > 0:
    print(f"Amount Due: {remaining}")
    coin = int(input("Insert Coin: ").strip())
    if coin in coins:
        remaining -= coin

print(f"Change Owed: {-remaining}")

# submit50 cs50/problems/2022/python/coke