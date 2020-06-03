import itertools
import enchant

d = enchant.Dict("en_US")


def make_anagrams(name):
    final_list = []
    for i in range(1, len(name)):
        all_perm = ["".join(perm) for perm in itertools.combinations(name, i)]
        for possible_names in all_perm:
            if d.check(possible_names) and len(possible_names) != 1:
                final_list.append(possible_names)

    return final_list


if __name__ == '__main__':
    print(make_anagrams('theguywithcurlyhair'))
