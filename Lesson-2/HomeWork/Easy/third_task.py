def change(lst)->list:
    first_elm = lst[0]
    last_elm = lst[-1]
    lst[0]=last_elm
    lst[-1]=first_elm
    return lst

tmp = [1,2,3,4,5]
changed_tmp = change(tmp)
print(changed_tmp)