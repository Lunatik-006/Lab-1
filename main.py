RED = '\u001b[41m'
WHITE = '\u001b[47m'
BLACK = '\u001b[40m'
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
def uzor(h,l):
    diameter=9
    for t in range(h):
        radius = (diameter/2)-0.5
        for i in range(diameter):
            st=f''
            for j in range(diameter):
                x = i - radius
                y = j - radius
                if radius**2-4<= x**2 + y**2 <= radius**2+2:
                    st+=f'{BLACK}{" "*(2)}{END}'
                else:
                    st+=f'{WHITE}{" "*(2)}{END}'
            print(st*(2*l))
uzor(1,2)

#task3
def gr():
    for x in range(9,-2,-1):
        if x==9: print(f'{x}{" "}{"^"}{"  "}{"-"*(x*2-2)}{"//"}{"-"*(16-x*2)}')
        if 8>=x>=1: print(f'{x}{" "}{"|"}{"  "}{"-"*(x*2-2)}{"//"}{"-"*(18-x*2)}')
        if x==0: print(f'{"  "}{"|"}{"  "}{"-"*17}{">"}')
        if x==-1: 
            st=f'{0}{"   "}'
            for i in range(1,10):
                st+=f'{3*i}{" "}'
            print(st)
gr()

#task4
def pr():
    f=open('sequence.txt').readlines()
    print(len([float(i.split()[0]) for i in f if -3.0<=float(i.split()[0])<=3.0])/len(f)*100)
pr()