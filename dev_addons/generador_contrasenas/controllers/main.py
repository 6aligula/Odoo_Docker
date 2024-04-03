from odoo import http
from odoo.http import request
import random
import string

class GeneradorContrasenas(http.Controller):
    @http.route('/generador_contrasenas', auth='public', website=True, methods=['GET'])
    def index(self, **kw):
        # Simplemente renderiza la página con el formulario
        return request.render("generador_contrasenas.index", {})

    @http.route('/generador_contrasenas/generar', auth='user', website=True, methods=['POST'])
    def generar(self, **post):
        longitud = post.get('longitud', 8)
        con_digitos = post.get('con_digitos', 'off') == 'on'
        con_mayusculas = post.get('con_mayusculas', 'off') == 'on'
        con_minusculas = post.get('con_minusculas', 'off') == 'on'
        con_simbolos = post.get('con_simbolos', 'off') == 'on'

        caracteres = ''
        
        if con_digitos:
            caracteres += string.digits
        if con_mayusculas:
            caracteres += string.ascii_uppercase
        if con_minusculas:
            caracteres += string.ascii_lowercase
        if con_simbolos:
            caracteres += string.punctuation

        if not caracteres:
            # Asegúrate de tener al menos un conjunto de caracteres para evitar un bucle infinito
            caracteres = string.ascii_letters

        contrasena = ''.join(random.choice(caracteres) for i in range(int(longitud)))
        
        # Renderiza una página que muestra la contraseña generada
        return request.render("generador_contrasenas.resultado_generacion", {'contrasena': contrasena})
