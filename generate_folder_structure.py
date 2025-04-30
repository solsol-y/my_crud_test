# readme.md에 넣을 폴더 구조를 생성하는 스크립트
# 사용법: python generate_folder_structure.py > folder_structure.md

import os

EXCLUDE = {'.git', '__pycache__', '.venv'}

def print_folder_structure(start_path, indent="", md_lines=None):
    if md_lines is None:
        md_lines = ["```", f"{os.path.basename(start_path)}/"]

    for item in sorted(os.listdir(start_path)):
        if item in EXCLUDE:
            continue
        path = os.path.join(start_path, item)
        if os.path.isdir(path):
            md_lines.append(f"{indent}├── {item}/")
            print_folder_structure(path, indent + "│   ", md_lines)
        else:
            md_lines.append(f"{indent}├── {item}")
    
    return md_lines

if __name__ == "__main__":
    structure = print_folder_structure(".")
    structure.append("```")

    with open("folder_structure.md", "w", encoding="utf-8") as f:
        f.write("\n".join(structure))

    print("✅ 폴더 구조가 folder_structure.md 파일에 저장되었습니다.")
