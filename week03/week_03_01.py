class FileReader:
    
    def __init__(self, full_file_name):
        self.path = full_file_name
    
    def read(self):
        try:
            with open(self.path, 'r') as f:
                content = f.read()
            return content
        except IOError:
            return ""