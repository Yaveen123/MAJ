
"""
The original intention of this game was to be able go through a maze and dodge certain enemies:
- Matt, where you had to shift a code cypher for to decode a coffee machine.
- Anil, where you had to solve a maths problem
- Jeff, where you had to find his hat
However the scale of the project exceeded the time limit set for this project.
"""

from majWindowSetup import *
from majPrint import *
from majMaze import runMaze
from majPlayer import Player
#from majMazeOLD import *

WINDOWWIDTH, WINDOWHEIGHT = FirstStart.getWindowThroughSetupProcess() # Abstracted method. 
TEXTENDSPEED = 2

# Starting sequence
Print.printCentredSlow("It's 8:30am.", WINDOWHEIGHT, WINDOWWIDTH, 0.01, TEXTENDSPEED)
Print.printCentredSlow("You've made the mistake of coming late to school.", WINDOWHEIGHT, WINDOWWIDTH, 0.01, TEXTENDSPEED)
Print.printCentredSlow("You must reach the classroom without being seen.", WINDOWHEIGHT, WINDOWWIDTH, 0.01, TEXTENDSPEED)
Print.clear(True)



maze, playerStartingWidth, playerStartingHeight = runMaze(WINDOWWIDTH, WINDOWHEIGHT, '☻')
player = Player(playerStartingWidth, playerStartingHeight, WINDOWWIDTH, WINDOWHEIGHT) # Initialise the player with starting postion. 

Print.printMaze(maze, WINDOWHEIGHT, WINDOWWIDTH)
while True:
    maze = player.movePlayer(maze)
    Print.clear(True)
    Print.printMaze(maze, WINDOWHEIGHT, WINDOWWIDTH)
    