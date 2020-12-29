====================
General observations
====================

License
=======

The code is licensed under the terms of the GPL version 2 upgrading to GPL 3
would require consent from all former contributors. Copyright years of files
have not been consistently incremented/updated on changes.

Languages
=========

The code base is a mix of Perl, Shell and PHP code. Most of the code is
implemented in PHP.

Code structure
==============

The code is structured into several directories. PHP namespaces are not used
because the code predates that feature.

There are a few entry point scripts in the :doc:`www directory <DIR-www>`. These
include scripts from the :doc:`includes directory <DIR-includes>` and the
:doc:`pages directory <DIR-pages>`.

Variable and file naming
========================

Unfortunately the scripts included from the entry point scripts are named with
numbers instead of real file names which makes it hard to understand the request
flow. Variable naming is inconsistent. There are some variables that hide the
meaning and require a lot of code reading / tracing to reveal their purpose.

Comments and inline documentation
=================================

The code base is not documented in a good way, there are neither class nor
method or function comments. Comments are just used for the license header
in most of the files.

Web application
===============

URL structure
-------------

The main web application uses a URL structure with a few entry point PHP scripts
that include other PHP scripts. URL parameters trigger the inclusion of PHP
fragments from other files.

Security functionality
----------------------

The technical side of the web application (i.e. the web server configuration) is
sufficient but not state of the art. HSTS is used but other configurations like
the TLS protocol support is lacking.

There is no CSRF protection implemented in the application which allows cross
site request forgery attacks against the users.

The application uses string concatenation to build SQL statements which makes
it very likely that the code can be abused for SQL injection attacks. Instead
of using prepared statements there are a lot of attempts to sanitize input. This
is obviously not sustainable.

HTML / CSS / Javascript
-----------------------

The HTML code tries to be HTML 4.01 compatible but the code structure makes it
hard to verify. There are formatting instructions sprinkled in the code and
leads to a lack of proper content / formatting separation. The code uses only
a small amount of JavaScript.

The code uses some obsolete constructs like ActiveX controls and the keygen tag
which need to be replaced.

Signer / CommModule
===================

The signer is a custom set of software components implemented in Perl. The
implementation is brittle and cannot properly cope with broken input. All
input that is not understood by the application leads to crashes. The
countermeasure is the ``commdaemon`` script that takes care of restarting crashed
signer components.

The signer ``server.pl`` and the signer client ``client.pl`` use external tools
(openssl, gpg, xdelta) and rely heavily on a stable set of parameters. This
poses risks to implement operating system package updates.

The :doc:`signer protocol <signer>` is a mix of binary and text protocol. The
protocol includes a rudimentary 8 bit CRC code which is not properly checked
in responses from the signer server.

An attempt to make the signer code more understandable is implemented in a
`feature branch <https://github.com/jandd/cacert-devel/tree/signer_rework_for_devsetup>`_
of Jan Dittberner's clone of the cacert-devel repository.

Handling of certificate data
============================

Certificate data (especially Subject DN, SubjectAlternativeName extensions) are
handled as strings which is not portable and may lead to corruption of data.

The web application code adds subjectAlternativeName fields to the Subject DN
of certificate requests for the signer. It would be a better idea to generate
the proper ASN.1 structures (either a complete TBSCertificate or separate
Subject DN and subjectAlternativeName extension structures) and pass these to
the signer.

Coupling of applications
========================

There is a close coupling between the data structures of the Web application,
the signer client and (on test systems) the Test-Manager application. This has
the consequence that changes in the database structure have to be implemented
in all applications that use the same database tables or expect the same
consistency guarantees.

Database structure
==================

The database structure has been developed before MySQL had proper foreign key
support. There are some tables that form relationships but theses are not
formally expressed in the database schema definition.

The database schema in the release branch (as of 2020-12-29) are incomplete.
There has been an effort to provide a `more complete schema`_ in a recent
`pull request <https://github.com/CAcertOrg/cacert-devel/pull/21>`_.

.. _more complete schema: https://github.com/jandd/cacert-devel/tree/replace_deprecated_mysql_api/scripts/db_migrations

Character set handling / Internationalization
=============================================

The web application, the CAcert automated testing system (CATS) as well as the
signer use Latin1 / ISO-8859-1 as the only supported character set. This is a
blocker for more international adoption.

Translations are using the GNU gettext library. Translation files are pulled
from translations.cacert.org via a Makefile in the
:doc:`locale directory <DIR-locale>`. It might be a good idea to store a
verified state of translations in the repository and update them during the
release process.

Testing
=======

Testing is only performed manually. There are no automated tests.

Deployment and configuration
============================

The deployment process for the software requires changes to application files.
An attempt to fix this situation has been made in the pull request for the
`MySQL compatibility fixes`_ and the `signer rework`_ of Jan Dittberner.

The application should be configurable via environment variables like a proper
`12 factor application`_. Jan implemented a `docker-compose`_ based
`developer setup`_ that implements the configuration in that way.

.. _MySQL compatibility fixes: https://github.com/CAcertOrg/cacert-devel/pull/21
.. _signer rework: https://github.com/jandd/cacert-devel/tree/signer_rework_for_devsetup
.. _12 factor application: https://12factor.net/
.. _docker-compose: https://docs.docker.com/compose/
.. _developer setup: https://git.dittberner.info/jan/cacert-devsetup

.. _general-conclusion:

Conclusions
===========

From `my <https://jan.dittberner.info>`_ point of view after getting familiar
with the existing code base I come to the following conclusions: The current
software would require a complete rewrite that takes the following things into
consideration:

- UTF-8 handling for everything
- proper ASN.1 handling
- cleaner separation between components
- modern web application standard with clean separation of content and
  presentation
- secure development practices
- documented and automated deployment
- continuous integration of changes to avoid long living feature branches
- signer protocol with better binary support, strong consistency checks and
  testability
- signer support for requesting CA certificates and GPG public keys used for
  signing to allow fully automated bootstrapping of the signer client and web
  application
- automated tests for critical functionality

I suggest to use a more `modern statically typed language`_ with proper support
for PKI idioms and some CSS, and client side (ECMA/JavaScript) frameworks to
avoid reimplementation of essential stuff.

.. _modern statically typed language: https://golang.org/