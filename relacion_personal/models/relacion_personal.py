# Copyright 2022 Marcelo
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class RelacionPersonal(models.Model):

    _name = "relacion.personal"
    _description = "Relacion Personal"  # TODO
    _rec_name = "nombre"

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

