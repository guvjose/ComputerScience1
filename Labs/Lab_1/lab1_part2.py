def DiffInBytes(bytes):
  manufacturer_bytes = bytes
  actual_bytes = manufacturer_bytes - ((2**10 - 10**3) * bytes / 1000) * 3
  difference = manufacturer_bytes - actual_bytes
  print '%d GB in base 10 is actually %d GB in base 2, %d GB less than advertised' % (manufacturer_bytes, actual_bytes, difference)

DiffInBytes(128)
DiffInBytes(256)
DiffInBytes(512)
DiffInBytes(1024)