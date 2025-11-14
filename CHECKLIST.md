# ✓ CHECKLIST CHẠY COLAB - In ra hoặc mở trên điện thoại

## TRƯỚC KHI BẮT ĐẦU
- [ ] File 23127240.zip đã có ở Desktop/testLai 2/
- [ ] Đã đọc hướng dẫn một lượt
- [ ] Có 6-12 giờ rảnh (hoặc chạy qua đêm)
- [ ] Internet ổn định

## BƯỚC 1: MỞ COLAB
- [ ] Vào https://colab.research.google.com/
- [ ] Đăng nhập Gmail
- [ ] File → Upload notebook
- [ ] Chọn ArXiv_Scraper_Colab.ipynb

## BƯỚC 2: ĐỔI RUNTIME
- [ ] Runtime → Change runtime type
- [ ] Hardware accelerator: **None** (CPU only)
- [ ] Save

## BƯỚC 3: CHẠY CÁC CELL

### Cell 1: Cài packages
- [ ] Click ▶️
- [ ] Đợi thấy "✅ Dependencies installed"

### Cell 2: Upload code
- [ ] Click ▶️
- [ ] Chọn file 23127240.zip
- [ ] Đợi upload xong

### Cell 3: Verify
- [ ] Click ▶️
- [ ] Thấy tất cả ✅

### Cell 4: Test 3 bài
- [ ] Click ▶️
- [ ] Đợi 3-5 phút
- [ ] Thành công → Tiếp tục

### Cell 5: Xem test results
- [ ] Click ▶️
- [ ] Check có data

## BƯỚC 4: CHẠY FULL (QUAN TRỌNG!)

### Nếu muốn NHANH (5-6 giờ):
```python
%cd /content/23127240/src
!cp config_optimized.py config.py
!python main.py
```

### Hoặc chạy bình thường (10-12 giờ):
- [ ] Click ▶️ ở Cell 6

### Sau khi bắt đầu:
- [ ] ✓ Tab Colab đang mở
- [ ] ✓ Laptop có sạc
- [ ] ✓ Internet ổn định
- [ ] ✓ Ghi lại thời gian bắt đầu: __:__

## BƯỚC 5: ĐỢI... (5-12 GIỜ)

Có thể làm:
- [ ] Đi ngủ / làm việc khác
- [ ] Check progress mỗi 1-2 giờ
- [ ] Chạy Cell 7 để monitor (optional)

Lưu ý:
- [ ] ⚠️ ĐỪNG đóng tab Colab
- [ ] ⚠️ ĐỪNG tắt máy/laptop

## BƯỚC 6: SAU KHI XONG

Dấu hiệu xong:
- [ ] Thấy "✅ SCRAPING COMPLETED!"
- [ ] Không còn log chạy nữa

### Cell 8: Xem results
- [ ] Click ▶️
- [ ] Copy các số liệu:
  - Total time: _____ giờ
  - Success rate: _____ %
  - Max RAM: _____ MB
  - Max Disk: _____ GB
  - Avg time/paper: _____ giây

### Cell 12: Download summary
- [ ] Click ▶️
- [ ] Download file summary.zip
- [ ] Lưu vào máy

### Cell 13: Upload lên Drive
- [ ] Click ▶️
- [ ] Connect to Google Drive
- [ ] Cho phép access
- [ ] Đợi 30-60 phút upload
- [ ] Check Drive có folder Lab1_ArXiv_Data

## BƯỚC 7: NỘP BÀI

### Trên Moodle:
- [ ] Upload 23127240.zip (source code)
- [ ] Upload Report.docx (có metrics đã copy)

### Link Google Drive:
- [ ] Vào Drive/Lab1_ArXiv_Data
- [ ] Share → Anyone with link → Copy link
- [ ] Paste vào Report hoặc comment

## BƯỚC 8: XÁC NHẬN

- [ ] Đã nộp đủ files trên Moodle
- [ ] Link Drive accessible
- [ ] Report có đủ metrics
- [ ] Code chạy được trên Colab

## ✅ HOÀN THÀNH!

---

## NẾU BỊ DISCONNECT:

- [ ] Reconnect Colab
- [ ] Upload lại zip (Cell 2)
- [ ] Chạy lại Cell 6
- [ ] Code tự động resume!

---

## NẾU CÓ LỖI:

| Lỗi | Giải pháp |
|-----|-----------|
| Rate limit 429 | Đợi 5 phút, chạy lại |
| Out of memory | Restart runtime |
| Module not found | Chạy lại Cell 1 |
| File not found | Check Cell 2, upload lại |

---

**Thời gian bắt đầu:** __:__ ngày __/__/2025
**Dự kiến xong:** __:__ ngày __/__/2025
**Thực tế xong:** __:__ ngày __/__/2025

**Tổng thời gian:** _____ giờ

---

📱 **Tip:** Chụp màn hình checklist này để theo dõi!
