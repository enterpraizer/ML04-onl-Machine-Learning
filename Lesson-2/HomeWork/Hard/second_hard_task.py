def search_substring(sub_string, string):
    sub_string = sub_string.lower()
    string = string.lower()

    if sub_string in string:
        print('Есть контакт')

    else:
        print('Мимо')