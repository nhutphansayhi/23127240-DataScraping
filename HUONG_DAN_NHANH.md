# 🚀 Hướng dẫn chạy trên Google Colab - Siêu nhanh

## Bước 1: Chuẩn bị (đã xong ✅)

File `23127240.zip` đã được tạo ở:
```
/Users/nhutphan/Desktop/testLai 2/23127240.zip
```

## Bước 2: Mở Google Colab

1. Mở trình duyệt, vào: **https://colab.research.google.com/**
2. Đăng nhập bằng Gmail của bạn
3. Click **File** → **Upload notebook**
4. Chọn file `ArXiv_Scraper_Colab.ipynb` từ folder `23127240/`

## Bước 3: Đổi Runtime sang CPU

**CỰC KỲ QUAN TRỌNG!**

1. Click **Runtime** → **Change runtime type**
2. **Hardware accelerator**: Chọn **None** (không phải GPU/TPU)
3. **Runtime shape**: Standard (hoặc High-RAM nếu bạn có Pro)
4. Click **Save**

> ⚠️ Phải dùng CPU-only vì đây là yêu cầu của bài tập!

## Bước 4: Chạy từng Cell

### Cell 1: Cài đặt dependencies
```python
!pip install arxiv==2.1.0 requests==2.31.0 pandas==2.0.3 psutil -q
```
Click nút ▶️ hoặc nhấn **Shift + Enter**

Đợi ~30 giây cho đến khi thấy "✅ Dependencies installed"

---

### Cell 2: Upload source code

Click ▶️, sẽ có nút **Choose Files** hiện ra.

**Chọn file:** `23127240.zip` (từ Desktop/testLai 2/)

Đợi upload xong (1-2 phút)

---

### Cell 3: Kiểm tra files

Click ▶️ để verify tất cả files đã được upload đúng.

Phải thấy tất cả files có dấu ✅

---

### Cell 4: Test với 3 bài báo

Click ▶️ để chạy test nhanh.

Đợi ~3-5 phút. Nếu thành công → Tiếp tục bước tiếp theo!

---

### Cell 5: Xem kết quả test

Click ▶️ để xem stats của 3 bài test.

---

## Bước 5: Chạy FULL (5000 bài) - QUAN TRỌNG!

### Option A: Chạy với config tối ưu (KHUYẾN NGHỊ) ⭐

```python
%cd /content/23127240/src

# Dùng config nhanh
!cp config_optimized.py config.py

# Chạy full
!python main.py
```

**Thời gian:** 5-6 giờ

### Option B: Chạy bình thường

Chỉ cần chạy Cell 6 trong notebook.

**Thời gian:** 10-12 giờ

---

## Bước 6: Đợi... và monitor

**Trong lúc chạy:**
- ☕ Đi làm việc khác, nhưng giữ tab Colab mở
- 💻 Laptop cần sạc hoặc pin đầy
- 🌐 Kết nối internet ổn định
- 📱 Có thể dùng điện thoại/máy khác, nhưng đừng đóng tab Colab

**Theo dõi tiến trình:**
- Có thể chạy Cell 7 (Monitor) để xem progress
- Hoặc refresh Cell 6 để xem log mới nhất

---

## Bước 7: Sau khi chạy xong

### Cell 8: Xem kết quả cuối cùng

Click ▶️ để xem tất cả metrics:
- Total time
- Success rate
- Max RAM
- Max Disk
- Average time per paper

**📋 COPY TẤT CẢ SỐ LIỆU NÀY VÀO BÁO CÁO!**

---

### Cell 12: Download tóm tắt

Click ▶️ để download file `23127240_summary.zip` (chứa JSON, CSV)

File nhỏ nên download nhanh.

---

### Cell 13: Upload lên Google Drive

**ĐÂY LÀ BƯỚC QUAN TRỌNG NHẤT!**

```python
# Cell sẽ yêu cầu connect Drive
# Click link "Connect to Google Drive"
# Chọn tài khoản Gmail
# Cho phép Colab truy cập Drive
```

