output = ''

files = ['a_an_example.txt', 'b_basic.txt', 'c_coarse.txt', 'd_difficult.txt', 'e_elaborate.txt']
for file in files:
    with open(file, 'r') as f:

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


files = ['a_an_example_out.txt', 'b_basic_out.txt', 'c_coarse_out.txt', 'd_difficult_out.txt', 'e_elaborate_out.txt']
for file in files:
    with open(file, 'w') as fout:
        fout.write(output)
        fout.close()