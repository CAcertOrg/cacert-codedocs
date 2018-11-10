.. index:: cgi-bin

=========================
Directory :file:`cgi-bin`
=========================

The `cgi-bin` directory contains

.. index:: PHP

.. sourcefile:: cgi-bin/siteseal.cgi
   :links:
      www/sealgen.php

   a PHP CGI script that generates some JavaScript code to invoke
   :sourcefile:`sealgen.php <www/sealgen.php>`. The configuration on
   www.cacert.org does not seem to support this script
   https://www.cacert.org/cgi-bin/siteseal.cgi returns a 403 response.

   .. todo: check whether this is linked anywhere or can be removed
