
[c, p] = map(int, input().strip().split(" "))
cbs = {}
project = {}
last_bb = -1
last_bb_name = ''
bbs = {}

for i in range(c):  # numS -> number of skills
    [name, numS] = map(str, input().strip().split(" "))
    cbs[name] = {}
    for j in range(int(numS)):
        [skill, level] = map(str, input().strip().split(" "))
        cbs[name][skill] = int(level)

for i in range(p):
    [name, duration, score, bb, numR] = map(str, input().strip().split(" "))
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
        [nameS, level] = map(str, input().strip().split(" "))
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

pnames=[key for key in project]
for day in range(last_bb):
    pname = bb_min()


    for name in pnames:
        output[name] = []
        for role in project[name]['roles'].keys():
            cbr = findCbr(role, project[name]['roles'][role])
            output[name].append(cbr)
        project[name]['start'] = day
        # pnames.pop()

# for pName in project:
#     for skill in project[pName]['roles']:



# print(pname)
    # print(cbs)
    # print(project)
print(output)