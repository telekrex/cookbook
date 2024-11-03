@echo off
cd Source
python -m PyInstaller --onedir "Program.py" -n "Program" --noconsole --icon="myicon.ico"