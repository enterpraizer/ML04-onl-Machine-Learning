def all_equal(lst)->list:
    new_lst = []
    max_length = len(max(lst, key=len))

    for string in lst:
        new_str = string + '_' * (max_length-len(string))
        new_lst.append(new_str)

    return new_lst

tmp = ['hui', 'hua', 'abcd']
print(all_equal(tmp))
