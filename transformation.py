#!/usr/bin/env python
"""
Many different matrix transformations used in computer graphics, such as a rotation matrix or a viewport matrix.
"""
__author__ = "Thommy Scheffner"
__copyright__ = "Copyright 2019, Goethe University for DocStrings and for 'do not modify this method' methods"
__credits__ = ["Thommy Scheffner"]

__license__ = "GPL"
__version__ = "3.7.3"
__maintainer__ = "Thommy Scheffner"
__email__ = "itzthommy@gmx.de"
__status__ = "Completed"

import math

class Vec4():
    def __init__(self, x = 0, y = 0, z = 0, w = 0):
        """Constructor for Vec4
        DO NOT MODIFY THIS METHOD"""
        self.values = [x,y,z,w]

    def __str__(self):

        """Returns the vector as a string representation

        DO NOT MODIFY THIS METHOD"""

        toReturn = ''

        if self is None: return '0.00 0.00 0.00 0.00'

        for c in range(0,4):

            if "%.2f" % self.values[c] == "-0.00":

                toReturn += "0.00"

            else:

                toReturn += "%.2f" % self.values[c]

            if c != 3:

                toReturn += ' '

        return toReturn

class Matrix4():
    def __init__(self, row1=None, row2=None, row3=None, row4=None):
        """Constructor for Matrix4
        DO NOT MODIFY THIS METHOD"""
        if row1 is None: row1 = Vec4()
        if row2 is None: row2 = Vec4()
        if row3 is None: row3 = Vec4()
        if row4 is None: row4 = Vec4()
        self.m_values = [row1,row2,row3,row4]

    def __str__(self):

        """Returns a string representation of the matrix

        DO NOT MODIFY THIS METHOD"""

        toReturn = ''

        if self is None: return '0.00 0.00 0.00 0.00\n0.00 0.00 0.00 0.00\n0.00 0.00 0.00 0.00\n0.00 0.00 0.00 0.00'

        for r in range(0,4):

            for c in range(0,4):

                if "%.2f" % self.m_values[r].values[c] == "-0.00":

                    toReturn += "0.00"

                else:

                    toReturn += "%.2f" % self.m_values[r].values[c]

                if c != 3:

                    toReturn += ' '

            toReturn += '\n'

        return toReturn


    def __mul__(self, other):
        """Implement multiplication for Matrix4(and all its subclasses) by both other Matrix4s and Vec4s.
        Make sure to support the multiplication operator. Do not modify the originals
        while multiplying"""
        multiplied_matrix = Matrix4()

        if type(other) == Matrix4 or type(other) == RotationMatrix or type(other) == ScaleMatrix or type(other) == TranslationMatrix or type(other) == OrthogonalMatrix or type(other) == PerspectiveMatrix or type(other) == ViewportMatrix:
    
            for rowx in range(0,4):
                for coly in range(0,4):
                    for rowy in range(0,4):
                        multiplied_matrix.m_values[rowx].values[coly] += self.m_values[rowx].values[rowy] * other.m_values[rowy].values[coly]
        else:
            x = int
            y = int
            z = int
            w = int
        
            multiplied_matrix = Vec4(0,0,0,0)
            x = (self.m_values[0].values[0]*other.values[0]) + (self.m_values[1].values[0]*other.values[1]) + (self.m_values[2].values[0]*other.values[2]) + (self.m_values[3].values[0]*other.values[3])
        
            y = (self.m_values[0].values[1]*other.values[0]) + (self.m_values[1].values[1]*other.values[1]) + (self.m_values[2].values[1]*other.values[2]) + (self.m_values[3].values[1]*other.values[3])
        
            z = (self.m_values[0].values[2]*other.values[0]) + (self.m_values[1].values[2]*other.values[1]) + (self.m_values[2].values[2]*other.values[2]) + (self.m_values[3].values[2]*other.values[3])
        
            w = (self.m_values[0].values[3]*other.values[0]) + (self.m_values[1].values[3]*other.values[1]) + (self.m_values[2].values[3]*other.values[2]) + (self.m_values[3].values[3]*other.values[3])

            multiplied_matrix = Vec4(x,y,z,w)
            
                         
        return multiplied_matrix

