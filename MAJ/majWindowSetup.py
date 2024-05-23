try:
    import os
    import keyboard
except:
    while True:
        os.system('cls || clear')
        print('Please ensure that you have the "Keyboard" and "OS" libraries installed on your computer.\n')
        print('Install via pip by running the following commands on your terminal:')
        print('       pip install keyboard')
        print('       pip install os')
        input()


class FirstStart: # Using a class means the variables inside them stay inside and and don't unnessesarily clutter the type hinting. 
    def drawOutline(w, h): # Draws the window
        print('█', end='') 
        for i in range(w):
            print('▒',end='')
        print('█')

        for i in range(h):
            print('▒', end='')
            for i in range(w):
                print(' ',end='')
            print('▒')

        print('█', end='')
        for i in range(w):
            print('▒',end='')
        print('█')

    def printPrompt(): # Prints the prompt
        print("Resize the window to fit your screen and you're able to view these prompts.")
        print(' Enter [w] to decrease height.')
        print(' Enter [a] to decrease width.')
        print(' Enter [s] to increase height.')
        print(' Enter [d] to increase width.')
        print(' Enter [p] to continue.')   
    
    def getKeyboardInput(width, height): # Get the keyboard input.
        keyboardInput = None
        while keyboardInput == None:
            if keyboard.is_pressed('w'):  # if key 'w' is pressed 
                keyboardInput = 'w'
                break
            if keyboard.is_pressed('a'):  # if key 'a' is pressed 
                keyboardInput = 'a'
                break
            if keyboard.is_pressed('s'):  # if key 's' is pressed 
                keyboardInput = 's'
                break
            if keyboard.is_pressed('d'):  # if key 'd' is pressed 
                keyboardInput = 'd'
                break
            if keyboard.is_pressed('p'):  # if key 'p' is pressed 
                keyboardInput = 'p'
                break
        match keyboardInput.lower(): # Increase/decrease height/width based on input.
            case 'w': 
                if not height < 5: 
                    height -= 1
            case 'a': 
                if not width < 20:
                    width -= 1
            case 's': height += 1
            case 'd': width += 1
            case 'p': 
                return None
        return (width, height)
    
    def getWindowThroughSetupProcess(): # Run the setup process.
        width = 30
        height = 10

        while True:
            os.system('cls')

            FirstStart.drawOutline(width, height)
            FirstStart.printPrompt()

            try: 
                width, height = FirstStart.getKeyboardInput(width, height) # If the input returns None, then the program will raise an error.
            except: # This error is handled by returning the specified height/width as a tuple.
                os.system('cls || clear')
                return (width, height)