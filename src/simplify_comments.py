# Script để đơn giản hóa comments trong code
# Xóa docstrings formal, giữ lại comments ngắn gọn

import re
import sys

def simplify_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Nhưng giữ lại nếu nó là module docstring ở đầu file
    lines = content.split('\n')
    new_lines = []
    in_docstring = False
    docstring_count = 0
    skip_until_newline = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Module docstring đầu file - giữ lại nhưng sẽ sửa sau
                # Single line docstring
                continue
            else:
                in_docstring = True
                continue
        
        # Skip multi-line docstrings