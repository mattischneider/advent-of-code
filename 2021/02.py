with open("2021/02.txt", 'r') as f:
    planned_course = [l.split(' ') for l in f.readlines()]

hor_pos = sum(int(d[1]) for d in planned_course if d[0] == 'forward')
ups = sum(int(d[1]) for d in planned_course if d[0] == 'up')
downs = sum(int(d[1]) for d in planned_course if d[0] == 'down')

print('part1', hor_pos * (downs-ups))

aim = 0
depth = 0
for d in planned_course:
    if d[0] == 'up':
        aim -= int(d[1])
    if d[0] == 'down':
        aim += int(d[1])
    if d[0] == 'forward':
        depth += int(d[1]) * aim

print('part2', hor_pos * depth)
