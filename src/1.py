from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# 初始化全局变量
zoom_factor = 1.0

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, 1, 500)
    glMatrixMode(GL_MODELVIEW)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -5.0)
    glScalef(zoom_factor, zoom_factor, zoom_factor)
    
    # 画一个立方体
    glutWireCube(1.0)
    
    glFlush()
    glutSwapBuffers()

def mouseWheel(button, dir, x, y):
    global zoom_factor
    if dir > 0:
        zoom_factor *= 0.9  # 缩小
    else:
        zoom_factor *= 1.1  # 放大
    glutPostRedisplay()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w / h, 1, 500)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Zoom with Mouse Wheel")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMouseWheelFunc(mouseWheel)
    glutMainLoop()

main()
