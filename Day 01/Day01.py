# Solution 1 - storing all elves' calories in a list

cals = []
with open('input1.txt', mode='r') as fin:
    line = fin.readline()
    while line != '':
        cur_cal = 0
        while line.strip() != '':
            cur_cal += int(line.strip())
            line = fin.readline()
        cals.append(cur_cal)
        line = fin.readline()

print(f"Max Cals = {max(cals)}")
print(f"Top3 = {sum(sorted(cals, reverse=True)[:3])}")

# Solution 2 - only storing top n elves' calories; maintain order using heap
import heapq

n = 3
top_n = []
with open('input1.txt', mode='r') as fin:
    line = fin.readline()
    while line != '':
        cur_cal = 0
        while line.strip() != '':
            cur_cal += int(line.strip())
            line = fin.readline()
        if len(top_n) < n:
            heapq.heappush(top_n, cur_cal)
        else:
            if top_n[0] < cur_cal:
                heapq.heappush(top_n, cur_cal)
                top_n = top_n[1:]
        line = fin.readline()


print(f"Max Cals = {top_n[-1]}")
print(f"Top3 = {sum(top_n)}")

