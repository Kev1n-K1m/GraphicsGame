from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math, time
import ImportObject


class girl1:
    def __init__(self, x, y, z):
        self.posX = x
        self.posY = y
        self.posZ = z
        self.sizeX = 0.4
        self.sizeY = 0.4
        self.sizeZ = 0.4
        self.rotation = 180.0
        self.speed = 0

        self.obj = ImportObject.ImportedObject("./objects/girl1")

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
        glRotatef(self.rotation, 0.0, 5.0, 0.0)
        glScalef(self.sizeX, self.sizeY, self.sizeZ)
        glCallList(self.displayList)
        glPopMatrix()

    def update(self, delta_time):
        # Update position
        # self.posX += self.speed * delta_time
        self.posZ += self.speed * delta_time

        # Update rotation
        self.rotation += 0.0 * delta_time
        self.rotation %= 360  # Keep rotation in bounds

        # React to environment (e.g., light)
        self.react_to_light()

    def react_to_light(self):
        # Example reaction to light: change color based on light intensity
        light_pos = glGetLightfv(GL_LIGHT0, GL_POSITION)
        light_intensity = glGetLightfv(GL_LIGHT0, GL_DIFFUSE)
        distance_to_light = math.sqrt((self.posX - light_pos[0])**2 + (self.posY - light_pos[1])**2 + (self.posZ - light_pos[2])**2)
        intensity_factor = max(0.0, min(1.0, 1.0 / distance_to_light))

        # Adjust the object's color based on light intensity
        glColor3f(intensity_factor, intensity_factor, intensity_factor)


    def update_rotation(self, angle_increment):
        self.rotation += angle_increment
        self.rotation %= 360  # Keep rotation in bounds

    def __del__(self):
        if self.displayList:
            glDeleteLists(self.displayList, 1)
