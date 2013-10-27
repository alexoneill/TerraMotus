import threading
import Queue
import time

from src.tools import errors, optimize, parser, plane

class Worker(threading.Thread):
  fileName = "data.csv"
  errorVal = 2047.0

  exit = False

  # In degrees
  triangleNormalRadix = 5

  hasData = False
  fileRead = False
  fileExists = False

  queueMax = None
  physicsQueue = Queue.Queue()
  graphicsQueue = Queue.Queue()

  def __init__(self, queueMax = 0):
    self.queueMax = queueMax
    self.physicsQueue = Queue.Queue(queueMax)
    self.graphicsQueue = Queue.Queue(queueMax)

    try:
      open(self.fileName).close()
      self.fileExists = True
    except:
      self.fileExists = False

    threading.Thread.__init__(self)

  def run(self):
    while(not(self.exit)):
      try:
        self.rawData = parser.parse(self.fileName)
        self.fileRead = True
      except:
        self.fileRead = False
        continue

      print "Converting"
      self.dataPlane = plane.PlaneData(self.rawData)
      print "Erroring"
      self.dataPlane = errors.averageErrors(self.dataPlane, self.errorVal)
      #self.dataPlane = optimize.groupTriangles(self.dataPlane)

      print "Storing"
      self.physicsQueue.add(self.dataPlane)
      self.graphicsQueue.add(self.dataPlane)

  def stop(self):
    self.exit = True
