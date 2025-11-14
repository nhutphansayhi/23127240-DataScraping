# Bắt đầu từ đây - Hướng dẫn chạy Colab cho Lab 1

Mình viết file này để tự nhắc mình (và chia sẻ cho bạn nếu cần) cách chạy scraper trên Google Colab.

## File cần dùng

- `23127240.zip` (760KB) - code đã nén sẵn
- `ArXiv_Scraper_Colab.ipynb` - notebook để chạy trên Colab  
- `HUONG_DAN_NHANH.md` - nếu cần đọc kỹ hơn
- `CHECKLIST.md` - để check từng bước

## 3 bước chính:

### BƯỚC 1: Mở Colab (2 phút)

1. Mở Chrome/Firefox
2. Vào: **https://colab.research.google.com/**
3. Đăng nhập Gmail
4. **File** → **Upload notebook**
5. Chọn file: `ArXiv_Scraper_Colab.ipynb` (từ folder này)

### BƯỚC 2: Đổi sang CPU (30 giây)

1. **Runtime** → **Change runtime type**
2. Chọn **Hardware accelerator: None**
3. Click **Save**

### BƯỚC 3: Làm theo Notebook (5-12 giờ)

Notebook có 14 cells, mỗi cell có hướng dẫn rõ ràng.

**Chỉ cần:**
- Click ▶️ ở mỗi cell
- Đọc hướng dẫn
- Làm theo

**Quan trọng nhất:**
- Cell 2: Upload file `23127240.zip` (760KB)
- Cell 6: Chạy full scraper (đợi 5-12 giờ)
- Cell 13: Upload lên Drive (30-60 phút)

## Timeline ước tính

| Thời gian | Việc |
|-----------|------|
| 0:00 | Bắt đầu |
| 0:10 | Upload code xong, test |
| 0:15 | Chạy full |
| 5-12h sau | Xong |
| +1h | Upload Drive |

## Tips từ kinh nghiệm

**1. Để chạy nhanh hơn:**

Trong Cell 6, thêm dòng này trước khi chạy:
```python
!cp src/config_optimized.py src/config.py
```
Sẽ giảm từ 10-12h xuống còn 5-6h.

**2. Giữ tab Colab mở**

Đừng đóng tab. Minimize hay chuyển tab khác ok, nhưng đừng tắt.

**3. Chạy ban đêm**

Mình hay bật lúc 10-11 giờ tối, đi ngủ, sáng dậy xong.

**4. Nếu bị disconnect**

Không sao, reconnect lại, upload code và chạy lại Cell 6. Code tự skip các bài đã xong rồi.

## Mấy thắc mắc hay gặp

**Mất bao lâu?**  
Khoảng 5-6 giờ nếu dùng config tối ưu, hoặc 10-12 giờ nếu không optimize.

**Có cần ngồi canh không?**  
Không, chỉ cần giữ tab mở. Có thể làm việc khác bình thường.

**Nếu bị disconnect thì sao?**  
Reconnect lại, upload code và chạy lại Cell 6. Code tự động skip các bài đã làm rồi.

**Colab free có đủ không?**  
Đủ nhưng dễ bị disconnect. Mình nghĩ nên mua Pro 99k cho chắc.

**Làm sao biết xong?**  
Thấy dòng "SCRAPING COMPLETED!" là xong.

## Kết quả cuối cùng

Sau khi xong sẽ có:
- Full data 5000 papers trên Drive
- File stats (JSON, CSV)  
- Metrics để điền Report
- Code để nộp Moodle

## Lưu ý quan trọng

Theo yêu cầu đề bài:
- Phải chạy trên 1 Colab duy nhất (không được chia nhiều Colab)
- Được phép optimize trong code (giảm delay, dùng batch API)

## Nếu gặp lỗi

1. Đọc lại file HUONG_DAN_NHANH.md
2. Google error message
3. Hỏi bạn cùng lớp hoặc trợ giảng

---

## Tóm lại

3 việc cần làm:
1. Mở Colab → Upload notebook
2. Đổi sang CPU 
3. Click run từng cell

Notebook có hướng dẫn rõ từng bước rồi.

---

**MSSV: 23127240**

*Note: Nên bắt đầu sớm để có thời gian xử lý nếu có vấn đề.*
