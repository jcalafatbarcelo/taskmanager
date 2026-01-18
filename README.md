# TaskManager

> 🎓 **Proyecto académico de prácticas** para el **Máster en Desarrollo e Inteligencia Artificial**
>
> *Módulo 0: Fundamentos de Programación Python*

Un gestor de tareas simple y eficiente desarrollado en Python que permite crear, listar, completar y eliminar tareas. Las tareas se persisten automáticamente en un archivo JSON para mantener los datos entre sesiones.

## 🎯 Descripción del Proyecto

TaskManager es una aplicación de línea de comandos que proporciona una interfaz intuitiva para gestionar tareas del día a día. Este proyecto forma parte del **Módulo 0: Fundamentos de Programación Python** del Máster en Desarrollo e Inteligencia Artificial, y demuestra conceptos fundamentales de programación en Python incluyendo:

- **Programación orientada a objetos** (POO)
- **Manejo de archivos** y persistencia de datos
- **Trabajar con JSON** para serialización de datos
- **Pruebas unitarias** y testing
- **Integración con APIs externas** (OpenAI)
- **Gestión de variables de entorno** y configuración
- **Patrones de diseño** y buenas prácticas

## ✨ Características

- ✅ **Agregar tareas simples**: Crea nuevas tareas con descripción única
- 🤖 **Agregar tareas complejas con IA**: Integración con OpenAI para desglosar tareas complejas en subtareas simples y accionables
- 📋 **Listar tareas**: Visualiza todas las tareas con su estado (completada o pendiente) e identificador único
- ✓ **Completar tareas**: Marca tareas como completadas con actualización instantánea
- 🗑️ **Eliminar tareas**: Elimina tareas por su ID
- 💾 **Persistencia automática**: Guarda automáticamente las tareas en archivo JSON después de cada operación
- 🔄 **Carga automática**: Carga las tareas guardadas al iniciar la aplicación
- 📝 **Interfaz interactiva**: Menú intuitivo basado en opciones numéricas
- 🧪 **Pruebas unitarias**: Suite completa de tests con cobertura de todas las funciones principales
- 📊 **Logging integrado**: Sistema de logging para auditoría y depuración
- 🎯 **Gestión de IDs**: Generación automática y secuencial de IDs para las tareas

## 📚 Objetivos de Aprendizaje

Este proyecto educativo fue diseñado para que el estudiante practique y consolide los siguientes conceptos:

- ✅ Crear clases y trabajar con instancias de objetos
- ✅ Implementar métodos y atributos de clase
- ✅ Realizar operaciones CRUD (Create, Read, Update, Delete)
- ✅ Serializar y deserializar datos en JSON
- ✅ Escribir pruebas unitarias efectivas
- ✅ Integrar APIs externas en aplicaciones Python
- ✅ Utilizar librerías estándar (logging, json, unittest)
- ✅ Aplicar buenas prácticas de programación

## 📋 Requisitos

- Python 3.10 o superior (por el uso de match statements)
- OpenAI API key (opcional, solo si se desea usar la funcionalidad de IA)

## 🛠️ Stack Tecnológico

| Tecnología | Versión | Descripción |
| ----------- | --------- | ------------- |
| **Python** | 3.10+ | Lenguaje de programación principal |
| **JSON** | Estándar | Formato de persistencia de datos |
| **unittest** | Librería estándar | Framework de pruebas unitarias |
| **logging** | Librería estándar | Sistema de logging y auditoría |
| **OpenAI API** | v1.0+ | Inteligencia artificial para desgloses de tareas |
| **python-dotenv** | 1.0+ | Gestión de variables de entorno |
| **Git** | 2.0+ | Control de versiones |

**Dependencias principales** (ver `requirements.txt`):

- `openai` - Cliente para interactuar con la API de OpenAI
- `python-dotenv` - Para cargar variables de entorno desde archivo `.env`

## � Configuración

### Variables de entorno

Para usar la funcionalidad de IA (agregar tareas complejas), debes configurar tu API key de OpenAI:

1. Crea un archivo `.env` en la raíz del proyecto:

   ```config
   OPENAI_API_KEY=tu_api_key_aqui
   ```

2. Instala la librería `python-dotenv`:

   ```bash
   pip install python-dotenv
   ```

**Nota**: Sin configurar la API key, la opción de "Agregar tarea compleja (IA)" retornará un error.

1. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/jcalafatbarcelo/taskmanager.git
   cd taskmanager
   ```

2. **Crear un entorno virtual** (recomendado):

   ```bash
   python -m venv .venv
   ```

3. **Activar el entorno virtual**:
   - En Windows:

     ```bash
     .venv\Scripts\activate
     ```

   - En macOS/Linux:

     ```bash
     source .venv/bin/activate
     ```

4. **Instalar dependencias** (si las hay):

   ```bash
   pip install -r requirements.txt
   ```

## 📖 Uso

### Ejecutar la aplicación

```bash
python main.py
```

### Menú de opciones

Una vez iniciada la aplicación, verás el siguiente menú:

```Text
--- Gestor de Tareas Inteligente ---
1. Añadir tarea
2. Añadir tarea compleja (IA)
3. Listar tareas
4. Completar tarea
5. Eliminar tarea
6. Salir
```

### Opciones disponibles

1. **Añadir tarea simple**: Introduce una descripción simple y crea una tarea directamente

   ```Text
   Elige una opción: 1
   Descripción de la tarea: Comprar leche
   ```

2. **Añadir tarea compleja (IA)**: Introduce una tarea compleja y la IA la desglosa automáticamente en subtareas

   ```Text
   Elige una opción: 2
   Descripción de la tarea compleja: Organizar una reunión de equipo en la oficina
   ```

   La IA generará subtareas como:
   - Reservar sala de reuniones
   - Enviar invitaciones a los asistentes
   - Preparar la agenda
   - Etc.

3. **Listar tareas**: Muestra todas las tareas con su estado

   ```Text
   Elige una opción: 3
   ```

   Salida:

   ```Text
   [ ] #1: Comprar leche
   [✓] #2: Hacer la compra
   ```

4. **Completar tarea**: Marca una tarea como completada

   ```Text
   Elige una opción: 4
   ID de la tarea a completar: 1
   ```

5. **Eliminar tarea**: Elimina una tarea del listado

   ```Text
   Elige una opción: 5
   ID de la tarea a eliminar: 1
   ```

6. **Salir**: Cierra la aplicación

   ```Text
   Elige una opción: 6
   Saliendo...
   ```

## 🧪 Pruebas Unitarias

El proyecto incluye un conjunto completo de pruebas unitarias usando `unittest`.

### Ejecutar los tests

```bash
python -m unittest test_task_manager.py -v
```

### Cobertura de tests

Los tests cubren las siguientes funcionalidades:

- `test_add_task` - Verifica que se agrega una tarea correctamente
- `test_list_task` - Verifica que se listan todas las tareas
- `test_complete_task` - Verifica que se marca una tarea como completada
- `test_delete_task` - Verifica que se elimina una tarea
- `test_load_tasks` - Verifica que se cargan las tareas desde archivo
- `test_save_tasks` - Verifica que se guardan las tareas en archivo

**Resultado esperado**: Todos los tests deben pasar (OK)

## 📁 Estructura del Proyecto

```Text
taskmanager/
├── main.py                 # Punto de entrada de la aplicación
├── task_manager.py         # Clase TaskManager y Task
├── ai_service.py           # Servicio de IA (integración futura)
├── test_task_manager.py    # Pruebas unitarias
├── tasks.json              # Archivo de persistencia de tareas (se crea automáticamente)
├── requirements.txt        # Dependencias del proyecto
├── README.md              # Este archivo
└── .gitignore             # Archivos ignorados por Git
```

## 📦 Clases Principales

### Task

Representa una tarea individual con atributos y métodos para gestionar su información.

```python
class Task:
    def __init__(self, id, description, completed=False)
    def __str__(self)  # Retorna la representación visual de la tarea
    
    # Atributos:
    # - id: Identificador único de la tarea (entero)
    # - description: Descripción de la tarea (string)
    # - completed: Estado de completación (booleano, por defecto False)
```

**Ejemplo de salida**:

```Text
[✓] #1: Comprar leche      # Tarea completada
[ ] #2: Hacer la compra    # Tarea pendiente
```

### TaskManager (class)

Gestiona la colección de tareas, incluyendo operaciones CRUD y persistencia en archivo.

```python
class TaskManager:
    FILENAME = "tasks.json"  # Nombre del archivo de persistencia
    
    def __init__()                   # Inicializa el gestor y carga las tareas
    def add_task(description)        # Agrega una nueva tarea
    def list_task()                  # Lista todas las tareas en el log
    def complete_task(id)            # Marca una tarea como completada
    def delete_task(id)              # Elimina una tarea por ID
    def load_tasks()                 # Carga tareas desde el archivo JSON
    def save_tasks()                 # Guarda todas las tareas en archivo JSON
```

### AIService

Módulo para integración con inteligencia artificial (OpenAI) para desglosar tareas complejas.

```python
def create_simple_tasks(description)
    # Toma una descripción de tarea compleja y retorna una lista de subtareas
    # Requiere: Variable de entorno OPENAI_API_KEY configurada
    # Retorna: Lista de subtareas generadas por IA
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crea una rama para tu funcionalidad (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👤 Autor

- **Jaime Calafat Barceló** - [GitHub](https://github.com/jcalafatbarcelo)

## 📞 Soporte

Si tienes preguntas o encuentras problemas, por favor abre un issue en el repositorio.

---

**Última actualización**: 18 de enero de 2026
