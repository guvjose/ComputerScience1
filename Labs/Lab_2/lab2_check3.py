# Jose Guvenilir
# guvenj
# lab 2 checkpoint 3

def bpop_next(bpop):
  bpop = (10*bpop)/(1 + 0.1*bpop) - 0.05*bpop*fpop
  return max(0, bpop)
def fpop_next(fpop):
  fpop = 0.4*fpop + 0.02*fpop*bpop
  return max(0, fpop)

bpop = 100
fpop = 5

# print bpop, fpop
# bpop = int(bpop_next(bpop))
# fpop = int(fpop_next(fpop))
# print bpop, fpop
# bpop = int(bpop_next(bpop))
# fpop = int(fpop_next(fpop))
# print bpop, fpop
# bpop = int(bpop_next(bpop))
# fpop = int(fpop_next(fpop))
# print bpop, fpop
# bpop = int(bpop_next(bpop))
# fpop = int(fpop_next(fpop))
# print bpop, fpop
# bpop = int(bpop_next(bpop))
# fpop = int(fpop_next(fpop))
# print bpop, fpop
# bpop = int(bpop_next(bpop))
# fpop = int(fpop_next(fpop))
# print bpop, fpop

for i in range(0, 6):
  print bpop, fpop
  bpop = int(bpop_next(bpop))
  fpop = int(fpop_next(fpop))
print bpop, fpop