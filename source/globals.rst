.. this file should contain all definitions of global variables

    .. php:global:: $_SESSION['mconn']

    This global variable defines the status of the database connection

    * TRUE if a connection could be established
    * FALSE otherwise

    .. php:global:: $_SESSION['_config']['normalhostname']

    This global variable defines the main CAcert-website

    * "www.cacert.org" for production
    * "test.cacert.org" for testing

    .. php:global:: $_SESSION['_config']['securehostname']

    This global variable defines the secure CAcert-website

    * "secure.cacert.org" for production
    * "       cacert.org" for testing

    .. php:global:: $_SESSION['_config']['tverify']

    This global variable defines TVERIFY 

    * "tverify.cacert.org" for production
    * "                  " for testing

    .. todo:: checkout what TVERIFY means, check names for test-system

    .. php:global:: $_SESSION['_config']['language'] 

    .. php:global:: $_SESSION['_config']['recode']
