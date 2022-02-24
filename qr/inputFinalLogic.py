# Google Hash Code 2022, Qualification round
# Meta Warriors
[c, p] = map(int, input().strip().split(" "))
cbs = {}
project = {}

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
    project[name]['roles'] = {}
    for j in range(int(numR)):
        [nameS, level] = map(str, input().strip().split(" "))
        project[name]['roles'][nameS] = int(level)

# print(cbs)
# print(project)
