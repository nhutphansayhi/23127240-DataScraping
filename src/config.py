# File config - các thiết lập cơ bản
# Sinh viên: Phan Thành Nhựt - MSSV: 23127240

STUDENT_ID = "23127240"

# Phạm vi cần scrape (theo yêu cầu đề bài)
# - Tháng 11/2023: từ 2311.14685 đến 2311.18840 
# - Tháng 12/2023: từ 2312.00001 đến 2312.00844
# => Tổng: 5000 papers
START_YEAR_MONTH = "2311"
START_ID = 14685
END_YEAR_MONTH = "2312"
END_ID = 844

# Delay giữa các request để tránh bị chặn
ARXIV_API_DELAY = 3.0  # arXiv API yêu cầu tối thiểu 3 giây
SEMANTIC_SCHOLAR_DELAY = 1.1

# Retry khi bị lỗi
MAX_RETRIES = 3
RETRY_DELAY = 5.0

# Thư mục lưu dữ liệu
DATA_DIR = f"../{STUDENT_ID}_data"
LOGS_DIR = "./logs"

# Giới hạn kích thước file (100MB)
MAX_FILE_SIZE = 100 * 1024 * 1024

# API Semantic Scholar để lấy references
SEMANTIC_SCHOLAR_API_BASE = "https://api.semanticscholar.org/graph/v1"
SEMANTIC_SCHOLAR_FIELDS = "references,references.paperId,references.externalIds,references.title,references.authors,references.publicationDate,references.year"

