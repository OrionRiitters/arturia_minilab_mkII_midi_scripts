import Live
from .Arturia_MiniLab_mkII import Arturia_MiniLab_mkII

def create_instance(c_instance):
    ' Creates and returns the APC20 script '
    return Arturia_MiniLab_mkII(c_instance)


# local variables:
# tab-width: 4
