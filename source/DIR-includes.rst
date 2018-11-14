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

    :file:`includes/account_stuff.php` provides two procedures to be used for building the output of some HTML-pages.
    
    .. php:function:: showheader($title = "CAcert.org", $title2 = "")

        This function renders a page depending on the calling file. It is expected that only files

            www/wot.php (web-of-trust),

            www/gpg.php (gpg-key), 

            www/disputes.php (disputes) and 

            www/advertising.php (advertising) 
            
        are using this function.

        :param string $title: 
        :param string $title2:
        :global: * *(int)* - $id:
        :global: * *(string)* - $PHP_SELF:

    .. php:function:: showfooter()

        This function renders a page-footer.
        

.. sourcefile:: includes/account.php
    :uses:
        includes/loggedin.php
        includes/lib/l10n.php
        includes/lib/check_weak_key.php
        includes/notary.inc.php
        includes/general.php
        includes/account_stuff.php
        includes/notary.inc.php
        SOME__sanitizeHTML
        ..         ?-check_email
        ..         ?-make_hash
        includes/mysql.php__sendmail
        ..         ?-account_email_delete
        ..         ?-checkWeakKeySPKAC
        ..         ?-write_user_agreement
        ..         ?-generatecertpath
        ..         ?-checkWeakKeyCSR
        ..         ?-waitForResult
        ..         ?-checkEmail
        ..         ?-account_domain_delete
        ..         ?-clean_csr
        ..         ?-extractit
        ..         ?-getcn
        ..         ?-getalt
        ..         ?-HashAlgorithms::clean_csr
        ..         ?-checkWeakKeyX509
        ..         ?-unset
        ..         ?-valid_ticket_number
        ..         ?-write_se_log
        ..         ?-revoke_all_private_cert
        ..         ?-runCommand
        ..         ?-check_client_cert_running
        ..         ?-check_server_cert_running
        ..        ?-check_gpg_cert_running
        ..        ?-check_is_orgadmin
        ..        ?-account_delete



    .. php:function:: buildSubject(array $domains, $include_xmpp_addr = true)

        Build a subject string as needed by the signer

        :param array(string) $domains: First domain is used as CN and repeated in subjectAltName. Duplicates should already been removed
        :param bool $include_xmpp_addr: [default: true] Whether to include the XmppAddr in the subjectAltName. This is needed if the Jabber server is jabber.example.com but a Jabber ID on that server would be alice@example.com
        :return: * (string) - subject string as needed by the signer

    .. php:function:: buildSubjectFromSession()

        Builds the subject string from the session variables $_SESSION['_config']['rows'] and $_SESSION['_config']['altrows']

        :return: * (string) - 

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

   :file:`includes/notary.inc.php` provides a set of funktions; here listed in the given order:
   
    .. php:function:: query_init ($query)

        Accesss the database to execute the passed query.
       
        :param string $query:    query to execute
        :return: * (resource) - result of the passed query.
 
    .. php:function:: query_getnextrow ($res)

        Return the next row of a previous received result of a database query.
       
        :param resource $res:      Result of a previous database query.
        :return: * (object) - next row in the passed resource 
 
    .. php:function:: query_get_number_of_rows ($resultset)

        Return the number of rows of the passed $resource which has to be the result of a previous database query, select-statement
       
        :param resource $resultset: Result of a previous database query
        :return: * (int) - number of rows in the passed resource
    
    .. php:function:: get_number_of_assurances ($userid)

        Returns the number of assurances the user with the passed userid has given.

        :param int $userid: userid of be controled
        :return: * (int) - number of given assurances

    .. php:function:: get_number_of_ttpassurances ($userid)

        Returns the number of TTP-assurances the user with the passed userid has received.

        :param int $userid: userid of be controled
        :return: * (int) - number of received TTP-assurances

    .. php:function:: get_number_of_assurees ($userid)

        Returns the number of assurances the user with the passed userid has received.

        :param int $userid: userid of be controled
        :return: * (int) - number of received assurances

    .. php:function:: get_top_assurer_position ($no_of_assurances)

        Returns the ranking of an assurer with the passed number of given assurances.

        :param int $no_of_assurances: number of assurances 
        :return: * (int) - position at the list of top assurers

    .. php:function:: get_top_assuree_position ($no_of_assurees)

        Returns the ranking of an assuree with the passed number of received assurances.

        :param int $no_of_assurances: number of assurances 
        :return: * (int) - position at the list of top assurees

    .. php:function:: get_given_assurances($userid, $log=0)

        Get the list of assurances given by the user

        :param int $userid: id of the assurer
        :param int $log: if set to 1 also includes deleted assurances
        :return: * (resource) - a MySQL result set
	    
    .. php:function:: get_received_assurances($userid, $log=0)

        Get the list of assurances received by the user

        :param int $userid: id of the assuree
        :param int $log: if set to 1 also includes deleted assurances
        :return: * (resource) - a MySQL result set

    .. php:function:: get_given_assurances_summary ($userid)

        Get the count of given assurances of the user with the passed userid grouped by points, awarded, method
        
        :param int $userid: id of the assurer
        :return: * (resource) - list of number of given assurances grouped by points, awarded, method

    .. php:function:: get_received_assurances_summary ($userid)

        Get the count of received assurances of the user with the passed userid grouped by points, awarded, method
        
        :param int $userid: id of the assuree
        :return: * (resource) - list of number of received assurances grouped by points, awarded, method

    .. php:function:: get_user ($userid)

        Get data of user with the passed userid.

        :param int $userid: id of the user
        :return: * (resource) - data frum table users belonging to passed userid.

    .. php:function:: get_cats_state ($userid)

        Get the number of passed CATS for the given userid.
        
        :param int $userid: id of a user
        :return: * (int) - number of passed CATS

    .. php:function:: calc_awarded($row)

        Calculate awarded points (corrects some issues like out of range points or points that were issued by means that have been deprecated)

        :param array $row: associative array containing the data from the `notary` table
        :return: * (int) - the awarded points for this assurance

    .. php:function:: calc_experience(&$row, &$sum_points, &$sum_experience)

        Calculate the experience points from a given Assurance.

        :param array  $row: [inout] associative array containing the data from the `notary` table, the keys 'experience' and 'calc_awarded' will be added
        :param int    $sum_points: [inout] the sum of already counted assurance points the assurer issued
        :param int    $sum_experience: [inout] the sum of already counted experience points that were awarded to the assurer

    .. php:function:: calc_assurances(&$row, &$sum_points, &$sum_experience)

        Calculate the points received from a received Assurance.

        :param array  $row: [inout] associative array containing the data from the `notary` table, the keys 'experience' and 'calc_awarded' will be added
        :param int    $sum_points: [inout] the sum of already counted assurance points the assuree received
        :param int    $sum_experience: [inout] the sum of already counted experience points that were awarded to the assurer

    .. php:function:: show_user_link($user)

        Generate a link to the support engineer page for the user with the name of the user as link text

        :param array $user: associative array containing the data from the `user` table
        :return: * (string) - name of the user with the passed userid or System or deleted

    .. php:function:: show_email_link($user)

        Generate a link to the support engineer page for the user with the email address as link text
        
        :param array $user: associative array containing the data from the `user` table
        :return: * (string) - email-address

    .. php:function:: get_assurer_ranking($userid,&$num_of_assurances,&$rank_of_assurer)

        Getting the number of given assurances and the rank of the user with the passed userid.

        :param int $userid: id of an user
        :param int $num_of_assurances: [inout] number of given assurances
        :param int $rank_of_assurer: [inout] rank in assurer-list

    .. php:function:: get_assuree_ranking($userid,&$num_of_assurees,&$rank_of_assuree)

        Getting the number of received assurances and the rank of the user with the passed userid.

        :param int $userid: id of an user
        :param int $num_of_assurees: [inout] number of received assurances
        :param int $rank_of_assuree: [inout] rank in assuree-list

    .. php:function:: output_ranking($userid)

        Generating HTML-code for showing the assurer/assuree data
        
        :param int $userid: userid to build the page format

    .. php:function:: output_assurances_header($title, $support, $log)

        Render header for the assurance table (same for given/received)
        
        :param string $title: The title for the table
        :param int    $support: set to 1 if the output is for the support interface
        :param int    $log: if set to 1 also includes deleted assurances

    .. php:function:: output_assurances_footer($points_txt,$sumpoints,$experience_txt,$sumexperience,$support,$log)

        Render footer for the assurance table (same for given/received)
        
        :param string $points_txt: Description for sum of assurance points
        :param int    $sumpoints: sum of assurance points
        :param string $experience_txt: Description for sum of experience points
        :param int    $sumexperience: sum of experience points
        :param int    $support: set to 1 if the output is for the support interface
        :param int    $log: if set to 1 also includes deleted assurances

    .. php:function:: output_assurances_row($assurance,$userid,$other_user,$support,$ticketno,$log)

        Render an assurance for a view

        :param array   $assurance: associative array containing the data from the `notary` table
        :param int     $userid: Id of the user whichs given/received assurances are displayed
        :param array   $other_user: associative array containing the other users data from the `users` table
        :param int     $support: set to 1 if the output is for the support interface
        :param string  $ticketno: ticket number currently set in the support interface
        :param int     $log: if set to 1 also includes deleted assurances

    .. php:function:: output_summary_header()

        Render the header for the summary. 

    .. php:function:: output_summary_footer()

        Render the footer for the summary.

    .. php:function:: output_summary_row($title,$points,$points_countable,$remark)

        Render a row of the summary of points

        :param string $title: The description of the row
        :param inf $points: 
        :param int $points_countable:
        :param string $remark:

    .. todo:: check points and points_countable

    .. php:function:: output_given_assurances_content($userid,&$sum_points,&$sum_experience,$support,$ticketno,$log)

        Helper function to render assurances given by the user

        :param int  $userid: id of a user
        :param int &$sum_points: [out] sum of given points
        :param int &$sum_experience: [out] sum of experience points gained
        :param int  $support: set to 1 if the output is for the support interface
        :param string $ticketno: the ticket number set in the support interface
        :param int  $log: if set to 1 also includes deleted assurances

    .. php:function:: output_received_assurances_content($userid,&$sum_points,&$sum_experience,$support,$ticketno,$log)

        Helper function to render assurances received by the user

        :param int  $userid: id of a user
        :param int& $sum_points: [out] sum of received points
        :param int& $sum_experience: [out] sum of experience points the assurers gained
        :param int  $support: set to 1 if the output is for the support interface
        :param string $ticketno: the ticket number set in the support interface
        :param int  $log: if set to 1 also includes deleted assurances

    .. php:function:: check_date_limit ($userid,$age)

        Checks if the user with the passed userid has reached a given age.

        :param int $userid: id of a user
        :param int $age: the age to be checked against
        :return: * (int) - 1: if the given age is reached; 0 else

    .. php:function:: max_points($userid)

        Determin, how many points the user can issue at most.

        :param int $userid: id of a user
        :return: * (int) - max to issue points

    .. php:function:: output_summary_content($userid,$display_output)

        Calculate points and render them for output.

        :param int $userid: id of a user
        :param int $display_output: flag if to display (1) or not (0)
        :retur: * (int) - max to issue points

    .. php:function:: output_given_assurances($userid, $support=0, $ticketno='', $log=0)

        Render assurances given by the user

        :param int $userid: 
        :param int $support: set to 1 if the output is for the support interface
        :param string $ticketno: the ticket number set in the support interface
        :param int $log: if set to 1 also includes deleted assurances

    .. php:function:: output_received_assurances($userid, $support=0, $ticketno='', $log=0)

        Render assurances received by the user

        :param int $userid:
        :param int $support: set to 1 if the output is for the support interface
        :param string $ticketno: the ticket number set in the support interface
        :param int $log: if set to 1 also includes deleted assurances

    .. php:function:: output_summary($userid)

        Render the page output for a user.

        :param int $userid:

    .. todo:: more documentation from line 833 on 
















        
        
    
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
