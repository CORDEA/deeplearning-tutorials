#!/usr/bin/env python
# encoding:utf-8
#
# Copyright 2015-2017 Yoshihiro Tanaka
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__Author__ =  "Yoshihiro Tanaka"
__date__   =  "2015-01-22"

import os
from os import path

FOLDER = path.expanduser('~/caffe/101_ObjectCategories/')

train = open("train.txt", 'w')
val   = open("val.txt", 'w')

species = 0
for dirname in os.listdir(FOLDER):
    files = os.listdir(FOLDER + '/' + dirname)

    valFlag = True
    for filename in files:
        line = ' '.join([path.join(dirname, filename), str(species)]) + '\n'
        if valFlag:
            val.write(line)
            valFlag = False
        else:
            train.write(line)
    species += 1

train.close()
val.close()
