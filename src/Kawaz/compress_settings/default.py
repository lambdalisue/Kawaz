#!/usr/bin/env python
# vim: set fileencoding=utf8 :
"""Compress settings for base


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

COMPRESS_CSS = {
    'default': {
        'source_filenames': (
            r'static/css/baseline/baseline.reset.css',
            r'static/css/baseline/baseline.base.css',
            r'static/css/baseline/baseline.grid.css',
            r'static/css/baseline/baseline.type.css',
            r'static/css/baseline/baseline.form.css',
            r'static/css/baseline/baseline.table.css',
        ),
        'output_filename': r'static/css/default.compressed.css',
        'extra_context': {
            'media': 'screen, projection',
        }
    },
}
COMPRESS_JS = {
    'default': {
        'source_filenames': (
            r'static/javascript/html5.js',
            r'static/javascript/jquery-1.6.1.min.js',
            r'static/javascript/jquery-ui-1.8.5.full.min.js',
        ),
        'output_filename': r'static/javascript/default.compressed.js',
    },
}