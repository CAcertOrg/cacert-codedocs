===================
Directory structure
===================

root Directory
==============

The root directory contains

- a :file:`.gitignore` file with a list of excluded files
- a :file:`LICENSE` file the `GPL`_ license text
- a :file:`README` file with very rudimentary documentation stating the
  license and a list of system requirements

.. _GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0

Directory :file:`cgi-bin`
=========================

The `cgi-bin` directory contains

.. _cgi-bin-siteseal-cgi:

- :file:`siteseal.cgi` a PHP CGI script that generates some JavaScript code
  to invoke :ref:`sealgen.php <www-sealgen-php>`. The configuration on
  www.cacert.org does not seem to support this script
  https://www.cacert.org/cgi-bin/siteseal.cgi returns a 403 response.

.. todo: check whether this is linked anywhere or can be removed

Directory :file:`www`
=====================

This contains the PHP code that is the entry point to the application:

.. _www-sealgen-php:

- :file:`sealgen.php` generates a small site seal image from
  :ref:`www/images/secured.png <www-images-secured-png>`. This could be
  replaced with a static image if it is used at all. This is referenced
  by :ref:`cgi-bin/siteseal.cgi <cgi-bin-siteseal-cgi>`

Directory :file:`www/images`
============================

.. _www-images-secured-png:

- :file:`secured.png` is a small image used by
  :ref:`www/sealgen.php <www-sealgen-php>`
