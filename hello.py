import sys
import multiprocessing as mp

print("python version %s" % str(sys.version))
print("core           %s" % str(mp.cpu_count()))
