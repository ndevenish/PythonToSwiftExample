"""Bridge.py. The main Python-(Swift) plugin bundle entry module"""

import sys
import logging

import objc
from Foundation import NSObject
from Cocoa import NSView
from AppKit import NSGraphicsContext, NSRectToCGRect
import Quartz

# Create the loggers and set them up
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
logger.info("Loaded python bundle")

# Load the protocol from Objective-C
BridgeInterface = objc.protocolNamed("PythonToSwiftExample.BridgeInterface")

class Bridge(NSObject, protocols=[BridgeInterface]):
  """The principal bundle class"""
  @classmethod
  def createInstance(self):
    return Bridge.alloc().init()

  def getPythonInformation(self):
    return sys.version

class ColouredView(NSView):
  """Custom NSView that colours the background"""
  def drawRect_(self, dirtyRect):
    context = NSGraphicsContext.currentContext().CGContext()
    Quartz.CGContextSetRGBFillColor(context, 1.0, 0.0, 0.0, 1.0)
    Quartz.CGContextFillRect(context, dirtyRect)
