# https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e 

from colorama import init, Fore
import random

class MazeGen:
    def __init__(self, cell, wall, width ,height):
        self.cellChar = cell
        self.wallChar = wall
        self.width = width
        self.height = height
    
        
    def generateMaze(self):
        # Get randomised starting position.
        self.startingHeight = int(random.random()*self.height)
        self.startingWidth = int(random.random()*self.width)
        
        #Check if the starting position isn't on the edge of the maze.
        if self.startingHeight == 0:
            self.startingHeight +=1
        if self.startingHeight == self.height-1:
            self.startingHeight -= 1
        
        if self.startingWidth == 0:
            self.startingWidth += 1
        if self.startingWidth == self.width-1:
            self.startingWidth -= 1

        # Generate the walls 
        self.maze[self.startingHeight][self.startingWidth] = self.cellChar
        self.walls = []
        
        self.walls.append([self.startingHeight-1, self.startingWidth])
        self.walls.append([self.startingHeight, self.startingWidth-1])
        self.walls.append([self.startingHeight, self.startingWidth+1])
        self.walls.append([self.startingHeight-1, self.startingWidth])
        
        # Ensure the blocks around the starting cell are walls
        self.maze[self.startingHeight-1][self.startingWidth] = self.wallChar
        self.maze[self.startingHeight][self.startingWidth-1] = self.wallChar
        self.maze[self.startingHeight][self.startingWidth+1] = self.wallChar
        self.maze[self.startingHeight+1][self.startingWidth] = self.wallChar

        
        self.makeWalls(self.width, self.height)
        self.createMaze()
        self.createEntranceExit(self.width, self.height)
        self.printMaze()
    
    def createMaze(self):
        # While there are walls in the list, pick a random wall from the list.
        while self.walls:
            self.randWall = self.walls[int(random.random()*len(self.walls))-1]
            
            # Check left wall
            if self.randWall[1] != 0: 
                if self.maze[self.randWall[0]][self.randWall[1]-1] == 'u' and self.maze[self.randWall[0]][self.randWall[1]+1] == 'c':
                    # Find no. surrounding cells.
                    self.s_cells = self.surroundingCells(self.randWall, self.maze)
                    
                    if self.s_cells < 2:
                        # New path
                        self.maze[self.randWall[0]][self.randWall[1]] = 'c'
                        
                        # Upper cells and new walls
                        if self.randWall[0] != 0:
                            if self.maze[self.randWall[0]-1][self.randWall[1]] != 'c':
                               self.maze[self.randWall[0]-1][self.randWall[1]] = 'w'
                            if ([self.randWall[0]-1, self.randWall[1]] not in self.walls): 
                                self.walls.append([self.randWall[0]-1, self.randWall[1]])
                    
                        # Bottom cell
                        if self.randWall[0] != self.height-1:
                            if (self.maze[self.randWall[0]+1][self.randWall[1]] != 'c'):
                                self.maze[self.randWall[0]+1][self.randWall[1]] = 'w'
                            if ([self.randWall[0]+1, self.randWall[1]] not in self.walls): 
                                self.walls.append([self.randWall[0]+1, self.randWall[1]])
                    
                        # Left cell
                        if self.randWall[1] != 0:
                            if (self.maze[self.randWall[0]][self.randWall[1]-1] != 'c'):
                                self.maze[self.randWall[0]][self.randWall[1]-1] = 'w'
                            if ([self.randWall[0], self.randWall[1]-1] not in self.walls): 
                                self.walls.append([self.randWall[0], self.randWall[1]-1])

                    self.deleteWall(self.randWall)
                    continue
                continue

            # Check if upper wall
            if self.randWall[0] != 0: 
                if self.maze[self.randWall[0]-1][self.randWall[1]] == 'u' and self.maze[self.randWall[0]+1][self.randWall[1]] == 'c':
                    # Find no. surrounding cells.
                    self.s_cells = self.surroundingCells(self.randWall, self.maze)
                    
                    if self.s_cells < 2:
                        # New path
                        self.maze[self.randWall[0]][self.randWall[1]] = 'c'
                        
                        # Upper cells and new walls
                        if self.randWall[0] != 0:
                            if self.maze[self.randWall[0]-1][self.randWall[1]] != 'c':
                               self.maze[self.randWall[0]-1][self.randWall[1]] = 'w'
                            if ([self.randWall[0]-1, self.randWall[1]] not in self.walls): 
                                self.walls.append([self.randWall[0]-1, self.randWall[1]])
                    
                        # Left cell
                        if self.randWall[1] != 0:
                            if (self.maze[self.randWall[0]][self.randWall[1]-1] != 'c'):
                                self.maze[self.randWall[0]][self.randWall[1]-1] = 'w'
                            if ([self.randWall[0], self.randWall[1]-1] not in self.walls): 
                                self.walls.append([self.randWall[0], self.randWall[1]-1])
                        
                        # Right cell
                        if self.randWall[0] != self.width-1:
                            if (self.maze[self.randWall[0]][self.randWall[1]+1] != 'c'):
                                self.maze[self.randWall[0]][self.randWall[1]+1] = 'w'
                            if ([self.randWall[0]+1, self.randWall[1]] not in self.walls): 
                                self.walls.append([self.randWall[0], self.randWall[1]+1])

                    self.deleteWall(self.randWall)
                    continue
                continue

            

            # Bottom walls
            if self.randWall[0] != self.height - 1:
                if self.maze[self.randWall[0]+1][self.randWall[1]] == 'u' and self.maze[self.randWall[0]-1][self.randWall[1]] == 'c':
                    # Find no. surrounding cells.
                    self.s_cells = self.surroundingCells(self.randWall, self.maze)
                    
                    if self.s_cells < 2:
                        # New path
                        self.maze[self.randWall[0]][self.randWall[1]] = 'c'
                        
                        # Upper cells and new walls
                        if self.randWall[0] != self.height-1:
                            if self.maze[self.randWall[0]+1][self.randWall[1]] != 'c':
                               self.maze[self.randWall[0]+1][self.randWall[1]] = 'w'
                            if ([self.randWall[0]+1, self.randWall[1]] not in self.walls): 
                                self.walls.append([self.randWall[0]+1, self.randWall[1]])
                    
                        # Left cell
                        if self.randWall[1] != 0:
                            if (self.maze[self.randWall[0]][self.randWall[1]-1] != 'c'):
                                self.maze[self.randWall[0]][self.randWall[1]-1] = 'w'
                            if ([self.randWall[0], self.randWall[1]-1] not in self.walls): 
                                self.walls.append([self.randWall[0], self.randWall[1]-1])
                        
                        # Right cell
                        if self.randWall[1] != self.width-1:
                            if (self.maze[self.randWall[0]][self.randWall[1]+1] != 'c'):
                                self.maze[self.randWall[0]][self.randWall[1]+1] = 'w'
                            if ([self.randWall[0], self.randWall[1]+1] not in self.walls): 
                                self.walls.append([self.randWall[0], self.randWall[1]+1])

                    self.deleteWall(self.randWall)
                    continue
                continue
            
            if self.randWall[1] != self.width-1:
                if self.maze[self.randWall[0]][self.randWall[1]+1] == 'u' and self.maze[self.randWall[0]][self.randWall[1]-1] == 'c':
                    # Find no. surrounding cells.
                    self.s_cells = self.surroundingCells(self.randWall, self.maze)
                    
                    if self.s_cells < 2:
                        # New path
                        self.maze[self.randWall[0]][self.randWall[1]] = 'c'
                        
                        # Upper cells and new walls
                        if self.randWall[0] != self.width-1:
                            if self.maze[self.randWall[0]][self.randWall[1]+1] != 'c':
                               self.maze[self.randWall[0]][self.randWall[1]+1] = 'w'
                            if ([self.randWall[0], self.randWall[1]+1] not in self.walls): 
                                self.walls.append([self.randWall[0], self.randWall[1]+1])
                    
                        # Left cell
                        if self.randWall[1] != 0:
                            if (self.maze[self.randWall[0]+1][self.randWall[1]] != 'c'):
                                self.maze[self.randWall[0]+1][self.randWall[1]] = 'w'
                            if ([self.randWall[0]+1, self.randWall[1]] not in self.walls): 
                                self.walls.append([self.randWall[0]+1, self.randWall[1]])
                        
                        # Right cell
                        if self.randWall[0] != 0:
                            if (self.maze[self.randWall[0]-1][self.randWall[1]] != 'c'):
                                self.maze[self.randWall[0]-1][self.randWall[1]] = 'w'
                            if ([self.randWall[0-1], self.randWall[1]] not in self.walls): 
                                self.walls.append([self.randWall[0]-1, self.randWall[1]])
                        self.deleteWall(self.randWall)
                    continue
                continue
            

    def deleteWall(self, rand_wall):
        for wall in self.walls:
            if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                self.walls.remove(wall)
    
    def makeWalls(self, width, height):
        for i in range(0, height):
            for j in range(0, width):
                if self.maze[i][j] == 'u':
                    self.maze[i][j] = 'w'
    
    def createEntranceExit(self, width, height):
        for i in range(0, width):
            if self.maze[1][i] == 'c':
                self.maze[0][i] = 'c'
                break
        for i in range(width-1, 0, -1):
            if self.maze[height-2][i] == 'c':
                self.maze[height-1][i] = 'c'
                break

    def surroundingCells(self, rand_wall, maze):
        s_cells = 0
        if (maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
            s_cells += 1
        if (maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
            s_cells += 1
        if (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
            s_cells +=1
        if (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
            s_cells += 1
        return s_cells
    
    # Create a standard maze.
    def initialiseMaze(self):
        self.maze = []
        for i in range(0, self.height):
            line = []
            for j in range(0, self.width):
                line.append('u')
            self.maze.append(line)
        return self.maze

    # Print the maze.
    def printMaze(self):
        for i in range(0, len(self.maze)):
            for j in range(0, len(self.maze[0])):
                if self.maze[i][j] == 'u':
                    print(Fore.WHITE, f'{self.maze[i][j]}', end='')
                elif self.maze[i][j] == 'c':
                    print(Fore.GREEN, f'{self.maze[i][j]}', end='')
                else:
                    print(Fore.RED, f'{self.maze[i][j]}', end='')
            print('\n')
    


newMaze = MazeGen('u','h',10,10)
newMaze.initialiseMaze()
newMaze.generateMaze()