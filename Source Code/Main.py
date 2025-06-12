import random
import time

# Get user preferences
try:
    initial_balance = float(input("Enter your initial balance (e.g., 1800): "))
    initial_bet = float(input("Enter your initial bet amount (e.g., 0.18): "))
    target_profit = float(input("Enter your target profit (e.g., 10): "))
    max_losses = int(input("Enter max allowed consecutive losses (e.g., 13): "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()

balance = initial_balance
bet_amount = initial_bet
consecutive_losses = 0
start_time = time.time()
bets = 0

print("\nStarting Auto Bet...\n")

while True:
    profit = balance - initial_balance
    if profit >= target_profit:
        print(f"\nTarget profit of ₹{target_profit:.2f} reached!")
        break

    if consecutive_losses == max_losses:
        print(f"\nStopped after {max_losses} consecutive losses.")
        break

    if balance < bet_amount:
        print("\nInsufficient balance to continue.")
        break

    bets += 1
    current_bet = bet_amount
    win = random.random() < 0.495
    balance -= current_bet

    if win:
        balance += current_bet * 2
        bet_amount = initial_bet
        consecutive_losses = 0
        result = "WIN"
    else:
        consecutive_losses += 1
        bet_amount *= 2
        result = "LOSS"

    elapsed_minutes = (time.time() - start_time) / 60
    avg_profit_per_min = profit / elapsed_minutes if elapsed_minutes > 0 else 0

    print(f"{result}: Bet={current_bet:.2f} | Balance={balance:.2f} | Profit={profit:.2f} | Avg/Min={avg_profit_per_min:.2f}")

    time.sleep(1/3)
