import argparse
import re
from logzero import logger

__version__ = '0.0.1'


def main(args):
  file_path = args.arg

  file = open(file_path)
  lines = file.readlines()

  hotkey_number = 0

  for line in lines:
    if (line.startswith('bindsym')):
      hotkey_number += 1
      split = re.compile('([^\s]{1,}) ([^\s]{1,}) (.*)').split(line)
      split.remove('')
      split.remove('\n')
      split.remove('bindsym')
      print('Bind: {}'.format(split[0]))
      print('Command: {}\n'.format(split[1]))

if __name__ == '__main__':
  parser = argparse.ArgumentParser()

  parser.add_argument('arg', help='Config file path')

#   parser.add_argument(
#     '-v',
#     '--verbose',
#     action='count',
#     default=0,
#     help='Verbosity (-v, -vv, etc)')

  parser.add_argument(
    '--version',
    action='version',
    version='%(prog)s (version {version})'.format(version=__version__))

  args = parser.parse_args()
  main(args)
