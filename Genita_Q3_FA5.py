names = ["Me", "Lia", "Jake"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

daily_totals = []

for day in range(len(days)):
    total = 0
    for person in range(len(steps)):
        total += steps[person][day]
    daily_totals.append(total)
    print(days[day], "total steps:", total)

print()

most_active_total = daily_totals[0]
most_active_day = days[0]

for i in range(len(daily_totals)):
    if daily_totals[i] > most_active_total:
        most_active_total = daily_totals[i]
        most_active_day = days[i]

print("Most active day:", most_active_day)
print("Steps on most active day:", most_active_total)

