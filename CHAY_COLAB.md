# 🚀 Hướng Dẫn Chạy Trên Google Colab

## Bước 1: Mở Google Colab
Vào: https://colab.research.google.com/

## Bước 2: Tạo Notebook Mới & Copy Code

### Cell 1: Clone Repository
```python
!git clone https://github.com/nhutphansayhi/23127240-DataScraping.git
%cd 23127240-DataScraping/src
```

### Cell 2: Cài Đặt Packages
```python
!pip install requests arxiv bibtexparser psutil feedparser
```

### Cell 3: Chạy Scraper (Test 55 Papers - Sẽ Thấy Batch Report Ở Paper 50)
```python
!python main.py --start-id 14685 --end-id 14739
```

**HOẶC** chạy đủ 5000 papers:
```python
!python main.py
```

## 📊 Xem Kết Quả

### Cell 4: Xem Stats
```python
import json
with open('../23127240_data/scraping_stats.json') as f:
    stats = json.load(f)
    print(json.dumps(stats, indent=2))
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

## ⚡ Lưu Ý Quan Trọng:

1. **Runtime**: Chọn `Runtime > Change runtime type > T4 GPU` (nhanh hơn, miễn phí)
2. **Batch Report**: Code sẽ in báo cáo 15 metrics **MỖI 50 PAPERS** 
3. **Checkpoint**: Nếu bị ngắt, chạy lại Cell 3 - nó sẽ tự động skip papers đã scrape
4. **Time Limit**: Colab free chỉ chạy 12h liên tục. Với 5000 papers (~10-15s/paper) cần ~14-20 giờ
   - Nên chạy từng batch: 
     - Batch 1: `--start-id 14685 --end-id 14934` (250 papers)
     - Batch 2: `--start-id 14935 --end-id 15184` (250 papers)
     - ...

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
