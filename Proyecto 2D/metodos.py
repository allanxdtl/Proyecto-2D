from OpenGL.GL import *
import math

factor=0.25

def draw_line(color, p1, p2):
    glBegin(GL_LINES)
    glColor(color[0]/255, color[1]/255, color[2]/255)
    glVertex2f(p1[0]*factor, p1[1]*factor)
    glVertex2f(p2[0]*factor, p2[1]*factor)
    glEnd()
    
    
def draw_lines_connected(color, points, argument):
    glBegin(argument)
    glColor(color[0]/255, color[1]/255, color[2]/255)
    for i in points:
        glVertex2f(i[0]*factor, i[1]*factor)
        glColor(color[0]/255, color[1]/255, color[2]/255)
    glEnd()
    
    
def draw_hollow_circle(color, cx, cy, rx, ry):
    num_segments=100
    glEnable(GL_LINE_SMOOTH)
    glBegin(GL_LINE_LOOP)
    glColor(color[0] / 255, color[1] / 255, color[2] / 255)

    for i in range(num_segments):
        angle = 2 * math.pi * i / num_segments
        x = cx + rx * math.cos(angle)
        y = cy + ry * math.sin(angle)
        glVertex2f(x, y)

    glEnd()
    glDisable(GL_LINE_SMOOTH)
    
def DibujarElipse(cx, cy, rx, ry, *color):
    segments=100
    glColor3f(*color)
    glBegin(GL_TRIANGLE_FAN)  
    for i in range(segments):
        angle = 2 * math.pi * i / segments
        x = cx + rx * math.cos(angle)
        y = cy + ry * math.sin(angle)
        glVertex2f(x, y)
    glEnd()
    
def draw_quad(color, points):
    glBegin(GL_QUADS)
    glColor(color[0]/255, color[1]/255, color[2]/255)
    for i in points:
        glVertex(i[0]*factor, i[1]*factor)
    glEnd()
    
    
def draw_triangle(color, points):
    glBegin(GL_TRIANGLES)
    glColor(color[0]/255, color[1]/255, color[2]/255)
    for i in points:
        glVertex2f(i[0]*factor, i[1]*factor)
    glEnd()