# Bài Tập Lớn: Thu Thập Dữ Liệu từ arXiv

Em làm bài Lab 1 môn Nhập môn Khoa học Dữ liệu.

**Sinh viên:** Phan Thành Nhựt  
**MSSV:** 23127240  
**Lớp:** Nhập môn Khoa học Dữ liệu  

**Phạm vi scrape:** 5000 papers từ 2311.14685 đến 2312.00844

## Mô tả

Bài này em làm scraper để tự động tải papers từ arXiv, bao gồm:
- Tải source code TeX (cả các version khác nhau: v1, v2, v3...)
- Xóa hình ảnh trong file TeX để giảm dung lượng
- Lưu thông tin metadata dạng JSON
- Tạo file BibTeX cho references
- Lấy thông tin citations từ Semantic Scholar
- Chỉ giữ lại references có arXiv ID

## Cách chạy

### Yêu cầu

- Python 3.8+
- pip
- Internet để gọi API

### Cài đặt

1. **Extract project**
   ```bash
   cd 23127240
   ```

2. **Tạo virtual environment (nên làm)**
   ```bash
   python -m venv venv
   
   # Windows:
   venv\Scripts\activate
   
   # Mac/Linux:
   source venv/bin/activate
   ```

3. **Cài packages**
   ```bash
   cd src
   pip install -r requirements.txt
   ```

## Cách chạy

### Chạy scraper

```bash
cd src
python main.py
```

Mặc định sẽ chạy từ 2311.14685 đến 2312.00844 (theo config).

### Chạy với range tùy chỉnh

```bash
python main.py --start-ym 2311 --start-id 14685 --end-ym 2311 --end-id 14700
```

**Các tham số:**
- `--start-ym`: Tháng bắt đầu (dạng YYMM, ví dụ: 2311)
- `--start-id`: Số ID bắt đầu
- `--end-ym`: Tháng kết thúc
- `--end-id`: Số ID kết thúc
- `--output`: Folder lưu kết quả (mặc định là `../23127240_data`)

**Ví dụ:**

```bash
# Chạy toàn bộ 5000 papers
python main.py

# Test với vài papers đầu
python main.py --start-id 14685 --end-id 14690
```

## Output Structure

The scraper creates the following directory structure:

```
23127240_data/
├── 2311-14685/
│   ├── tex/
│   │   ├── v1/
│   │   ├── v2/
│   │   └── ...
│   ├── metadata.json
│   ├── references.bib
│   └── references.json
├── 2311-14686/
│   └── ...
└── scraping_stats.json   # Overall scraping statistics
```

### File Descriptions

1. **tex/** - Contains all versions of the paper's TeX source files with figures removed
2. **metadata.json** - Paper metadata including title, authors, submission date, revised dates, abstract, categories, DOI, journal reference
3. **references.bib** - BibTeX entry for the paper
4. **references.json** - Dictionary of references that have arXiv IDs with metadata

## Processing Details

### Figure Removal

The scraper automatically removes figures from TeX files to reduce storage size by removing `\includegraphics` commands, `\begin{figure}...\end{figure}` environments, and deleting image files.

### API Rate Limits

The scraper respects API rate limits with 3 seconds delay between arXiv requests and 1.1 seconds delay between Semantic Scholar requests.

### Error Handling

Automatic retry up to 3 attempts for failed requests, graceful handling of missing papers, and detailed logging of all operations.

## Logging

Logs are saved to `logs/scraper.log` with progress updates, download status, error messages, and performance statistics.

## Statistics Tracking

The scraper tracks comprehensive statistics as required:

### Data Statistics
- Number of papers scraped successfully
- Overall success rate
- Average paper size before and after removing figures
- Average number of references per paper
- Average success rate for scraping reference metadata

### Performance Metrics

#### Running Time
- Total runtime (wall time)
- Entry discovery time
- Average time to process each paper
- Total paper processing time

#### Memory Footprint
- Maximum RAM used during scraping
- Average RAM consumption
- Maximum disk storage required
- Final output storage size

All statistics are saved to `scraping_stats.json` in the output directory.

## Performance Notes

- **Runtime**: Approximately 10-15 seconds per paper
- **Storage**: Each paper typically uses 50-500 KB after figure removal
- **Memory**: Peak usage around 200-300 MB

## Troubleshooting

### Common Issues

1. **"Paper not found" errors** - Some arXiv IDs may not exist, scraper continues with other papers
2. **Rate limit errors** - Automatically handled with delays
3. **Connection timeouts** - Automatic retry for failed requests
4. **Import errors** - Ensure all packages installed: `pip install -r requirements.txt`

### Testing on Google Colab

To run the scraper on Google Colab:

```python
!pip install arxiv requests sickle pandas psutil

!python main.py
```

## System Requirements

- **Python**: 3.8 or higher
- **Disk Space**: At least 1 GB free
- **RAM**: Minimum 2 GB recommended
- **Network**: Stable internet connection

## License

This project is created for educational purposes as part of the Introduction to Data Science course.

## Contact

**Student ID:** 23127240

