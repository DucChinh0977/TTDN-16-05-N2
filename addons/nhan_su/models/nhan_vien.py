from odoo import models, fields, api


class NhanVien(models.Model):
    _name = 'nhan_vien'
    _description = 'Nhân viên'
    _order = 'ho_ten asc'

    # ===== Thông tin cá nhân =====
    ma_dinh_danh = fields.Char(
        string="Mã định danh",
        required=True,
        index=True
    )

    ho_ten = fields.Char(
        string="Họ tên",
        required=True
    )

    ngay_sinh = fields.Date(string="Ngày sinh")
    que_quan = fields.Char(string="Quê quán")
    dia_chi = fields.Char(string="Địa chỉ")
    email = fields.Char(string="Email")
    so_dien_thoai = fields.Char(string="Số điện thoại")
    so_bhxh = fields.Char(string="Số BHXH")

    # ===== Thông tin công việc =====
    phong_ban_id = fields.Many2one(
        'phong_ban',
        string="Phòng ban",
        ondelete='set null'
    )

    chuc_vu_id = fields.Many2one(
        'chuc_vu',
        string="Chức vụ",
        ondelete='set null'
    )

    ngay_vao_lam = fields.Date(string="Ngày vào làm")

    luong = fields.Float(
        string="Lương cơ bản",
        help="Lương tháng"
    )

    trang_thai = fields.Selection(
        [
            ('dang_lam', 'Đang làm việc'),
            ('nghi_viec', 'Nghỉ việc')
        ],
        default='dang_lam',
        string="Trạng thái"
    )

    # ===== Quan hệ mở rộng =====
    lich_su_cong_tac_ids = fields.One2many(
        'lich_su_cong_tac',
        'nhan_vien_id',
        string="Lịch sử công tác"
    )

    chung_chi_ids = fields.One2many(
        'chung_chi',
        'nhan_vien_id',
        string="Chứng chỉ"
    )

    cham_cong_ids = fields.One2many(
        'cham_cong',
        'nhan_vien_id',
        string="Chấm công"
    )

    # ===== Ràng buộc =====
    _sql_constraints = [
        (
            'ma_dinh_danh_unique',
            'unique(ma_dinh_danh)',
            'Mã định danh đã tồn tại!'
        )
    ]

    # ===== Hiển thị tên =====
    def name_get(self):
        return [(rec.id, f"[{rec.ma_dinh_danh}] {rec.ho_ten}") for rec in self]
