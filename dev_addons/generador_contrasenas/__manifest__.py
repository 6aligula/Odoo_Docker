{
    'name': "Mi Modulo",
    'summary': "Generar contraseñas aleatorias seguras",
    'version': '1.0',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/generador_contrasenas_view.xml',
        'views/resultado_view.xml',
        'views/menu_views.xml',
    ],

    'demo': [],
    'installable': True,
    'application': True,
}
