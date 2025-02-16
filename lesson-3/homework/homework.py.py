# 1.Get Value: Given a dictionary and a key, retrieve the associated value, considering what to return if the key doesn’t exist.
# dict1=eval(input('Enter the dict: '))
# key1=eval(input('Enter the key: '))
# if key1 in dict1.keys():
#     print(dict1[key1])
# else:
#     print('There is no such key in this dictionary')

# 2.Check Key: Given a dictionary and a key, check if the key is present in the dictionary.
# dict1=eval(input('Enter the dict: '))
# key1=eval(input('Enter the key: '))
# if key1 in dict1.keys():
#     print('This key is present in the dictionary')
# else:
#     print('This key is present in the dictionary')

# 3.Count Keys: Determine the number of keys in the dictionary.
# dict1=eval(input('Enter the dict: '))
# keylist=dict1.keys()
# print(len(keylist))

# 4.Get All Keys: Create a list that contains all the keys in the dictionary.
# dict1=eval(input('Enter the dict: '))
# mylist=[]
# keylist=dict1.keys()
# keylist=list(keylist)
# print(keylist)

# 5.Get All Values: Create a list that contains all the values in the dictionary.
# dict1=eval(input('Enter the dict: '))
# print(dict1.values())

# 6.Merge Dictionaries: Given two dictionaries, create a new dictionary that combines both.
# dict1=eval(input('Enter the first dict: '))
# dict2=eval(input('Enter the second dict: '))
# keylist=list(dict2.keys())
# valuelist=list(dict2.values())
# for i in range(len(dict2)):
#     dict1[keylist[i]]=valuelist[i]
# print(dict1)

# 7.Remove Key: Given a dictionary and a key, remove the key if it exists, handling the case if it doesn’t.
# dict1=eval(input('Enter the dict: '))
# key1=eval(input('Enter the key: '))
# keylist=list(dict1.keys())
# valuelist=list(dict1.values())
# mydict=dict()
# if key1 in dict1.keys():
#     keylist.remove(key1)
#     valuelist.remove(dict1[key1])
#     for i in range(len(keylist)):
#         mydict[keylist[i]]=valuelist[i]
#     print(mydict)    
# else: 
#     print('There is no such key')

# 8.Clear Dictionary: Create a new empty dictionary.
# mydict=dict()
# print(mydict)

# 9.Check if Dictionary is Empty: Determine if a dictionary has any elements.
# dict1=eval(input('Enter the dict: '))
# if len(dict1)==0:
#     print('Empty dictionary')
# else:
#     print('Not empty dictionary')

# 10.Get Key-Value Pair: Given a dictionary and a key, retrieve the key-value pair if the key exists.
# dict1=eval(input('Enter the dict: '))
# key1=eval(input('Enter the key: '))
# if key1 in dict1.keys():
#     print(key1,':',dict1[key1])
# else:
#     print('There is no such key')

# 11.Update Value: Given a dictionary, update the value for a specified key.
# dict1=eval(input('Enter the dict: '))
# key1=eval(input('Enter the key: '))
# nv=eval(input('Enter new value: '))
# dict1[key1]=nv
# print(dict1)

# 12.Count Value Occurrences: Given a dictionary, count how many times a specific value appears across the keys.
# dict1=eval(input('Enter the dict: '))
# v1=eval(input('Enter the value: '))
# mylist=list(dict1.values())
# print('This value has',mylist.count(v1),'appearences in the given dictionary')

# 13.Invert Dictionary: Given a dictionary, create a new dictionary that swaps keys and values.
# dict1=eval(input('Enter the dict: '))
# mylist1=list(dict1.keys())
# mylist2=list(dict1.values())
# x=0
# clist=mylist2.copy()
# mylist=list()
# mydict=dict()
# for i in range(len(mylist2)):
#     if mylist2.count(mylist2[i])==1:
#         mydict[mylist2[i]]=mylist1[i]
#     else:
#         for j in range(0,(mylist2.count(mylist2[i])-1)):
#             mylist.append(mylist1[(clist.index(mylist2[i])+x)])
#             x+=1
#             clist.remove(mylist2[i])
#         mydict[mylist2[i]]=list(mylist)
# print(mydict)


