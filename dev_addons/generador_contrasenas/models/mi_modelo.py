from odoo import models, fields

class MiModelo(models.Model):
    _name = 'mi.modelo'
    _description = 'Descripción de mi modelo'

    name = fields.Char('Nombre')