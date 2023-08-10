@echo off
call C:\Users\23174\anaconda3\Scripts\activate.bat base
python change_image_path.py
hexo clean
hexo g -d
pause
