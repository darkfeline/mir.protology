# Copyright 2016 Allen Li
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

setup(
    name='mir.protology',
    version='0.1.0',
    description='Distribution template for the mir namespace',
    long_description='',
    keywords='',
    url='https://github.com/darkfeline/mir.protology',
    author='Allen Li',
    author_email='darkfeline@felesatra.moe',
    classifiers=[
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.5',
    ],

    py_modules=['mir.protology'],
    packages=[],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'protology = mir.protology:main',
        ],
    },
)
