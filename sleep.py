from random import randint

listS = [6, 7, 67, 13, 14, 12]


def bubble(listy) -> list:
    count = 0
    for i in range(listy.__len__()):
        if i == listy.__len__()-1 and count == 0:
            print(f"List has been sorted:\n {listy}")
            return listy
        elif i+1 == listy.__len__():
            bubble(listy)
        elif listy[i] > listy[i+1]:
            placeholder = listy[i]
            listy[i] = listy[i+1]
            listy[i+1] = placeholder
            count += 1

#bubble(listS)
def selection(listy) -> list:
    for j in range(listy.__len__()-1):
        main = j
        for  i in range(j,listy.__len__()):
            if listy[main] > listy[i]:
                main = i
                
        placeholder = listy[j]
        listy[j] = listy[main]
        listy[main] = placeholder
    return listy

def inertia(listy) -> list:
    for i in range(1, listy.__len__()):
        cur_val = listy[i]
        j = i-1
        while j >= 0 and cur_val < listy[j]:
            listy[j+1] = listy[j]
            j-=1
        listy[j+1] = cur_val
        print(listy)
    return listy




print(inertia(listS))





"""
[6,60.2,7,10,16,3]
[6,60.2,7,10,16,3]
[6,7,60.2,10,16,3]
[6,7,10,60.2,16,3]
[6,7,10,16,60.2,3]
[3,6,7,10,16,60.2]
"""