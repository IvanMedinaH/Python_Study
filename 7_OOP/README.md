# Programación Orientada a Objetos (OOP) en Python

Este módulo contiene una serie completa de ejemplos de estudio sobre Programación Orientada a Objetos en Python.

## Estructura de Aprendizaje

### 1. **IntroduccionOOP.py**
**Punto de partida - Conceptos fundamentales**
- ¿Qué es una clase?
- Atributos y métodos
- Pilares de la OOP (Encapsulamiento, Herencia, Polimorfismo)
- Ejemplo completo: Sistema de Biblioteca
- Ventajas de la OOP

**Recomendación:** Comienza aquí para entender los conceptos básicos.

---

### 2. **ClasesPython.py**
**Clases y Objetos - Fundamentos**
- Concepto básico de clases
- Atributos de clase
- Atributos de instancia
- Diferencia entre atributos de clase e instancia
- Método `__str__` para representación
- Crear múltiples objetos
- Objetos dentro de otros objetos (composición)

**Importante:** Entender la diferencia entre clase (molde) y objeto (instancia).

---

### 3. **ConstructoresPython.py**
**Constructores y Inicialización**
- Constructor básico (`__init__`)
- Múltiples parámetros en el constructor
- Parámetros con valores por defecto
- Inicialización de múltiples atributos
- Constructores que calculan valores
- Validación en constructores
- Constructores con listas
- Composición de objetos en el constructor
- Contador de objetos creados
- Procesamiento de datos en el constructor

**Clave:** El constructor se ejecuta automáticamente al crear un objeto.

---

### 4. **MetodosPython.py**
**Métodos - Comportamiento de los Objetos**
- Método básico
- Métodos con parámetros
- Métodos que retornan valores
- Métodos que modifican atributos
- Métodos especiales (`__str__`, `__repr__`)
- Múltiples métodos en una clase
- Métodos auxiliares privados (por convención)
- Métodos que trabajan con listas

**Nota:** Los métodos son funciones que actúan sobre los datos del objeto.

---

### 5. **EncapsulacionPython.py**
**Encapsulamiento - Control de Acceso**
- Atributos públicos vs privados (convención)
- Métodos públicos vs privados
- Getters (métodos para obtener valores)
- Setters (métodos para establecer valores)
- Encapsulamiento con validación
- Propiedades (@property)
- Encapsulamiento en listas
- Métodos privados para lógica interna
- Double underscore (name mangling)

**Objetivo:** Proteger los datos internos y controlar cómo se accede a ellos.

---

### 6. **HerenciaPython.py**
**Herencia Simple - Reutilización de Código**
- Herencia básica
- Métodos sobrescritos
- Usar `super()` para llamar a métodos de la clase padre
- Herencia de atributos y métodos
- Métodos adicionales en la clase hija
- Verificar herencia con `isinstance()` e `issubclass()`
- Herencia con atributos privados
- Jerarquía de herencia
- Herencia y constructores
- Métodos heredados disponibles en la clase hija

**Ventaja:** Las clases hijas heredan todo de la clase padre y pueden extender su funcionalidad.

---

### 7. **EjerciciosPracticos.py**
**Práctica - Refuerza lo Aprendido**

Contiene 8 ejercicios completos:

1. **Clase Estudiante** - Atributos, lista de calificaciones, cálculo de promedio
2. **Clase Rectángulo** - Validación en constructor, cálculo de área y perímetro
3. **Clase Temperatura** - Encapsulamiento, conversión de unidades
4. **Herencia Simple** - Vehículos (Auto y Motocicleta)
5. **Lista de Objetos** - Carrito de compras con productos
6. **Polimorfismo** - Diferentes animales, mismo método (sonido)
7. **Métodos Privados** - Validación y encriptación de contraseñas
8. **Jerarquía de Herencia** - Persona → Empleado → Gerente

**Recomendación:** Ejecuta y modifica estos ejercicios para practicar.

---

## Orden Recomendado de Estudio

```
1. IntroduccionOOP.py
   ↓
2. ClasesPython.py
   ↓
3. ConstructoresPython.py
   ↓
4. MetodosPython.py
   ↓
5. EncapsulacionPython.py
   ↓
6. HerenciaPython.py
   ↓
7. EjerciciosPracticos.py
```

## Cómo Ejecutar los Ejemplos

```bash
# Desde la carpeta del proyecto
python 7_OOP/IntroduccionOOP.py
python 7_OOP/ClasesPython.py
python 7_OOP/ConstructoresPython.py
python 7_OOP/MetodosPython.py
python 7_OOP/EncapsulacionPython.py
python 7_OOP/HerenciaPython.py
python 7_OOP/EjerciciosPracticos.py
```

## Conceptos Clave a Recordar

### Clases
- Una **clase** es una plantilla para crear objetos
- Define la estructura (atributos) y el comportamiento (métodos)

### Objetos
- Un **objeto** es una instancia específica de una clase
- Cada objeto tiene sus propios valores de atributos

### Atributos
- Datos que caracterizan a un objeto
- Atributos de clase: compartidos por todas las instancias
- Atributos de instancia: únicos para cada objeto

### Métodos
- Funciones definidas dentro de una clase
- Actúan sobre los datos del objeto
- Pueden acceder y modificar atributos

### Constructor (`__init__`)
- Método especial que se ejecuta al crear un objeto
- Se usa para inicializar los atributos
- Es opcional pero muy recomendado

### Encapsulamiento
- Ocultar detalles internos (usar `_nombre` por convención)
- Proporcionar una interfaz pública controlada
- Usar getters y setters para acceder a datos privados

### Herencia
- Una clase puede heredar de otra
- La clase hija obtiene todos los atributos y métodos de la clase padre
- Permite reutilizar código y crear jerarquías

### Polimorfismo
- Diferentes objetos pueden responder al mismo método de forma diferente
- Ejemplo: `sonido()` en perro, gato, pájaro producen resultados distintos

## Tips Importantes

✅ **DO:**
- Usar nombres descriptivos para clases y métodos
- Inicializar atributos en `__init__`
- Usar `self` para referirse a atributos del objeto
- Encapsular datos sensibles con `_`
- Usar `super()` para llamar a métodos de la clase padre

❌ **DON'T:**
- No acceder directamente a atributos privados (`_atributo`)
- No crear demasiadas responsabilidades en una clase
- No olvidar el parámetro `self` en los métodos
- No mezclar lógica de negocio con presentación

---

**¡Buena suerte con tu aprendizaje de OOP!** 🚀
