from xml.dom import minidom

from config_2_jenkinsfile import utils

def dump_2_jenkinsfile(args):
  xml_config_file = args.config_xml_file
  if utils.check_if_xml_file(xml_config_file):
    dom = minidom.parse(xml_config_file)
    script_element = dom.getElementsByTagName('script')
    print(script_element[0].firstChild.nodeValue)
  else:
    print('Please provide a file with .xml extension')
