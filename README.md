# arXiv Paper Scraper - Lab 1

Đây là bài Lab 1 của mình (MSSV: 23127240) môn Nhập môn Khoa học Dữ liệu.

## Thông tin bài tập

**MSSV:** 23127240  
**Paper range:** 2311.14685 đến 2312.00844 (5000 papers)  
**Môn:** Introduction to Data Science - Lab 1

## Chức năng chính

Project này scrape papers từ arXiv bao gồm:
- Download full TeX source (tất cả versions: v1, v2, v3...)
- Xóa figures trong TeX files
- Tạo metadata file (JSON)
- Tạo BibTeX references
- Crawl citations từ Semantic Scholar API
- Filter chỉ lấy references có arXiv ID

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

## Chạy scraper

### Chạy cơ bản

```bash
python main.py
```

Sẽ scrape từ 2311.14685 đến 2312.00844 (config mặc định).

### Tùy chỉnh range

```bash
python main.py --start-ym 2311 --start-id 14685 --end-ym 2312 --end-id 843
```

### Arguments

- `--start-ym`: Tháng bắt đầu (YYMM, vd: "2311")
- `--start-id`: ID bắt đầu (vd: 14685)
- `--end-ym`: Tháng kết thúc (YYMM, vd: "2312")
- `--end-id`: ID kết thúc (vd: 843)
- `--output`: Thư mục output (mặc định: `../23127240_data`)

### Ví dụ

```bash
# Chạy full
python main.py

# Chạy 1 range nhỏ
python main.py --start-ym 2311 --start-id 14685 --end-ym 2311 --end-id 14690
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

