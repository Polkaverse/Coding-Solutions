def part1(x):
   for space in range(0,x+1):
       print (' '*(x-space) + '*'*(2*space+1))

def part2(y):
   for d in range(0,y):
       print (' '*(days-(d+1)) + '*'*(2*d+3))


while 1:
    days = input()
    days = int(days)
    if days <= 1:
        print("You cannot generate christmas tree")
    elif days > 20:
        print("Tree is no more")
    else:
        part1(days)
        part2(days-1)
for z in range(0,days-3):
    part2(days-2-(1*z))
    print(' '*(days) + '*')
    print(' '*(days) + '*')
