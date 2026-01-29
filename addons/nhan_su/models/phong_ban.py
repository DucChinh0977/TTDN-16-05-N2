from odoo import models, fields


class PhongBan(models.Model):
    _name = 'phong_ban'
    _description = 'Phòng ban'
    _order = 'ten_phong asc'

    ma_phong = fields.Char(
        string="Mã phòng",
        required=True
    )

    ten_phong = fields.Char(
        string="Tên phòng",
        required=True
    )

    mo_ta = fields.Text(string="Mô tả")

    nhan_vien_ids = fields.One2many(
        'nhan_vien',
        'phong_ban_id',
        string="Danh sách nhân viên"
    )
