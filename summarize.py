# oh god this is janky as hell please forgive me

with open('grade.txt') as f:
    content = f.readlines()

f = open('grade_summary.md', 'w')
output = ['# Summary:',
          '| Function | # Correct | # Possible |',
          '|----------|-----------|------------|',
          '', '', '# Detailed Report:', '']

current_test = None
test_results = {'Total points earned': [0, 0]}

for i in range(5, len(content) - 2):
    if current_test != content[i][0:content[i].find('/')]:        
        current_test = content[i][0:content[i].find('/')]
        test_results[current_test] = [0, 0]

        output.append('')
        output.append('#### {0}'.format(current_test))
        output.append('|Test|Status|')
        output.append('|----|------|')

    if content[i][content[i].find(': ') + 2:-1] == 'Correct':
        test_results[current_test][0] += 1
        test_results['Total points earned'][0] += 1
    test_results[current_test][1] += 1
    test_results['Total points earned'][1] += 1
    
    output.append('| {} | {} |'.format(content[i][content[i].find('/') + 1: content[i].find(': ')], content[i][content[i].find(': ') + 2:-1]))

tests = list(test_results.keys())
    
for i in range(len(tests)):
    output.insert(3 + i, '| {0} | {1} | {2} |'.format(tests[i], test_results[tests[i]][0], test_results[tests[i]][1]))
    
for line in output:
    f.write('{}{}'.format(line, '\n'))

f.close()
