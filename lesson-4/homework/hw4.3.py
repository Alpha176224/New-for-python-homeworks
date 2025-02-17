txt=input('enter txt : ')
list1=list(txt.strip())
list2=list()
ylist=list()
li=ylist+['a','e','u','o']
l=-1
for i in range(0,len(list1)-1):
    if l+3>i or bool(list1[i] in li):
        list2.append(list1[i])
    else:
        list2.append(f'{list1[i]}_')
        l=i
        li.append(list1[i])
list2.append(list1[-1])
print(''.join(list2))