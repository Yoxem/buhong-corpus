#!/usr/bin/env python3
#-*-coding:utf-8-*-

import os.path
from pyexcel import get_book
from pyexcel_io import save_data

sheet = get_book(file_name="kautian.ods")
s_names = sheet.sheet_names()

dest_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "result_csvs")

try:
    os.makedirs(dest_dir)
except FileExistsError:
    print(f"the folder {dest_dir} exists!")

for i in range(len(s_names)):
    sheet[i].save_as(os.path.join(dest_dir, f"{s_names[i]}.csv"))
