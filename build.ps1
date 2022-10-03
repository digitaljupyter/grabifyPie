# Pyinstaller command to build the pie.py to output-bins
pyinstaller --distpath=output-bins ip/pie.py
pyinstaller --distpath=output-bins roblox/roblox-scraper.py

Remove-Item pie.spec
