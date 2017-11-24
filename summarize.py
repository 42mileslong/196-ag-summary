# oh god this is janky as hell please forgive me

with open('grade.txt') as f:
    content = f.readlines()

f = open('grade_summary.txt', 'w')
output = content[0:5]

current_test = None
test_results = {}

for i in range(5, len(content) - 2):
    if current_test != content[i][0:content[i].find('/')]:
        output.append('\n')
        
        current_test = content[i][0:content[i].find('/')]
        test_results[current_test] = [0, 0]

    print(content[i][content[i].find(':'):])
    if content[i][content[i].find(': '):] == ': Correct\n':
        test_results[current_test][0] += 1
    test_results[current_test][1] += 1
    
    output.append(content[i])

tests = list(test_results.keys())
    
for i in range(len(tests)):
    output.insert(3+i, '{}: {}/{} \n'.format(tests[i], test_results[tests[i]][0], test_results[tests[i]][1]))
    
for line in output:
    f.write(line)

f.close()
