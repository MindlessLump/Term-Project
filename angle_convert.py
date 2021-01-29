from __future__ import division # Enables float division
import math                     # Imports trig functions, Pi, and more


def degrees_minutes_seconds_to_radians(degrees, minutes, seconds):
    full_degrees = degrees + (minutes/60) + (seconds/3600)
    radians = full_degrees * math.pi / 180
    return radians


def radians_to_degrees_minutes_seconds(radians):
    full_degrees = radians * 180 / math.pi
    degrees = int(full_degrees)
    full_degrees = 60 * (full_degrees - degrees)
    minutes = int(full_degrees)
    full_degrees = 60 * (full_degrees - minutes)
    seconds = round(full_degrees, 2)
    return degrees, minutes, seconds