# 14.Find Keys with Value: Given a dictionary and a value, create a list of all keys that have that value
# dict1=eval(input('Enter the dict: '))
# v=eval(input('Enter the value: '))
# l1=list(dict1.keys())
# l2=list(dict1.values())
# mylist=list()
# x=0
# for i in range(0,l2.count(v)):
#     mylist.append(l1[l2.index(v)+x])
#     l2.remove(v)
#     x+=1
# print(mylist)

# 15.Create a Dictionary from Lists: Given two lists (one of keys and one of values), create a dictionary that pairs them.
# l1=eval(input('Enter the list of keys: '))
# l2=eval(input('enter the list of values: '))
# mydict=dict()
# for i in range(len(l1)):
#     mydict[l1[i]]=l2[i]
# print(mydict)

# 16.Check for Nested Dictionaries: Given a dictionary, check if any values are also dictionaries.
# dict1=eval(input('Enter the dict: '))
# l1=list(dict1.values())
# n=0
# for i in list(l1):
#     n+=bool(type(i)==dict)
# print(bool(n))

# 17.Get Nested Value: Given a nested dictionary, retrieve a value from within one of the inner dictionaries.
# dict1=eval(input('Enter the nested dict: '))
# glist=eval(input('Enter a sequence of keys that describes the path to the target value as list: '))
# for i in list(glist):
#     dict1=dict1[i]
# print(dict1)

# 18.Create Default Dictionary: Create a dictionary that provides a default value for missing keys.
# i don't understand this problem

# 19.Count Unique Values: Given a dictionary, determine the number of unique values it contains.
# dict1=eval(input('Enter the dict: '))
# print('This dictionary has',len(set(dict1.values())),'unnique values')

# 20.Sort Dictionary by Key: Create a new dictionary sorted by keys.
# dict1=eval(input('Enter the dict: '))
# mydict=dict1.copy()
# mylist=list(dict1.keys())
# dict1.clear()
# mylist=sorted(mylist)
# for i in list(mylist):
#     dict1[i]=mydict[i]
# print(dict1)

# 21.Sort Dictionary by Value: Create a new dictionary sorted by values.
# dict1=eval(input('Enter the dict: '))
# mydict=dict1.copy()
# mylist1=list(dict1.values())
# mylist2=list(dict1.keys())
# dict1.clear()
# x=0
# mylist=sorted(mylist1)
# for i in list(mylist):
#     dict1[mylist2[(mylist1.index(i)+x)]]=i
#     if mylist.count(i)>1:
#         mylist.remove(i)
#         x+=1
# print(dict1)

# 22.Filter by Value: Given a dictionary, create a new dictionary that only includes items with values that meet a certain condition.
# I don't understand the problem

# 23.Check for Common Keys: Given two dictionaries, check if they have any keys in common.
# dict1=eval(input('Enter the first dict: '))
# dict2=eval(input('Enter the second dict: '))
# set1=set(dict1.keys())
# set2=set(dict2.keys())
# if bool(set1.intersection(set2))==0:
#     print('They don\'t have keys in common')
# else:
#     print('They have keys in common')

# 24.Create Dictionary from Tuple: Given a tuple of key-value pairs, create a dictionary from it.
# tuple1=eval(input('Enter the tuple (enterkey and value pairs in subtuple): '))
# mydict=dict()
# for i in tuple(tuple1):
#     mydict[i[0]]=i[1]
# print(mydict)

# 25.Get the First Key-Value Pair: Retrieve the first key-value pair from a dictionary.
# dict1=eval(input('Enter the dict: '))
# tuple1=(list(dict1.keys())[0],dict1[(list(dict1.keys())[0])])
# print(tuple1)
#task1
# l=input('Enter list ')
# e=input('Enter element ')
# print(l.count(str(e)))

#task2
# numbers = input("Enter numbers separated by spaces: ")
# numbers = list(map(int, numbers.split()))
# total=sum(numbers)
# print("The sum of the elements is:", total)

# task3
# numbers = input("Enter numbers separated by spaces: ")
# numbers = list(map(int, numbers.split()))
# print('The largest element is: ',max(numbers))

