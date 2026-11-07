## Requirement
* pip3
* python3 

## Method
1. change to the folder: `buhong/thirdParty/moeDict`
2. It's recommended to create a Python environment in the subfolder `env` inside the working directory `work_dir`  first: `python3 -m venv  [/path/to/work_dir.env]`.
3. then entering the environment: `source [work_dir]/env/bin/activate`
4. install mooules: `pip3 install pyexcel pyexcel-ods`
5. run the Python script `python3 ./kautian_to_csvs.py` 
6. the result is in `[work_dir]/result_csvs`
