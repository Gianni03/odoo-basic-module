from odoo import models, fields

class MiModelo(models.Model):
  _name = 'mi.modelo'
  _descripcion = 'Mi modelo Básico'

  name = fields.Char(string='Nombre')
  lineas_ids = fields.One2many('mi.modelo.linea', 'modelo_id', string='Líneas')