# task4
# numbers = input("Enter numbers separated by spaces: ")
# numbers = list(map(int, numbers.split()))
# print('The smallest element is: ',min(numbers)

# task5
# mylist = input("Enter elements of list separated by spaces: ")
# mylist = list(mylist.split())
# myelement =input('ENter the element: ')
# if myelement in mylist:
#     print('This element is present in list')
# else:
#      print('This element is not present in list')

# task6
# mylist = input("Enter elements of list separated by spaces: ")
# mylist = list(mylist.split())
# if len(mylist)==0:
#     print('This list is empty')
# else:
#     print("The first element of this list is ",mylist[0])


# task7
# mylist = input("Enter elements of list separated by spaces: ")
# mylist = list(mylist.split())
# if len(mylist)==0:
#     print('This list is empty')
# else:
#     print("The last element of this list is ",mylist[-1])

# task8
# mylist = input("Enter elements of list separated by spaces: ")
# mylist = list(mylist.split())
# print('The new list is ',list(mylist[:3]))

# task9
# mylist = input("Enter elements of list separated by spaces: ")
# mylist = list(mylist.split())
# print('The reversed list is ',list(mylist[::-1]))

# task10
# mylist = input("Enter elements of list separated by spaces: ")
# mylist = list(mylist.split())
# print('The sorted list is ',list(sorted(mylist)))

# task11
# mylist = input("Enter elements of list separated by spaces: ")
# mylist = list(mylist.split())
# print('The new list without duplicates is ',list(set(mylist)))

# task12
# my_list = input("Enter elements of list separated by spaces: ")
# my_list = list(my_list.split())
# my_element=input('Enter the element ')
# k=int(input('Enter the index '))
# my_list.insert(k,my_element)
# print('The new list is',my_list)

# task13
# my_list = input("Enter elements of list separated by spaces: ")
# my_list = list(my_list.split())
# my_element=input('Enter the element ')
# print('The index(first occurence) of given element is ',my_list.index(my_element))

# task14
# my_list = input("Enter elements of list separated by spaces: ")
# my_list = list(my_list.split())
# print(bool(len(my_list)))

# task15
# numbers = input("Enter numbers separated by spaces: ")
# numbers = list(map(int, numbers.split()))
# N=0
# for i in numbers:
#     N+=((i+1)%2)
# print(N,' of them are even')

# task16
# numbers = input("Enter numbers separated by spaces: ")
# numbers = list(map(int, numbers.split()))
# N=0
# for i in numbers:
#     N+=((i)%2)
# print(N,' of them are odd')

# task17
# list_1= eval(input("Enter first list: "))
# list_2= eval((input("Enter second list: ")))
# print(list_1+list_2)

# task18
# list1= eval(input("Enter list: "))
# sublist1= eval(input("Enter sublist list: "))
# n=len(sublist1)
# if sublist1[0] in list1:
#     m=list1.index(sublist1[0])
#     list2=list1[m:m+n]
#     print(sublist1==list2)
# else:
#     print('False')

# task19
# list1= eval(input("Enter list: "))
# el1=eval(input('Enter element to replace: '))
# eln=input('Enter new element: ')
# if el1 in list1:
#     n=list1.index(el1)
#     list1.remove(el1)
#     list1.insert(n,eln)
# else:
#     print('Element is not  found in list')
# print(list1)

# task20
# list1= eval(input("Enter list: "))
# m=max(list1)
# n=list1.count(m)
# for i in range(n):
#     list1.remove(m)
# print('The second largest element is: ',max(list1))

# task21
# list1= eval(input("Enter list: "))
# set1=set(list1)
# set1.remove(min(set1))
# print('The second smallest element is: ',min(set1))

# task22
# list1= eval(input("Enter list: "))
# for i in list(list1):
#     if i%2==1:
#         list1.remove(i)
# print('The set of even numbers is ',list1)

# task23
# list1= eval(input("Enter list: "))
# for i in list(list1):
#     if i%2==o:
#         list1.remove(i)
# print('The set of odd numbers is ',list1)

# task24
# list1= eval(input("Enter list: "))
# print('The number of elements is ',len(list(list1)))

