[app]
# Nombre y metadata de tu app
title = MyGraphApp
package.name = mygraphapp
package.domain = org.example
# Versión debe estar obligatoriamente
version = 0.1

# Carpeta con tu código
source.dir = .

# Entrada principal (archivo Python)
source.main = main.py

# Extensiones a incluir
source.include_exts = py,png,jpg,kv,atlas

# Requisitos de Python y librerías
requirements = python3,kivy==2.1.0,matplotlib,numpy,pillow

# Dependencias Kivy Garden
garden_requirements = matplotlib

# Config Android (básico y moderno)
android.minapi = 24
android.sdk = 33
android.ndk = 25b
android.archs = armeabi-v7a,arm64-v8a

# Usa rama develop para mejores builds de matplotlib
p4a.branch = develop

# Mostrar logs mínimos (opcional, para debugging)
log_level = 2

[buildozer]
# Opcional: limpia antes de compilar para evitar problemas de caché
clean_build = True

