#!/bin/bash
#
# Kawaz Install Shell for Developer
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
install markdown
install django
install django-haystack
install django-compress
install django-reversetag
install django-pagination
install git+git://github.com/alex/django-filter.git django-filter
install git+git://github.com/psychotechnik/django-breadcrumbs.git django-breadcrumbs
install hg+https://bitbucket.org/ubernostrum/django-registration django-registration

# Checkout packages
echo "Checkout development packages..."
DST="../development/packages"
mkdir -p $DST
git clone git@github.com:lambdalisue/django-mfw.git "$DST/django-mfw"
git clone git@github.com:lambdalisue/e4u.git "$DST/e4u"
git clone git@github.com:lambdalisue/uamd.git "$DST/uamd"
git clone git@github.com:lambdalisue/django-qwert.git "$DST/django-qwert"
git clone git@github.com:lambdalisue/django-object-permission.git "$DST/django-object-permission"
git clone git@github.com:lambdalisue/django-universaltag.git "$DST/django-universaltag"
git clone git@github.com:lambdalisue/django-googlemap-widget.git "$DST/django-googlemap-widget"
git clone git@github.com:lambdalisue/django-markupfield.git "$DST/django-markupfield"
git clone git@github.com:lambdalisue/django-markitup-widget.git "$DST/django-markitup-widget"
git clone git@github.com:lambdalisue/django-codemirror-widget.git "$DST/django-codemirror-widget"
git clone git@github.com:lambdalisue/django-modify-history.git "$DST/django-modify-history"

hg clone https://lambdalisue@bitbucket.org/lambdalisue/django-piston "$DST/django-piston"

# Copy local_settings, local_site
echo "Copy local_settings.py and local_site.py"
cp ../src/Kawaz/local_settings.develop.py ../src/Kawaz/local_settings.py
cp ../src/Kawaz/local_site.develop.py ../src/Kawaz/local_site.py

echo "Done."
