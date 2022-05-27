import argparse
import os
import yara
pars = argparse.ArgumentParser()
pars.add_argument('rule',help='yara rule here.')
pars.add_argument('path',help='the path you want the rules to match')
arg = pars.parse_args()
path = arg.directory
rl = yara.compile(filepath=args.rule)
for root, dirs, files in os.listdir(path):
    for filename in files:
        x = os.path.join(root, filename)
        if os.path.isfile(x):
                y = open(x,"r").read()
                if rl.match(x):
                     print(x)
                     print("rule matched")
                else:
                     print(x)
                     print("rule not matched")
                	
        	

