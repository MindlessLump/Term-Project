from __future__ import division  # Enables float division
import math  # Imports trig functions, Pi, and more


def combine_degrees(degrees, minutes, seconds):
    return degrees + (minutes/60) + (seconds/3600)


def split_degrees(full_degrees):
    degrees = int(full_degrees)
    full_degrees = 60 * (full_degrees - degrees)
    minutes = int(full_degrees)
    full_degrees = 60 * (full_degrees - minutes)
    seconds = round(full_degrees, 2)
    return degrees, minutes, seconds


def degrees_minutes_seconds_to_radians(degrees, minutes, seconds):
    radians = combine_degrees(degrees, minutes, seconds) * math.pi / 180
    return radians


def radians_to_degrees_minutes_seconds(radians):
    full_degrees = radians * 180 / math.pi
    return split_degrees(full_degrees)


def position_to_cartesian_t0(data_set, radius):
    arr = data_set.split()
    t = arr[0]
    lat_d = arr[1]
    lat_m = arr[2]
    lat_s = arr[3]
    ns_bit = arr[4]
    lgt_d = arr[5]
    lgt_m = arr[6]
    lgt_s = arr[7]
    ew_bit = arr[8]
    alt = arr[9]

    # Adjust radius used for calculations to accommodate altitude
    radius += alt

    # Combine latitude and longitude into a single angle in radians
    latitude = degrees_minutes_seconds_to_radians(lat_d, lat_m, lat_s)
    longitude = degrees_minutes_seconds_to_radians(lgt_d, lgt_m, lgt_s)
    if ns_bit < 0:
        latitude = (2 * math.pi) - latitude
    if ew_bit < 0:
        longitude = (2 * math.pi) - longitude

    # Z-component
    z = radius * math.sin(latitude)

    # X-component
    x = radius * math.cos(latitude) * math.cos(longitude)

    # Y-component
    y = radius * math.cos(latitude) * math.sin(longitude)

    return x, y, z
