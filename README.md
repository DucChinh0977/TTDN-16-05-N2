# 📌 HỆ THỐNG QUẢN LÝ DOANH NGHIỆP TRÊN ODOO  
**(Quản lý Nhân sự – Quản lý Công việc – Quản lý Khách hàng)**

<p align="center">
  <img src="https://img.shields.io/badge/Ubuntu-22.04-E95420?style=for-the-badge&logo=ubuntu&logoColor=white" />
  <img src="https://img.shields.io/badge/github-%23181717.svg?style=for-the-badge&logo=github&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-14-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" />
  <img src="https://img.shields.io/badge/Odoo-15%2F16-purple.svg" />
</p>

---

## 📖 Giới thiệu

Dự án được xây dựng trên nền tảng **Odoo**, nhằm mục tiêu phát triển một hệ thống quản lý doanh nghiệp bao gồm:

- 👤 **Quản lý Nhân sự**
- 📋 **Quản lý Công việc / Dự án**
- 🤝 **Quản lý Khách hàng**
- 📊 Theo dõi tiến độ, nhật ký công việc, đánh giá nhân viên

Phục vụ mục đích **học tập – đồ án học phần – thực tập doanh nghiệp**.

---

## 1️ Cài đặt môi trường & công cụ

### 1.1. Clone project từ GitHub

```bash
git clone https://github.com/DucChinh0977/TTDN-16-05-N2.git
cd TTDN-16-05-N2
```

### 1.2. Cài đặt thư viện hệ thống (Ubuntu 22.04)
sudo apt update
sudo apt install -y \
    git python3.10 python3.10-dev python3.10-venv \
    build-essential libssl-dev libffi-dev \
    libxml2-dev libxslt1-dev libldap2-dev \
    libsasl2-dev libpq-dev zlib1g-dev

### 1.3. Khởi tạo môi trường ảo Python
python3.10 -m venv venv
source venv/bin/activate

Cài đặt thư viện Python:

pip install -r requirements.txt

## 2️ Thiết lập cơ sở dữ liệu PostgreSQL
### 2.1. Chạy PostgreSQL bằng Docker
docker-compose up -d

Kiểm tra container:

docker ps

## 3️ Cấu hình Odoo
### 3.1. Tạo file odoo.conf

Tạo file odoo.conf tại thư mục gốc:

[options]
addons_path = addons
db_host = localhost
db_port = 5432
db_user = odoo
db_password = odoo
xmlrpc_port = 8069

### 3.2. Một số tham số chạy Odoo
-c <đường_dẫn_odoo.conf>     # Chỉ định file config
-d <tên_database>            # Database sử dụng
-u <tên_module>              # Update module
--dev=all                    # Bật developer mode

## 4️ Chạy hệ thống
source venv/bin/activate
python odoo-bin -c odoo.conf

Truy cập trình duyệt:

👉 http://localhost:8069

## 5️ Các module chính

📦 quan_ly_nhan_su – Quản lý nhân viên

📦 quan_ly_cong_viec – Quản lý dự án, công việc, nhật ký

📦 quan_ly_khach_hang – Quản lý khách hàng

## 6 POSTER:

<p align="center">
  <img src="/Slide1.PNG" width="800"/>
</p>

## END.



