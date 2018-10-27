==========================
Building the documentation
==========================

This documentation is maintained as a set of ReStructuredText documents and
uses `Sphinx <http://www.sphinx-doc.org/>`_ to build HTML formatted
representations of the documents.

Getting the documentation source
--------------------------------

The documentation is available from the git repository cacert-codedocs on
git.cacert.org. You can browse the `repository
<http://git.cacert.org/gitweb/?p=cacert-codedocs.git;a=summary>`_ via gitweb.

You can clone the repository anonymously by executing::

   git clone git://git.cacert.org/cacert-codedocs.git

If you want to contribute to the documentation please ask git-admin@cacert.org
to setup a user in the group git-doc on git.cacert.org for you. You will have
to provide an SSH public key (either RSA with at least 2048 Bits modulus or an
ECDSA or ED25519 key with similar strength) with your request.

If you have a user in the git-doc group you can clone the repository by
executing::

   git clone ssh://<username>@git.cacert.org/var/cache/git/cacert-codedocs.git

.. note:: replace ``<username>`` with your actual username

Building with Sphinx
--------------------

To build this documentation you need a Python 3 installation. To isolate the
documentation build from your system Python 3 packages using a virtual
environment is recommended. Management of the virtual environment can be done
with pipenv as described below.

Python 3 installation instructions can be found on the `Python website`_.

.. _Python website: https://www.python.org/

.. topic:: Building the documentation on a Debian system

   The following example shows how to build the documentation on a Debian system:

   .. code-block:: bash

      # Install required operating system packages
      sudo apt-get install python3 python3-pip make
      # install pipenv
      python3 -m pip install -U pip pipenv
      # use pipenv to install require dependencies into a virtual environment
      pipenv install
      # Build the documentation
      pipenv run make html

   .. note::

      The above commands should be run from the root directory of a git clone
      of the cacert-codedocs git repository. The result of the :program:`make`
      exection will be available in the :file:`build/html/` directory
      directory.

Continuous integration
----------------------

If changes are pushed to the cacert-codedocs git repository on git.cacert.org
a `Jenkins Job <https://jenkins.cacert.org/job/cacert-codedocs/>`_ is
automatically triggered. If the documentation is built successfully it can be
viewed in the `docs/_build/html directory of the Job's workspace
<https://jenkins.cacert.org/job/cacert-codedocs/ws/build/html/>`_. You may
open `index.html
<https://jenkins.cacert.org/job/cacert-codedocs/ws/build/html/index.html>`_
to browse the documentation (there are some JavaScript and SVG glitches due to
Content-Security-Policy settings).

If the documentation build is successful the result is pushed to a webserver
document root on :doc:`infradocs:systems/webstatic` and is publicly available at
https://codedocs.cacert.org/.
