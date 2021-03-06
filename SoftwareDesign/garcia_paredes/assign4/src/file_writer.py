from writer import Writer

class FileWriter(Writer):
  def __init__(self, file_name, *operations):
    self.file_name = file_name
    self.target = open(file_name, "w+")
    self.is_closed = False
    super().__init__(*operations)
    
  def write_to_target(self, message):
    if not self.target.closed:
      self.target.write(message)
      self.target.flush()
  
  def close(self):
    self.target.close()
  
  def get_contents(self):
    with open(self.file_name, "r") as target:
      return target.read()
