from odoo import http
from odoo.http import request
import random
import string

class GeneradorContrasenas(http.Controller):
    @http.route('/generador_contrasenas', auth='public', website=True)
    def index(self, **kw):
        return request.render("generador_contrasenas.index", {})

    @http.route('/generador_contrasenas/generar', type='json', auth='user', website=True)
    def generar(self, longitud=8, con_digitos=True, con_mayusculas=True, con_minusculas=True, con_simbolos=True):
        caracteres = ''
        
        if con_digitos:
            caracteres += string.digits
        if con_mayusculas:
            caracteres += string.ascii_uppercase
        if con_minusculas:
            caracteres += string.ascii_lowercase
        if con_simbolos:
            caracteres += string.punctuation

        contrasena = ''.join(random.choice(caracteres) for i in range(int(longitud)))
        
        return {'contrasena': contrasena}
