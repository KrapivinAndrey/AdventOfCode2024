from numpy.ma.core import ones_like

left = []
right = []
with open('input.txt') as f:
    for line in f:
        one, two = line.split()
        left.append(int(one))
        right.append(int(two))
left.sort()
right.sort()
ans1 = sum([abs(x - y) for x, y in zip(right, left)])
print(ans1)