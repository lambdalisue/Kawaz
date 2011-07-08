#!/usr/bin/env python
# vim: set fileencoding=utf8 :
"""Local pre settings module

This module will be loaded before settings.py loaded.


Copyright:
    Copyright 2011 Alisue allright reserved.

License:
    Licensed under the Apache License, Version 2.0 (the "License"); 
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unliss required by applicable law or agreed to in writing, software
    distributed under the License is distrubuted on an "AS IS" BASICS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
__author__  = 'Alisue <lambdalisue@hashnote.net>'
__version__ = '1.0.0'
__date__    = '2011/06/12'
import sys
import os.path
ROOT = os.path.join(os.path.dirname(__file__), '../../')
LIB = os.path.join(ROOT, "development/packages")
#--- Add PYTHON_PATH ---------------------------------
PYTHON_PATHS = (
    os.path.join(LIB, 'e4u'),
    os.path.join(LIB, 'uamd'),
    os.path.join(LIB, 'django-qwert'),
    os.path.join(LIB, 'django-mfw'),
    os.path.join(LIB, 'django-piston'),
    os.path.join(LIB, 'django-modify-history'),
    os.path.join(LIB, 'django-universaltag'),
    os.path.join(LIB, 'django-markupfield'),
    os.path.join(LIB, 'django-object-permission'),
    os.path.join(LIB, 'django-googlemap-widget'),
    os.path.join(LIB, 'django-markitup-widget'),
    os.path.join(LIB, 'django-codemirror-widget'),
)
for path in PYTHON_PATHS:
    if path not in sys.path: sys.path.append(path)
#-----------------------------------------------------

# Mark as loaded
LOCAL_PRE_SETTINGS_LOADED = True
