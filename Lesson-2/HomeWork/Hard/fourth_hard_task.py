def count_max(string: str):
    count_dict = {}

    for symbol in string:
        if symbol in count_dict:
            count_dict[symbol] += 1
        else:
            count_dict[symbol] = 1

    keys = {}
    for _ in range(3):
        max_el = max(count_dict, key=count_dict.get)
        keys[max_el] = count_dict[max_el]
        count_dict.pop(max(count_dict, key=count_dict.get))

    return keys

s = '1112222333344444555555'
print(count_max(s))
