import sys 
from distutils.core import setup 
import py2exe 
from glob import glob 
 
#Make sure setup knows where all of your 
#program modules are, modify dirs below as needed 
sys.path.append ('.\core') 
sys.path.append ('.\ent') 
sys.path.append ('.\gfx') 
sys.path.append ('.\phx') 
sys.path.append ('.\state') 
sys.path.append ('.\ui\gui') 
sys.path.append ('.\ui\haptic') 
 
#Link Microsoft visual C runtimes... 
#again, modify dir as needed 
data_files = [("MicrosoftVisualCRunTimes", glob(r'.\redis\*.*'))] 
 
setup(data_files=data_files,console=['CellDefender.py'])