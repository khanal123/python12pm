"""only if
 ncell to ncell call dhamaka
 0-5 min 5min bonus
 5-10 min 10min bonus
 10-15 min 15 min bonus   and so on
ncell to ntc
0-20 min 5 min bonus
20-40 min 10 min bonus  and so on
"""
bonus = 0
call_time = int(input("enter number of minute called"))
sim = int(input("enter 1 for ncell-ncell and 2 for ncell-ntc"))
if sim == 1:
    for i in range(1, call_time + 1):
        if i % 5 == 0:
            bonus += 5
elif sim == 2:
    for i in range(1, call_time + 1):
        if i % 20 == 0:
            bonus += 5

else:
    print("invalid choice")
print(f"you have got {bonus} minute bonus")