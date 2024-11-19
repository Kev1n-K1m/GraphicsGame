from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math, time
import ImportObject


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import ImportObject

class star:
    def __init__(self, x, y, z, R):
        self.posX = x
        self.posY = y
        self.posZ = z
        self.sizeX = 1.0
        self.sizeY = 1.0
        self.sizeZ = 1.0
        self.rotation = 0.0

        if R == 0:
            self.obj = ImportObject.ImportedObject("./objects/star")
        elif R == 1:
            self.obj = ImportObject.ImportedObject("./objects/starR")
        else:
            raise ValueError("Invalid value for R. Must be 0 or 1.")

        self.displayList = None
        self.makeDisplayLists()

    def makeDisplayLists(self):
        self.obj.loadOBJ()
        self.displayList = glGenLists(1)
        glNewList(self.displayList, GL_COMPILE)
        self.obj.drawObject()
        glEndList()

    def draw(self):
        glPushMatrix()
        glTranslatef(self.posX, self.posY, self.posZ)
        glRotatef(self.rotation, 0.0, 1.0, 0.0)
        glScalef(self.sizeX, self.sizeY, self.sizeZ)
        glCallList(self.displayList)
        glPopMatrix()

    def update_rotation(self, angle_increment):
        self.rotation += angle_increment
        self.rotation %= 360  # Keep rotation in bounds

    def __del__(self):
        if self.displayList:
            glDeleteLists(self.displayList, 1)

# Example usage:
# star_instance = Star(0.0, 0.0, 0.0, 0)
# star_instance.draw()
