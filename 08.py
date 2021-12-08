with open("08.txt", 'r') as f:
    signals = [[s.strip().split(' ') for s in l.split(' | ')]
               for l in f.readlines()]

print('part1:', sum(sum(1 for a in x[1] if len(
    a) in [2, 3, 4, 7]) for x in signals))
