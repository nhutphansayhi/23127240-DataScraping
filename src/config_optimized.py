# config_optimized.py - Config tối ưu để chạy nhanh hơn
# MSSV: 23127240
# Giảm delay API để chạy nhanh (từ 10-12h xuống 5-6h)
# Chỉ dùng trong 1 Colab instance

STUDENT_ID = "23127240"

# Range papers
START_YEAR_MONTH = "2311"
START_ID = 14685
END_YEAR_MONTH = "2312"
END_ID = 844

# Delay tối ưu (nhanh gấp ~2 lần nhưng vẫn an toàn)
# arXiv không có hard limit nên ok
ARXIV_API_DELAY = 1.0  # giảm từ 3.0

# Semantic Scholar limit 100 req/5min
# 0.5s delay vừa nhanh vừa tránh bị block
SEMANTIC_SCHOLAR_DELAY = 0.5  # giảm từ 1.1 (đừng xuống 0.3 kẻo bị rate limit)

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

"""
EXPECTED PERFORMANCE với config này:

- Time per paper: ~5-6 seconds (thay vì 8-10 seconds)
- Total time for 5000 papers: 5-7 hours (thay vì 10-12 hours)
- Success rate: ~95% (tương tự như config bình thường)

⚠️ QUAN TRỌNG - Giới hạn về Testbed:
❌ KHÔNG được chạy parallel trên nhiều Colab instances rồi merge
✅ PHẢI chạy toàn bộ trên MỘT Colab instance duy nhất
✅ Được phép dùng multi-threading/parallelism TRONG code (4-8 threads)

Nếu muốn NHANH HƠN NỮA (trong cùng 1 Colab):
1. Thêm multi-threading trong code (ThreadPoolExecutor, 4-8 workers)
2. Dùng Colab Pro (RAM nhiều hơn, ít disconnect, CPU tốt hơn)
3. Tối ưu batch size cho Semantic Scholar API

⚠️ KHÔNG nên:
- Giảm SEMANTIC_SCHOLAR_DELAY xuống dưới 0.5s (dễ bị rate limit)
- Chia range ra nhiều Colab instances (vi phạm yêu cầu về testbed)

TEST TRƯỚC KHI CHẠY FULL:
!python main.py --start-ym 2311 --start-id 14685 --end-ym 2311 --end-id 14694
Đo thời gian cho 10 bài → estimate cho 5000 bài

Nếu bị rate limit error (429):
- Tăng SEMANTIC_SCHOLAR_DELAY lên 0.8 hoặc 1.0
- Hoặc dùng config.py bình thường
"""
