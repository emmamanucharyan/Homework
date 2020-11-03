def merge_sort( my_list ):
  if len(my_list) == 1:
    return my_list
  else:
    list1 = my_list[:len(my_list)//2]
    list2 = my_list[len(my_list)//2:]
    list1 = merge_sort(list1)
    list2 = merge_sort(list2)
    return merge(list1,list2)


def merge(list1, list2):
    temp_list = []
    while len(list1) > 0 and len(list2) > 0:
      if list1[0] > list2[0]:
        temp_list.append(list2[0])
        list2.pop(0)
      else:
        temp_list.append(list1[0])
        list1.pop(0)
    while len(list1) > 0:
      temp_list.append(list1[0])
      list1.pop(0)

    while len(list2) > 0:
      temp_list.append(list2[0])
      list2.pop(0)
    return temp_list


a = merge_sort([7,87,3,54,45,65,4,2,6])
print(a)
