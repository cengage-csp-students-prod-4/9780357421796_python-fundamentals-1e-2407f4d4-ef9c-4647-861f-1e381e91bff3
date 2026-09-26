def content_combiner(dic1, dic2):
    new_dic = dict()
    for key, value in dic1.items():
        new_dic[key] = value

    for key, value in dic2.items():
        new_dic[key] = value

    return new_dic


