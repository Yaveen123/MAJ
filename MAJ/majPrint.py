try:
    import os
    import time
except:
    while True:
        os.system('cls || clear')
        print('Please ensure that you have the "Time" and "OS" libraries installed on your computer.\n')
        print('Install via pip by running the following commands on your terminal:')
        print('       pip install time')
        print('       pip install os')
        input()

class Print:
    def printCentered(item: str, wH: int, wW: int): # Polymorphic method used to print centered text.
        print('\n'*(wH//2)) # Push text to centre y
        print(' '*((wW//2)-len(item)//2), end=item) # Push text to centre x
        print('\n'*(wH//2)) # Push everything else down y

    def printCentredSlow(item: str, wH: int, wW: int, animSpeed: int, endWait: int): # Print centered text with an animation 
        j = "" 
        for x in item:
            j = j + x
            time.sleep(animSpeed)
            os.system('cls || clear')
            Print.printCentered(j, wH, wW) # Utilises polymorphed code.
        time.sleep(endWait)
    
    def clear(all:bool):
        os.system('cls || clear')
        if all:
            pass
    
    def printMaze(maze, height, width):
        mazeStr = ''
        for i in range(0, height):
            for j in range(0, width):
                if (maze[i][j] == 'u'):
                    mazeStr = mazeStr + str(maze[i][j]) 
                elif (maze[i][j] == ' '):
                    mazeStr = mazeStr + str(maze[i][j])
                else:
                    mazeStr = mazeStr + str(maze[i][j])
            mazeStr = mazeStr + '\n'
        print(mazeStr)
        print("[W] to move up\n[A] to move left\n[D] to move right\n[S] to move down\nReach an exit in as little moves as possible.\nOnly one exit works.")