Đợi 30-60 phút để copy toàn bộ data lên Drive.

Sau khi xong, vào Drive của bạn sẽ thấy folder `Lab1_ArXiv_Data`

---

## Bước 8: Nộp bài

### Trên Moodle (Code + Report):

1. **Source code:** File `23127240.zip` (cái bạn đã upload lên Colab)
2. **Report:** File Word/PDF có các metrics từ Cell 8

### Trên Google Drive (Data):

1. Vào Drive → Folder `Lab1_ArXiv_Data`
2. Click phải → Share → "Anyone with the link can view"
3. Copy link
4. Paste link vào Report hoặc comment khi nộp Moodle

---

## ⚠️ Xử lý khi gặp vấn đề

### "Colab disconnected"

**Giải pháp:**
1. Reconnect lại
2. Upload lại file zip (Cell 2)
3. Chạy lại Cell 6

Code sẽ tự động resume, skip các bài đã xong!

### "Rate limit error (429)"

**Giải pháp:**
- Đợi vài phút rồi chạy lại
- Hoặc sửa config tăng delay:
  ```python
  SEMANTIC_SCHOLAR_DELAY = 0.8  # tăng từ 0.5
  ```

### "Out of memory"

**Giải pháp:**
- Runtime → Restart runtime
- Chạy lại từ đầu
- Hoặc nâng cấp Colab Pro

---

## 💡 Tips để chạy mượt

1. **Dùng Colab Pro** nếu có thể (99k/tháng)
   - Ít disconnect
   - RAM nhiều hơn
   - Priority cao hơn

2. **Chạy vào ban đêm**
   - Ít người dùng Colab
   - Server ít load
   - Bạn có thể ngủ trong lúc đó

3. **Giữ tab mở**
   - Đừng đóng tab Colab
   - Có thể minimize hoặc chuyển sang tab khác
   - Nhưng đừng đóng hoàn toàn

4. **Kết nối ổn định**
   - Dùng Wifi nhà hoặc dây mạng
   - Tránh dùng 4G (dễ mất kết nối)

---

## 📊 Timeline ước tính

| Thời điểm | Việc làm | Thời gian |
|-----------|----------|-----------|
| 00:00 | Upload và setup | 10 phút |
| 00:10 | Bắt đầu chạy full | - |
| 06:00 | Xong! (nếu dùng config tối ưu) | 5-6 giờ |
| 06:10 | Xem results, download | 10 phút |
| 07:10 | Upload lên Drive | 30-60 phút |
| 08:00 | Hoàn thành! | ✅ |

**Tổng:** Khoảng 7-8 giờ (chủ yếu là đợi)

---

## ✅ Checklist cuối cùng

- [ ] Đã upload notebook lên Colab
- [ ] Đã đổi runtime sang CPU-only
- [ ] Đã upload source code (23127240.zip)
- [ ] Đã test với 3 bài (Cell 4)
- [ ] Đã chạy full 5000 bài (Cell 6)
- [ ] Đã copy metrics vào Report
- [ ] Đã download summary files
- [ ] Đã upload full data lên Drive
- [ ] Đã share link Drive
- [ ] Đã nộp trên Moodle

---

## 🎉 Kết luận

Nếu làm theo hướng dẫn này:
- ✅ Chạy đúng trên một Colab instance (đáp ứng requirements)
- ✅ Metrics chính xác từ môi trường chuẩn hóa
- ✅ Hoàn thành trong 5-6 giờ (hoặc 10-12 giờ nếu không optimize)
- ✅ Có đầy đủ data và statistics để nộp bài

**Chúc bạn làm bài thành công! 🚀**

---

**P/S:** Nếu gặp bất kỳ lỗi nào, đọc lại phần "Xử lý khi gặp vấn đề" hoặc xem file `HUONG_DAN_CHAY_COLAB.md` để biết chi tiết hơn.
