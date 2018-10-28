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

.. index:: cgi-bin

Directory :file:`cgi-bin`
=========================

The `cgi-bin` directory contains

.. index:: php

.. _cgi-bin-siteseal-cgi:

- :file:`siteseal.cgi` a PHP CGI script that generates some JavaScript code
  to invoke :ref:`sealgen.php <www-sealgen-php>`. The configuration on
  www.cacert.org does not seem to support this script
  https://www.cacert.org/cgi-bin/siteseal.cgi returns a 403 response.

.. todo: check whether this is linked anywhere or can be removed

.. index:: commmodule
.. index:: Perl
.. index:: bash

Directory :file:`CommModule`
============================

This directory contains the CommModule that is implemented in Perl:

.. _commmodule-client-pl:

- :file:`client.pl` the real client, running on the webserver

  The style of the Perl code seems a bit inconsistent (mix of uppercase and
  lowercase function names, usage of brackets). The code uses database polling
  in a loop. It might be a better idea to use some kind of queueing (Redis,
  AMQP, ...) to not waste resources when there is nothing to do). Function
  parameters are not named which makes the code hard to read.

  The script calls several system binaries that need to be present in
  compatible versions:

  - :program:`openssl`
  - :program:`xdelta`

  The script uses several Perl standard library modules as well as the
  following third party modules:

  .. index:: Perl, thirdparty

  - `DBD::mysql <https://metacpan.org/pod/DBD::mysql>`_
  - `DBI <https://metacpan.org/pod/DBI>`_
  - `Device::SerialPort <https://metacpan.org/pod/Device::SerialPort>`_
  - `File::CounterFile <https://metacpan.org/pod/File::CounterFile>`_

  The script references several openssl configuration files in the HandleCerts
  function that are not included in the code repository. There are some
  openssl configuration files with similar names in
  https://svn.cacert.org/CAcert/SystemAdministration/signer/

  The database password is parsed from
  :ref:`includes/mysql.php <includes-mysql-php>` and relies on the
  exact code that is defined there. Database name, user and host are hardcoded
  in the DBI->connect call.

  The script implements the client side of the signer protocol which is
  specified in :doc:`signer`.

  The script performs the following operations:

  - parse password from :file:`includes/mysql.php`
  - read a list of CRL files and logs their SHA-1 hashes
  - read :file:`serial.conf`, create a Device::SerialPort instance `$portObj`,
    sets serial parameters and saves :file:`serial.conf`
  - run a main loop as long as a file :file:`./client.pl-active` is present.
    The main loop performs the following tasks

    - handle pending OpenPGP key signing request via ``HandleGPG()``
    - handle pending certificate signing requests:

      - personal client certificates via ``HandleCerts(0, 0)``
      - personal server certificates via ``HandleCerts(0, 1)``
      - organization client certificates via ``HandleCerts(1, 0)``
      - organization server certificates via ``HandleCerts(1, 1)``

    - handle pending certificate revocation requests

      - personal client certificates via ``RevokeCerts(0, 0)``
      - personal server certificates via ``RevokeCerts(0, 1)``
      - organization client certificates via ``RevokeCerts(1, 0)``
      - organization server certificates via ``RevokeCerts(1, 1)``

    - refresh :term:`CRLs <CRL>` via ``RefreshCRLs()`` in every 100st
      iteration
    - send a :ref:`NUL request <signer-nul-request-format>` to keep the signer
      connection alive
    - sleep for 2.7 seconds

  There is potential for optimization in the main loop. The CRL update could
  be performed if a certificate has been revoked. The NUL request needs only
  to be sent if no other request has been sent.

  The script uses a lot of temporary files instead of piping input and
  output to and from external commands.

  .. todo:: describe more in-depth what each of the main loop steps does

- :file:`commdaemon` a script to run :ref:`client.pl <commmodule-client-pl>`
  or :ref:`server.pl <commmodule-server-pl>`

  This bash script is automatically restarting the :file:`{script}` given as
  the first parameter as long as a file :file:`{script}-active` exists.
  Informational messages and errors are logged to syslog via
  :command:`logger`.

  The script is most probably used to recover from crashed scripts. This
  could be implemented via :command:`supervisor` or :command:`systemd`
  instead of a custom script.

- :file:`commmodule` a script for startup/shutdown of CommModule from
  /etc/init.d
- :file:`logclean.sh` maintenance script for logfiles generated by CommModule
- :file:`serial.conf` serial port configuration file

.. _commmodule-server-pl:

- :file:`server.pl` the real server, running on the signing server

  This script implements the signer (server) side of the signer protocol and
  performs the actual signing operations.

  The script contains a some code that is duplicated by
  :ref:`client.pl <commmodule-client-pl>`.

- :file:`usbclient.pl` obsoleted USB version of
  :ref:`client.pl <commmodule-client-pl>` above

.. todo: remove unused file (usbclient.pl)

.. todo: add a serial.conf template and move the actual serial.conf into
   configuration management

.. todo: clarify why log rotation is implemented with a custom
   logclean.sh script instead of using logrotate

Directory :file:`includes`
==============================

.. _includes-mysql-php:
.. _includes-mysql-php-sample:

- :file:`mysql.php.sample` is a template for the database connection handling
  code that is meant to be copied to :file:`mysql.php`.

  The template defines the MySQL connection as a session variable `mconn` and
  tries to connect to that database. It also defines the session variables
  `normalhostname`, `securehostname` and `tverify`.

  The template defines a function :php:func:`sendmail` for sending mails.

  .. php:function:: sendmail($to, $subject, $message, $from, $replyto="", \
         $toname="", $fromname="", $errorsto="returns@cacert.org", \
         $use_utf8=true)

     Send an email. The function reimplements functionality that is readily
     available in PHP. The function does not properly escape headers and
     sends raw SMTP commands.

     :param string $to:       recipient email address
     :param string $subject:  subject
     :param string $message:  email body
     :param string $from:     from email address
     :param string $replyto:  reply-to email address
     :param string $fromname: unused in the code
     :param string $toname:   unused in the code
     :param string $errorsto: email address used for Sender and Errors-To
                              headers
     :param bool $use_utf8:   decides whether the Content-Type header uses
                              a charset parameter of utf-8 or iso-8859-1

  Configuration and actual code are mixed. It would be better to have a
  separate file that just includes configuration.

  This file is parsed by :ref:`CommModule/client.pl <commmodule-client-pl>`
  format changes might break the CommModule code.

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