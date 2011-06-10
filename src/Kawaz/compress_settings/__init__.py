#!/usr/bin/env python
# vim: set fileencoding=utf8 :
"""Compress Dynamic Loader

Dynamically load compress settings modules in compress_settings directory.

Datas:
    COMPRESS_CSS - loaded COMPRESS_CSS
    COMPRESS_JS - loaded COMPRESS_JS
    
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
__date__    = '2011/06/09'
import os, imp, glob
ROOT = os.path.dirname(__file__)

COMPRESS_CSS = {}
COMPRESS_JS = {}

def autodiscover():
    """Automatically discover compress setting modules"""
    
    for path in glob.glob("%s/*.py" % ROOT):
        filename = os.path.basename(path)
        if filename == '__init__.py':
            # Ignore this module
            continue
        mod = imp.load_source(filename, path)
        COMPRESS_CSS.update(mod.COMPRESS_CSS)
        COMPRESS_JS.update(mod.COMPRESS_JS)
autodiscover()