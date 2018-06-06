# -*- coding: utf-8 -*-

# Copyright © 2016 Mike Ray and others.

# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""Implementation of compile_html based on kramdown.

kramdown is available in the repos of several distributions.

For Debian:

sudo apt-get install ruby-kramdown

"""

import codecs
import os
from os.path import abspath
import subprocess

from nikola.plugin_categories import PageCompiler
from nikola.utils import makedirs, write_metadata


class CompileKramdown(PageCompiler):
    """Compile kramdown into HTML."""

    name = "kramdown"
    demote_headers = True

    def compile_html(self, source, dest, is_two_file=True):
        makedirs(os.path.dirname(dest))
        command = ['kramdown', '-o', 'html', abspath(source)]

        # Windows kludge
        if os.name == 'nt':
            command[4] = command[4].replace("\\", "\\\\")

        with open(abspath(dest), 'wt') as f:
            subprocess.check_call(command, stdout=f)

    def create_post(self, path, **kw):
        content = kw.pop('content', 'Write your post here.')
        onefile = kw.pop('onefile', False)
        # is_page is not used by create_post as of now.
        kw.pop('is_page', False)
        metadata = {}
        metadata.update(self.default_metadata)
        metadata.update(kw)
        makedirs(os.path.dirname(path))
        if not content.endswith('\n'):
            content += '\n'
        with codecs.open(path, "wb+", "utf8") as fd:
            if onefile:
                fd.write("<!--\n")
                fd.write(write_metadata(metadata))
                fd.write("-->\n\n")
            fd.write(content)
