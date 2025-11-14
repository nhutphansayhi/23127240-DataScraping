#!/usr/bin/env python3
"""
⚠️⚠️⚠️ WARNING - KHÔNG DÙNG SCRIPT NÀY CHO SUBMISSION! ⚠️⚠️⚠️

Script này chia paper range để chạy parallel trên NHIỀU Colab instances,
nhưng điều này VI PHẠM yêu cầu của Lab 1!

YÊU CẦU CHÍNH THỨC:
- Testbed phải là "a Google Colab instance" (MỘT instance duy nhất)
- Metrics phải đo từ toàn bộ hệ thống chạy trong một môi trường chuẩn hóa

SCRIPT NÀY CHỈ DÙNG ĐỂ:
- Development/testing trên máy local
- Hiểu cách chia range
- Learning purposes

KHÔNG DÙNG CHO:
- Final submission
- Benchmarking performance metrics
- Nộp bài Lab 1

Usage (chỉ cho development):
    python split_range.py --num-parts 5
"""

import argparse
from pathlib import Path


def parse_range(start_ym, start_id, end_ym, end_id):
    """Chuyển range thành list các paper IDs"""
    papers = []
    
    # Xử lý month đầu
    current_ym = int(start_ym)
    current_id = start_id
    
    while current_ym < int(end_ym):
        # Giả sử mỗi tháng có tầm 20000 papers (estimate)
        # Thực tế có thể ít hơn
        max_id = 20000
        while current_id <= max_id:
            papers.append((str(current_ym), current_id))
            current_id += 1
        
        # Sang tháng mới
        if len(str(current_ym)) == 4:
            year = current_ym // 100
            month = current_ym % 100
            if month == 12:
                current_ym = (year + 1) * 100 + 1
            else:
                current_ym = year * 100 + (month + 1)
        
        current_id = 1
    
    # Xử lý month cuối
    while current_id <= end_id:
        papers.append((str(current_ym), current_id))
        current_id += 1
    
    return papers