# task25
# list1= eval(input("Enter list: "))
# from copy import copy
# list2=list1.copy()
# print('Copy of the given list is :',list2)

# task26 
# list1= eval(input("Enter list: "))
# list1=list(list1)
# n=len(list1)
# if n%2==0:
#     n1=int(n/2)
#     n2=int((n+2)/2)
#     print('Middle elements are ',list1[n1],'and ',list1[n2])
# else:
#     n3=int((n-1)/2)
#     print('Middle element is ',list1[n3])

# task27
# list1= eval(input("Enter list: "))
# a=int(input('Enter the starting index: '))
# b=int(input('Enter the ending index: '))
# print('Maximum element of a specified sublist is ',max(list1[a:b+1]))   

# task28
# list1= eval(input("Enter list: "))
# a=int(input('Enter the starting index: '))
# b=int(input('Enter the ending index: '))
# print('Minimum element of a specified sublist is ',min(list1[a:b+1])) 

# task29
# list1= eval(input("Enter list: "))
# a=int(input('Enter the index of element: '))
# if a>-len(list1) and a<len(list1):
#     list1.remove(list1[a])
#     print(list1)
# else:
#     print('IndexError')

# task30
# list1= eval(input("Enter the list of numbers: "))
# n=0
# for i in range(0,len(list1)-1):
#     n+=bool(list1[i]<=list1[i+1])
# print(n==len(list1)-1)

# task31
# list1= eval(input("Enter the list of numbers: "))
# n=int(input('Enter number: '))
# list2=list1.copy()
# for i in range(0,len(list1)):
#     for j in range(1,n):
#        list2.insert(n*i,list1[i])
# print(list2)

# task32
# list1= eval(input("Enter the first list: "))
# list2= eval(input("Enter the second list: "))
# list_merge=list1+list2
# list_merge.sort()
# print(list_merge)

# task33
# list1= eval(input("Enter the list: "))
# element1=eval(input('Enter the element: '))
# n=list1.count(element1)
# listofindexes=[]
# for i in range(0,n):
#     listofindexes.append(list1.index(element1)+i)
#     list1.remove(element1)
# print('Index list of this element in the given list is: ',listofindexes)

# task34
# list1= eval(input("Enter the list: "))
# n=int(input('Enter the number of positions to shift: '))
# n=n%(len(list1))
# print('The rotated list is: ',list1[-n:]+list1[:-n])

# task35
# n=int(input('Enter starting number: '))
# m=int(input('Enter ending number: '))
# listr=[]
# for i in range(n,m+1):
#     listr.append(i)
# print(listr)

# task36
# list1= eval(input("Enter the list of numbers: "))
# S=0
# for i in list(list1):
#     if i>0:
#         S+=i
# print('The sum of all positive numbers is: ',S)

# task37
# list1= eval(input("Enter the list of numbers: "))
# S=0
# for i in list(list1):
#     if i<0:
#         S+=i
# print('The sum of all negative numbers is: ',S)

# task38
# list1= eval(input("Enter the list of numbers: "))
# checklist=list1[-1::-1]
# if list1==checklist:
#     print('This list is a palindrome')
# else:
#     print('This list is not a palindrome')

# task39
# list1= eval(input("Enter the list of numbers: "))
# n=int(input('Enter the number of elements that every sublists should contain: '))
# newlist=[]
# r=(len(list1))%n
# for i in range(0,(len(list1)-r)//n):
#     newlist.append(list(list1[i*n:(i+1)*n]))
# newlist.append(list(list1[-r:]))
# print('The nested list is ',newlist)

# task40
# list1= eval(input("Enter the list: "))
# newlist=[]
# for i in list(list1):
#     if list1.count(i)==1:
#         newlist.append(i)
# print(newlist)
# 1.Union of Sets: Given two sets, create a new set that contains all unique elements from both sets.
# set1=eval(input('Enter the first set: '))
# set2=eval(input('Enter the second set: '))
# print(set1.union(set2))

# 2.Intersection of Sets: Given two sets, create a new set that contains elements common to both sets.
# set1=eval(input('Enter the first set: '))
# set2=eval(input('Enter the second set: '))
# print(set1.intersection(set2))

