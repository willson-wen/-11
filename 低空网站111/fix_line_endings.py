import os

def fix_line_endings(directory):
    """修复文件的行尾结束符"""
    text_extensions = {'.py', '.js', '.html', '.css', '.md', '.txt', '.json', '.yml', '.yaml', '.conf'}
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in text_extensions):
                file_path = os.path.join(root, file)
                try:
                    # 读取文件内容
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # 统一使用LF
                    content = content.replace('\r\n', '\n')
                    
                    # 写回文件
                    with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
                        f.write(content)
                    
                    print(f'已修复: {file_path}')
                except Exception as e:
                    print(f'处理文件时出错 {file_path}: {str(e)}')

if __name__ == '__main__':
    fix_line_endings('.') 