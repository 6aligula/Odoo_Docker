from odoo import models, fields

class MiModelo(models.Model):
    _name = 'x_generador_contrasenas.mi_modelo'
    _description = 'Descripción de XGeneradorContrasenasMiModelo'

    name = fields.Char('Nombre')