import argparse
import yara

parse=argparse.ArgumentParser()
parse.add_argument('f')
parse.add_argument('r')
arg=parse.parse_args()
folder = args.f
x = open(arg.r, 'r').read()
rl = yara.compile(x)
print(rl.match(arg.folder))
