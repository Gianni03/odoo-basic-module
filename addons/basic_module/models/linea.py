from odoo import models, fields

class MiModeloLinea(models.Model):
  _name = 'mi.modelo.linea'
  _description = 'Línea de Mi Modelo'

  name = fields.char(string='Description')
  modelo_id = fields.Mmany2one('mi_modelo', string='Modelo relacionado')