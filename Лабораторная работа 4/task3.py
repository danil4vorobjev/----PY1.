def delete(list_, index=None):
    if index is None:
        index = -1
        return list_[:index]
    else:
        list1 = list_[:index]
        list2 = list_[index + 1:]
        list1.extend(list2)
        return list1



print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
