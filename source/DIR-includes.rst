.. index:: includes 
.. index:: PHP

==========================
Directory :file:`includes`
==========================

.. sourcefile:: includes/.cvsignore

   :file:`.cvsignore` includes the parameters for CVS, which files to ignore by
   versioning

   .. note:: CVS is long dead, is this still used?

.. sourcefile:: includes/.gitignore

   :file:`.gitignore` contains file patterns to be ignored by Git.

.. sourcefile:: includes/about_menu.php
   :links:
      http://blog.cacert.org/
      http://wiki.CAcert.org/
      www/policy/
      //wiki.cacert.org/FAQ/Privileges
      www/index.php?id=47
      www/logos.php
      www/stats.php
      http://blog.CAcert.org/feed/
      www/index.php?id=7
      //wiki.cacert.org/Board
      https://lists.cacert.org/wws
      www/src-lic.php

   :file:`about_menu.php` is a part (<div>) of a PHP-Page, containing most of
   the CAcert-related links.

.. sourcefile:: includes/account_stuff.php

.. sourcefile:: includes/account.php
   :uses:
      includes/about_menu.php
      .... showheader

.. sourcefile:: includes/general_stuff.php

.. sourcefile:: includes/general.php

.. sourcefile:: includes/keygen.php

.. sourcefile:: includes/loggedin.php

.. sourcefile:: includes/mysql.php

   :file:`includes/mysql.php` is not contained in the :cacertgit:`cacert-devel`
   repository but is used by several other files. The file is copied from
   :sourcefile:`includes/mysql.php.sample` and defines the database connection
   information.

   This file is parsed directly by :sourcefile:`CommModule/client.pl`
   format changes might break the CommModule code.

.. sourcefile:: includes/mysql.php.sample

   :file:`mysql.php.sample` is a template for the database connection handling
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

.. sourcefile:: includes/notary.inc.php

.. sourcefile:: includes/shutdown.php

.. sourcefile:: includes/sponsorinfo.php

.. sourcefile:: includes/tverify_stuff.php


.. index:: includes/lib
.. index:: PHP

Directory :file:`includes/lib`
==============================

.. sourcefile:: includes/lib/account.php

.. sourcefile:: includes/lib/check_weak_key.php

.. sourcefile:: includes/lib/general.php

.. sourcefile:: includes/lib/l10n.php
