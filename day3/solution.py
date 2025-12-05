with open("input", "r") as f:
    banks = f.read().splitlines()

def resolve_bank(bank_joltages, remaining_batteries, battery_string = ""):
    if remaining_batteries == 1:
        next_bat_idx = bank_joltages.index(max(bank_joltages))
    else:
        next_bat_idx = bank_joltages.index(max(bank_joltages[:-(remaining_batteries-1)]))
    battery_string += str(bank_joltages[next_bat_idx])
    remaining_batteries -= 1
    if remaining_batteries == 0:
        return battery_string
    else:
        return resolve_bank(bank_joltages[next_bat_idx + 1:], remaining_batteries, battery_string)

total_joltage = 0
total_joltage_p2 = 0
for bank in banks:
    bat_joltages = [int(bat) for bat in bank]
    total_joltage += int(resolve_bank(bat_joltages, 2))
    total_joltage_p2 += int(resolve_bank(bat_joltages, 12))

print("P1:", total_joltage)
print("P2:", total_joltage_p2)
