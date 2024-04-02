### 1. Crear la estructura básica del módulo

Primero, crea la estructura de carpetas y archivos básicos para tu módulo en la carpeta `dev_addons`. Un módulo de Odoo típicamente tiene una estructura como la siguiente:

```bash
dev_addons/
└── generador_contrasenas/
    ├── __init__.py
    ├── __manifest__.py
    ├── controllers/
    │   ├── __init__.py
    │   └── main.py  
    ├── models/
    │   └── __init__.py
	│   └── mi_modelo.py 
    ├── security/
    │   └── ir.model.access.csv
    ├── static/
	|   └── src/ 
	│       └── js/ 
	│           └── mi_script.js
	|   
    ├── views/
        ├── generador_contrasenas_view.xml 
        └── menu_views.xml  
```


# Explicación
Cada archivo y carpeta tiene su propósito:

- `__init__.py`: Hace que Python trate los directorios como módulos. También se utiliza para importar partes del módulo.
- `__manifest__.py`: Contiene información sobre el módulo, como nombre, descripción, dependencias, datos demo, etc.
- `controllers/`: Contiene los controladores para manejar peticiones web.
- `models/`: Define los modelos de datos (objetos).
- `security/`: Define las reglas de seguridad y los grupos de acceso.
- `views/`: Contiene las definiciones de la interfaz de usuario como vistas, acciones y menús.
- `data/`: Datos iniciales que son cargados al instalar el módulo.

### 2. Configurar el archivo `__manifest__.py`

Este archivo contiene metadatos del módulo. Asegúrate de llenar correctamente los campos como 'name', 'version', 'category', 'depends', etc. Aquí hay un ejemplo básico:

```python
{
    'name': "Mi Modulo",
    'summary': "Generar contraseñas aleatorias seguras",
    'version': '1.0',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/generador_contrasenas_view.xml',
        'views/menu_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'generador_contrasenas/static/src/js/mi_script.js',
        ],
    },
    'demo': [],
    'installable': True,
    'application': True,
}

```

### 3. Crear un modelo

En la carpeta `models`, crea un nuevo archivo para definir tu modelo de datos, que heredará de `models.Model`. En el archivo `__init__.py` dentro de models, importa tu modelo. Por ejemplo:

```python
from . import mi_modelo
```

Y en `mi_modelo.py`:

```python
from odoo import models, fields

class MiModelo(models.Model):
	_name = 'x_generador_contrasenas.mi_modelo'
	_description = 'Descripción de XGeneradorContrasenasMiModelo'

    name = fields.Char('Nombre')
```

### 4. Añadir vistas y menús

Dentro de la carpeta `views`, crea los archivos XML que definirán la interfaz de usuario de tu módulo. Estos archivos especificarán cómo se muestran los modelos de datos en la interfaz de Odoo.

`generador_contrasenas_view.xml`
```xml
<odoo>
    <template id="index" name="Generador de Contraseñas">
        <t t-call="website.layout">
            <div id="wrap" class="oe_structure oe_empty">
                <div class="container">
                    <h1>Generador de Contraseñas</h1>
                    <form id="generador_form">
                        <input type="number" name="longitud" placeholder="Longitud de la contraseña" />
                        <div>
                            <input type="checkbox" name="con_digitos" id="con_digitos" checked="true" />
                            <label for="con_digitos">Incluir Dígitos</label>
                        </div>
                        <div>
                            <input type="checkbox" name="con_mayusculas" id="con_mayusculas" checked="true" />
                            <label for="con_mayusculas">Incluir Mayúsculas</label>
                        </div>
                        <div>
                            <input type="checkbox" name="con_minusculas" id="con_minusculas" checked="true" />
                            <label for="con_minusculas">Incluir Minúsculas</label>
                        </div>
                        <div>
                            <input type="checkbox" name="con_simbolos" id="con_simbolos" checked="true" />
                            <label for="con_simbolos">Incluir Símbolos</label>
                        </div>
                        <button type="button" onclick="generarContrasena()">Generar Contraseña</button>
                    </form>
                    <div id="contrasena_generada"></div>
                </div>
            </div>
            <script>
                function generarContrasena() {
                    var form = document.getElementById('generador_form');
                    var formData = new FormData(form);
                    odoo.define('generador_contrasenas.generar', function (require) {
                        'use strict';
                        var ajax = require('web.ajax');
                        ajax.jsonRpc("/generador_contrasenas/generar", 'call', {
                            'longitud': formData.get('longitud'),
                            'con_digitos': formData.get('con_digitos') ? true : false,
                            'con_mayusculas': formData.get('con_mayusculas') ? true : false,
                            'con_minusculas': formData.get('con_minusculas') ? true : false,
                            'con_simbolos': formData.get('con_simbolos') ? true : false
                        }).then(function (data) {
                            document.getElementById('contrasena_generada').innerText = 'Contraseña Generada: ' + data.contrasena;
                        });
                    });
                }
            </script>
        </t>
    </template>
    
    <template id="assets_frontend" inherit_id="web.assets_frontend">
		<xpath expr="." position="inside">
		<script type="text/javascript" src="/generador_contrasenas/static/src/js/mi_script.js"></script>
		</xpath>
	</template>
</odoo>

```
 Codigo del fichero `menu_views.xml` dentro de la carpeta `views`
