import sys
import multiprocessing as mp

print("python version %s" % str(sys.version))
print("core           %s" % str(mp.cpu_count()))

if True:
  print("tady")
else:
  print("tady ne")
  a = 0
  b = 1
  c = b / a
