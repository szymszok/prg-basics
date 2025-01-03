judges = [(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]

points = []
for jumper in judges:
    maxx = max(jumper)
    minn = min(jumper)
    summ = sum(jumper)
    result = summ - maxx - minn
    points.append(result)

print(points)