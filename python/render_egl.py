import os
os.environ["MUJOCO_GL"] = "egl"

import mujoco
import numpy as np
from PIL import Image

# 1. Define a basic XML model (a single sphere falling onto a floor)
xml_string = """
<mujoco>
  <worldbody>
    <light diffuse=".5 .5 .5" pos="0 0 3" dir="0 0 -1"/>
    <geom type="plane" size="10 10 0.1" rgba=".9 0.9 0.9 1"/>
    <body pos="0 0 1">
      <joint type="free"/>
      <geom type="sphere" size="0.1" rgba="1 0 0 1"/>
    </body>
  </worldbody>
</mujoco>
"""

# 2. Load the model and structural simulation placeholders
model = mujoco.MjModel.from_xml_string(xml_string)
data = mujoco.MjData(model)

# 3. Step physics forward slightly 
mujoco.mj_step(model, data)

# 4. Instantiate the Renderer object (automatically initializes EGL backend)
renderer = mujoco.Renderer(model, height=480, width=640)

# 5. Sync the visual scene configurations with the physical states
renderer.update_scene(data)

# 6. Grab the RGB pixel matrix array from the GPU buffer
rgb_array = renderer.render()

# 7. Convert and save image
img = Image.fromarray(rgb_array)
img.save("headless_render.png")
print("Render completed and saved successfully!")
