# Building from source (https://mujoco.readthedocs.io/en/latest/programming/#building-from-source)

ERROR: CMake Error at build/_deps/glfw3-src/src/CMakeLists.txt:76 (message):
        Failed to find wayland-scanner

FIX1: sudo apt-get install libwayland-bin


ERROR: CMake Error at /usr/share/cmake-3.28/Modules/FindPkgConfig.cmake:619 (message):
  The following required packages were not found:

   - wayland-client>=0.2.7
   - wayland-cursor>=0.2.7
   - wayland-egl>=0.2.7
   - xkbcommon>=0.5.0

Call Stack (most recent call first):
  /usr/share/cmake-3.28/Modules/FindPkgConfig.cmake:841 (_pkg_check_modules_internal)
  build/_deps/glfw3-src/src/CMakeLists.txt:163 (pkg_check_modules)

FIX1: sudo apt install libwayland-dev libwayland-bin wayland-protocols libxkbcommon-dev

ERROR: CMake Error at /usr/share/cmake-3.28/Modules/FindPackageHandleStandardArgs.cmake:230 (message):
  Could NOT find X11 (missing: X11_X11_INCLUDE_PATH X11_X11_LIB)
Call Stack (most recent call first):
  /usr/share/cmake-3.28/Modules/FindPackageHandleStandardArgs.cmake:600 (_FPHSA_FAILURE_MESSAGE)
  /usr/share/cmake-3.28/Modules/FindX11.cmake:665 (find_package_handle_standard_args)
  build/_deps/glfw3-src/src/CMakeLists.txt:181 (find_package)

FIX: sudo apt-get install libx11-dev


ERROR: CMake Error at build/_deps/glfw3-src/src/CMakeLists.txt:186 (message):
        RandR headers not found; install libxrandr development package

FIX: sudo apt-get install libxrandr-dev

ERROR: CMake Error at build/_deps/glfw3-src/src/CMakeLists.txt:192 (message):
        Xinerama headers not found; install libxinerama development package

FIX: sudo apt-get install libxinerama-dev

ERROR: CMake Error at build/_deps/glfw3-src/src/CMakeLists.txt:204 (message):
          Xcursor headers not found; install libxcursor development package

FIX: sudo apt-get install sudo apt-get install libxcursor-dev

ERROR: CMake Error at build/_deps/glfw3-src/src/CMakeLists.txt:210 (message):
          XInput headers not found; install libxi development package

FIX: sudo apt-get install libxi-dev

Furthermore: sudo apt-get install libglfw3-dev

Now I can build and install from source

# Python bindings from source (https://mujoco.readthedocs.io/en/latest/python.html#building-from-source)

sudo apt-get install python3.12-venv

Worked

Can access virtual environment with source /tmp/mujoco/bin/activate
