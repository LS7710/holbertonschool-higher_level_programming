#!/usr/bin/python3
'''BaseGeometry class.'''


class BaseGeometry:
    '''A BaseGeometry class.'''
    def area(self):
        '''computing the area.'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''validating the value.'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
