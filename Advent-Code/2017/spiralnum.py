from itertools import cycle

test1 = 1
test2 = 12
test3 = 23
test4 = 1024
inputNum = 277678

# Helper Functions to Make a Grid for Number Spiral
def moveRight(x, y):
    return x+1, y

def moveDown(x, y):
    return x, y-1

def moveLeft(x, y):
    return x-1, y

def moveUp(x, y):
    return x, y+1

moves = [moveRight, moveDown, moveLeft, moveUp]

def generateGrid(endPoint):
    _moves = cycle(moves)
    n = 1
    pos = 0,0
    times_to_move = 1

    yield n,pos

    while True:
        for _ in range(2):
            move = next(_moves)
            for _ in range(times_to_move):
                if n >= endPoint:
                    return
                pos = move(*pos)
                n+=1
                yield n,pos

        times_to_move+=1

# print list(generateGrid(277678))

def generateSumGrid(endPoint):
    # grid is [x_coord, y_coord] : [grid_value, sum_value]
    grid = {(0,0) : [1,1]}
    _moves = cycle(moves)
    pos = 0,0
    times_to_move = 1
    n = 1
    
    # This is gross please don't do this next time lololo
    breakFlag = 0

    while True:
        if (breakFlag):
            break

        for _ in range(2):
            if (breakFlag):
                break
            move = next(_moves)
            for _ in range(times_to_move):
                if (breakFlag):
                    break

                if n >= endPoint:
                    return

                # Summation includes previous value + other adjacent values
                summedValue = 0
                pos = move(*pos)
                n+=1

                # Up
                if ((pos[0], pos[1]+1) in grid):
                    summedValue += grid[(pos[0], pos[1]+1)][1]

                # Right    
                if ((pos[0]+1, pos[1]) in grid):
                    summedValue += grid[(pos[0]+1, pos[1])][1]

                # Down
                if ((pos[0], pos[1]-1) in grid):
                    summedValue += grid[(pos[0], pos[1]-1)][1]

                # Left 
                if ((pos[0]-1, pos[1]) in grid):
                    summedValue += grid[(pos[0]-1, pos[1])][1]
                
                # Top Left
                if ((pos[0]-1, pos[1]+1) in grid):
                    summedValue += grid[(pos[0]-1, pos[1]+1)][1]

                # Top Right
                if ((pos[0]+1, pos[1]+1) in grid):
                    summedValue += grid[(pos[0]+1, pos[1]+1)][1]

                # Bottom Right
                if ((pos[0]+1, pos[1]-1) in grid):
                    summedValue += grid[(pos[0]+1, pos[1]-1)][1]

                # Bottom Left
                if ((pos[0]-1, pos[1]-1) in grid):
                    summedValue += grid[(pos[0]-1, pos[1]-1)][1]
                                
                if summedValue > endPoint:
                    print "THIS IS IT"
                    print summedValue
                    breakFlag = 1
                    break 

                grid.update({pos : [n, summedValue]})


                print grid

        times_to_move+=1

    print grid
    return grid
        
print generateSumGrid(277678)