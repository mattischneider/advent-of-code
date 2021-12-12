with open("2021/03.txt", 'r') as f:
    consumptions = f.readlines()
    n = len(consumptions[0].strip())
    m = len(consumptions)

number_of_bits_set = [sum(int(c[i]) for c in consumptions) for i in range(n)]
gamma = ''.join(str(int(i > m/2)) for i in number_of_bits_set)
epsilon = ''.join(str(int(i < m/2)) for i in number_of_bits_set)

print('part 1:', int(gamma, 2) * int(epsilon, 2))

possible_oxygen_generators = consumptions[:]
possible_co_scrubbers = consumptions[:]
oxygen_generator = None
co_scrubber = None
for i in range(n):
    # oxy
    oyx_n = len(possible_oxygen_generators)
    oxy_number_of_bits_set = sum(int(c[i]) for c in possible_oxygen_generators)

    if oxy_number_of_bits_set >= oyx_n/2:
        possible_oxygen_generators = [
            p for p in possible_oxygen_generators if p[i] == '1']
    else:
        possible_oxygen_generators = [
            p for p in possible_oxygen_generators if p[i] == '0']

    if len(possible_oxygen_generators) == 1 and oxygen_generator is None:
        oxygen_generator = possible_oxygen_generators[0]

    # co2
    co_n = len(possible_co_scrubbers)
    co_number_of_bits_set = sum(int(c[i]) for c in possible_co_scrubbers)
    if co_number_of_bits_set >= co_n/2:
        possible_co_scrubbers = [
            p for p in possible_co_scrubbers if p[i] == '0']
    else:
        possible_co_scrubbers = [
            p for p in possible_co_scrubbers if p[i] == '1']

    if len(possible_co_scrubbers) == 1 and co_scrubber is None:
        co_scrubber = possible_co_scrubbers[0]

print('part 2:', int(oxygen_generator, 2) * int(co_scrubber, 2))
