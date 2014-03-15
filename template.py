#!/usr/bin/env python
import re
import os
import math
import shutil

from jinja2 import FileSystemLoader, Template
from jinja2.environment import Environment

def copy_dir(html_dir, dname):
    print 'COPYING {0} to {1}...'.format(dname, html_dir + dname),
    if os.path.exists(html_dir + dname):
        shutil.rmtree(html_dir + dname)
    shutil.copytree(dname, html_dir + dname)
    print 'DONE'

def main():
    env = Environment()
    env.loader = FileSystemLoader('.')

    html_dir = "compiled_html/"
    if not os.path.exists(html_dir):
        # shutil.rmtree(html_dir)
        os.makedirs(html_dir)
    copy_dir(html_dir, 'css')
    copy_dir(html_dir, 'img')
    copy_dir(html_dir, 'fonts')

    print 'COPMILING index.html.jinja2...',
    with open(html_dir + 'index.html', 'w+') as out_file:
        contents = env.get_template('jinja2/index.html.jinja2').render().encode('utf-8')
        out_file.write(contents)

    print 'FINISHED!'

if __name__ == '__main__':
    main()
