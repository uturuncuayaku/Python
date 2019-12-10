with open("data.txt", "r") as f:
    total = 0
    for line in f:
        stripped = line.strip()
        if stripped:
            cents = float(stripped) * 100
            total += int(cents)

print(total/100)

