from odoo import models, fields, api


class NhanVien(models.Model):
    _name = 'quan_ly_nhan_su.nhan_vien'
    _description = 'Nhân viên (lõi hệ thống)'

    # ===== THÔNG TIN CƠ BẢN =====
    name = fields.Char(
        string='Họ và tên',
        required=True
    )

    ma_nhan_vien = fields.Char(
        string='Mã nhân viên',
        required=True
    )

    job_title = fields.Char(string='Chức vụ')
    department = fields.Char(string='Phòng ban')
    active = fields.Boolean(default=True)

    # ===== THỐNG KÊ – HIỆU SUẤT (PHẦN ĂN ĐIỂM) =====
    so_cong_viec = fields.Integer(
        string='Tổng số công việc',
        compute='_compute_hieu_suat'
    )

    so_cong_viec_hoan_thanh = fields.Integer(
        string='Số công việc hoàn thành',
        compute='_compute_hieu_suat'
    )

    ty_le_dung_han = fields.Float(
        string='Tỷ lệ hoàn thành đúng hạn (%)',
        compute='_compute_hieu_suat'
    )

    # ===== LOGIC TÍNH HIỆU SUẤT =====
    @api.depends()
    def _compute_hieu_suat(self):
        CongViec = self.env['cong_viec']

        for nv in self:
            tasks = CongViec.search([
                ('nhan_vien_ids', 'in', nv.id)
            ])

            nv.so_cong_viec = len(tasks)

            hoan_thanh = tasks.filtered(
                lambda t: t.phan_tram_cong_viec == 100
            )
            nv.so_cong_viec_hoan_thanh = len(hoan_thanh)

            dung_han = hoan_thanh.filtered(
                lambda t: t.han_chot and t.han_chot >= fields.Datetime.now()
            )

            nv.ty_le_dung_han = (
                len(dung_han) / len(hoan_thanh) * 100
                if hoan_thanh else 0
            )