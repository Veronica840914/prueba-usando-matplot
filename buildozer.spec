[app]
# Nombre de tu app
title = MyGraphApp
# Paquete, en formato reverso de dominio sin espacios
package.name = mygraphapp
package.domain = org.example

# Script principal
source.include_exts = py,png,jpg,kv,atlas
source.main = main.py

# Versiones mínimas y arquitectura (ajusta según tu necesidad)
android.minapi = 24
android.archs = arm64-v8a,armeabi-v7a

# Requisitos principales
requirements = python3,kivy==2.1.0,matplotlib,numpy,pillow

# Para usar matplotlib de Kivy Garden
garden_requirements = matplotlib

# Rama estable de python-for-android (usar develop para mejor soporte matplotlib)
p4a.branch = develop

# Nivel de logs (2 para mostrar mensajes relevantes)
log_level = 2

# Nombre del archivo apk
android.release_artifact = apk

# Permisos si son necesarios (no estrictamente requerido para tu app, pero para referencia)
# android.permissions = INTERNET

# Ajustes opcionales para acelerar compilación (puedes quitar el .buildozer para rebuild limpio)
# clean_build = True

