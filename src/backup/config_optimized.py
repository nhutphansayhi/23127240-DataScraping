
STUDENT_ID = "23127240"

# Paper range for Lab 1
START_YEAR_MONTH = "2311"
START_ID = 14685
END_YEAR_MONTH = "2312"
END_ID = 844

# ⚡ OPTIMIZED DELAYS (nhanh gấp ~2 lần, an toàn hơn)
# arXiv API không có hard limit, 1.0s là an toàn
ARXIV_API_DELAY = 1.0  # Giảm từ 3.0

# Semantic Scholar cho phép 100 req/5min
# 0.5s là balance tốt giữa tốc độ và tránh rate limit
SEMANTIC_SCHOLAR_DELAY = 0.5  # Giảm từ 1.1 (cẩn thận nếu xuống 0.3)

# Retry settings
MAX_RETRIES = 3
RETRY_DELAY = 5.0

# Paths
DATA_DIR = f"../{STUDENT_ID}_data"
LOGS_DIR = "./logs"

# File size limit
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB

# Semantic Scholar API
SEMANTIC_SCHOLAR_API_BASE = "https://api.semanticscholar.org/graph/v1"
SEMANTIC_SCHOLAR_FIELDS = "references,references.paperId,references.externalIds,references.title,references.authors,references.publicationDate,references.year"

# ⚡ BATCH SIZE for optimized scraper
# Càng lớn càng nhanh, nhưng 500 là optimal
BATCH_SIZE = 500

# Optional: Skip papers without source (saves time)
# Chỉ bật nếu requirements cho phép
SKIP_PAPERS_WITHOUT_SOURCE = False

# Optional: Skip figure removal (saves time)
# Chỉ bật nếu không bắt buộc phải xóa figure
SKIP_FIGURE_REMOVAL = False
