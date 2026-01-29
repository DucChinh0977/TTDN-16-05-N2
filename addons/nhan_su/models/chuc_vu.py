from odoo import models, fields


class ChucVu(models.Model):
    _name = 'chuc_vu'
    _description = 'Chức vụ'
    _order = 'ten_chuc_vu asc'

    ma_chuc_vu = fields.Char(
        string="Mã chức vụ",
        required=True
    )

    ten_chuc_vu = fields.Char(
        string="Tên chức vụ",
        required=True
    )

    mo_ta = fields.Text(string="Mô tả")

    nhan_vien_ids = fields.One2many(
        'nhan_vien',
        'chuc_vu_id',
        string="Nhân viên"
    )
