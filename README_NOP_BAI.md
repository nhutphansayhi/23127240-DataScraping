# Lab 1 - arXiv Paper Scraper

**MSSV:** 23127240  
**Họ tên:** [Điền tên của bạn]  
**Lớp:** [Điền lớp của bạn]

---

## Files nộp

### Trên Moodle:
1. **Source code:** `23127240.zip` (file này)
2. **Report:** `Report_23127240.docx` (hoặc PDF)

### Trên Google Drive:
- Link: [Paste link Drive ở đây]
- Chứa folder `Lab1_ArXiv_Data` với full data 5000 papers

---

## Hướng dẫn chạy

### Cách 1: Chạy trên Google Colab (recommend)

**File:** `ArXiv_Scraper_Colab.ipynb`

**Bước:**
1. Upload notebook lên Colab
2. Đổi runtime sang CPU (Hardware accelerator: None)
3. Follow hướng dẫn trong notebook
4. Đợi 5-12 giờ tùy config

**Xem thêm:** `BAT_DAU_O_DAY.md` hoặc `HUONG_DAN_NHANH.md`

### Cách 2: Chạy trên máy local

```bash
cd 23127240/src
pip install -r requirements.txt
python main.py
```

---

## Kết quả

Sau khi chạy xong trên Colab:

### Metrics (copy từ Cell 8):
- **Total runtime:** _____ giờ
- **Success rate:** _____ %
- **Max RAM used:** _____ MB
- **Max disk used:** _____ GB
- **Avg time per paper:** _____ giây
- **Total papers scraped:** _____/5000

### Files output:
- `scraping_stats.json` - Statistics tổng hợp
- `paper_details.csv` - Chi tiết từng paper
- `2311-14685/` đến `2312-00844/` - Folders chứa papers

---

## Cấu trúc project

```
23127240/
├── src/
│   ├── main.py                       # File chính để chạy
│   ├── arxiv_scraper.py              # Scrape arXiv papers
│   ├── reference_scraper.py          # Scrape references
│   ├── reference_scraper_optimized.py # Batch API (nhanh hơn)
│   ├── bibtex_generator.py           # Tạo BibTeX
│   ├── utils.py                      # Helper functions
│   ├── config.py                     # Config bình thường
│   ├── config_optimized.py           # Config tối ưu (5-6h)
│   └── requirements.txt              # Dependencies
│
├── ArXiv_Scraper_Colab.ipynb         # Notebook để chạy Colab
├── README.md                         # File này
├── BAT_DAU_O_DAY.md                  # Quick start
└── HUONG_DAN_NHANH.md                # Hướng dẫn chi tiết
```

---

## Tối ưu đã làm

1. **Batch API**: Dùng Semantic Scholar batch API (query 500 papers cùng lúc)
2. **Giảm delays**: API delays từ 3.0s → 1.0s (arXiv), 1.1s → 0.5s (Semantic Scholar)
3. **Resume support**: Tự động skip papers đã scrape nếu bị disconnect
4. **Efficient downloads**: Concurrent downloads cho nhiều versions

**Kết quả:** Giảm từ 10-12 giờ xuống còn 5-6 giờ

---

## Lưu ý

- Testbed: Google Colab CPU-only (theo yêu cầu đề bài)
- Phải chạy trên 1 Colab instance duy nhất (không được chia nhiều Colab)
- Metrics đo từ môi trường Colab

---

## Troubleshooting

**Nếu bị disconnect:**
- Reconnect Colab
- Upload lại code
- Chạy lại cell, code tự động resume

**Nếu bị rate limit:**
- Tăng delay trong config.py
- Hoặc dùng config bình thường thay vì config_optimized

**Nếu out of memory:**
- Restart runtime
- Hoặc dùng Colab Pro

---

## Tham khảo

- arXiv API: https://info.arxiv.org/help/api/index.html
- Semantic Scholar API: https://www.semanticscholar.org/product/api
- Google Colab: https://colab.research.google.com/

---

**Ngày nộp:** [Điền ngày nộp]  
**Thời gian hoàn thành:** [Điền thời gian chạy thực tế]

---

*Note: File này là part of submission package. Các file markdown khác (HUONG_DAN_*.md) là notes để tự nhắc mình cách chạy.*
