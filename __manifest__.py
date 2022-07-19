{
    'name' : "Student Management",
    'version' : "1.0.0",
    'author' : "Nitin",
    'depends': ['base','mail'],
    'license': "AGPL-3",
    'sequence': -100,
    'category': 'Uncategorized',
    'data': [
        'security/ir.model.access.csv',
        'views/s_views.xml',
        'views/c_views.xml',
        'views/sub_views.xml',
        'views/a.xml',
        'views/menu.xml',
        ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}