def simple_split(start_ym, start_id, end_ym, end_id, num_parts):
    """
    Chia range đơn giản dựa trên số lượng
    Đơn giản hơn và chính xác hơn cho case này
    """
    # Tính tổng số papers (estimate)
    start_val = int(start_ym) * 100000 + start_id
    end_val = int(end_ym) * 100000 + end_id
    total_papers = end_val - start_val + 1
    
    papers_per_part = total_papers // num_parts
    
    ranges = []
    current_start = start_val
    
    for i in range(num_parts):
        if i == num_parts - 1:
            # Phần cuối lấy hết
            current_end = end_val
        else:
            current_end = current_start + papers_per_part - 1
        
        # Convert back to ym and id
        start_ym_part = str(current_start // 100000)
        start_id_part = current_start % 100000
        end_ym_part = str(current_end // 100000)
        end_id_part = current_end % 100000
        
        ranges.append({
            'start_ym': start_ym_part,
            'start_id': start_id_part,
            'end_ym': end_ym_part,
            'end_id': end_id_part,
            'estimate_papers': papers_per_part if i < num_parts - 1 else (end_val - current_start + 1)
        })
        
        current_start = current_end + 1
    
    return ranges


def generate_config_file(part_num, range_info, output_dir, student_id):
    """Tạo file config cho 1 part"""
    
    config_content = f'''"""
Configuration for Part {part_num}
Generated for parallel Colab execution
"""

STUDENT_ID = "{student_id}"

# Paper range for this part
START_YEAR_MONTH = "{range_info['start_ym']}"
START_ID = {range_info['start_id']}
END_YEAR_MONTH = "{range_info['end_ym']}"
END_ID = {range_info['end_id']}

# Optimized delays for faster scraping
ARXIV_API_DELAY = 1.0
SEMANTIC_SCHOLAR_DELAY = 0.3

MAX_RETRIES = 3
RETRY_DELAY = 5.0

DATA_DIR = f"../{student_id}_data_part{part_num}"
LOGS_DIR = "./logs"

MAX_FILE_SIZE = 100 * 1024 * 1024

SEMANTIC_SCHOLAR_API_BASE = "https://api.semanticscholar.org/graph/v1"
SEMANTIC_SCHOLAR_FIELDS = "references,references.paperId,references.externalIds,references.title,references.authors,references.publicationDate,references.year"
'''
    
    output_file = output_dir / f"config_part{part_num}.py"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(config_content)
    
    return output_file


def generate_instructions(ranges, output_dir):
    """Tạo file hướng dẫn sử dụng"""
    
    instructions = '''# HƯỚNG DẪN CHẠY PARALLEL TRÊN NHIỀU COLAB

## Bạn đã chia range thành {} phần!

'''.format(len(ranges))
    
    instructions += "## Chi tiết từng phần:\n\n"
    for i, r in enumerate(ranges, 1):
        instructions += f"**Part {i}:**\n"
        instructions += f"- Range: {r['start_ym']}.{r['start_id']} → {r['end_ym']}.{r['end_id']}\n"
        instructions += f"- Estimate: ~{r['estimate_papers']} papers\n"
        instructions += f"- Config file: `config_part{i}.py`\n\n"
    
    instructions += '''
## Cách sử dụng:

### Bước 1: Chuẩn bị {} Colab notebooks

1. Mở {} tab Colab khác nhau
2. Upload source code vào mỗi tab
3. Ở mỗi tab, replace file `config.py` bằng file `config_part{}.py` tương ứng

### Bước 2: Chạy đồng thời

Chạy tất cả {} Colab cùng lúc!

**Ví dụ với Part 1:**
```python
# Trên Colab, sau khi upload code
%cd /content/23127240/src

# Copy config của part này
!cp config_part1.py config.py

# Chạy
!python main.py
```

Làm tương tự cho các part khác.

### Bước 3: Merge kết quả

Sau khi tất cả các part chạy xong:

1. Download data từ mỗi Colab về (hoặc copy sang Drive)
2. Merge vào 1 folder:
   ```bash
   mkdir merged_data
   cp -r part1_data/* merged_data/
   cp -r part2_data/* merged_data/
   cp -r part3_data/* merged_data/
   # ... tiếp tục
   ```

3. Merge statistics:
   - Mở file `scraping_stats.json` của mỗi part
   - Cộng các số liệu lại
   - Tạo file stats tổng hợp

### Ước tính thời gian:

- Mỗi part chạy độc lập: ~{} giờ
- Chạy đồng thời {} part: **tổng cộng ~{} giờ**
- So với chạy tuần tự: Nhanh gấp **{}x**!

### Lưu ý:

- ⚠️ Phải cẩn thận khi merge data
- ⚠️ Đảm bảo không có paper bị trùng hoặc thiếu
- ⚠️ Tính toán lại statistics tổng hợp
- ✅ Nên dùng cách này nếu deadline gấp
- ✅ Cần nhiều tabs/windows để quản lý

## Tips:

1. **Đánh dấu rõ ràng:** Đặt tên mỗi Colab tab là "Part 1", "Part 2", v.v.
2. **Monitor progress:** Check định kỳ mỗi tab
3. **Backup:** Download data ngay khi xong, đừng để Colab disconnect
4. **Network:** Đảm bảo internet ổn định cho tất cả tabs

Chúc bạn scrape thành công! 🚀
'''.format(
        len(ranges), len(ranges), len(ranges),
        len(ranges), 
        10 / len(ranges), len(ranges), 10 / len(ranges), len(ranges)
    )
    
    output_file = output_dir / "PARALLEL_INSTRUCTIONS.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(instructions)
    
    return output_file


def main():
    parser = argparse.ArgumentParser(
        description='Chia paper range để chạy parallel trên nhiều Colab'
    )
    parser.add_argument(
        '--start-ym',
        default='2311',
        help='Start year-month (default: 2311)'
    )
    parser.add_argument(
        '--start-id',
        type=int,
        default=14685,
        help='Start paper ID (default: 14685)'
    )
    parser.add_argument(
        '--end-ym',
        default='2312',
        help='End year-month (default: 2312)'
    )
    parser.add_argument(
        '--end-id',
        type=int,
        default=844,
        help='End paper ID (default: 844)'
    )
    parser.add_argument(
        '--num-parts',
        type=int,
        default=5,
        help='Số lượng parts để chia (default: 5)'
    )
    parser.add_argument(
        '--student-id',
        default='23127240',
        help='Student ID (default: 23127240)'
    )
    parser.add_argument(
        '--output-dir',
        default='./parallel_configs',
        help='Thư mục output (default: ./parallel_configs)'
    )
    
    args = parser.parse_args()
    
    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)
    
    print("=" * 80)
    print("CHIA PAPER RANGE CHO PARALLEL EXECUTION")
    print("=" * 80)
    print(f"\n📊 Input range: {args.start_ym}.{args.start_id} → {args.end_ym}.{args.end_id}")
    print(f"🔢 Số parts: {args.num_parts}")
    print(f"📁 Output dir: {output_dir}")
    
    # Split range
    ranges = simple_split(
        args.start_ym, args.start_id,
        args.end_ym, args.end_id,
        args.num_parts
    )
    
    print(f"\n✅ Đã chia thành {len(ranges)} parts:\n")
    
    # Generate config files
    for i, range_info in enumerate(ranges, 1):
        config_file = generate_config_file(i, range_info, output_dir, args.student_id)
        print(f"Part {i}:")
        print(f"  Range: {range_info['start_ym']}.{range_info['start_id']:05d} → {range_info['end_ym']}.{range_info['end_id']:05d}")
        print(f"  Papers: ~{range_info['estimate_papers']}")
        print(f"  Config: {config_file}")
        print()
    
    # Generate instructions
    instructions_file = generate_instructions(ranges, output_dir)
    print(f"✅ Đã tạo file hướng dẫn: {instructions_file}")
    
    print("\n" + "=" * 80)
    print("🎉 HOÀN TẤT!")
    print("=" * 80)
    print(f"\nĐọc file hướng dẫn để biết cách sử dụng:")
    print(f"  cat {instructions_file}")
    print(f"\nHoặc xem trực tiếp trong folder: {output_dir}/")
    print("\n⚡ Ước tính: Chạy {0} Colab đồng thời → xong trong ~{1:.1f} giờ!".format(
        args.num_parts, 10 / args.num_parts
    ))


if __name__ == '__main__':
    main()
