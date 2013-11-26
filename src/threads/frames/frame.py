from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Frame(object):
  clearColor = (0, 0, 0, 0)
  defaultColor = (1, 1, 1)

  def preGL(self):
    glClearColor(*Frame.clearColor)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(*Frame.defaultColor)
    glLoadIdentity()
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    glMatrixMode(GL_MODELVIEW)

  def draw(self):
    self.preGL()
 
  def keyboard(self, key, x, y): pass

  def specialKeys(self, key, x, y): pass

  def __init__(self, frameSize):
    (self.width, self.height) = self.frameSize = frameSize