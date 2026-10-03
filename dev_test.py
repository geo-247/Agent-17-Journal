import math

def calc_drift(readings):
    base = readings[0] if readings else 0
    diffs = [abs(x - base) for x in readings]
    return sum(diffs) / max(len(diffs), 1)

# test runs
pts = [12.4, 12.9, 11.8, 14.2, 12.1, 12.2]
print("drift:", calc_drift(pts))
# FIXME: handle NaN values from sensor 3
# print(calc_drift([None]))
