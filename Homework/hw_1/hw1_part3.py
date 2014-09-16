# Jose Guvenilir
# guvenj
# homework 1 part 3


# returns volume of water needed to fill lock
def volume_solid(width, length, depth):
  return width*length*depth

# returns amount of water needed for each lock in a year
def water_needed_perlock(volume):
  ships_per_day = 35
  return volume*365*35

width = 32
length = 320
depth = 10

vol_water_needed = 2*water_needed_perlock(volume_solid(width, length, depth))
daily_rain = vol_water_needed/270
mms_rain_perday = vol_water_needed/270.0/600000.0

print 'Panama canal statistics:'
print 'The total volume of water needed in Gatun lake:', vol_water_needed, 'm^3'
print 'In rainy season, daily rain should be at least:', daily_rain, 'm^3'
print 'This means, it rains about', mms_rain_perday, 'millimeters every day during the rainy season'