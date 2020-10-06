from pkg_resources import get_distribution 
#to access the resource files, and for extensible applications and frameworks to automatically discover plugins

__version__ = get_distribution('flask_minimal').version
