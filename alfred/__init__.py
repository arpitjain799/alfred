# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 JinTian.
#
# This file is part of alfred
# (see http://jinfagang.github.io).
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
"""Bring in all of the public Alfred interface into this module."""
import importlib

# pylint: disable=g-bad-import-order

from .modules import *
from .vis import *
from .fusion import *
from .dl.torch.common import print_shape
from .utils.log import logger
from .dl.torch.common import device
from .utils.progress import pbar, prange

globals().update(importlib.import_module("alfred").__dict__)