# 3.Difference of Sets: Given two sets, create a new set with elements from the first set that are not in the second.
# set1=eval(input('Enter the first set: '))
# set2=eval(input('Enter the second set: '))
# print(set1.difference(set2))

# 4.Check Subset: Given two sets, check if one set is a subset of the other.
# set1=eval(input('Enter the first set: '))
# set2=eval(input('Enter the second set: '))
# print((set1.intersection(set2)==set1 or set1.intersection(set2)==set2))

# 5.Check Element: Given a set and an element, check if the element exists in the set.
# set1=eval(input('Enter the set: '))
# el1=eval(input('Enter the element: '))
# if el1 in set1:
#     print('The set has such element')
# else:
#      print('The set doesn\'t have such element')

# 6.Set Length: Determine the number of unique elements in a set.
# set1=eval(input('Enter the set: '))
# print('The length of this set is',len(set1))

# 7.Convert List to Set: Given a list, create a new set that contains only the unique elements from that list.
# list1=eval(input('Enter the list: '))
# print(set(list1))

# 8.Remove Element: Given a set and an element, remove the element if it exists.
# set1=eval(input('Enter the set: '))
# el1=eval(input('Enter the element: '))
# if el1 in set1:
#     set1.remove(el1)
# print(set1)

# 9.Clear Set: Create a new empty set from an existing set.
# set1=eval(input('Enter the set: '))
# set1.clear()
# print(set1)

# 10.Check if Set is Empty: Determine if a set has any elements.
# set1=eval(input('Enter the set: '))
# if bool(set1)==0:
#     print('This set is empty')
# else:
#     print('This set is not empty')

# 11.Symmetric Difference: Given two sets, create a new set that contains elements that are in either set but not in both.
# set1=eval(input('Enter the first set: '))
# set2=eval(input('Enter the second set: '))
# print(set1.symmetric_difference(set2))

# 12.Add Element: Given a set and an element, add the element to the set if it is not already present.
# set1=eval(input('Enter the set: '))
# el1=eval(input('Enter the element: '))
# if el1 not in set1:
#     set1.add(el1)
# print(set1)

# 13.Pop Element: Given a set, remove and return an arbitrary element from the set.
# set1=eval(input('Enter the set: '))
# myset=set(set1)
# myset.pop()
# elr=list(set1.difference(myset))[0]
# print('Removed element is',elr)
# print('The set is',set1)

# 14.Find Maximum: From a given set of numbers, find the maximum element.
# set1=eval(input('Enter the set: '))
# print(max(set1))

# 15.Find Minimum: From a given set of numbers, find the minimum element.
# set1=eval(input('Enter the set: '))
# print(min(set1))

# 16.Filter Even Numbers: Given a set of integers, create a new set that contains only the even numbers.
# set1=eval(input('Enter the set of numbers: '))
# mylist=list(set1)
# newset=set()
# for i in list(mylist):
#     if i%2==0:
#         newset.add(i)
# print(newset)
 
# 17.Filter Odd Numbers: Given a set of integers, create a new set that contains only the odd numbers.
# set1=eval(input('Enter the set of numbers: '))
# mylist=list(set1)
# newset=set()
# for i in list(mylist):
#     if i%2==1:
#         newset.add(i)
# print(newset)

# 18.Create a Set of a Range: Create a set of numbers in a specified range (e.g., from 1 to 10).
# n=int(input('Enter the starting number: '))
# m=int(input('Enter the ending number: '))
# myset=set()
# for i in range(n,m+1):
#     myset.add(i)
# print(myset)

# 19.Merge and Deduplicate: Given two lists, create a new set that merges both lists and removes duplicates.
# list1=eval(input('Enter the set: '))
# list2=eval(input('Enter the set: '))
# set1=set(list1+list2)
# print(set1)

# 20.Check Disjoint Sets: Given two sets, check if they have no elements in common.
# set1=eval(input('Enter the first set: '))
# set2=eval(input('Enter the second set: '))
# if bool(set1.intersection(set2))==0:
#     print('This sets have no elements in common')
# print('This sets have elements in common')

# 21.Remove Duplicates from a List: Given a list, create a set from it to remove duplicates, then convert back to a list.
# list1=eval(input('Enter the set: '))
# myset=set(list1)
# print(list(myset))

