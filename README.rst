.. image:: https://img.shields.io/pypi/v/theknights.svg
        :target: https://pypi.python.org/pypi/theknights

.. image:: https://img.shields.io/travis/portugueslab/theknights.svg
        :target: https://travis-ci.com/portugueslab/theknights

.. image:: https://codecov.io/gh/portugueslab/theknights/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/portugueslab/theknights

.. image:: https://upload.wikimedia.org/wikipedia/en/e/eb/Knightni.jpg?download


The Knights (who say NI)
========================

This package fakes parts of the `nidaqmx`_ package for controlling NI boards. It should be used like:

.. code-block:: python

    import logging

    try:
        import nidaqmx
    except ImportError:
        import theknights as nidaqmx


The main purpose is to enable testing, development and continuous integration on machines which do not have NI boards attached.
This package has been developed in the `Portugues lab`_. Documentation can be found `here`_ .



Credits
-------

The package was created with Cookiecutter_ and this_ template.

.. _`nidaqmx`: https://nidaqmx-python.readthedocs.io/en/latest/
.. _`Portugues lab`: http://www.portugueslab.com
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _this: https://github.com/audreyr/cookiecutter-pypackage
.. _here: https://portugueslab.github.io/theknights
