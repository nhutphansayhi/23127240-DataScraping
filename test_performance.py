#!/usr/bin/env python3
"""
Script để test performance của config tối ưu vs config bình thường
Chạy với 10 bài báo để estimate thời gian cho 5000 bài

Usage:
    python test_performance.py
"""

import time
import sys
import os
from pathlib import Path


def run_test(config_name, num_papers=10):
    """Chạy test với config cụ thể"""
    
    print(f"\n{'='*80}")
    print(f"Testing với {config_name}")
    print(f"{'='*80}\n")
    
    # Backup config hiện tại
    config_path = Path("src/config.py")
    backup_path = Path("src/config.py.backup")
    
    if config_path.exists():
        os.rename(config_path, backup_path)
    
    try:
        # Copy config test vào
        test_config = Path(f"src/{config_name}")
        if not test_config.exists():
            print(f"❌ File {config_name} không tồn tại!")
            return None
        
        os.system(f"cp src/{config_name} src/config.py")
        
        # Chạy test
        print(f"🧪 Chạy test với {num_papers} bài báo...\n")
        
        start_time = time.time()
        
        # Chạy với range nhỏ
        cmd = f"cd src && python main.py --start-ym 2311 --start-id 14685 --end-ym 2311 --end-id {14685 + num_papers - 1}"
        result = os.system(cmd)
        
        end_time = time.time()
        elapsed = end_time - start_time
        
        if result == 0:
            print(f"\n✅ Test hoàn thành!")
            print(f"⏱️  Thời gian: {elapsed:.2f} giây cho {num_papers} bài")
            print(f"📊 Trung bình: {elapsed/num_papers:.2f} giây/bài")
            
            # Estimate cho 5000 bài
            estimated_total = (elapsed / num_papers) * 5000
            estimated_hours = estimated_total / 3600
            
            print(f"\n📈 Ước tính cho 5000 bài:")
            print(f"   • Tổng thời gian: {estimated_hours:.2f} giờ ({estimated_total/60:.2f} phút)")
            
            return {
                'config': config_name,
                'time_per_paper': elapsed / num_papers,
                'estimated_hours': estimated_hours
            }
        else:
            print(f"❌ Test thất bại với exit code {result}")
            return None
            
    finally:
        # Restore config
        if backup_path.exists():
            os.rename(backup_path, config_path)


def main():
    print("=" * 80)
    print("PERFORMANCE TEST - So sánh Config Bình thường vs Config Tối ưu")
    print("=" * 80)
    print("\nScript này sẽ:")
    print("1. Test config bình thường (config.py)")
    print("2. Test config tối ưu (config_optimized.py)")
    print("3. So sánh kết quả\n")
    
    print("⚠️  Lưu ý: Test sẽ scrape 10 bài báo thật để đo thời gian")
    print("         Cần khoảng 2-5 phút để hoàn thành\n")
    
    response = input("Bạn có muốn tiếp tục? (y/n): ")
    if response.lower() != 'y':
        print("Đã hủy.")
        return
    
    # Kiểm tra files tồn tại
    if not Path("src/config.py").exists():
        print("❌ Không tìm thấy src/config.py")
        return
    
    if not Path("src/config_optimized.py").exists():
        print("❌ Không tìm thấy src/config_optimized.py")
        print("   Hãy tạo file này hoặc dùng config có sẵn")
        return
    
    results = []
    
    # Test 1: Config bình thường
    print("\n" + "🔍 TEST 1: CONFIG BÌNH THƯỜNG")
    result1 = run_test("config.py", num_papers=10)
    if result1:
        results.append(result1)
    
    # Test 2: Config tối ưu
    print("\n" + "⚡ TEST 2: CONFIG TỐI ƯU")
    result2 = run_test("config_optimized.py", num_papers=10)
    if result2:
        results.append(result2)
    
    # So sánh kết quả
    if len(results) == 2:
        print("\n" + "="*80)
        print("📊 KẾT QUẢ SO SÁNH")
        print("="*80)
        
        print(f"\n{'Config':<30} {'Giây/bài':<15} {'Giờ cho 5000 bài':<20}")
        print("-" * 80)
        
        for r in results:
            config_name = "Bình thường" if "config.py" in r['config'] else "Tối ưu"
            print(f"{config_name:<30} {r['time_per_paper']:<15.2f} {r['estimated_hours']:<20.2f}")
        
        # Tính speedup
        speedup = results[0]['estimated_hours'] / results[1]['estimated_hours']
        time_saved = results[0]['estimated_hours'] - results[1]['estimated_hours']
        
        print("\n" + "="*80)
        print(f"⚡ Config tối ưu NHANH HƠN {speedup:.2f}x")
        print(f"⏰ Tiết kiệm được {time_saved:.2f} giờ ({time_saved*60:.0f} phút)")
        print("="*80)
        
        print("\n💡 Khuyến nghị:")
        if speedup >= 2.5:
            print(f"   ✅ Config tối ưu nhanh hơn rất nhiều! Nên dùng cho Colab")
        elif speedup >= 1.5:
            print(f"   ✅ Config tối ưu nhanh hơn đáng kể. Recommend sử dụng")
        else:
            print(f"   ⚠️  Speedup không cao lắm, có thể do network hoặc API")
        
        if results[1]['estimated_hours'] <= 4:
            print(f"   🎉 Với config tối ưu, bạn có thể hoàn thành trong ~{results[1]['estimated_hours']:.1f} giờ!")
        
    elif len(results) == 1:
        print(f"\n⚠️  Chỉ test được 1 config")
        print(f"   Kết quả: {results[0]['estimated_hours']:.2f} giờ cho 5000 bài")
    else:
        print("\n❌ Không có kết quả nào thành công")


if __name__ == '__main__':
    main()
