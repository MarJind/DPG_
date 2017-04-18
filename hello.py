import sys
import multiprocessing as mp

print("python version %s" % str(sys.version))
print("core           %s" % str(mp.cpu_count()))

if 1:
  print("tady")
else:
  print("tady ne")
