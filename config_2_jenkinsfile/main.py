import argparse

from config_2_jenkinsfile import arguments

def main():
  parser = argparse.ArgumentParser(allow_abbrev=False)
  arguments.add_arguments(parser)

  args = parser.parse_args()
  args.func(args)

if __name__ == '__main__':
  main()
