def check_if_xml_file(file_name):
  if len(file_name) < 4: return False # filename too short to be an xml
  return file_name[-4:] == '.xml'
