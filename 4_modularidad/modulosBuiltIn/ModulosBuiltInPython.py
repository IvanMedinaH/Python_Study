"""MÓDULOS BUILT-IN DE PYTHON
Los módulos built-in son parte de la librería estándar de Python.
Se importan y usan según sea necesario."""

#---------------------------------------------------
"""MÓDULOS DEL SISTEMA Y ARCHIVOS"""
import os                   # Sistema operativo y archivos
import sys                  # Sistema e interprete de Python
import pathlib              # Rutas de archivos (moderno)
import shutil               # Operaciones de archivo de alto nivel
import tempfile             # Archivos y directorios temporales
import glob                 # Búsqueda de archivos con patrones
import fileinput            # Lectura de múltiples archivos

#---------------------------------------------------
"""MÓDULOS DE FECHA Y HORA"""
import datetime             # Fechas, horas y duraciones
import time                 # Tiempo y duración
import calendar             # Calendario

#---------------------------------------------------
"""MÓDULOS DE DATOS Y STRINGS"""
import json                 # Trabajar con JSON
import csv                  # Trabajar con CSV
import re                   # Expresiones regulares
import string               # Constantes de strings
import textwrap             # Formateo de texto
import difflib              # Comparación de secuencias

#---------------------------------------------------
"""MÓDULOS MATEMÁTICOS Y NUMÉRICOS"""
import math                 # Funciones matemáticas
import random               # Números y elementos aleatorios
import statistics           # Estadísticas básicas
import decimal              # Números decimales de precisión
import fractions            # Fracciones
import numbers              # Tipos numéricos abstractos

#---------------------------------------------------
"""MÓDULOS DE ESTRUCTURAS DE DATOS"""
import collections          # Tipos de datos especializados
import array                # Arrays tipados
import heapq                # Operaciones de montículo
import bisect               # Búsqueda binaria y inserción
import itertools            # Herramientas para iteración
import functools            # Herramientas funcionales
import operator             # Operadores como funciones

#---------------------------------------------------
"""MÓDULOS DE ENCRIPTACIÓN Y SEGURIDAD"""
import hashlib              # Funciones hash
import hmac                 # Códigos de autenticación
import secrets              # Generación segura de números aleatorios
import base64               # Codificación base64

#---------------------------------------------------
"""MÓDULOS DE COMPRESIÓN Y ARCHIVOS"""
import zipfile              # Trabajar con archivos ZIP
import tarfile              # Trabajar con archivos TAR
import gzip                 # Compresión GZIP
import bz2                  # Compresión BZIP2
import lzma                 # Compresión LZMA

#---------------------------------------------------
"""MÓDULOS DE FORMATO Y SERIALIZACIÓN"""
import pickle               # Serialización de objetos Python
import struct               # Manejo de datos binarios
import pprint               # Impresión con formato
import html                 # Parseo de HTML
import html.parser          # Parser de HTML
import xml.etree.ElementTree  # Parseo de XML
import urllib.parse         # Análisis de URLs

#---------------------------------------------------
"""MÓDULOS DE ENTRADA/SALIDA Y STREAMS"""
import io                   # Trabajar con streams
import codecs               # Codificadores y decodificadores
import getpass              # Entrada de contraseña sin eco

#---------------------------------------------------
"""MÓDULOS DE COMANDOS Y PROCESOS"""
import subprocess           # Ejecución de procesos
import shlex                # Análisis simple de shell
import argparse             # Análisis de argumentos de línea de comandos
import optparse             # Análisis de opciones deprecated
import configparser         # Análisis de archivos de configuración
import gettext              # Traducciones

#---------------------------------------------------
"""MÓDULOS DE CONCURRENCIA"""
import threading            # Hilos
import multiprocessing      # Multiprocesamiento
import queue                # Colas
import asyncio              # Programación asincrónica
import concurrent.futures   # Ejecutores concurrentes

#---------------------------------------------------
"""MÓDULOS DE RED Y COMUNICACIÓN"""
import socket               # Comunicación de red
import urllib.request       # Lectura de URLs
import http.client          # Cliente HTTP
import http.server          # Servidor HTTP
import ssl                  # Soporte SSL/TLS
import email                # Procesamiento de emails
import imaplib              # Protocolo IMAP
import smtplib              # Protocolo SMTP
import ftplib               # Protocolo FTP
import xmlrpc.client        # Cliente XML-RPC
import xmlrpc.server        # Servidor XML-RPC
import ipaddress            # Manejo de direcciones IP

#---------------------------------------------------
"""MÓDULOS DE BASE DE DATOS"""
import sqlite3              # Base de datos SQLite
import dbm                  # Interfaz de diccionario persistente
import shelve               # Persistencia de objetos

#---------------------------------------------------
"""MÓDULOS DE PROGRAMACIÓN Y UTILITARIOS"""
import types                # Tipos de objetos dinámicos
import typing               # Sugerencias de tipos (type hints)
import abc                  # Clases base abstractas
import dataclasses          # Decorador para clases de datos
import enum                 # Enumeraciones
import copy                 # Copiar objetos
import pydoc                # Generador de documentación
import inspect              # Inspección de objetos
import sys                  # Variables y funciones del sistema
import importlib            # Sistema de importación
import importlib.util       # Utilidades de importación
import pkgutil              # Utilidades de paquetes
import modulefinder         # Búsqueda de módulos
import runpy                # Ejecución de módulos
import contextlib           # Herramientas de contexto
import atexit               # Manejadores de salida
import traceback            # Manejo de excepciones
import warnings             # Control de advertencias
import locale               # Servicios de localización
import codecs               # Registros de codificadores

