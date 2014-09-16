# Jose Guvenilir
# guvenj
# homework 1 part 2


# boring method

# sp1 = 21
# sp2 = 32
# sp3 = 28
# sp4 = 24
# sp5 = 29
# fs1 = 24
# fs2 = 28
# fs3 = 19
# fs4 = 23
# fs5 = 24

# print 'Short program scores', sp1, sp2, sp3, sp4, sp5
# print 'Free skating scores', fs1, fs2, fs3, fs4, fs5
# print 'Spread of the short program is', (max(sp1, sp2, sp3, sp4, sp5) - min(sp1, sp2, sp3, sp4, sp5))/((sp3 + sp4 + sp5)/3.0)
# print 'Spread of the free skating is', (max(fs1, fs2, fs3, fs4, fs5) - min(fs1, fs2, fs3, fs4, fs5))/((fs1 + fs4 + fs5)/3.0)
# print 'Total score for the short program is', sp3 + sp4 + sp5
# print 'Total score for the free skating is', fs1 + fs4 + fs5
# print 'The total score for the competitor is', sp3 + sp4 + sp5 + fs1 + fs4 + fs5

# fun method

# calculates and prints data about the two lists
def calc_scores(list1, list2):
  sumSPScores = (sum(list1) - max(list1) - min(list1))
  sumFSScores = (sum(list2) - max(list2) - min(list2))
  avgSP = sumSPScores/3.0
  avgFS = sumFSScores/3.0
  spreadSP = (max(list1) - min(list1))/avgSP
  spreadFS = (max(list2) - min(list2))/avgFS
  print 'Short program scores', list1[0], list1[1], list1[2], list1[3], list1[4]
  print 'Free skating scores', list2[0], list2[1], list2[2], list2[3], list2[4]
  print 'Spread of the short program is', spreadSP
  print 'Spread of the free skating is', spreadFS
  print 'Total score for the short program is', sumSPScores
  print 'Total score for the free skating is', sumFSScores
  print 'The total score for the competitor is', sumSPScores + sumFSScores

# list of scores
spScores = [21, 32, 28, 24, 29]
fsScores = [24, 28, 19, 23, 24]

calc_scores(spScores, fsScores)