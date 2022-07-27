# Copyright 2022 Marcelo
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models

black_list = {'create_date', 'create_uid', 'write_date', 'write_uid', '__last_update', 'company_id', 'id'}

class Personal(models.Model):

    _name = "personal"
    _description = "Personal"  # TODO
    _rec_name = "nombre"

    """ Crear los campos de personal """

    numero = fields.Integer()
    no_organico = fields.Integer()
    no_emp = fields.Integer()
    grado = fields.Char()
    nombre = fields.Char()
    adscripcion = fields.Char()
    alta_ads1 = fields.Date()
    apartado = fields.Char()
    ads_ant = fields.Char()
    alta_ads2 = fields.Date()
    cargo = fields.Char()
    tipo_i = fields.Char()
    rol = fields.Char()
    genero = fields.Char()
    x_or = fields.Integer(string="OR")
    estatus = fields.Char()
    tipo_proc = fields.Char()
    oficio_proc = fields.Char()
    fecha_proc = fields.Date()
    fecha_ing = fields.Date()
    fecha_ing_c = fields.Date()
    observaciones = fields.Char()
    institucion = fields.Char()
    etiquet_org = fields.Char()
    escala = fields.Char()
    mandos = fields.Char()
    residencia = fields.Char()
    coper = fields.Char()
    ubi_func = fields.Char()
    situacion = fields.Char()
    covid = fields.Char()
    imagen = fields.Image(string="Image")
    active = fields.Boolean(default=True)

    def crear_relacion_personal(self):
        for record in self:
            write_fields = self.fields_get()
            data_fields = set(write_fields.keys()) - black_list
            data = record.read()[0]
            write_dict = {}
            for value in data:
                if value in data_fields:
                    write_dict[value] = data[value]
            relacion_personal = self.env["relacion.personal"].sudo().create(write_dict)
            action = {
                'name': 'Relacion Personal',
                'view_mode': 'form',
                'res_model': 'relacion.personal',
                'res_id': relacion_personal.id,
                'type': 'ir.actions.act_window',
            }
            record.active = False
            return action
            
