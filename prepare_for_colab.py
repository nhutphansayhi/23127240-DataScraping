#!/usr/bin/env python3
"""
Script kiểm tra và chuẩn bị project trước khi upload lên Google Colab
Student ID: 23127240
"""

import os
import sys
import zipfile
from pathlib import Path
import json

class ColabPreparationChecker:
    def __init__(self, project_dir):
        self.project_dir = Path(project_dir)
        self.src_dir = self.project_dir / "src"
        self.errors = []
        self.warnings = []
        
    def check_all(self):
        """Chạy tất cả các kiểm tra"""
        print("=" * 80)
        print("🔍 KIỂM TRA PROJECT TRƯỚC KHI UPLOAD LÊN COLAB")
        print("=" * 80)
        print()
        
        self.check_directory_structure()
        self.check_required_files()
        self.check_config_file()
        self.check_requirements()
        self.check_file_sizes()
        self.estimate_colab_requirements()
        
        self.print_summary()
        
        return len(self.errors) == 0
    
    def check_directory_structure(self):
        """Kiểm tra cấu trúc thư mục"""
        print("📁 Kiểm tra cấu trúc thư mục...")
        
        if not self.project_dir.exists():
            self.errors.append(f"Thư mục project không tồn tại: {self.project_dir}")
            return
        
        if not self.src_dir.exists():
            self.errors.append(f"Thư mục src không tồn tại: {self.src_dir}")
            return
        
        print("  ✅ Cấu trúc thư mục OK")
    
    def check_required_files(self):
        """Kiểm tra các file bắt buộc"""
        print("\n📄 Kiểm tra các file bắt buộc...")
        
        required_files = [
            "src/main.py",
            "src/arxiv_scraper.py",
            "src/reference_scraper.py",
            "src/bibtex_generator.py",
            "src/utils.py",
            "src/config.py",
            "src/requirements.txt"
        ]
        
        optional_files = [
            "src/reference_scraper_optimized.py",
            "README.md",
            "ArXiv_Scraper_Colab.ipynb"
        ]
        
        for file_path in required_files:
            full_path = self.project_dir / file_path
            if full_path.exists():
                print(f"  ✅ {file_path}")
            else:
                self.errors.append(f"File bắt buộc không tồn tại: {file_path}")
                print(f"  ❌ {file_path}")
        
        for file_path in optional_files:
            full_path = self.project_dir / file_path
            if full_path.exists():
                print(f"  ✅ {file_path} (optional)")
            else:
                self.warnings.append(f"File optional không tồn tại: {file_path}")
                print(f"  ⚠️  {file_path} (optional - nên có)")
    
    def check_config_file(self):
        """Kiểm tra file config.py"""
        print("\n⚙️  Kiểm tra file config.py...")
        
        config_file = self.src_dir / "config.py"
        if not config_file.exists():
            self.errors.append("File config.py không tồn tại")
            return
        
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check required variables
            required_vars = [
                'STUDENT_ID',
                'START_YEAR_MONTH',
                'START_ID',
                'END_YEAR_MONTH',
                'END_ID',
                'ARXIV_API_DELAY',
                'SEMANTIC_SCHOLAR_DELAY'
            ]
            
            for var in required_vars:
                if var in content:
                    print(f"  ✅ {var} có trong config")
                else:
                    self.errors.append(f"Biến {var} không có trong config.py")
                    print(f"  ❌ {var} không tìm thấy")
            
            # Check paper range
            if 'START_YEAR_MONTH' in content and 'END_YEAR_MONTH' in content:
                # Extract values (basic parsing)
                import re
                start_ym = re.search(r'START_YEAR_MONTH\s*=\s*["\'](\d+)["\']', content)
                end_ym = re.search(r'END_YEAR_MONTH\s*=\s*["\'](\d+)["\']', content)
                start_id = re.search(r'START_ID\s*=\s*(\d+)', content)
                end_id = re.search(r'END_ID\s*=\s*(\d+)', content)
                
                if start_ym and end_ym and start_id and end_id:
                    print(f"\n  📊 Paper range: {start_ym.group(1)}.{start_id.group(1)} → {end_ym.group(1)}.{end_id.group(1)}")
                    
                    # Estimate number of papers
                    # This is approximate
                    start_val = int(start_ym.group(1)) * 100000 + int(start_id.group(1))
                    end_val = int(end_ym.group(1)) * 100000 + int(end_id.group(1))
                    est_papers = end_val - start_val + 1
                    print(f"  📈 Ước tính số bài báo: ~{est_papers}")
                    
                    if est_papers < 4000:
                        self.warnings.append(f"Số lượng bài báo có vẻ ít (<4000). Kiểm tra lại range.")
                    elif est_papers > 6000:
                        self.warnings.append(f"Số lượng bài báo có vẻ nhiều (>6000). Kiểm tra lại range.")
        
        except Exception as e:
            self.errors.append(f"Lỗi khi đọc config.py: {e}")
    
    def check_requirements(self):
        """Kiểm tra file requirements.txt"""
        print("\n📦 Kiểm tra dependencies...")
        
        req_file = self.src_dir / "requirements.txt"
        if not req_file.exists():
            self.errors.append("File requirements.txt không tồn tại")
            return
        
        try:
            with open(req_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            required_packages = ['arxiv', 'requests', 'pandas']
            found_packages = []
            
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    package = line.split('==')[0].split('>=')[0].split('<=')[0].strip()
                    found_packages.append(package)
            
            for pkg in required_packages:
                if pkg in found_packages:
                    print(f"  ✅ {pkg}")
                else:
                    self.warnings.append(f"Package {pkg} không có trong requirements.txt")
                    print(f"  ⚠️  {pkg} không tìm thấy")
            
            print(f"\n  📋 Tổng số packages: {len(found_packages)}")
        
        except Exception as e:
            self.errors.append(f"Lỗi khi đọc requirements.txt: {e}")
    
    def check_file_sizes(self):
        """Kiểm tra kích thước files"""
        print("\n💾 Kiểm tra kích thước files...")
        
        total_size = 0
        large_files = []
        
        for file_path in self.project_dir.rglob('*'):
            if file_path.is_file():
                # Skip data directories and __pycache__
                if any(part in file_path.parts for part in ['data', '__pycache__', '.git', 'venv']):
                    continue
                
                size = file_path.stat().st_size
                total_size += size
                
                if size > 10 * 1024 * 1024:  # > 10MB
                    large_files.append((file_path, size))
        
        print(f"  📊 Tổng kích thước project: {total_size / (1024*1024):.2f} MB")
        
        if large_files:
            print("\n  ⚠️  Files lớn (>10MB):")
            for file_path, size in large_files:
                print(f"    • {file_path.name}: {size/(1024*1024):.2f} MB")
                self.warnings.append(f"File lớn: {file_path.name} ({size/(1024*1024):.2f} MB)")
        
        if total_size > 100 * 1024 * 1024:  # > 100MB
            self.warnings.append("Project lớn hơn 100MB, upload có thể lâu")
    
    def estimate_colab_requirements(self):
        """Ước tính yêu cầu tài nguyên Colab"""
        print("\n📈 Ước tính yêu cầu Colab...")
        
        # Read config to estimate
        config_file = self.src_dir / "config.py"
        if config_file.exists():
            try:
                with open(config_file, 'r') as f:
                    content = f.read()
                
                import re
                start_ym = re.search(r'START_YEAR_MONTH\s*=\s*["\'](\d+)["\']', content)
                end_ym = re.search(r'END_YEAR_MONTH\s*=\s*["\'](\d+)["\']', content)
                start_id = re.search(r'START_ID\s*=\s*(\d+)', content)
                end_id = re.search(r'END_ID\s*=\s*(\d+)', content)
                
                if all([start_ym, end_ym, start_id, end_id]):
                    start_val = int(start_ym.group(1)) * 100000 + int(start_id.group(1))
                    end_val = int(end_ym.group(1)) * 100000 + int(end_id.group(1))
                    est_papers = end_val - start_val + 1
                    
                    # Estimates (rough)
                    avg_time_per_paper = 5  # seconds
                    avg_size_per_paper = 0.5  # MB
                    
                    est_time_hours = (est_papers * avg_time_per_paper) / 3600
                    est_disk_gb = (est_papers * avg_size_per_paper) / 1024
                    est_ram_gb = 2.0  # Base estimate
                    
                    print(f"  ⏱️  Ước tính thời gian: {est_time_hours:.1f} - {est_time_hours*2:.1f} giờ")
                    print(f"  💿 Ước tính dung lượng disk: {est_disk_gb:.1f} - {est_disk_gb*2:.1f} GB")
                    print(f"  💾 Ước tính RAM cần: {est_ram_gb:.1f} - {est_ram_gb*1.5:.1f} GB")
                    
                    print("\n  💡 Khuyến nghị:")
                    if est_time_hours > 10:
                        print("    • Thời gian chạy lâu (>10h) - Nên dùng Colab Pro")
                    if est_disk_gb > 80:
                        self.warnings.append("Dung lượng có thể vượt quá giới hạn Colab Free (100GB)")
                        print("    • Disk usage cao - Cân nhắc Colab Pro hoặc chạy theo batch")
                    
                    print("    • Giữ tab Colab mở trong suốt quá trình chạy")
                    print("    • Kết nối internet ổn định")
                    print("    • Có thể cần 12-24 giờ để hoàn thành")
                    
            except Exception as e:
                print(f"  ⚠️  Không thể ước tính: {e}")
    
    def print_summary(self):
        """In tổng kết"""
        print("\n" + "=" * 80)
        print("📋 TỔNG KẾT")
        print("=" * 80)
        
        if not self.errors and not self.warnings:
            print("\n✅ HOÀN HẢO! Project sẵn sàng upload lên Colab!")
            print("\n🚀 Bước tiếp theo:")
            print("  1. Nén project thành file zip")
            print("  2. Upload lên Google Colab")
            print("  3. Làm theo hướng dẫn trong notebook")
        else:
            if self.errors:
                print(f"\n❌ CÓ {len(self.errors)} LỖI CẦN SỬA:")
                for i, error in enumerate(self.errors, 1):
                    print(f"  {i}. {error}")
            
            if self.warnings:
                print(f"\n⚠️  CÓ {len(self.warnings)} CẢNH BÁO:")
                for i, warning in enumerate(self.warnings, 1):
                    print(f"  {i}. {warning}")
            
            if self.errors:
                print("\n❌ Vui lòng sửa các lỗi trước khi upload lên Colab")
                return False
            else:
                print("\n⚠️  Có một số cảnh báo nhưng vẫn có thể chạy được")
                print("🚀 Project có thể upload lên Colab, nhưng nên xem lại các cảnh báo")
        
        print("\n" + "=" * 80)
        return True
    
    def create_zip(self, output_file=None):
        """Tạo file zip để upload"""
        if output_file is None:
            output_file = self.project_dir.parent / f"{self.project_dir.name}.zip"
        
        print(f"\n📦 Tạo file zip: {output_file}")
        
        # Files/folders to exclude
        exclude_patterns = [
            '__pycache__',
            '.git',
            '.vscode',
            'venv',
            '.env',
            '.DS_Store',
            '*.pyc',
            '.ipynb_checkpoints'
        ]
        
        # Also exclude data directories
        exclude_dirs = []
        for item in self.project_dir.iterdir():
            if item.is_dir() and 'data' in item.name.lower():
                exclude_dirs.append(item.name)
        
        with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in self.project_dir.rglob('*'):
                if file_path.is_file():
                    # Check if should exclude
                    should_exclude = False
                    
                    for pattern in exclude_patterns:
                        if pattern in str(file_path):
                            should_exclude = True
                            break
                    
                    for exclude_dir in exclude_dirs:
                        if exclude_dir in file_path.parts:
                            should_exclude = True
                            break
                    
                    if not should_exclude:
                        arcname = file_path.relative_to(self.project_dir.parent)
                        zipf.write(file_path, arcname)
                        print(f"  ✅ Added: {arcname}")
        
        zip_size = output_file.stat().st_size / (1024 * 1024)
        print(f"\n✅ Tạo zip thành công!")
        print(f"  📊 Kích thước: {zip_size:.2f} MB")
        print(f"  📁 Vị trí: {output_file}")
        
        if zip_size > 50:
            print(f"\n  ⚠️  File zip khá lớn ({zip_size:.2f} MB)")
            print(f"     Upload có thể mất vài phút")
        
        return output_file


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Kiểm tra và chuẩn bị project trước khi upload lên Colab'
    )
    parser.add_argument(
        'project_dir',
        nargs='?',
        default='.',
        help='Đường dẫn đến thư mục project (default: thư mục hiện tại)'
    )
    parser.add_argument(
        '--create-zip',
        action='store_true',
        help='Tạo file zip sau khi kiểm tra thành công'
    )
    parser.add_argument(
        '--output',
        help='Đường dẫn file zip output (default: tên_project.zip)'
    )
    
    args = parser.parse_args()
    
    # Get project directory
    project_dir = Path(args.project_dir).resolve()
    
    print(f"📂 Project directory: {project_dir}\n")
    
    # Create checker
    checker = ColabPreparationChecker(project_dir)
    
    # Run checks
    success = checker.check_all()
    
    # Create zip if requested and checks passed
    if args.create_zip:
        if success or (not checker.errors):
            output_file = Path(args.output) if args.output else None
            checker.create_zip(output_file)
        else:
            print("\n❌ Có lỗi, không tạo file zip. Vui lòng sửa lỗi trước.")
            sys.exit(1)
    
    # Exit code
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
