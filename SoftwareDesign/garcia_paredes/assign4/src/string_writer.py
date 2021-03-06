from writer import Writer

class StringWriter(Writer):
  def __init__(self, *operations):
    self.target = ""
    self.is_closed = False
    super().__init__(*operations)
  
  def write_to_target(self, message):
    if not self.is_closed:
      self.target += message
  
  def close(self):
    self.is_closed = True
  
  def get_contents(self):
    return self.target
