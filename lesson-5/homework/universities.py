universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(given_list1):
    '''The input should be a list of lists where each individual list contains three elements: (a) the name of a university, (b) the total number of enrolled students, and (c) the annual tuition fees.'''
    total_students_list = [triplelist[1] for triplelist in given_list1]
    tution_fees_list = [triplelist[2] for triplelist in given_list1]
    return(total_students_list,tution_fees_list)

def mean(given_list2):
    s=0
    for i in given_list2:
        s+=i
    return(round((s/len(given_list2)),2))

def median(given_list3):
    n=len(given_list3)
    if n%2==0:
        return((given_list3[(n/2)]+given_list3[(n/2+1)])/2)
    else:
        m = int((n+1)/2)
        return(given_list3[m])
      
list2,list3=enrollment_stats(universities)
print('******************************')
print(f'Total students: {sum(list2)}')
print(f'Total tuition: ${sum(list3)}\n')

print(f'Student mean: {mean(list2)}')
print(f'Student median: {median(list2)}\n')

print(f'Tuition mean: ${mean(list3)}')
print(f'Tuition median: ${median(list3)}')
print('******************************')

