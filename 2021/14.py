import parse
from collections import Counter, defaultdict


def polymer_template_to_dict(polymer_template: str) -> defaultdict:
    out = defaultdict(int)
    for i in range(len(polymer_template)-1):
        out[polymer_template[i:(i+2)]] += 1
    return out


def do_insert(polymer_dict: defaultdict, insertion_rules: list[tuple[str, str]]) -> defaultdict:
    out = polymer_dict.copy()
    for pair, insert in insertion_rules:
        if pair in polymer_dict.keys():
            out[pair[0]+insert] += polymer_dict[pair]
            out[insert+pair[1]] += polymer_dict[pair]
            out[pair] -= polymer_dict[pair]
    return out


def get_counter_of_chars(result: defaultdict, last_letter: str) -> Counter:
    out = defaultdict(lambda: 0)
    for a, i in result.items():
        out[a[0]] += i
    out[last_letter] += 1
    return Counter(out)


if __name__ == '__main__':
    with open("2021/14.txt", 'r') as f:
        polymer_template_string, insertions_raw = f.read().split('\n\n')
        insertion_rules = [(d['pair'].strip(), d['insert'].strip())
                           for d in parse.findall('{pair} -> {insert}', insertions_raw)]
    last_letter = polymer_template_string[-1]
    polymer_dict = polymer_template_to_dict(polymer_template_string)
    for i in range(40):
        polymer_dict = do_insert(polymer_dict, insertion_rules)
        if i == 9 or i == 39:
            part_number = 1 if i == 9 else 2
            c = get_counter_of_chars(polymer_dict, last_letter)
            most_common_value = c.most_common()[0][1]
            least_common_value = c.most_common()[-1][1]
            print(f'part{part_number}: {most_common_value-least_common_value}')
