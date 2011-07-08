#!/bin/bash
#
# Kawaz Install Shell for Developer
#

# WARNING:
#   This install script is not checked yet
#

# Definition
#------------------------------------------
check() {
    if [[ `which $1` = "" ]]; then
        echo "$1: Not installed."
        exit 1
    else
        echo "$1: Ok"
    fi
}
install() {
    echo "Install $1 ..."
    if [[ $# = 1 ]]; then
        yes | sudo pip -q install "$1"
    else
        yes | sudo pip -q install "$1#egg=$2"
    fi
}

# Check required packages
echo "Checking required packages..."
ERR=0
check pip
check git
check hg
if [ $ERR = 1 ]; then
    exit 1;
fi

# Install required python packages
echo "Install required python packages..."
install dateutils
install docutils
install south
install pyyaml
install whoosh
install django
install django-haystack
install django-compress
install django-reversetag
install django-pagination
install git+git://github.com/alex/django-filter.git django-filter
install git+git://github.com/psychotechnik/django-breadcrumbs.git django-breadcrumbs
install hg+https://bitbucket.org/ubernostrum/django-registration django-registration

install git+git://github.com/lambdalisue/django-mfw.git django-mfw
install git+git://github.com/lambdalisue/django-qwert.git django-qwert
install git+git://github.com/lambdalisue/django-object-permission.git django-object-permission
install git+git://github.com/lambdalisue/django-modify-history.git django-modify-history
install git+git://github.com/lambdalisue/django-universaltag.git django-universaltag
install git+git://github.com/lambdalisue/django-googlemap-widget.git django-googlemap-widget
install git+git://github.com/lambdalisue/django-markitup-widget.git django-markitup-widget
install git+git://github.com/lambdalisue/django-codemirror-widget.git django-codemirror-widget
install git+git://github.com/lambdalisue/django-markupfield.git django-markupfield
install hg+https://lambdalisue@bitbucket.org/lambdalisue/django-piston django-piston

echo "Done."