class RotationMatrix(Matrix4):
    def __init__(self, m_axis ="x", m_angle = 180, *args, **kwargs):
        """Constructor for RotationMatrix
        DO NOT MODIFY THIS METHOD"""
        super(RotationMatrix, self).__init__(*args, **kwargs)
        self.m_axis = m_axis
        self.m_angle = m_angle
        self.update()

    def setAxis(self, m_axis):
        """Sets the rotation axis
        DO NOT MODIFY THIS METHOD"""
        self.m_axis = m_axis
        self.update()

    def setAngle(self, rot):
        """Sets the rotation angle, in degrees
        DO NOT MODIFY THIS METHOD"""
        self.m_angle = rot
        self.update()

    def update(self):
        """Calculates the rotation matrix.
        After calling this method self is a rotation matrix
        using the given rotational axis and angle."""
        test = math.sin(math.radians(self.m_angle))
        arctest = float
        if test < 0:
            arctest = test-2*test
        elif test == 0:
            arctest = 0
        elif test > 0:
            arctest = test-2*test

        if self.m_axis == 'x' or self.m_axis == 'X':

            self.m_values[0].values[0] = 1
            self.m_values[1].values[0] = 0
            self.m_values[2].values[0] = 0
            self.m_values[3].values[0] = 0

            self.m_values[0].values[1] = 0
            self.m_values[1].values[1] = math.cos(math.radians(self.m_angle))
            self.m_values[2].values[1] = math.sin(math.radians(self.m_angle))
            self.m_values[3].values[1] = 0

            self.m_values[0].values[2] = 0
            self.m_values[1].values[2] = arctest
            self.m_values[2].values[2] = math.cos(math.radians(self.m_angle))
            self.m_values[3].values[2] = 0

            self.m_values[0].values[3] = 0
            self.m_values[1].values[3] = 0
            self.m_values[2].values[3] = 0
            self.m_values[3].values[3] = 1
            
        elif self.m_axis == 'y' or self.m_axis == 'Y':

            self.m_values[0].values[0] = math.cos(math.radians(self.m_angle))
            self.m_values[1].values[0] = 0
            self.m_values[2].values[0] = arctest
            self.m_values[3].values[0] = 0

            self.m_values[0].values[1] = 0
            self.m_values[1].values[1] = 1
            self.m_values[2].values[1] = 0
            self.m_values[3].values[1] = 0

            self.m_values[0].values[2] = math.sin(math.radians(self.m_angle))
            self.m_values[1].values[2] = 0
            self.m_values[2].values[2] = math.cos(math.radians(self.m_angle))
            self.m_values[3].values[2] = 0

            self.m_values[0].values[3] = 0
            self.m_values[1].values[3] = 0
            self.m_values[2].values[3] = 0
            self.m_values[3].values[3] = 1
            
        elif self.m_axis == 'z' or self.m_axis == 'Z':

            self.m_values[0].values[0] = math.cos(math.radians(self.m_angle))
            self.m_values[1].values[0] = math.sin(math.radians(self.m_angle))
            self.m_values[2].values[0] = 0
            self.m_values[3].values[0] = 0

            self.m_values[0].values[1] = arctest
            self.m_values[1].values[1] = math.cos(math.radians(self.m_angle))
            self.m_values[2].values[1] = 0
            self.m_values[3].values[1] = 0

            self.m_values[0].values[2] = 0
            self.m_values[1].values[2] = 0
            self.m_values[2].values[2] = 1
            self.m_values[3].values[2] = 0

            self.m_values[0].values[3] = 0
            self.m_values[1].values[3] = 0
            self.m_values[2].values[3] = 0
            self.m_values[3].values[3] = 1
            
        else:
            pass
        
        return self

