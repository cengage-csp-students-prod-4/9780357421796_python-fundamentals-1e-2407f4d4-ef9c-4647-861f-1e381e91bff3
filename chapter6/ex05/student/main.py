def unite_lists(list1, list2):
    new_list = []

    for item in list1:
        if item not in new_list:
            new_list.append(item)

    for item in list2:
        if item not in new_list:
            new_list.append(item)

    return new_list