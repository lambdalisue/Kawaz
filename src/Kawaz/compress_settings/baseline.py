#!/usr/bin/env python
# vim: set fileencoding=utf8 :
"""Compress settings for CSS framework 'baseline'


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
    'baseline': {
        'source_filenames': (
            r'static/css/baseline/baseline.reset.css',
            r'static/css/baseline/baseline.base.css',
            r'static/css/baseline/baseline.grid.css',
            r'static/css/baseline/baseline.type.css',
            r'static/css/baseline/baseline.form.css',
            r'static/css/baseline/baseline.table.css',
        ),
        'output_filename': r'static/css/baseline/baseline.compressed.css',
        'extra_context': {
            'media': 'screen, projection',
        }
    },
    'baseline-iphone': {
        'source_filenames': (
            r'static/css/baseline/baseline.iphone.css',
        ),
        'output_filename': r'static/css/baseline/baseline.iphone.compressed.css',
        'extra_context': {
            'media': 'only screen and (max-device-width: 480px)',
        }
    },
}
COMPRESS_JS = {
    'baseline': {
        'source_filenames': (
            r'static/javascript/baseline/html5.js',
        ),
        'output_filename': r'static/javascript/baseline/html5.compressed.js',
    },
}