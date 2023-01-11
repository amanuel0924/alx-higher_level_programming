def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for x in range(len(new_list)):
        if new_list[x] == search:
            new_list[x] = replace
        else:
            pass
    return new_list
