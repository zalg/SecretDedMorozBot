import itertools as it
import random

def is_no_violations(lst, rstr):
    lst.append(lst[0])
    for i in range(len(lst)-1):
        k = tuple(lst[i:i+2])
        print(k)
        if k in rstr:
            return False
    return True


l = [1,2,3,4,5,6]
def make_pairs(lst, rstr):
    #make it unic
    random.shuffle(lst)
    p = it.permutations(lst)
    att = it.count(1)
    for combination in p:
        print('!attempt '+str(next(att)))
        print('!Shuffled list is - ' + str(combination))
        if is_no_violations(list(combination), rstr):
            rslt = []
            lst = list(combination)
            lst.append(lst[0])
            for i in range(len(lst)-1):
                k = tuple(lst[i:i+2])
                rslt.append(k)
            return rslt
    return []




    


