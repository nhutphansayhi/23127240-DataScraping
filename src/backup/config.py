# config.py - Các config cơ bản cho scraper
# MSSV: 23127240

STUDENT_ID = "23127240"

# Range papers cần scrape (theo đề Lab 1)
# Tháng 11/2023: 2311.14685 → 2311.18840 (~4156 papers)
# Tháng 12/2023: 2312.00001 → 2312.00844 (~844 papers)
# Tổng: 5000 papers
START_YEAR_MONTH = "2311"
START_ID = 14685
END_YEAR_MONTH = "2312"
END_ID = 844

# Delay giữa các API calls (tránh bị rate limit)
ARXIV_API_DELAY = 3.0  # arXiv API
SEMANTIC_SCHOLAR_DELAY = 1.1  # Semantic Scholar API

# Retry nếu API fail
MAX_RETRIES = 3
RETRY_DELAY = 5.0

# Thư mục lưu data
DATA_DIR = f"../{STUDENT_ID}_data"
LOGS_DIR = "./logs"

MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB

# Semantic Scholar API config
SEMANTIC_SCHOLAR_API_BASE = "https://api.semanticscholar.org/graph/v1"
SEMANTIC_SCHOLAR_FIELDS = "references,references.paperId,references.externalIds,references.title,references.authors,references.publicationDate,references.year"
