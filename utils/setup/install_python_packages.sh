#!/bin/sh
#
# Installer of Python Packages
#
# --- Definition
install(){
    if [ $# = 1 ]; then
        # from PyPI
        yes | pip -q install $0
    else
        yes | pip -q install $0#egg=$1
    fi
}
clone(){
    git clone $0 ../../packages/$1
}
# --- Required packages check
FAILUR=0
echo "Checking required packages to run..."
if [ `which pip` = "" ]; then
    echo "ERROR: You need to install pip before execute this install script."
    FAILUR=1
fi
if [ `which git` = "" ]; then
    echo "ERROR: You need to install git before execute this install script."
    FAILUR=1
fi
if [ `which hg` = "" ]; then
    echo "ERROR: You need to install mercurial before execute this install script."
    FAILUR=1
fi
if [ $FAILUR = 1 ]; then
    exit 1;
fi
# --- Install required packages
echo "Installing required packages..."
# PyPy
install dateutils
install docutils
install south
install pyyaml
install django
install django-haystack
install django-compress
install django-reversetag
install django-pagination
# Git
install git+git://github.com/alex/django-filter.git django-filter
install git+git://github.com/psychotechnik/django-breadcrumbs.git django-breadcrumbs
# Mercurial
install hg+https://bitbucket.org/ubernostrum/django-registration django-registration
# --- Install develop packages or clone repository
echo "Do you want to install development packages? (no for develop environment) (yes/no)"
read INPUT
if [ $INPUT = "yes" ]; then
    echo "Installing develop packages..."
	# Github
	install git+git://github.com/lambdalisue/django-mfw.git django-mfw
	install git+git://github.com/lambdalisue/django-qwert.git django-qwert
	install git+git://github.com/lambdalisue/django-object-permission.git django-object-permission
	install git+git://github.com/lambdalisue/django-universaltag.git django-universaltag
	install git+git://github.com/lambdalisue/django-googlemap.git django-googlemap
	install git+git://github.com/lambdalisue/django-markupfield.git django-markupfield
	# Mercurial
	install hg+https://bitbucket.org/lambdalisue/django-piston django-piston
else
    echo "Cloning develp packages..."
    mkdir -p ../../packages
    clone git@github.com:lambdalisue/django-mfw.git django-mfw
    clone git@github.com:lambalisue/e4u.git e4u
    clone git@github.com:lambalisue/uamd.git uamd
    clone git@github.com:lambdalisue/django-qwert.git django-qwert
    clone git@github.com:lambdalisue/django-object-permission.git django-object-permission
    clone git@github.com:lambdalisue/django-universaltag django-universaltag
    clone git@github.com:lambdalisue/django-googlemap django-googlemap
    clone git@github.com:lambdalisue/django-markupfield django-markupfield
	mercurial  hg+https://bitbucket.org/lambdalisue/django-piston django-piston
fi
