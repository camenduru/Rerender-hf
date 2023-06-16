import os
import sys

cur_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
gmflow_dir = os.path.join(cur_dir, 'gmflow_module')
controlnet_dir = os.path.join(cur_dir, 'ControlNet')
sys.path.insert(0, gmflow_dir)
sys.path.insert(0, controlnet_dir)

import ControlNet.share  # noqa: F401 E402
