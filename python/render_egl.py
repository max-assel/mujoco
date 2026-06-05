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
      <camera name="ball_camera" output="depth" pos="1.0 0 0" euler="0 90 -90"/>
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

#4.5 Set up the camera view (optional, otherwise defaults will be used)
camera_name = 'ball_camera'
camera_id = model.camera(camera_name).id
attached_cam = mujoco.MjvCamera()
attached_cam.type = mujoco.mjtCamera.mjCAMERA_FIXED
attached_cam.fixedcamid = camera_id

renderer.enable_depth_rendering()

# 5. Sync the visual scene configurations with the physical states
renderer.update_scene(data, attached_cam)

# 6. Grab the RGB pixel matrix array from the GPU buffer
# rgb_array = renderer.render()

# 6.5 Grab the depth buffer as well (optional)
depth_array = renderer.render()

# Scale depth values to [0, 1]
depth_scaled = (depth_array - np.min(depth_array)) / (np.max(depth_array) - np.min(depth_array))
# Convert to 8-bit grayscale
depth_pixels = (depth_scaled * 255).astype(np.uint8)

# 7. Convert and save RGBimage
img = Image.fromarray(depth_pixels)
img.save("headless_render_depth.png")

# 8. Convert and save depth image (optional)
# Normalize depth values to the range [0, 255] for visualization
# depth_normalized = (depth_array - np.min(depth_array)) / (np.max(depth_array) - np.min(depth_array)) * 255
# depth_image = Image.fromarray(depth_normalized.astype(np.uint8))
# depth_image.save("headless_render_depth.png")

print("Render completed and saved successfully!")