# 22.Get Unique Elements in Order: Given a list, create a set that contains unique elements while maintaining their first appearance order.
# list1=eval(input('Enter the set: '))
# mylist=[]
# for i in list(list1):
#     if i not in mylist:
#         mylist.append(i)
# print(set(mylist))

# 23.Create Nested Sets: Create a set of sets, where each inner set contains a specified number of unique elements.
# n=int(input('Enter the number of element that inner sets should contain: '))
# mylist=[]
# innerset=set()
# for i in range(1,8):
#     for j in range(i*n,i*(n+1)+1):
#         innerset.add(j)
#     set1=frozenset(innerset)
#     mylist.append(set1) 
#     innerset.clear()
# print(set(mylist))  

# 24.Count Unique Elements: Given a list, determine the count of unique elements using a set.
# list1=eval(input('Enter the set: '))
# myset=set(list1)
# print('This list has',len(myset),'unique elements')

# 25.Generate Random Set: Create a set with a specified number of random integers within a certain range.
# s=int(input('Enter starting number of the numbers range: '))
# e=int(input('Enter ending number of the numbers range: '))
# n=int(input('Enter the specified number of random integers: '))
# myset=set()
# for i in range(s,e+1):
#     myset.add(i)
# m=len(myset)-n
# for j in range(0,m):
#     myset.pop()
# print(myset)
# 1.Count Occurrences: Given a tuple and an element, find how many times the element appears in the tuple.
# tuple1=eval(input('Enter the tuple: '))
# el1=eval(input('Enter an element: '))
# if el1 in tuple1:
#     print('This element has',tuple1.count(el1),'occurences in the given tuple')
# else:
#     print('This element is not exist in the given tuple')

# 3.Max Element: From a given tuple, determine the largest element.
# tuple1=eval(input('Enter the tuple: '))
# print('The largest element is',max(tuple1),'in this tuple')

# 4.Min Element: From a given tuple, determine the smallest element.
# tuple1=eval(input('Enter the tuple: '))
# print('The smallest element is',min(tuple1),'in this tuple')

# 5.First Element: Access the first element of a tuple, considering what to return if the tuple is empty.
# tuple1=eval(input('Enter the tuple: '))
# if bool(tuple1)==0:
#     print('The list is empty')
# else:
#     print('The first element of this tuple is',tuple1[0])

# 6.Last Element: Access the last element of a tuple, considering what to return if the tuple is empty.
# tuple1=eval(input('Enter the tuple: '))
# if bool(tuple1)==0:
#     print('The list is empty')
# else:
#     print('The last element of this list is',tuple1[-1])

# 7.Tuple Length: Determine the number of elements in the tuple.
# tuple1=eval(input('Enter the tuple: '))
# print('The length of given tuple is'),len(tuple1))

# 8.Slice Tuple: Create a new tuple that contains only the first three elements of the original tuple.
# tuple1=eval(input('Enter the tuple: '))
# print('The first 3 elements of this tuple is',tuple1[0:3])

# 9.Concatenate Tuples: Given two tuples, create a new tuple that combines both.
# tuple1=eval(input('Enter first tuple: '))
# tuple2=eval(input('Enter second tuple: '))
# print(tuple(list(tuple1)+list(tuple2)))

# 10.Check if Tuple is Empty: Determine if a tuple has any elements.
# tuple1=eval(input('Enter the tuple: '))
# if bool(tuple1)==0:
#     print('The tuple is empty')
# else:
#     print('The tuple is not empty')

# 11.Get All Indices of Element: Given a tuple and an element, find all the indices of that element in the tuple.
# tuple1=eval(input('Enter the tuple: '))
# tuple1=list(tuple1)
# el1=eval(input('Enter the element: '))
# n=tuple1.count(el1)
# myset=set()
# if bool(tuple1)==0:
#     print('The tuple is empty')
# else:
#     for i in range(0,n):
#         myset.add((tuple1.index(el1))+i)
#         tuple1.remove(el1)
# print('The set of indexes is:',myset)

# 12.Find Second Largest: From a given tuple, find the second largest element.
# tuple1=eval(input('Enter the tuple: '))
# set1=set(tuple1)
# set1.remove(max(set1))
# print('The second largest element is',max(set1))

