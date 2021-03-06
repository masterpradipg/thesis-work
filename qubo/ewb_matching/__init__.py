from __future__ import print_function

# package version
from .common.version import thesis
__version__ = common.version.sqaodpy_version

from .common.envcheck import *
from .common.cuda_probe import is_cuda_available



import sys
this = sys.modules[__name__]
this.ext_loaded = True
    
# imports
from .common.preference import algorithm
from .common.preference import minimize
from .common.preference import maximize
from .common import *
from . import py
try :
    from . import cpu
    if is_cuda_available() :
        from . import cuda    
except Exception as e:
    print(e)
    check_env()
    raise e

