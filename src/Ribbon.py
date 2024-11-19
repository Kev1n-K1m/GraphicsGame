from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Ribbon:
    def __init__(self, x, y, z, width, length,thickness):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.length = length
        self.thickness = thickness

    # def draw(self):
    #     glPushMatrix()
    #     glTranslatef(self.x, self.y, self.z)
    #     glColor3f(0.0, 0.0, 1.0) 
    #     glBegin(GL_QUADS)
    #     glVertex3f(-self.width / 2, 0, -self.length / 2)
    #     glVertex3f(self.width / 2, 0, -self.length / 2)
    #     glVertex3f(self.width / 2, 0, self.length / 2)
    #     glVertex3f(-self.width / 2, 0, self.length / 2)
    #     glEnd()
    #     glPopMatrix()
    def draw(self):
        # Push the current matrix stack
        glPushMatrix()
        
        # Translate to the position of the ribbon
        glTranslatef(self.x, self.y, self.z)
        
        # Set the color of the ribbon
        glColor3f(1.0, 0.0, 0.0)
        
        # Define the half dimensions for easier calculations
        half_width = self.width / 2
        half_length = self.length / 2
        half_thickness = self.thickness / 2  # Define the thickness of the ribbon
        
        # Draw the top face
        glBegin(GL_QUADS)
        glVertex3f(-half_width, half_thickness, -half_length)
        glVertex3f(half_width, half_thickness, -half_length)
        glVertex3f(half_width, half_thickness, half_length)
        glVertex3f(-half_width, half_thickness, half_length)
        glEnd()
        
        # Draw the bottom face
        glBegin(GL_QUADS)
        glVertex3f(-half_width, -half_thickness, -half_length)
        glVertex3f(half_width, -half_thickness, -half_length)
        glVertex3f(half_width, -half_thickness, half_length)
        glVertex3f(-half_width, -half_thickness, half_length)
        glEnd()
        
        # Draw the front face
        glBegin(GL_QUADS)
        glVertex3f(-half_width, -half_thickness, half_length)
        glVertex3f(half_width, -half_thickness, half_length)
        glVertex3f(half_width, half_thickness, half_length)
        glVertex3f(-half_width, half_thickness, half_length)
        glEnd()
        
        # Draw the back face
        glBegin(GL_QUADS)
        glVertex3f(-half_width, -half_thickness, -half_length)
        glVertex3f(half_width, -half_thickness, -half_length)
        glVertex3f(half_width, half_thickness, -half_length)
        glVertex3f(-half_width, half_thickness, -half_length)
        glEnd()
        
        # Draw the left face
        glBegin(GL_QUADS)
        glVertex3f(-half_width, -half_thickness, -half_length)
        glVertex3f(-half_width, -half_thickness, half_length)
        glVertex3f(-half_width, half_thickness, half_length)
        glVertex3f(-half_width, half_thickness, -half_length)
        glEnd()
        
        # Draw the right face
        glBegin(GL_QUADS)
        glVertex3f(half_width, -half_thickness, -half_length)
        glVertex3f(half_width, -half_thickness, half_length)
        glVertex3f(half_width, half_thickness, half_length)
        glVertex3f(half_width, half_thickness, -half_length)
        glEnd()
        
        # Pop the current matrix stack
        glPopMatrix()
