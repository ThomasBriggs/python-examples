l1= [10, 5, 2, 3, 7, 5]
ans = 10

l2 = [10, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 7, 5]

def sum_pairs(ints, s):

    best_pair = [0, len(ints)]
    last_pair = None
    
    for i in range(len(ints)):
        if i >= best_pair[1]:
            return [ints[best_pair[0]], ints[best_pair[1]]]
        for j in range(i+1, best_pair[1]):
            # if (last_pair == [ints[i],ints[j]]):
            #     pass
            # else:
                last_num = ints[j]
                print("i_index={}, i_value={}\tj_index={}, j_value={}".format(i, ints[i], j, ints[j]))
                if ints[i] + ints[j] == s:
                    print("found pair ={},{}".format(i,j))
                    if i >= best_pair[0]:
                        if j <= best_pair[1]:
                            best_pair = [i, j]
                            print(best_pair)
    return None
print(sum_pairs(l2, ans))