from sysconfig import get_paths
from pprint import pprint

info = get_paths()  # a dictionary of key-paths

# pretty print it for now
pprint(info)
{'data': '/usr/local',
 'include': '/usr/local/include/python3.9',
 'platinclude': '/usr/local/include/python3.9',
 'platlib': '/usr/local/lib/python3.9/dist-packages',
 'platstdlib': '/usr/lib/python3.9',
 'purelib': '/usr/local/lib/python3.9/dist-packages',
 'scripts': '/usr/local/bin',
 'stdlib': '/usr/lib/python3.9'}