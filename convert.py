import glob
import os
import subprocess

file_list = glob.glob("/home/qvieth/Downloads/*.xls")
# basename_without_ext = os.path.splitext(os.path.basename(stock_code_list[0]))[0]

# filename

os.chdir("/home/qvieth/Downloads")

for i in file_list:
    subprocess.run(["libreoffice", "--convert-to", "xlsx", f"{i}", "--headless"])
