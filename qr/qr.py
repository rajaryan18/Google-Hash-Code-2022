# Google Hash Code 2022, Qualification round
# Meta Warriors
cbs = {}
project = {}
last_bb = -1
last_bb_name = ''
bbs = {}
output = {}
files = ['ain.txt','bin.txt','cin.txt', 'din.txt', 'ein.txt', 'fin.txt']
for file in files:
    with open(file, 'r') as f:
        [c, p] = map(int, f.readline().strip().split(" "))

        for i in range(c):  # numS -> number of skills
            [name, numS] = map(str, f.readline().strip().split(" "))
            cbs[name] = {}
            for j in range(int(numS)):
                [skill, level] = map(str, f.readline().strip().split(" "))
                cbs[name][skill] = int(level)

        for i in range(p):
            [name, duration, score, bb, numR] = map(
                str, f.readline().strip().split(" "))
            project[name] = {}
            project[name]['duration'] = int(duration)
            project[name]['score'] = int(score)
            project[name]['bb'] = int(bb)
            bbs[name] = int(bb)
            if last_bb <= int(bb):
                last_bb_name = name
                last_bb = max(last_bb, int(bb))
            project[name]['start'] = -1
            project[name]['roles'] = {}
            for j in range(int(numR)):
                [nameS, level] = map(str, f.readline().strip().split(" "))
                project[name]['roles'][nameS] = int(level)

        # 2 4 5 1 1

        output = {}
        # name: [contributers]
        # project[outputs.key()]['start'] and project[outputs.key()]['duration']

        def bb_min():
            global last_bb, last_bb_name
            minbb = last_bb
            pname = [last_bb_name]
            for projects in project:
                # projects = { name (key): { 'bb' : int } }
                if minbb > project[projects]['bb']:
                    minbb = project[projects]['bb']
                    pname = []
                    pname.append(projects)
                elif minbb == project[projects]['bb']:
                    pname.append(projects)
            return pname

        def findCbr(skill, level):
            global cbs
            for cb in cbs:
                for sk in cbs[cb]:
                    if sk == skill and level <= cbs[cb][sk]:
                        return cb
            

        pnames = [key for key in project]
        for day in range(last_bb):
            pname = bb_min()

            for name in pnames:
                output[name] = []
                for role in project[name]['roles'].keys():
                    cbr = findCbr(role, project[name]['roles'][role])
                    output[name].append(cbr)
                project[name]['start'] = day
                # pnames.pop()
        f.close()
# for pName in project:
#     for skill in project[pName]['roles']:


# print(pname)
    # print(cbs)
    # print(project)
# print(output)
#files = ['aout.txt', 'bout.txt', 'cout.txt', 'dout.txt', 'eout.txt', 'fout.txt']
# print(n)
#for file in files:
    with open('o' + file, 'w') as f:
        keys = [key for key in output]
        n = len(keys)
        for key in output:
            # print(key)
            # print(output[key].join(" "))
            if (output[key] == [None]):
                n -= 1

        # print(n)
        f.write(str(n))
        # f.write('\n')
        # print(keys)
        for key in output:
            if(output[key][0] != None):
                f.write('\n')
                f.write(key)
                f.write('\n')
            for k in output[key]:
                if(k == None):
                    break
                f.write(k)
                f.write(" ")
            # f.write('\n')
        f.close()
        output = {}
