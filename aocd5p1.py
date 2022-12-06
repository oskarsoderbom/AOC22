#partone

cratelistrough = open('/Users/oskarsoderbom/aocd5.txt').read()
cratelist = cratelistrough.split('\n')

demandsraw = open('/Users/oskarsoderbom/aocd5v2.txt').read()
demands = demandsraw.split('\n')


excrates = [['[N]', '[Z]'], ['[D]','[C]','[M]'], ['[P]']]
exstring = ["move 1 from 2 to 1", "move 3 from 1 to 3", "move 2 from 2 to 1", "move 1 from 1 to 2"]
#Vrider om listorna så att de går horisontellt ist för vertikalt
#Används just nu
wrapped = []
for i in range(0, len(cratelist[0]),4):
    tmp = [row[i:i+4] for row in cratelist]
    wrapped.append(tmp)

wrappedv2 = []
for count, value in enumerate(wrapped):
    tmp2 = []
    for var in range(len(value)):
        if wrapped[count][var] == '    ':
            pass
        else:
            tmp2.append(wrapped[count][var])
    wrappedv2.append(tmp2)


wrappedv3 = []
for count, value in enumerate(wrapped):
    tmp2 = []
    for var in range(len(value)):
        if wrapped[count][var] == '    ':
            pass
        else:
            tmp2.append(wrapped[count][var])
    wrappedv3.append(tmp2)




#Kortar ned textinputen till bara siffror
shortinput = []
for j,k in enumerate(demands):
    new = demands[j].split(' ')
    move = int(new[1])
    start = int(new[3])
    end = int(new[5])
    shortinput.append([move, start, end])

#Kortar ned textinputen till bara siffror
shortinputtest = []
for j,k in enumerate(exstring):
    new = exstring[j].split(' ')
    move = int(new[1])
    start = int(new[3])
    end = int(new[5])
    shortinputtest.append([move, start, end])

#Detta ger galet ful output men fungerar på testcaset i alla fall :)

for x, y in enumerate(shortinput):
    for i in range(y[0]):
        over = wrappedv2[y[1]-1].pop(0)   #för antalet crates som ska flyttas så plockas den översta lådan
        wrappedv2[y[2]-1].insert(0, over) #och läggs in här på nytt ställe
answer = [row[0] for row in wrappedv2] #och här plockar vi bara ut de översta
print(f'Answer to problem nr 1 is {answer}')


#Part two
for line in shortinput:

    mover = wrappedv3[line[1]-1][:line[0]] #vilka vill vi flytta?

    for index, item in reversed(list(enumerate(mover))): #loopar baklänges här för att få i rätt ordning

        wrappedv3[line[1]-1].remove(item)

        wrappedv3[line[2]-1].insert(0, item)

newanswer = [rad[0] for rad in wrappedv3]
print(f'Answer to problem nr2 is : {newanswer}')
