
import os
import shutil
from pathlib import Path

def deckpath():
   
    return Path(os.path.join(os.path.expanduser("~"), "Desktop"))

def directories(base_path):
    dirs = {
        'videos': base_path / 'Videos',
        'screenshots': base_path / 'Screenshots',
        'pdfs': base_path / 'PDFs',
        'docs': base_path / 'Docs'
    }
    for dir_path in dirs.values():
        if not dir_path.exists():
            dir_path.mkdir()
    return dirs

def categorize_and_move_files(base_path, dirs):
    
    video_exts = {'.mp4', '.mkv', '.avi', '.mov'}
    screenshot_exts = {'.png', '.jpg', '.jpeg', '.bmp', '.gif'}
    pdf_ext = {'.pdf'}
    doc_exts = {'.doc', '.docx'}

    for file in base_path.iterdir():
        if file.is_file():
            ext = file.suffix.lower()
            if ext in video_exts:
                shutil.move(str(file), dirs['videos'])
            elif ext in screenshot_exts:
                shutil.move(str(file), dirs['screenshots'])
            elif ext in pdf_ext:
                shutil.move(str(file), dirs['pdfs'])
            elif ext in doc_exts:
                shutil.move(str(file), dirs['docs'])

def main():
   
    desktop_path = deckpath()
    dirs = directories(desktop_path)
    categorize_and_move_files(desktop_path, dirs)
    print("Files are organized now")

if __name__ == "__main__":
    main()