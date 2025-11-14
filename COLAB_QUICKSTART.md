# Chạy scraper trên Colab - Quick Guide

Tài liệu này mình viết để chia sẻ cách chạy scraper cho Lab 1 trên Google Colab.

## TL;DR (Đọc nhanh)

1. Upload notebook `ArXiv_Scraper_Colab.ipynb` lên Colab
2. Đổi runtime sang CPU only
3. Upload source code (file zip)
4. Chạy từng cell theo thứ tự
5. Đợi 3-12 giờ (tùy cách tối ưu)
6. Download kết quả về

**Muốn chạy nhanh hơn?** → Đọc phần [Tips tối ưu](#tips-nhanh)

## Files quan trọng

| File | Mô tả |
|------|-------|
| `ArXiv_Scraper_Colab.ipynb` | Notebook chính để chạy trên Colab |
| `HUONG_DAN_CHAY_COLAB.md` | Hướng dẫn chi tiết bằng tiếng Việt |
| `src/config.py` | Config bình thường (10-12 giờ) |
| `src/config_optimized.py` | Config tối ưu (3-5 giờ) ⭐ |
| `split_range.py` | Script chia range để chạy parallel |

## Cách chạy cơ bản

### 1. Chuẩn bị

```bash
# Nén source code
zip -r 23127240.zip 23127240/src 23127240/*.md 23127240/*.ipynb
```

### 2. Upload lên Colab

1. Vào https://colab.research.google.com/
2. Upload file `ArXiv_Scraper_Colab.ipynb`
3. Runtime → Change runtime type → **CPU only**
4. Làm theo hướng dẫn trong notebook

### 3. Đợi kết quả

- Chạy bình thường: 10-12 giờ
- Chạy tối ưu: 3-5 giờ
- Chạy parallel: 1-2 giờ

## Tips chạy nhanh hơn {#tips-nhanh}

### Option 1: Dùng config tối ưu (dễ nhất)

Trên Colab, sau khi upload code:

```python
# Thay config.py bằng config_optimized.py
!cp src/config_optimized.py src/config.py

# Chạy bình thường
!python main.py
```

**Kết quả:** Nhanh gấp 2-3 lần (3-5 giờ thay vì 10-12 giờ)

### Option 2: Chạy parallel nhiều Colab (nhanh nhất)

```bash
# Tạo configs cho 5 Colab instances
python3 split_range.py --num-parts 5
```

Sẽ tạo ra 5 file config khác nhau. Mở 5 tab Colab, mỗi tab dùng 1 config.

**Kết quả:** Nhanh gấp 5 lần (1-2 giờ)

**Đọc thêm:** File `parallel_configs/PARALLEL_INSTRUCTIONS.md` sau khi chạy script

### Option 3: Tweak thủ công

Sửa file `config.py`:

```python
# Giảm delays (cẩn thận với rate limits)
ARXIV_API_DELAY = 1.0          # từ 3.0
SEMANTIC_SCHOLAR_DELAY = 0.5   # từ 1.1 (đừng quá thấp, dễ bị block)
```

### Option 3: Thêm multi-threading (advanced)

Nếu biết code, có thể thêm concurrent downloads trong `main.py`:
- Dùng `ThreadPoolExecutor` với 4-8 workers
- Giảng viên confirm tối đa 4-8 threads là hiệu quả nhất

## Troubleshooting

### "Rate limit exceeded"

→ Tăng `SEMANTIC_SCHOLAR_DELAY` lên 0.5-1.0

### "Connection timeout"

→ Chạy lại, code tự động resume

### "Out of memory"

→ Restart runtime hoặc dùng Colab Pro

### "Colab disconnected"

→ Reconnect và chạy lại, nó sẽ skip các bài đã xong

## So sánh các cách chạy (trên MỘT Colab)

| Phương pháp | Thời gian | Độ khó | Hợp lệ? |
|------------|-----------|--------|---------|
| Chạy bình thường | 10-12h | ⭐ Dễ | ✅ |
| Dùng config tối ưu | 5-6h | ⭐ Dễ | ✅ **Recommend** |
| + Multi-threading | 4-5h | ⭐⭐ TB | ✅ |
| + Colab Pro | 4-5h | ⭐ Dễ | ✅ |
| ~~Nhiều Colab~~ | ~~1-2h~~ | ~~Khó~~ | ❌ **Vi phạm** |

## Tài liệu tham khảo

- `HUONG_DAN_CHAY_COLAB.md` - Hướng dẫn chi tiết bằng tiếng Việt
- `ArXiv_Scraper_Colab.ipynb` - Notebook có sẵn hướng dẫn
- `parallel_configs/PARALLEL_INSTRUCTIONS.md` - Hướng dẫn chạy parallel

## Notes từ kinh nghiệm

- ✅ Colab free cũng chạy được, nhưng dễ bị disconnect
- ✅ Colab Pro (99k/tháng) đáng để mua cho 1 tháng
- ✅ Test với 10 bài trước khi chạy full
- ✅ Luôn giữ tab Colab mở
- ⚠️ Không được skip việc chạy trên Colab (yêu cầu bắt buộc)
- ⚠️ Phải chạy đủ 5000 bài, không được chỉ chạy 100 bài

## FAQ nhanh

**Q: Bao lâu thì xong?**  
A: 5-6 giờ nếu dùng config tối ưu, 10-12 giờ nếu không tối ưu

**Q: Colab free có đủ không?**  
A: Đủ nhưng dễ disconnect, nên mua Pro (99k/tháng) nếu có thể

**Q: Bị disconnect giữa chừng thì sao?**  
A: Reconnect và chạy lại, code tự động resume từ chỗ dừng

**Q: Có cách nào chạy nhanh hơn 4-5 giờ không?**  
A: Khó! Đó đã là tối ưu trong giới hạn của một Colab instance. Không được chia ra nhiều Colab

---

Chúc bạn chạy thành công! Nếu có vấn đề gì thì đọc file `HUONG_DAN_CHAY_COLAB.md` để biết chi tiết hơn.

*Tài liệu này được viết dựa trên kinh nghiệm thực tế của sinh viên đã hoàn thành Lab 1.*
