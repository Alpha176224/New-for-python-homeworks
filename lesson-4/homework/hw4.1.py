list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
uncommons_list=list()
for i in list1:
    if i not in list2:
        uncommons_list.append(i)
    else:
        continue
for j in list2:
    if j not in list1:
        uncommons_list.append(j)
    else:
        continue       

print(uncommons_list)
    
