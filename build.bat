@echo on
pyinstaller --onefile "main.py" --icon="pes_indie.ico" --add-data=pes_indie.ico;. --add-data=demonyms.csv;. --name "OF Team Editor 5" --noconsole --version-file file_version_info.txt
pause