#!/usr/bin/python
# for bash we need to add the following to our .bashrc
# export PYTHONPATH=$PYTHONPATH:$RMANTREE/bin
import getpass
import time
# import the python renderman library
import prman
import math

def Cube(width,height,depth) :
  w=width/2.0
  h=height/2.0
  d=depth/2.0
  ri.ArchiveRecord(ri.COMMENT, 'Cube Generated by Cube Function')
  #rear
  face=[-w, -h, d, -w, h, d, w, -h, d, w, h, d]
  ri.Patch("bilinear",{'P':face})
  #front
  face=[-w, -h, -d, -w, h, -d, w, -h, -d, w, h, -d]
  ri.Patch("bilinear",{'P':face})
  #left
  face=[-w, -h, -d, -w, h, -d, -w, -h, d, -w, h, d]
  ri.Patch("bilinear",{'P':face})
  #right
  face=[w, -h, -d, w, h, -d, w, -h, d, w, h, d]
  ri.Patch("bilinear",{'P':face})
  #bottom
  face=[w, -h, d, w, -h, -d, -w, -h, d, -w, -h, -d]
  ri.Patch("bilinear",{'P':face})
  #top
  face=[w, h, d, w, h, -d, -w, h, d, -w, h, -d]
  ri.Patch("bilinear",{'P':face})
  ri.ArchiveRecord(ri.COMMENT, '--End of Cube Function--')

def Molecula() :

  ri.ArchiveRecord(ri.COMMENT, 'draw a sphere primitive')
  
  ri.TransformBegin()
  ri.Rotate(45, 0, 1, 0) #y axis
  ri.Rotate(45, 1, 0, 0) #x axis
  ri.Translate(0, 0, 0) #move the whole object


  ri.TransformBegin()
  radius = 0.5
  ri.Rotate(0, 1, 0, 0) #x axis
  #ri.Rotate(45, 0, 1, 0) #y axis
  ri.Rotate(-45, 0, 0, 1) #z axis
  #ri.Translate(1, groud_position + radius, 0)
  ri.Scale(0.1, 1, 0.1)
  ri.AttributeBegin()
  ri.Color([1, 1, 1])
  ri.Sphere (radius, -radius, radius, 360)
  ri.AttributeEnd()
  ri.TransformEnd()

  #bottom small ball
  ri.TransformBegin()
  rad = 0.05
  sqrt = math.sqrt(2)
  ri.Translate(- 0.5*radius*sqrt, - 0.5*radius*sqrt, 0.5*radius*sqrt)
  ri.AttributeBegin()
  ri.Color([1, 1, 1])
  ri.Sphere (rad, -rad, rad, 360)
  ri.AttributeEnd()
  ri.TransformEnd()

  #top small ball

  # ri.TransformBegin()
  # radius = 0.5
  # ri.Rotate(0, 1, 0, 0) #x axis
  # #ri.Rotate(45, 0, 1, 0) #y axis
  # ri.Rotate(45, 0, 0, 1) #z axis
  # #ri.Translate(1, groud_position + radius, 0)
  # ri.Scale(0.1, 1, 0.1)
  # ri.AttributeBegin()
  # ri.Color([1, 1, 1])
  # ri.Sphere (radius, -radius, radius, 360)
  # ri.AttributeEnd()
  # ri.TransformEnd()



  # ri.TransformBegin()
  # radius = 0.5
  # #ri.Rotate(45, 0, 1, 0) #y axis
  # ri.Rotate(90, 1, 0, 0) #x axis  
  # ri.Rotate(0, 0, 0, 1) #z axis
  # #ri.Translate(1, groud_position + radius, 0)
  # ri.Scale(0.1, 1, 0.1)
  # ri.AttributeBegin()
  # ri.Color([1, 1, 1])
  # ri.Sphere (radius, -radius, radius, 360)
  # ri.AttributeEnd()
  # ri.TransformEnd()

  ri.TransformEnd()

ri = prman.Ri() # create an instance of the RenderMan interface

filename = "__render" #"HelloWorld.rib"
# this is the begining of the rib archive generation we can only
# make RI calls after this function else we get a core dump
ri.Begin('simplescene.rib')
# ArchiveRecord is used to add elements to the rib stream in this case comments
# note the function is overloaded so we can concatinate output
ri.ArchiveRecord(ri.COMMENT, 'Comments start with a #')
ri.ArchiveRecord(ri.COMMENT, 'File simplescene.rib #')
ri.ArchiveRecord(ri.COMMENT, "Created by " + getpass.getuser())
ri.ArchiveRecord(ri.COMMENT, "Creation Date: " +time.ctime(time.time()))

# now we add the display element using the usual elements
# FILENAME DISPLAY Type Output format
ri.Display("Simplescene.exr", "file", "rgba")
# Specify PAL resolution 1:1 pixel Aspect ratio
ri.Format(720,576,1)
# now set the projection to perspective
ri.Projection(ri.PERSPECTIVE)

# now we start our world
ri.WorldBegin()
groud_position = -1
# move back 2 in the z so we can see what we are rendering
ri.ArchiveRecord(ri.COMMENT, 'move our world back 2 in the z so we can see it')
ri.Translate(0, 0, 2)

ri.ArchiveRecord(ri.COMMENT, 'draw ground with bilinear patch')
ri.TransformBegin()
height = 0.1
ri.Translate(0, groud_position - height/2, 0)
ri.AttributeBegin()
ri.Color([0.11, 0.49, 0.89])
Cube(7, height, 4)
ri.AttributeEnd()
ri.TransformEnd()

# ri.ArchiveRecord(ri.COMMENT, 'draw a sphere primitive')
# ri.TransformBegin()
# radius = 0.5
# ri.Translate(1, groud_position + radius, 0)
# ri.AttributeBegin()
# ri.Color([1, 0, 0])
# ri.Sphere (radius, -radius, radius, 360)
# ri.AttributeEnd()
# ri.TransformEnd()

# ri.ArchiveRecord(ri.COMMENT, 'draw a teapot')
# ri.TransformBegin()
# scale = 0.4
# ri.Scale(scale, scale, scale)
# ri.Translate(-2.5, groud_position + groud_position*(1 - scale), 1)
# ri.Rotate(-90, 1, 0, 0) #x axis
# ri.Rotate(0, 0, 1, 0) #y axis
# ri.Rotate(60, 0, 0, 1) #z axis
# ri.AttributeBegin()
# ri.Color([0, 1, 0])
# ri.Geometry("teapot")
# ri.AttributeEnd()
# ri.TransformEnd()

# ri.ArchiveRecord(ri.COMMENT, 'draw cube')
# ri.TransformBegin()
# dimension = 0.5
# ri.Translate(0, groud_position + dimension/2, 0)
# ri.Rotate(60, 0, 1, 0) #y axis
# ri.AttributeBegin()
# ri.Color([0, 0, 1])
# Cube(dimension, dimension, dimension)
# ri.AttributeEnd()
# ri.TransformEnd()

Molecula()

# end our world
ri.ArchiveRecord(ri.COMMENT, 'end our world')
ri.WorldEnd()
# and finally end the rib file
ri.End()
