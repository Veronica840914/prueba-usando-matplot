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

# Versiones Android compatibles y recomendadas
android.api = 33                   # API target
android.minapi = 24                # Android min version
android.ndk = 25b                 

# Arquitecturas a compilar
android.archs = armeabi-v7a,arm64-v8a

# Usa branch develop de python-for-android para mejor soporte
p4a.branch = develop

log_level = 2