class ScaleMatrix(Matrix4):
    def __init__(self, m_scale = Vec4(1,1,1), *args, **kwargs):
        """Constructor for ScaleMatrix
        DO NOT MODIFY THIS METHOD"""
        super(ScaleMatrix, self).__init__(*args, **kwargs)
        self.m_scale = m_scale
        self.update()

    def setScale(self, v):
        """Sets the scale vector, only x, y and z are relevant
        DO NOT MODIFY THIS METHOD"""
        self.m_scale = v
        self.update()

    def update(self):
        """Calculates the scale matrix.
        After calling this method self is a scale matrix
        using the given x, y and z of the m_scale vector."""

        for r in range(0,4):
            for c in range(0,4):
                if r == 0 and c == 0:
                    self.m_values[r].values[c] = self.m_scale.values[0]
                elif r == 1 and c == 1:
                    self.m_values[r].values[c] = self.m_scale.values[1]
                elif r == 2 and c == 2:
                    self.m_values[r].values[c] = self.m_scale.values[2]
                elif r == 3 and c == 3:
                    self.m_values[r].values[c] = 1
                else:
                    self.m_values[r].values[c] = 0
                    
        return self

class TranslationMatrix(Matrix4):
    def __init__(self, m_translation = Vec4(1,1,1), *args, **kwargs):
        super(TranslationMatrix, self).__init__(*args, **kwargs)
        self.m_translation = m_translation
        self.update()

    def setTranslation(self, v):
        """Sets the Translation vector, only x, y and z are relevant
        DO NOT MODIFY THIS METHOD"""
        self.m_translation = v
        self.update()

    def update(self):
        """Calculates the translation matrix.
        After calling this method self is a translation matrix
        using the given x, y and z of the m_translation vector."""

        for r in range(0,4):
            for c in range(0,4):
                if r == 0 and c == 0:
                    self.m_values[r].values[c] = 1
                elif r == 1 and c == 1:
                    self.m_values[r].values[c] = 1
                elif r == 2 and c == 2:
                    self.m_values[r].values[c] = 1
                elif r != 3 and c == 3:
                    
                    self.m_values[r].values[c] = self.m_translation.values[r]
                elif r == 3 and c == 3:
                    self.m_values[r].values[c] = 1
                else:
                    self.m_values[r].values[c] = 0
                    
        return self
    
class ProjectionMatrix(Matrix4):
    def __init__(self, l, r, b, t, n, f, *args, **kwargs):
        """Constructor for ProjectionMatrix
        DO NOT MODIFY THIS METHOD"""
        super(ProjectionMatrix, self).__init__(*args, **kwargs)
        self.m_left = l
        self.m_right = r
        self.m_bottom = b
        self.m_top = t
        self.m_near = n
        self.m_far = f
        self.update()

    def setLeft(self, l):
        """Sets the left plane
        DO NOT MODIFY THIS METHOD"""
        self.m_left = l
        self.update()

    def setRight(self, r):
        """Sets the right plane
        DO NOT MODIFY THIS METHOD"""
        self.m_right = r
        self.update()

    def setTop(self, t):
        """Sets the top plane
        DO NOT MODIFY THIS METHOD"""
        self.m_top = t
        self.update()

    def setBottom(self, b):
        """Sets the bottom plane
        DO NOT MODIFY THIS METHOD"""
        self.m_bottom = b
        self.update()

    def setNear(self, n):
        """Sets the near plane
        DO NOT MODIFY THIS METHOD"""
        self.m_near = n
        self.update()

    def setFar(self, f):
        """Sets the far plane
        DO NOT MODIFY THIS METHOD"""
        self.m_far = f
        self.update()

    def update(self):
        """Calculates the matrix
        DO NOT MODIFY THIS METHOD"""
        #Placeholder, please ignore.
        return self

