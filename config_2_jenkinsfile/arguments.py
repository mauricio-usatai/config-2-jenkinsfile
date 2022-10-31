from config_2_jenkinsfile.commands import dump_2_jenkinsfile

def add_arguments(parser):
  parser.add_argument(
    'config_xml_file',
    type=str,
    action='store',
  )

  parser.set_defaults(func=dump_2_jenkinsfile)