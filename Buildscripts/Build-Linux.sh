#!/bin/bash
cd Source
python3 -m PyInstaller --onedir "program.py" -n "Program" --noconsole --icon="myicon.ico"