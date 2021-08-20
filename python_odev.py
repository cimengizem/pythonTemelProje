def join_list(lst):
    
    lst1 = []
    lst2 = []
    
    for i in range(len(lst)):
        if type(lst[i]) is list:
            for j in range(len(lst[i])):
                if type(lst[i][j]) is list:
                    for k in range(len(lst[i][j])):
                        lst1.append(lst[i][j][k])
                else:
                    lst1.append(lst[i][j])
        else:
            lst1.append(lst[i])
            
    for i in lst1:
        if type(i) is list:
            for j in i:
                lst2.append(j)
        else:
            lst2.append(i)
            
    print(*lst1, sep=",")  

            
l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print("Soru 1")
join_list(l)


def list_reverse(lst):
    lst.reverse()
    
    for i in lst:
        if type(i) is list:
            i.reverse()
        else:
            continue
    
    return lst

l = [[1, 2], [3, 4], [5, 6, 7]]
print("Soru 2")
print(list_reverse(l))