output = ''

# 1) a_an_example.txt
# 2) b_basic.txt
# 3) c_coarse.txt
# 4) d_difficult.txt
# 5) e_elaborate.txt

with open('e_elaborate.txt', 'r') as f:

    c = int(f.readline())
    count = {}
    pre = []
    ans = [0]

    for i in range(2*c):
        pre.append(f.readline().strip().split(" "))
    for i in range(2*c):
        if(i %2 == 0):
            for j in range(1, int(pre[i][0])+1):
                ingre = pre[i][j]
                count[ingre] = count[ingre]+1/int(pre[i][0]) if ingre in count else 1/int(pre[i][0])
        else:
            for j in range(1, int(pre[i][0])+1):
                ingre = pre[i][j]
                count[ingre] = count[ingre]-1/int(pre[i][0]) if ingre in count else -1/int(pre[i][0])

    for key in count:
        if (count[key] >=0):
            ans.append(key)

    ans[0] = len(ans)-1


    #print(" ".join(list(map(str,ans))))
    output = " ".join(list(map(str, ans)))
    f.close()


with open('e_elaborate_out.txt', 'w') as fout:
    fout.write(output)
    fout.close()