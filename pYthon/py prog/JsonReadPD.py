# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 18:46:48 2019

@author: faculty
"""

import pandas as pd

json_file = "D:\\April\\people.json"

json_data = pd.read_json(json_file)
print(json_data)