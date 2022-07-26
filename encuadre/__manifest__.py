# Copyright 2022 Marcelo
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Encuadre',
    'description': """
        Agregar campos en la tabla de encuadre""",
    'version': '13.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Marcelo',
    'depends': [
        'base', 'hr', 'relacion_personal'
    ],
    'data': [
        'security/personal.xml',
        'views/personal.xml',
        'views/report.xml',
    ],
    'demo': [
    ],
}
