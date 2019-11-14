import os
import re

if __name__ == "__main__":
    pyFileRegEx = re.compile(r'.+\.py$')
    pyFiles = [f for f in os.listdir() if os.path.isfile(f)
               and re.match(pyFileRegEx, f)]
    print(pyFiles)
