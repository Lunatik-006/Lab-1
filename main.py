RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

#task1
def flag():
    for i in range(8):
        if 3<=i<=4: t=8
        elif i==0 or i==7: t=0
        else: t=2
        print(f'{RED}{"  "*((14-t)//2)}{END}{WHITE}{"  "*t}{END}{RED}{"  "*((14-t)//2)}{END}')
flag()

#task2
'''plot_list = [[0 for i in range(10)] for i in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = i ** 3

step = round(abs(result[0] - result[9]) / 9, 2)
print(step)

for i in range(10):
    for j in range(10):
        if j == 0:
            plot_list[i][j] = step * (8-i) + step

for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - result[9 - j]) < step:
            for k in range(9):
                if 8 - k == j:
                    plot_list[i][k+1] = 1

for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += '\t' + str(int(plot_list[i][j])) + '\t'
        if plot_list[i][j] == 0:
            line += '--'
        if plot_list[i][j] == 1:
            line += '!!'
    print(line)
print('\t0\t1 2 3 4 5 6 7 8 9')

for i in range(10):
    #print(plot_list[i])
    pass

file = open('sequence.txt', 'r')
list = []
for number in file:
    list.append(float(number))
file.close()
print(list)
print(RED+'YEAH!'+END)'''