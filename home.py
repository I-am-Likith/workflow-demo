def sel(lst):
    l = len(lst)
    for i in range(l):
        min = i
        for j in range(i+1,l):
            if lst[j] < lst[min]:
                min = j
        temp = lst[i]
        lst[i] = lst[min]
        lst[min] = temp
    return lst

lst = [13,46,54,22,20,11]
res= sel(lst)
print(res)