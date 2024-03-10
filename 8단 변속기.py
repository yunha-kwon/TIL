spd = list(map(int, input().split()))
spd_asc = sorted(spd)
spd_dsc = sorted(spd, reverse=True)

if spd == spd_asc:
    print('ascending')
elif spd == spd_dsc:
    print('descending')
else:
    print('mixed')