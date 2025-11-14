# Hướng Dẫn Chạy Code Trên Google Colab

Vì máy cá nhân không đủ mạnh nên em chạy trên Colab cho nhanh.

## Bước 1: Mở Colab
Vào trang: https://colab.research.google.com/

## Bước 2: Tạo Notebook mới và copy code dưới đây

### Cell 1: Clone code từ GitHub về
```python
!git clone https://github.com/nhutphansayhi/23127240-DataScraping.git
%cd 23127240-DataScraping/src
```

### Cell 2: Cài thư viện cần thiết
```python
!pip install requests arxiv bibtexparser psutil feedparser
```

### Cell 3: Chạy scraper

**Test với 55 papers (để xem báo cáo ở paper thứ 50):**
```python
!python main.py --start-id 14685 --end-id 14739
```

**Hoặc chạy luôn cả 5000 papers (mất ~14-20 giờ):**
```python
!python main.py
```

## Xem kết quả

### Cell 4: Xem thống kê
```python
import json
with open('../23127240_data/scraping_stats.json') as f:
    data = json.load(f)
    print(json.dumps(data, indent=2))
```

### Cell 5: Xem Paper Details CSV
```python
import pandas as pd
df = pd.read_csv('../23127240_data/paper_details.csv')
print(df.head(20))
print(f"\nTotal papers: {len(df)}")
print(f"Success rate: {df['success'].mean()*100:.2f}%")
```

### Cell 6: Download Kết Quả (Zip All Data)
```python
!cd .. && zip -r 23127240_results.zip 23127240_data/
from google.colab import files
files.download('../23127240_results.zip')
```

## ⚡ Lưu ý quan trọng:

1. **Chọn Runtime tốt hơn**: `Runtime > Change runtime type > T4 GPU` (miễn phí và nhanh)
2. **Báo cáo tự động**: Code sẽ in báo cáo 15 metrics **MỖI 50 PAPERS**
3. **Tự động resume**: Nếu bị ngắt giữa chừng, chạy lại Cell 3 - nó sẽ tự skip papers đã scrape xong
4. **Thời gian**: 
   - Code dùng batch scraper (6 luồng) nên **~8-10 giây/paper**
   - 5000 papers = **~11-14 giờ** (Colab free giới hạn 12h)
   - **Nên chạy từng batch ~3-4 giờ:**
     ```python
     # Batch 1: ~1500 papers (~3-4h)
     !python main.py --start-id 14685 --end-id 16184
     
     # Batch 2: ~1500 papers (~3-4h) 
     !python main.py --start-id 16185 --end-id 17684
     
     # Batch 3: ~2000 papers còn lại (~4-5h)
     !python main.py --start-id 17685 --end-id 844
     ```

## 📝 Ví Dụ Batch Report Mỗi 50 Papers:

```
╔══════════════════════════════════════════════════════════════════╗
║               BATCH REPORT: PAPER 50 / 250                       ║
╠══════════════════════════════════════════════════════════════════╣
║ I. DATA STATISTICS                                               ║
║ ---------------------------------------------------------------- ║
║ 📄 Papers scraped successfully     : 48                          ║
║ ✅ Overall success rate            : 96.00%                      ║
║ 📦 Avg paper size (before)         : 156.4 KB                   ║
║ 📦 Avg paper size (after)          : 89.2 KB                    ║
║ 📚 Avg references per paper        : 24.5                        ║
║ ✅ Reference metadata success      : 89.23%                      ║
║                                                                  ║
║ II. SCRAPER PERFORMANCE                                          ║
║ ---------------------------------------------------------------- ║
║ A. Running Time                                                  ║
║ ⏱️  Total wall time                : 8.5 min                     ║
║ ⏱️  Avg time per paper             : 10.2s                       ║
║ ⏱️  Total time per paper           : 10.2s                       ║
║ 🔍 Entry discovery time            : 0.15s                       ║
║                                                                  ║
║ B. Memory Footprint                                              ║
║ 💾 Maximum RAM used                : 256 MB                      ║
║ 💾 Maximum disk storage            : 8.9 MB                      ║
║ 💾 Final output storage            : 8.2 MB                      ║
║ 💾 Average RAM consumption         : 189 MB                      ║
╚══════════════════════════════════════════════════════════════════╝
```

## 🎯 File Nộp Bài:

- `23127240.zip` - Source code (đã có sẵn trong repo)
- `23127240_results.zip` - Kết quả scrape (download từ Cell 6)
- Link GitHub: https://github.com/nhutphansayhi/23127240-DataScraping

---
**MSSV: 23127240**