```xml
<odoo>
	<data>
	<!-- Acción del Menú para abrir la vista del generador de contraseñas -->
	
	<record id="action_generador_contrasenas" model="ir.actions.client">
		<field name="name">Generador de Contraseñas</field>
		<field name="tag">generador_contrasenas</field>
		<field name="target">new</field>
	</record>
	<!-- Elemento de Menú que enlaza a la acción -->
	
	<menuitem id="menu_generador_contrasenas_main" name="Generador de Contraseñas"
		action="action_generador_contrasenas"/>
	</data>
</odoo>
```

Dentro de la carpeta `static/src/js/` añadimos el script `mi_script.js`
```js
odoo.define('generador_contrasenas.generar', function(require) {

	'use strict';
	
	var ajax = require('web.ajax');
	
	function generarContrasena() {
	var form = document.getElementById('generador_form');
	var formData = new FormData(form);
	
	ajax.jsonRpc("/generador_contrasenas/generar", 'call', {
		'longitud': formData.get('longitud')
		'con_digitos': formData.get('con_digitos') ? true : false,
		'con_mayusculas': formData.get('con_mayusculas') ? true : false,
		'con_minusculas': formData.get('con_minusculas') ? true : false,
		'con_simbolos': formData.get('con_simbolos') ? true : false
	
	}).then(function (data) {
	
	document.getElementById('contrasena_generada').innerText = 'Contraseña Generada: ' + data.contrasena;
	
	});
	
	}
	
	window.generarContrasena = generarContrasena;

});
```

### 5. Añadir seguridad

Define las reglas de seguridad en `ir.model.access.csv` dentro de la carpeta `security`. Por ejemplo:
```csv
id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink
access_x_generador_contrasenas_mi_modelo,x_generador_contrasenas_mi_modelo,model_x_generador_contrasenas_mi_modelo,,1,1,1,1

```

### 6. Agregar el módulo a Odoo

Para que Odoo detecte el nuevo módulo, asegúrate de añadir el volumen de `dev_addons` a tu `docker-compose.yml` bajo el servicio de Odoo, algo así:
## !Ya esta configurado en el docker-compose

```yml
volumes:
    - ./dev_addons:/mnt/extra-addons
```

### Actualizar `__init__.py` en `controllers`

Para registrar tu controlador, necesitas importar el archivo `main.py` (o como lo hayas llamado) en el `__init__.py` dentro del directorio `controllers`. Suponiendo que tu archivo de controlador se llama `main.py` y está en el directorio `controllers`, el `__init__.py` debería verse así:
```python
from . import main
```

Asegúrate de que el archivo `__init__.py` en el directorio raíz del módulo importe el submódulo `controllers`.

```python
from . import controllers
```
### 7. Reiniciar Odoo y actualizar la lista de aplicaciones

Después de hacer tus cambios, necesitarás reiniciar tus contenedores de Odoo para que los cambios tengan efecto. Luego, actualiza la lista de aplicaciones desde la interfaz de administración de Odoo.

Después de hacer ctrl +  c, podéis volver a lanzar el docker-compose para que reconozca el nuevo modulo
```bash
docker-compose restart web
```

```bash
docker-compose up
Starting odoo_docker_db_1 ... done
Starting odoo_docker_web_1 ... done
Attaching to odoo_docker_db_1, odoo_docker_web_1
db_1   | 
db_1   | PostgreSQL Database directory appears to contain a database; Skipping initialization
db_1   | 
db_1   | 2024-04-02 13:33:58.771 UTC [1] LOG:  starting PostgreSQL 16.0 (Debian 16.0-1.pgdg120+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
db_1   | 2024-04-02 13:33:58.771 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
```

### 8. Instalar el módulo

Ve a la interfaz de Odoo, actualiza la lista de aplicaciones y busca tu módulo. Deberías poder instalarlo directamente desde la interfaz.

![[Pasted image 20240402184112.png]]
### 9. Debugar errores




¡Y eso es! Con estos pasos deberías ser capaz de construir un módulo básico en Odoo. Recuerda que la práctica hace al maestro, así que no dudes en experimentar y aprender más sobre las capacidades de Odoo mientras desarrollas tu módulo.