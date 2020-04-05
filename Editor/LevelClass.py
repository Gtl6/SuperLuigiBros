import os.path


# Set up a level object
class Level:
    width = 25
    height = 15
    filename = 'DEFAULT'
    level = []

    # Initialize
    def __init__(self, filename, screenInfo):
        self.filename = filename
        self.width = screenInfo[1]
        self.height = screenInfo[2]
        if(os.path.exists(os.path.join('..\\Levels', filename))):
            self.loadLevel()
        else:
            self.zeroLevel()

    # Just fill our level with lots of zeroes
    def zeroLevel(self):
        for i in range(0, self.height):
            self.level.append([])
            for j in range(0, self.width):
                # Fill up the level with a whole lotta nothin
                self.level[i].append(0)

    # Returns a 2D array of values
    def getSlice(self, camera_x, camera_y, screenInfo):
        returner = []
        # For each vertical slice
        for h in range(0, screenInfo[2]):
            returner.append([])
            for w in range(0, screenInfo[1]):
                returner[h].append(self.level[h + camera_y][w + camera_x])

        return returner

    # Puts the selected block on the screen at the selected position
    def stamp(self, selected, x, y, cx, cy):
        self.level[y + cy][x + cx] = selected

    # Check to make sure I can move the camera to the right
    def validateRight(self, camera_x, screenInfo):
        if self.width < camera_x + screenInfo[1]:
            for row in range(0, self.height):
                self.level[row].append(0)

    def convert_strints(self, theline):
        returner = []
        for strnum in theline:
            if strnum != '\n':
                returner.append(int(strnum))
        return returner

    def loadLevel(self):
        f = open(os.path.join('..\\Levels', self.filename), 'r')
        firstLine = f.readline().split(" ")
        self.level = []
        self.width = int(firstLine[0])
        self.height = int(firstLine[1])
        for line in range(0, self.height):
            myLine = f.readline().split(" ")
            myLine = self.convert_strints(myLine)
            self.level.append(myLine)

    def save(self):
        levelPath = os.path.join('..\\Levels', self.filename)
        # If the path already exists, erase it
        if os.path.exists(levelPath):
            open(levelPath, 'w').close()
        # Write your level out to it
        f = open(levelPath, 'w')
        f.write(str(self.width) + ' ')
        f.write(str(self.height) + '\n')
        for line in self.level:
            for val in line:
                f.write(str(val) + ' ')
            f.write('\n')
        f.close()