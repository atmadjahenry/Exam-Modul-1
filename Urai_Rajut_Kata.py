print('SOAL NO 3')

code ='Code' # CCoCodCode code[0,0,1,0,1,2,0,1,2,3]
python = 'Python' # PPyPytPythPythoPython
purwadhika = 'Purwadhika' #PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika

Code = 'CCoCodCode'
Python = 'PPyPytPythPythoPython'
Purwadhika = 'PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'

print('Urai')

for i in code :
    indexi = code.index(i)
    for y in range(indexi + 1) :
        # print(y, end = ' ')
        if y > (len(code)-1) :
            break


        print(code[y], end = '')

print('\n')


for i in python :
    indexi = python.index(i)
    for y in range(indexi + 1) :
        
        if y > (len(python)-1) :
            break


        print(python[y], end='')


print('\n')


for i in purwadhika :
    indexi = purwadhika.index(i)
    for y in range(indexi + 1) :
        # print(y, end='')
        if y > (len(purwadhika)-1) :
            break


        print(purwadhika[y], end='')


print('Rajut')


print(Code[-(Code.count('C')):])
print(Python[-(Python.count('P')):])
print(Purwadhika[-(Purwadhika.count('P')):])