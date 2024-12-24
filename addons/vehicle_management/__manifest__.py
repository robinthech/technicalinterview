{
    'name': "Vehicle Management",
    'summary': "Vehicle Management",
    'author': "Robinson Torres Herrera",
    'website': "https://github.com/robinthech",
    'category': 'Human Resources/Fleet',
    'version': '17.0.1.0.0',
    'depends': [
        'base',
        'contacts',
    ],
    'data': [
        'security/security.xml',
        "security/ir.model.access.csv",

        "views/my_company_vehicle_views.xml",
    ],
    'demo': [],
    'installable': True,
    'license': 'Other proprietary',
    "sequence": 10,
}
