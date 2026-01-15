names = ["Me", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

totals = []

for i in range(len(steps)):
    total_steps = sum(steps[i])
    totals.append(total_steps)
    print(names[i], "total steps:", total_steps)
print()
highest_total = totals[0]
highest_index = 0

for i in range(len(totals)):
    if totals[i] > highest_total:
        highest_total = totals[i]
        highest_index = i

print("Person with highest total steps:", names[highest_index])
print("Highest total steps:", highest_total)

lowest_total = totals[0]

for total in totals:
    if total < lowest_total:
        lowest_total = total
      
difference = highest_total - lowest_total
print("Difference between highest and lowest total steps:", difference)

