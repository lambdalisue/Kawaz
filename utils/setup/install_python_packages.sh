#!/bin/sh
#
# Installer of Python Packages
#

# PyPy
yes | pip install dateutil
yes | pip install docutils
yes | pip install south
yes | pip install pyyaml
yes | pip install django
yes | pip install django-haystack
yes | pip install django-compress
yes | pip install django-reversetag
yes | pip install django-pagination
#yes | pip install django-markupfield

# Github
yes | pip install git+git://github.com/alex/django-filter.git#egg=django-filter
yes | pip install git+git://github.com/psychotechnik/django-breadcrumbs.git#egg=django-breadcrumbs
yes | pip install git+git://github.com/lambdalisue/django-mfw#egg=django-mfw
yes | pip install git+git://github.com/lambdalisue/django-qwert#egg=django-qwert
yes | pip install git+git://github.com/lambdalisue/django-object-permission#egg=django-object-permission
yes | pip install git+git://github.com/lambdalisue/django-universaltag#egg=django-universaltag
yes | pip install git+git://github.com/lambdalisue/django-googlemap#egg=django-googlemap
yes | pip install git+git://github.com/lambdalisue/django-markupfield#egg=django-markupfield

# Marcurial
yes | pip install hg+https://bitbucket.org/lambdalisue/django-piston#egg=django-piston