import sys
import miltiprocessing as mp

print("python version %s" % str(sys.version))
print("core           %s" % str(mp.cpu_count()))
