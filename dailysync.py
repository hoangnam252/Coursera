#!/usr/bin/env python
import subprocess
from multiprocessing import Pool
import multiprocessing

src = "/home/student-00-ff71933b211f/data/prod/"
dest = "/home/student-00-ff71933b211f/data/prod_backup/"

if __name__ == "__main__":
        p = Pool(multiprocessing.cpu_count())
        p.apply(subprocess.call, args=(["rsync", "-arq", src, dest],))