def unite_lists(list1, list2):
    new_list = []

    for i in list1:
        if i in new_list:
            continue
        else:
            list1.append(i)
    for i in list2:
        if i in new_list:
            continue
        else:
            list2.append(i)

    return new_list
