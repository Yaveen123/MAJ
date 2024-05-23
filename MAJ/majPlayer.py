try:
    import os
    import keyboard
    from majPrint import Print
except:
    while True:
        os.system('cls || clear')
        print('Please ensure that you have the "Keyboard" and "OS" libraries installed on your computer.\n')
        print('Install via pip by running the following commands on your terminal:')
        print('       pip install keyboard')
        print('       pip install os')
        input()

class Player:
    def __init__(self, startingWidth, startingHeight, wW, wH): # Initialise the player
        self.currWidth = startingWidth
        self.currHeight = startingHeight
        self.wW = wW
        self.wH = wH 

    def movePlayer(self, maze): # Move the player without colliding with any walls or exiting the maze.
        try:
            match self.getKeyboardInput(): # Gets keyboard input.
                case 'w':
                    if maze[self.currHeight-1][self.currWidth] != '█':
                        maze[self.currHeight][self.currWidth] = ' '
                        maze[self.currHeight-1][self.currWidth] = '☻'
                        self.currHeight -= 1 
                case 'a':
                    if maze[self.currHeight][self.currWidth-1] != '█':
                        maze[self.currHeight][self.currWidth] = ' '
                        maze[self.currHeight][self.currWidth-1] = '☻'
                        self.currWidth -=1
                case 'd':
                    if maze[self.currHeight][self.currWidth+1] != '█':
                        maze[self.currHeight][self.currWidth] = ' '
                        maze[self.currHeight][self.currWidth+1] = '☻'
                        self.currWidth += 1
                case 's':
                    if maze[self.currHeight+1][self.currWidth] != '█':
                        maze[self.currHeight][self.currWidth] = ' '
                        maze[self.currHeight+1][self.currWidth] = '☻'
                        self.currHeight += 1
        except:
            while True:
                os.system('cls || clear')
                Print.printCentered("You win!", self.wH, self.wW)
                input('')
            

        return maze

    def getKeyboardInput(self): # Gets the keyboard project
        keyboardInput = None 
        while keyboardInput == None:
            if keyboard.is_pressed('w'):  # if key 'w' is pressed 
                keyboardInput = 'w'
                while keyboard.is_pressed('w'): # Waits till keyboard is not pressed to avoid repeat inputs.
                    pass
                break
            elif keyboard.is_pressed('a'):  # if key 'a' is pressed 
                keyboardInput = 'a'
                while keyboard.is_pressed('w'):
                    pass
                break
            elif keyboard.is_pressed('s'):  # if key 's' is pressed 
                keyboardInput = 's'
                while keyboard.is_pressed('w'):
                    pass
                break
            elif keyboard.is_pressed('d'):  # if key 'd' is pressed 
                keyboardInput = 'd'
                while keyboard.is_pressed('w'):
                    pass
                break
        
        return keyboardInput