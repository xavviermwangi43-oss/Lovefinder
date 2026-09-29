[app]
# (str) Title of your application
title = Love Finder

# (str) Package name
package.name = lovefinder

# (str) Package domain
package.domain = org.lovefinder

# (str) Source code where main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas,json

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 0

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Warn if build directory is not empty (1 = yes, 0 = no)
warn_on_root = 1

# (str) Path to build artifacts
build_dir = .buildozer

# (str) Path to generated packages
bin_dir = bin
