{
    'name': "Mi Modulo",
    'summary': "Generar contraseñas aleatorias seguras",
    'version': '1.0',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/generador_contrasenas_view.xml',
        'views/menu_views.xml',
        'data/initial_data.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
}
