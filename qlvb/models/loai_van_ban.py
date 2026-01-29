from odoo import models, fields

class LoaiVanBan(models.Model):
    _name = 'loai_van_ban'
    _description = 'Bảng chứa thông tin loại văn bản'
    _rec_name = 'ten_loai_van_ban'

    ma_loai_van_ban = fields.Char("Mã loại văn bản", required=True)
    ten_loai_van_ban = fields.Char("Tên loại văn bản", required=True)
