import os
import argparse
import re
pars = argparse.ArgumentParser()
pars.add_argument('rl',help='path of rule file')
pars.add_argument('directory',help='path of directory')
arg = pars.parse_args()
v = open(arg.rule,'r').read()
Directoy = args.directory
rl = re.compile(v)
for root, dirs, files in os.listdir(directory):
    for filename in files:
        x = os.path.join(root, filename)
        if os.path.isfile(x):
                y = open(x,'r').read()
                rl.search(y)
                if rl.search(a):
                    print(x, "1")
                else:
                     print(x, "0")

