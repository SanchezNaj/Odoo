# Copyright 2022 Marcelo
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Relacion Personal',
    'description': """
        Tabla de relacion de personal""",
    'version': '13.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Marcelo',
    'depends': [
        'base','hr'
    ],
    'data': [
        'security/group.xml',
        'security/relacion_personal.xml',
        'views/relacion_personal.xml',
        'views/report.xml'
    ],
    'demo': [
    ],
}
