#!/usr/bin/env python3

import os
import fileinput
import shutil 

from pathlib                                    import Path

################
# READ ENV VARS
################
with open('./config/vars.env', 'r') as f:
    lines           = f.readlines()

new_vars            = list()
for line in lines:
    data            = line.split('=')
    k               = data[0].strip()
    new_vars.append(k)
    v               = data[1].strip().replace("\"", "")

    if '$' in v:
        # print(f'replace variable because $: {v}')
        for var_key in new_vars:
            if f'${var_key}' in v:
                # print(f"""
                #     key {var_key} 
                #         is i var in {v}
                #             with val {os.environ[var_key]}
                # """)
                v               = v.replace(f'${var_key}', os.environ[var_key]).replace("\"", "")
                os.environ[k]   = v
    else:
        os.environ[k]   = v

    # print(f'{k} = {v}')

print('SAVE NEW ENV VARS VALUES')
for var in new_vars:
    print(f"{var} = {os.environ[var]}")

###############
# KAFKA CONFIG
###############
PROJECT_NAME      = os.environ['PROJECT_NAME']
files4tuning      = ['manage.py', 'settings/_base.py']

def replace_string(fname: str, replace: dict):
    # Read in the file
    with open(fname, 'r') as file :
        filedata = file.read()

    for k, v in replace.items():
        # Replace the target string
        filedata = filedata.replace(k, v)
    # Write the file out again
    with open(fname, 'w') as file:
        file.write(filedata)

replace                   = {k : os.environ[k] for k in new_vars}
print(f"""FOR REPLACE:
    {replace}
""")
for f in files4tuning:
    print(f)
    replace_string(f, replace)