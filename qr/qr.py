# Google Hash Code 2022, Qualification round
# Meta Warriors
[c, p] = map(int, input().strip().split(" "))
cbs = {}
project = {}

for i in range(c):  # numS -> number of skills
    [name, numS] = input().strip().split(" ")
    cbs[name] = {}
    for j in range(int(numS)):
        [skill, level] = input().strip().split(" ")
        cbs[name][skill] = int(level)
# { 'duration': int(duration) }
# project['name']['duration']
for i in range(p):
    [name, duration, score, bb, numR] = input().strip().split(" ")
    project[name]['duration'] = int(duration)
    project[name]['score'] = int(score)
    project[name]['bb'] = int(bb)
    project[name]['roles'] = {}
    for j in range(int(numR)):
        [nameS, level] = input().strip().split(" ")
        project[name]['roles'][nameS] = int(level)

print(cbs)
print(project)