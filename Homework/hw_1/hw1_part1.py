# Jose Guvenilir
# guvenj
# homework 1 part 1


# boring method

# ibc_10 = 200
# ibc_12 = 500
# ibc_14 = 2000
# ibc_16 = 12000
# ibc_18 = 24000
# ibc_20 = 65000
# ibc_22 = 70000
# alsibc_10 = 100
# alsibc_12 = 300
# alsibc_14 = 1500
# alsibc_16 = 13000
# alsibc_18 = 25000
# alsibc_20 = 105000
# alsibc_22 = 85000

# print '#icebucketchallenge vs #alsicebucketchallenge, percent change'
# print (ibc_12 - ibc_10)*100/ibc_10, 'vs', int((alsibc_12 - alsibc_10)*100.0/alsibc_10)
# print (ibc_14 - ibc_12)*100/ibc_12, 'vs', int((alsibc_14 - alsibc_12)*100.0/alsibc_12)
# print (ibc_16 - ibc_14)*100/ibc_14, 'vs', int((alsibc_16 - alsibc_14)*100.0/alsibc_14)
# print (ibc_18 - ibc_16)*100/ibc_16, 'vs', int((alsibc_18 - alsibc_16)*100.0/alsibc_16)
# print (ibc_20 - ibc_18)*100/ibc_18, 'vs', int((alsibc_20 - alsibc_18)*100.0/alsibc_18)
# print (ibc_22 - ibc_20)*100/ibc_20, 'vs', int((alsibc_22 - alsibc_20)*100.0/alsibc_20)
# print (alsibc_22-alsibc_20)*100
# print alsibc_20

# fun method

ibc = [200, 500, 2000, 12000, 24000, 65000, 70000]
alsibc = [100, 300, 1500, 13000, 25000, 105000, 85000]

print '#icebucketchallenge vs #alsicebucketchallenge, percentage change'

# goes through the ibc and alsibc lists, and calculates the percentages for both
for i in range(0, len(ibc) - 1):
  print int((ibc[i+1] - ibc[i])*100.0/ibc[i]), 'vs', int((alsibc[i+1] - alsibc[i])*100.0/alsibc[i])