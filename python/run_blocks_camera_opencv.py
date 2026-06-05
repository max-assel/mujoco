import mujoco as mj

import os

# Load in XML file
xml = "block_with_camera.xml"

#get the full path
dirname = os.path.dirname(__file__)
abspath = os.path.join(dirname + "/" + xml)
xml_path = abspath


# MuJoCo data structures
model = mj.MjModel.from_xml_path(xml_path)  # MuJoCo model
data = mj.MjData(model)                # MuJoCo data
cam = mj.MjvCamera()                        # Abstract camera
opt = mj.MjvOption()                        # visualization options