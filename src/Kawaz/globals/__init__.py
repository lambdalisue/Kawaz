# Auto-script
from django.template import add_to_builtins
add_to_builtins('compress.templatetags.compressed')
add_to_builtins('reversetag.templatetags.reversetag')
add_to_builtins('Kawaz.globals.templatetags.settings')