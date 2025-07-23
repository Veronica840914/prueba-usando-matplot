[app]
title = MyGraphApp
package.name = mygraphapp
package.domain = org.example
version = 0.1
source.dir = .
source.main = main.py
source.include_exts = py,png,jpg,kv,atlas

requirements = python3,kivy==2.1.0,matplotlib,numpy,pillow
garden_requirements = matplotlib

android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = armeabi-v7a,arm64-v8a

p4a.branch = develop

log_level = 2

[buildozer]
clean_build = True
