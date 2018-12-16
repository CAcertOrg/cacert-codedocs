.. index:: scripts
.. index:: PHP

================
Global Variables
================

    As the modules this website includes have to communicate together there are some global variables defined as arrays


.. index:: $_REQUEST

:php:global:`$_REQUEST`
=======================
.. php:global:: $_REQUEST['action']

.. php:global:: $_REQUEST['cert']

.. php:global:: $_REQUEST['domid']

.. php:global:: $_REQUEST['id']

.. php:global:: $_REQUEST["lang"]

.. php:global:: $_REQUEST['memid']

.. php:global:: $_REQUEST['oldid']

.. php:global:: $_REQUEST['orgid']`

.. php:global:: $_REQUEST['process']

.. php:global:: $_REQUEST['showdetails']

.. php:global:: $_REQUEST['ticketno']

.. index:: $_SERVER

:php:global:`$_SERVER`
======================

.. php:global:: $_SERVER['HTTP_ACCEPT_LANGUAGE']

.. php:global:: $_SERVER['HTTP_HOST']

Contains the recent host-header from the actual request (if sent). Is set by system.

This variable is used in :file:`includes/general.php`

.. php:global: $_SERVER['HTTPS']

Contains a non-empty value if the script is called by HTTPS. It is assumed to be the value "on".

This variable is used in :file:`includes/general.php`

.. php:global:: $_SERVER['PHP_SELF']


.. index:: $_SESSION

:php:global:`$_SESSION`
========================

.. php:global:: $_SESSION['mconn']

This global variable defines the status of the database connection

* TRUE if a connection could be established
* FALSE otherwise

.. index:: $_SESSION['_config']

----------------------------------
:php:global:`$_SESSION['_config']`
----------------------------------

.. php:global:: $_SESSION['_config']['errmsg']

This global variable is initialized in :file:`includes/general.php` with the value ''. 

.. php:global:: $_SESSION['_config']['filepath']

This global variable is initialized in :file:`includes/general.php` with the value '/www'. Meant is the root direcory. 

.. php:global:: $_SESSION['_config']['header']

.. php:global:: $_SESSION['_config']['language']

.. php:global:: $_SESSION['_config']['normalhostname']

This global variable defines the main CAcert-website, it is set in :file:`/includes/mysql.php`.

* "www.cacert.org" for production
* "test.cacert.org" for testing

.. php:global:: $_SESSION['_config']['recode']

.. php:global:: $_SESSION['_config']['securehostname']

This global variable defines the secure CAcert-website, it is set in :file:`/includes/mysql.php`.

* "secure.cacert.org" for production
* "       cacert.org" for testing

.. php:global:: $_SESSION['_config']['tverify']

This global variable defines TVERIFY, it is set in :file:`/includes/mysql.php`. 

* "tverify.cacert.org" for production
* "                  " for testing



.. todo:: checkout what TVERIFY means, check names for test-system

.. index:: $_SESSION['profile']

----------------------------------
:php:global:`$_SESSION['profile']`
----------------------------------

.. php:global:: $_SESSION['profile']['adadmin']

.. php:global:: $_SESSION['profile']['admin']

.. php:global:: $_SESSION['profile']['assurer']

.. php:global:: $_SESSION['profile']['dob']

.. php:global:: $_SESSION['profile']['email']

.. php:global:: $_SESSION['profile']['fname']

.. php:global:: $_SESSION['profile']['id']

Here the internal representation of the user is stored. It is used for database accesses. 'user'

.. php:global:: $_SESSION['profile']['lname']

.. php:global:: $_SESSION['profile']['locadmin']

.. php:global:: $_SESSION['profile']['mname']

.. php:global:: $_SESSION['profile']['orgadmin']

.. php:global:: $_SESSION['profile']['points']

Contains the total number of points for the user; calculated from :ref:`notary`.

.. php:global:: $_SESSION['profile']['suffix']

.. index:: globalConstants

================
Global Constants
================

.. php:const:: NULL_DATETIME

    This constant has the value '0000-00-00 00:00:00'

.. php:const:: THAWTE_REVOCATION_DATETIME

    This constant has the value '2010-11-16 00:00:00'.




==========
Exceptions
========== 

.. php:exception:: E_USER_NOTICE

.. php:exception:: E_USER_WARNING

.. php:exception:: E_USER_ERROR




