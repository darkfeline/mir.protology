mir.protology README
====================

.. image:: https://circleci.com/gh/darkfeline/mir.protology.svg?style=shield
   :target: https://circleci.com/gh/darkfeline/mir.protology
   :alt: CircleCI
.. image:: https://codecov.io/gh/darkfeline/mir.protology/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/darkfeline/mir.protology
   :alt: Codecov
.. image:: https://badge.fury.io/py/mir.protology.svg
   :target: https://badge.fury.io/py/mir.protology
   :alt: PyPI Release
.. image:: https://readthedocs.org/projects/mir-protology/badge/?version=latest
   :target: http://mir-protology.readthedocs.io/en/latest/
   :alt: Latest Documentation

Template project for Python projects under the mir namespace.

Before running any other make command, run::

  $ pipenv install --dev

To build an installable wheel, run::

  $ pipenv run make wheel

To build a source distribution, run::

  $ pipenv run make sdist

To run tests, run::

  $ pipenv run make check

To build docs, run::

  $ pipenv run make html

To build a TAGS file, run::

  $ make TAGS

To clean up all built files, run::

  $ make distclean