#---------------------------------------------------
"""MÓDULOS DE LOGGING Y DEBUG"""
import logging              # Registro de eventos
import logging.handlers     # Manejadores de logging
import pdb                  # Depurador de Python
import cProfile             # Profiler de CPU
import profile              # Profiler alternativo
import timeit               # Cronometraje de ejecución

#---------------------------------------------------
"""MÓDULOS DE CONSTANTES Y MISCELÁNEA"""
import builtins             # Funciones y tipos built-in
import keyword              # Palabras clave de Python
import token                # Constantes de tokens
import tokenize             # Tokenización de código Python
import ast                  # Análisis de sintaxis abstracta
import dis                  # Desamblador de bytecode
import sys                  # Parámetros y funciones del sistema
import sysconfig            # Variables de configuración del sistema
import platform             # Información de la plataforma

#---------------------------------------------------
"""EJEMPLOS DE USO"""

print("="*60)
print("EJEMPLOS DE MÓDULOS BUILT-IN")
print("="*60)

# RANDOM - Números aleatorios
print("\n1. MÓDULO RANDOM")
import random
print(f"Número aleatorio entre 1 y 10: {random.randint(1, 10)}")
print(f"Elemento aleatorio: {random.choice(['a', 'b', 'c'])}")
print(f"Muestra de 3 elementos: {random.sample(range(10), 3)}")

# DATETIME - Fechas y horas
print("\n2. MÓDULO DATETIME")
import datetime
hoy = datetime.date.today()
print(f"Fecha de hoy: {hoy}")

from datetime import datetime
ahora = datetime.now()
print(f"Fecha y hora actual: {ahora}")

# MATH - Operaciones matemáticas
print("\n3. MÓDULO MATH")
import math
print(f"Raíz cuadrada de 16: {math.sqrt(16)}")
print(f"Pi: {math.pi}")
print(f"Coseno de 0: {math.cos(0)}")

# OS - Sistema operativo
print("\n4. MÓDULO OS")
import os
print(f"Sistema operativo: {os.name}")
print(f"Directorio actual: {os.getcwd()}")

# JSON - Trabajar con JSON
print("\n5. MÓDULO JSON")
import json
datos = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
json_string = json.dumps(datos)
print(f"JSON string: {json_string}")
datos_recuperados = json.loads(json_string)
print(f"Datos recuperados: {datos_recuperados}")

# RE - Expresiones regulares
print("\n6. MÓDULO RE")
import re
texto = "Mi email es juan@example.com"
patron = r'[\w\.-]+@[\w\.-]+'
emails = re.findall(patron, texto)
print(f"Emails encontrados: {emails}")

# COLLECTIONS - Estructuras especializadas
print("\n7. MÓDULO COLLECTIONS")
from collections import Counter
lista = ['a', 'b', 'a', 'c', 'a', 'b']
contador = Counter(lista)
print(f"Conteo de elementos: {contador}")

# STATISTICS - Estadísticas
print("\n8. MÓDULO STATISTICS")
import statistics
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Media: {statistics.mean(numeros)}")
print(f"Mediana: {statistics.median(numeros)}")
print(f"Desviación estándar: {statistics.stdev(numeros)}")

# PATHLIB - Rutas de archivos (moderno)
print("\n9. MÓDULO PATHLIB")
from pathlib import Path
ruta = Path.cwd()
print(f"Directorio actual: {ruta}")
print(f"Directorio padre: {ruta.parent}")

# ITERTOOLS - Herramientas de iteración
print("\n10. MÓDULO ITERTOOLS")
import itertools
lista1 = ['a', 'b', 'c']
lista2 = [1, 2, 3]
combinaciones = list(itertools.product(lista1, lista2))
print(f"Producto cartesiano (primeros 3): {combinaciones[:3]}")

# HASHLIB - Funciones hash
print("\n11. MÓDULO HASHLIB")
import hashlib
texto = "contraseña123"
hash_sha256 = hashlib.sha256(texto.encode()).hexdigest()
print(f"SHA256 de 'contraseña123': {hash_sha256[:20]}...")

# ENUM - Enumeraciones
print("\n12. MÓDULO ENUM")
from enum import Enum

class Color(Enum):
    ROJO = 1
    VERDE = 2
    AZUL = 3

print(f"Color ROJO: {Color.ROJO.name} = {Color.ROJO.value}")

# DATACLASSES - Clases de datos
print("\n13. MÓDULO DATACLASSES")
from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str
    edad: int

persona = Persona("Carlos", 25)
print(f"Persona: {persona.nombre}, {persona.edad} años")

# TYPING - Type hints
print("\n14. MÓDULO TYPING")
from typing import List, Dict

def procesar_lista(items: List[int]) -> Dict[str, int]:
    return {"cantidad": len(items), "suma": sum(items)}

resultado = procesar_lista([1, 2, 3, 4, 5])
print(f"Resultado con type hints: {resultado}")

# DEFAULTDICT - Diccionarios con default
print("\n15. MÓDULO COLLECTIONS (defaultdict)")
from collections import defaultdict
grupos = defaultdict(list)
palabras = ['apple', 'apricot', 'banana', 'blueberry', 'cherry']
for palabra in palabras:
    grupos[palabra[0]].append(palabra)

print(f"Palabras agrupadas por letra inicial: {dict(grupos)}")

print("\n" + "="*60)
print("[OK] Ejemplos completados")
print("="*60)