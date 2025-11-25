#!/usr/bin/env python3
"""
Script de configuración rápida para el proyecto
===============================================

Este script automatiza la instalación inicial del proyecto.
Uso: python setup.py
"""

import os
import sys
import subprocess
import platform


def ejecutar_comando(comando, descripcion):
    """Ejecutar comando y mostrar resultado"""
    print(f"\n📌 {descripcion}...")
    try:
        resultado = subprocess.run(
            comando, shell=True, capture_output=True, text=True
        )
        if resultado.returncode == 0:
            print(f"✅ {descripcion} - Exitoso")
            return True
        else:
            print(f"❌ {descripcion} - Error")
            print(f"   {resultado.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error al ejecutar: {e}")
        return False


def main():
    print("\n" + "=" * 70)
    print("🚀 CONFIGURACIÓN RÁPIDA - Gestión de Contactos")
    print("=" * 70)

    sistema = platform.system()
    print(f"\n🖥️  Sistema operativo detectado: {sistema}")

    # 1. Verificar Python
    print("\n📋 Paso 1/6: Verificando Python...")
    try:
        resultado = subprocess.run(
            "python --version", shell=True, capture_output=True, text=True
        )
        if resultado.returncode != 0:
            resultado = subprocess.run(
                "python3 --version", shell=True, capture_output=True, text=True
            )
            python_cmd = "python3"
        else:
            python_cmd = "python"
        print(f"✅ Python encontrado: {resultado.stdout.strip()}")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("   Instala Python desde https://www.python.org/downloads/")
        return

    # 2. Crear entorno virtual
    print("\n📋 Paso 2/6: Creando entorno virtual...")
    if sistema == "Windows":
        crear_venv = f"{python_cmd} -m venv venv"
        activar_venv = "venv\\Scripts\\activate"
    else:
        crear_venv = f"{python_cmd} -m venv venv"
        activar_venv = "source venv/bin/activate"

    if ejecutar_comando(crear_venv, "Crear entorno virtual"):
        print(f"   Comando de activación: {activar_venv}")
    else:
        return

    # 3. Instalar dependencias
    print("\n📋 Paso 3/6: Instalando dependencias...")
    if sistema == "Windows":
        pip_install = "venv\\Scripts\\pip install -r requirements.txt"
    else:
        pip_install = "venv/bin/pip install -r requirements.txt"

    if not ejecutar_comando(pip_install, "Instalar requisitos"):
        return

    # 4. Aplicar migraciones
    print("\n📋 Paso 4/6: Aplicando migraciones...")
    if sistema == "Windows":
        migraciones = "cd crud && ..\\venv\\Scripts\\python manage.py migrate"
    else:
        migraciones = "cd crud && ../venv/bin/python manage.py migrate"

    if not ejecutar_comando(migraciones, "Migraciones de base de datos"):
        return

    # 5. Crear superusuario
    print("\n📋 Paso 5/6: Crear superusuario")
    print("\nResponde las siguientes preguntas:")
    if sistema == "Windows":
        createsuperuser = (
            "cd crud && ..\\venv\\Scripts\\python manage.py createsuperuser"
        )
    else:
        createsuperuser = "cd crud && ../venv/bin/python manage.py createsuperuser"

    try:
        subprocess.run(createsuperuser, shell=True)
        print("✅ Superusuario creado")
    except Exception as e:
        print(f"❌ Error: {e}")
        return

    # 6. Instrucciones finales
    print("\n" + "=" * 70)
    print("✅ CONFIGURACIÓN COMPLETADA")
    print("=" * 70)

    print("\n🎯 Próximos pasos:")
    print("\n1. Activar entorno virtual:")
    if sistema == "Windows":
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")

    print("\n2. Navegar a la carpeta del proyecto:")
    print("   cd crud")

    print("\n3. Iniciar servidor de desarrollo:")
    print("   python manage.py runserver")

    print("\n4. Acceder a la aplicación en tu navegador:")
    print("   🏠 Interfaz Web: http://127.0.0.1:8000/")
    print("   🔧 Panel Admin: http://127.0.0.1:8000/admin/")
    print("   📡 API REST: http://127.0.0.1:8000/api/")

    print("\n📚 Para más información:")
    print("   - Documentación completa: README.md")
    print("   - Instrucciones de instalación: INSTALACION.md")
    print("   - Cliente Python: cliente_python.py")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Configuración cancelada por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        sys.exit(1)
