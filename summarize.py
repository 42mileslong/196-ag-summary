with open('grade.txt') as f:
    content = f.readlines()
    
f = open('grade_summary.txt', 'w')
test = None

for i in range(5, len(content)):
    if test != content[i][0:content[i].find('/')]:
        test = content[i][0:content[i].find('/')]
        content.insert(i, '\n')

for line in content:
    f.write(line)

f.close()