class OrthogonalMatrix(ProjectionMatrix):
    def update(self):
        """Calculates the orthogonal projection matrix"""
        
        for r in range(0,4):
            for c in range(0,4):
                if r == 0 and c == 0:
                    self.m_values[r].values[c] = 2 / (self.m_right - self.m_left)
                    
                elif r == 1 and c == 1:
                    self.m_values[r].values[c] = 2 / (self.m_top - self.m_bottom)
                    
                elif r == 2 and c == 2:
                    self.m_values[r].values[c] = 2 / (self.m_far - self.m_near)
                    
                elif r != 3 and c == 3:
                    if r == 0:
                        self.m_values[r].values[c] = -(self.m_right + self.m_left) / (self.m_right - self.m_left)
                    elif r == 1:
                        self.m_values[r].values[c] = -(self.m_top + self.m_bottom) / (self.m_top - self.m_bottom)
        
                    elif r == 2:
                        self.m_values[r].values[c] = -(self.m_far + self.m_near) / (self.m_far - self.m_near)
                        
                elif r == 3 and c == 3:
                    self.m_values[r].values[c] = 1
                    
                else:
                    self.m_values[r].values[c] = 0
        return self

class PerspectiveMatrix(ProjectionMatrix):
    def update(self):
        """Calculates the perspective projection matrix"""
        
        for r in range(0,4):
            for c in range(0,4):
                if r == 0 and c == 0:
                    self.m_values[r].values[c] = 2 * self.m_near / (self.m_right - self.m_left)
                    
                elif r == 1 and c == 1:
                    self.m_values[r].values[c] = 2 * self.m_near / (self.m_top - self.m_bottom)
                    
                elif r != 3 and c == 2:
                    if r == 0:
                        self.m_values[r].values[c] = -(self.m_right + self.m_left) / (self.m_right - self.m_left)
                    elif r == 1:
                        self.m_values[r].values[c] = -(self.m_top + self.m_bottom) / (self.m_top - self.m_bottom)
                    elif r == 2:
                        self.m_values[r].values[c] = (self.m_near + self.m_far) / (self.m_far - self.m_near)
                    
                elif r == 2 and c == 3:
                    self.m_values[r].values[c] = -(2*(self.m_far * self.m_near)) / (self.m_far - self.m_near)
                    
                elif r == 3 and c == 2:
                    self.m_values[r].values[c] = 1
                    
                else:
                    self.m_values[r].values[c] = 0
        return self

class ViewportMatrix(Matrix4):
    def __init__(self, x, y, width, height, *args, **kwargs):
        """Constructor for ProjectionMatrix
        DO NOT MODIFY THIS METHOD"""
        super(ViewportMatrix, self).__init__(*args, **kwargs)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.update()

    def setX(self, x):
        """Sets x
        DO NOT MODIFY THIS METHOD"""
        self.x = x
        self.update()
    
    def setY(self, y):
        """Sets y
        DO NOT MODIFY THIS METHOD"""
        self.y = y
        self.update()

    def setHeight(self, height):
        """Sets height
        DO NOT MODIFY THIS METHOD"""
        self.height = height
        self.update()

    def setWidth(self, width):
        """Sets width
        DO NOT MODIFY THIS METHOD"""
        self.width = width
        self.update()

    def update(self):
        """Calculates the viewport matrix"""
        for r in range(0,4):
            for c in range(0,4):
                if r == 0 and c == 0:
                    self.m_values[r].values[c] = self.width / 2
                    
                elif r == 0 and c == 3:
                    self.m_values[r].values[c] = self.width / 2 + self.x
                    
                elif r == 1 and c == 1:
                    self.m_values[r].values[c] = self.height / 2
                    
                elif r == 1 and c == 3:
                    self.m_values[r].values[c] = self.height / 2 + self.y

                elif (r == 2 and c == 2) or (r == 3 and c == 3):
                    self.m_values[r].values[c] = 1
                    
                else:
                    self.m_values[r].values[c] = 0
        return self
