# Jose Guvenilir
# guvenj
# lab 2 checkpoint 1

## Function returns the length of a line 
## starting at (x1,y1) and ending at (x2,y2)
def line_length(x1,y1,x2,y2):
  length = (x1-x2)**2 + (y1-y2)**2
  length = length**(0.5)
  return length

length = line_length(1,1,4,5)
print length

# lab method of completing lab
# path1_length = 0
# path1_length += line_length(100, 100, 100, 160)
# path1_length += line_length(100, 160, 80, 160)
# path1_length += line_length(80, 160, 90, 120)
# print int(path1_length)

# more entertaining method of completing lab
list_of_points = [100, 100, 100, 160, 80, 160, 90, 120]

def path_length(points):
  path1_length = 0
  for i in range(0, len(list_of_points)-3):
    if i % 2 == 1:
      continue
    path1_length += line_length(list_of_points[i], list_of_points[i+1], list_of_points[i+2], list_of_points[i+3])
  return int(path1_length)

print path_length(list_of_points)