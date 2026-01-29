# quan_ly_nhan_su/__manifest__.py
{
    'name': 'Quản lý nhân sự',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Module lõi quản lý nhân viên',
    'depends': ['base'],        # ❗ CHỈ base
    'data': [
        'security/ir.model.access.csv',
        'views/nhan_vien_view.xml',
    ],
    'application': True,
    'installable': True,
}