def rec_sum_ends(lst):
    if len(lst) <= 2:
        return lst
    if len(lst) % 2 == 0:

        front_half = lst[:len(lst)//2]
        reversed_back_half = lst[:len(lst)//2-1:-1]
        combined = [sum(el) for el in zip(front_half, reversed_back_half)]   
        

    else:

        midpoint = ((len(lst)) // 2)
        #print(f"midpoint {midpoint}")
        front_half = lst[:midpoint]
        reversed_back_half = lst[:-midpoint-1:-1]   
        combined = [sum(el) for el in zip(front_half, reversed_back_half)]   
        combined.append(lst[len(lst)//2])

    print(combined)
    
    return rec_sum_ends(combined)

print(rec_sum_ends([1, 2, 1, 2, 1, 1, 1, 1]))
