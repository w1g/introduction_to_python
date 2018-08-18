import tempfile
import os

class File():
    def __init__(self, path):
        self.path = path
        if os.path.isfile(self.path):
            with open(self.path, 'r') as f:
                self._inner_state = f.read()
        else:
#           self.write('')
            self._inner_state = ''
            with open(self.path, 'a'):
                os.utime(self.path, None)
    
    def __iter__(self):
        self._iter_state = self._inner_state.split('\n')
        return self
    
    def __next__(self):
        if self._iter_state:
            return self._iter_state.pop(0)
        else:
            raise StopIteration     
    
    def __add__(self, cls):
       _path = tempfile.NamedTemporaryFile().name
       obj = File(_path)
       obj.write(self._inner_state + cls._inner_state)
       return obj
    
    def __str__(self):
        return f'{self.path}'
    
    def write(self, s):
        self._inner_state += s
        with open(self.path, 'a') as f:
            f.write(s)
            
    def read(self):
        return self._inner_state