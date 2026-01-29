from odoo import models, fields, api


class ChamCong(models.Model):
    _name = 'cham_cong'
    _description = 'Chấm công'
    _order = 'ngay desc'

    nhan_vien_id = fields.Many2one(
        'nhan_vien',
        string="Nhân viên",
        required=True,
        ondelete='cascade'
    )

    ngay = fields.Date(
        string="Ngày",
        required=True
    )

    so_cong = fields.Float(
        string="Số công",
        default=1.0
    )

    luong_co_ban = fields.Float(
        related='nhan_vien_id.luong',
        store=True,
        readonly=True
    )

    luong_ngay = fields.Float(
        string="Lương/ngày",
        compute='_compute_luong',
        store=True
    )

    tong_luong = fields.Float(
        string="Tổng lương",
        compute='_compute_luong',
        store=True
    )

    @api.depends('so_cong', 'luong_co_ban')
    def _compute_luong(self):
        for rec in self:
            rec.luong_ngay = rec.luong_co_ban / 26 if rec.luong_co_ban else 0
            rec.tong_luong = rec.so_cong * rec.luong_ngay