# 13.Find Second Smallest: From a given tuple, find the second smallest element.
# tuple1=eval(input('Enter the tuple: '))
# set1=set(tuple1)
# set1.remove(min(set1))
# print('The second smallest element is',min(set1))

# 14.Create a Single Element Tuple: Create a tuple that contains a single specified element.
# el1=eval(input('Enter the element: '))
# myset=(el1,)
# print(myset)

# 15.Convert List to Tuple: Given a list, create a tuple containing the same elements.
# list1=eval(input('Enter the list: '))
# print(tuple(list1))

# 16.Check if Tuple is Sorted: Determine if the tuple is sorted in ascending order and return a boolean.
# tuple1=eval(input('Enter the tuple: '))
# mylist=list(tuple1)
# mylist.sort()
# print(tuple1==tuple(mylist))

# 17.Find Maximum of Subtuple: Given a tuple, find the maximum element of a specified subtuple.
# tuple1=eval(input('Enter the tuple: '))
# n=int(input('Enter the starting inedx: '))
# m=int(input('Enter the ending index: '))
# mylist=list(tuple1)
# mytuple=tuple(mylist[n:m+1])
# print('The largest element of this subtuple is',max(mytuple))

# 18.Find Minimum of Subtuple: Given a tuple, find the minimum element of a specified subtuple.
# tuple1=eval(input('Enter the tuple: '))
# n=int(input('Enter the starting inedx: '))
# m=int(input('Enter the ending index: '))
# mylist=list(tuple1)
# mytuple=tuple(mylist[n:m+1])
# print('The smallest element of this subtuple is',min(mytuple))

# 19.Remove Element by Value: Given a tuple and an element, create a new tuple that removes the first occurrence of that element.
# tuple1=eval(input('Enter the tuple: '))
# el1=eval(input('Enter the element: '))
# mylist=list(tuple1)
# mylist.remove(el1)
# print(tuple(mylist))

# 20.Create Nested Tuple: Create a new tuple that contains subtuples, where each subtuple contains specified elements from the original tuple.
# tuple1=eval(input('Enter the tuple: '))
# indextuple=eval(input("Enter the tuple that the indexes of elements which are in common subtuple are in the common subtuple and same order: "))
# list1=[]
# mylist=[]
# for i in range (0,len(indextuple)):
#     for j in range (0,len(indextuple[i])):
#         n=indextuple[i][j]
#         mylist.append(tuple1[n])
#     list1.append(tuple(mylist))
#     mylist.clear()
# print(tuple(list1))

# 21.Repeat Elements: Given a tuple and a number, create a new tuple where each element is repeated that number of times.
# tuple1=eval(input('Enter the tuple: '))
# n=int(input('Enter the number of time to repeate'))
# mylist=[]
# for i in tuple(tuple1):
#     for j in range(0,n):
#         mylist.append(i)
# print(tuple(mylist))

# 22.Create Range Tuple: Create a tuple of numbers in a specified range (e.g., from 1 to 10).
# n=int(input('Enter starting number: '))
# m=int(input('Enter ending number '))
# mylist=[]
# for i in range(n,m+1):
#     mylist.append(i)
# print(tuple(mylist))
# 23.Reverse Tuple: Create a new tuple that contains the elements of the original tuple in reverse order.
# tuple1=eval(input('Enter the tuple: '))
# mylist=list(tuple1)
# print(tuple(mylist[-1::-1]))

# 24.Check Palindrome: Given a tuple, check if the tuple is a palindrome (reads the same forwards and backwards).
# tuple1=eval(input('Enter the tuple: '))
# mylist=list(tuple1)
# if mylist[-1::-1]==mylist:
#     print('This tuple is palindrome')
# else:
#     print('This tuple is not palindrome')

# 25.Get Unique Elements: Given a tuple, create a new tuple that contains only the unique elements while maintaining the original order.
# tuple1=eval(input('Enter the tuple: '))
# mylist=[]
# for i in tuple(tuple1):
#     if tuple1.count(i)==1:
#         mylist.append(i)
# print('The unique elements tuple is',tuple(mylist))