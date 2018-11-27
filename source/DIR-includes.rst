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
        SOME__checkWeakKeySPKAC
        SOME__checkWeakKeyCSR
        SOME__checkWeakKeyX509        
        includes/notary.inc.php
        SOME__check_email_exists
        SOME__account_email_delete
        SOME__write_user_agreement
        SOME__account_domain_delete
        SOME__valid_ticket_number
        SOME__write_se_log
        SOME__revoke_all_private_cert
        SOME__check_client_cert_running
        SOME__check_server_cert_running
        SOME__check_gpg_cert_running
        SOME__check_is_orgadmin
        SOME__account_delete
        includes/general.php
        SOME__loadem
        SOME__csrf_check
        SOME__sanitizeHTML
        SOME__checkEmail
        SOME__make_hash
        SOME__generatecertpath
        SOME__waitForResult
        SOME__clean_csr
        SOME__extractit
        SOME__getcn
        SOME__getalt
        SOME__runCommand
        includes/account_stuff.php
        SOME__showheader
        SOME__showfooter
        includes/mysql.php
        SOME__sendmail
        includes/lib/account.php
        SOME__HashAlgorithms::clean_csr

    .. php:function:: buildSubject(array $domains, $include_xmpp_addr = true)

        Build a subject string as needed by the signer

        :param array(string) $domains: First domain is used as CN and repeated in subjectAltName. Duplicates should already been removed
        :param bool $include_xmpp_addr: [default: true] Whether to include the XmppAddr in the subjectAltName. This is needed if the Jabber server is jabber.example.com but a Jabber ID on that server would be alice@example.com
        :return: * (string) - subject string as needed by the signer

    .. php:function:: buildSubjectFromSession()

        Builds the subject string from the session variables $_SESSION['_config']['rows'] and $_SESSION['_config']['altrows']

        :return: * (string) - 
        
    .. todo:: analyze the module 
    

.. sourcefile:: includes/general_stuff.php

.. sourcefile:: includes/general.php

.. sourcefile:: includes/keygen.php

.. sourcefile:: includes/loggedin.php
    :uses:
        includes/lib/general.php
        SOME__get_user_id_from_cert
        includes/lib/l10n.php
        SOME__L10n::get_translation
        SOME__L10n::set_translation
        SOME__L10n::init_gettext
        includes/mysql.php
        includes/notary.inc.php
        SOME__get_user_agreement_status


    .. todo:: analyze the module 




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

        Returns the number of assurances the user with the passed userid has given. Uses :php:func:`query_init` and :php:func:`query_getnextrow`.

        :param int $userid: userid of be controled
        :return: * (int) - number of given assurances

    .. php:function:: get_number_of_ttpassurances ($userid)

        Returns the number of TTP-assurances the user with the passed userid has received. Uses :php:func:`query_init` and :php:func:`query_getnextrow`.

        :param int $userid: userid of be controled
        :return: * (int) - number of received TTP-assurances

    .. php:function:: get_number_of_assurees ($userid)

        Returns the number of assurances the user with the passed userid has received. Uses :php:func:`query_init` and :php:func:`query_getnextrow`.

        :param int $userid: userid of be controled
        :return: * (int) - number of received assurances

    .. php:function:: get_top_assurer_position ($no_of_assurances)

        Returns the ranking of an assurer with the passed number of given assurances. Uses :php:func:`query_init` and :php:func:`query_get_number_of_rows`.

        :param int $no_of_assurances: number of assurances 
        :return: * (int) - position at the list of top assurers

    .. php:function:: get_top_assuree_position ($no_of_assurees)

        Returns the ranking of an assuree with the passed number of received assurances. Uses :php:func:`query_init` and :php:func:`query_get_number_of_rows`.

        :param int $no_of_assurances: number of assurances 
        :return: * (int) - position at the list of top assurees

    .. php:function:: get_given_assurances($userid, $log=0)

        Get the list of assurances given by the user. Uses :php:func:`query_init`.

        :param int $userid: id of the assurer
        :param int $log: if set to 1 also includes deleted assurances
        :return: * (resource) - a MySQL result set
	    
    .. php:function:: get_received_assurances($userid, $log=0)

        Get the list of assurances received by the user. Uses :php:func:`query_init`.

        :param int $userid: id of the assuree
        :param int $log: if set to 1 also includes deleted assurances
        :return: * (resource) - a MySQL result set

    .. php:function:: get_given_assurances_summary ($userid)

        Get the count of given assurances of the user with the passed userid grouped by points, awarded, method. Uses :php:func:`query_init`.
        
        :param int $userid: id of the assurer
        :return: * (resource) - list of number of given assurances grouped by points, awarded, method

    .. php:function:: get_received_assurances_summary ($userid)

        Get the count of received assurances of the user with the passed userid grouped by points, awarded, method. Uses :php:func:`query_init`.
        
        :param int $userid: id of the assuree
        :return: * (resource) - list of number of received assurances grouped by points, awarded, method

    .. php:function:: get_user ($userid)

        Get data of user with the passed userid. Uses :php:func:`query_init`.

        :param int $userid: id of the user
        :return: * (resource) - data frum table users belonging to passed userid.

    .. php:function:: get_cats_state ($userid)

        Get the number of passed CATS for the given userid. Uses :php:func:`query_init`.
        
        :param int $userid: id of a user
        :return: * (int) - number of passed CATS

    .. php:function:: calc_awarded($row)

        Calculate awarded points (corrects some issues like out of range points or points that were issued by means that have been deprecated)

        :param array $row: associative array containing the data from the `notary` table
        :return: * (int) - the awarded points for this assurance

    .. php:function:: calc_experience(&$row, &$sum_points, &$sum_experience)

        Calculate the experience points from a given Assurance. Uses :php:func:`calc_awarded`.

        :param array  $row: [inout] associative array containing the data from the `notary` table, the keys 'experience' and 'calc_awarded' will be added
        :param int    $sum_points: [inout] the sum of already counted assurance points the assurer issued
        :param int    $sum_experience: [inout] the sum of already counted experience points that were awarded to the assurer

    .. php:function:: calc_assurances(&$row, &$sum_points, &$sum_experience)

        Calculate the points received from a received Assurance. Uses :php:func:`calc_awarded`.

        :param array  $row: [inout] associative array containing the data from the `notary` table, the keys 'experience' and 'calc_awarded' will be added
        :param int    $sum_points: [inout] the sum of already counted assurance points the assuree received
        :param int    $sum_experience: [inout] the sum of already counted experience points that were awarded to the assurer

    .. php:function:: show_user_link($user)

        Generate a link to the support engineer page for the user with the name of the user as link text. Uses :php:func:`sanitizeHTML`. 

        :param array $user: associative array containing the data from the `user` table
        :return: * (string) - name of the user with the passed userid or System or deleted

    .. php:function:: show_email_link($user)

        Generate a link to the support engineer page for the user with the email address as link text. Uses :php:func:`sanitizeHTML`. 
        
        :param array $user: associative array containing the data from the `user` table
        :return: * (string) - email-address

    .. php:function:: get_assurer_ranking($userid,&$num_of_assurances,&$rank_of_assurer)

        Getting the number of given assurances and the rank of the user with the passed userid. Uses :php:func:`get_number_of_assurances` and :php:func:`get_top_assurer_position`. 

        :param int $userid: id of an user
        :param int $num_of_assurances: [inout] number of given assurances
        :param int $rank_of_assurer: [inout] rank in assurer-list

    .. php:function:: get_assuree_ranking($userid,&$num_of_assurees,&$rank_of_assuree)

        Getting the number of received assurances and the rank of the user with the passed userid. Uses :php:func:`get_number_of_assurees` and :php:func:`get_top_assuree_position`. 

        :param int $userid: id of an user
        :param int $num_of_assurees: [inout] number of received assurances
        :param int $rank_of_assuree: [inout] rank in assuree-list

    .. php:function:: output_ranking($userid)

        Generating HTML-code for showing the assurer/assuree data. Uses :php:func:`get_assurer_ranking` and :php:func:`get_assuree_ranking`. 
        
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

        Render an assurance for a view. Uses :php:func:`show_email_link`, :php:func:`show_user_link`, :php:func:`sanitizeHTML` and :php:func:`make_csrf`.

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

        Helper function to render assurances given by the user. Uses :php:func:`get_given_assurances`, :php:func:`get_user`, :php:func:`calc_experience` and :php:func:`output_assurances_row`. 

        :param int  $userid: id of a user
        :param int &$sum_points: [out] sum of given points
        :param int &$sum_experience: [out] sum of experience points gained
        :param int  $support: set to 1 if the output is for the support interface
        :param string $ticketno: the ticket number set in the support interface
        :param int  $log: if set to 1 also includes deleted assurances

    .. php:function:: output_received_assurances_content($userid,&$sum_points,&$sum_experience,$support,$ticketno,$log)

        Helper function to render assurances received by the user. Uses :php:func:`get_received_assurances`, :php:func:`get_user`, :php:func:`calc_assurances` and :php:func:`output_assurances_row`.

        :param int  $userid: id of a user
        :param int& $sum_points: [out] sum of received points
        :param int& $sum_experience: [out] sum of experience points the assurers gained
        :param int  $support: set to 1 if the output is for the support interface
        :param string $ticketno: the ticket number set in the support interface
        :param int  $log: if set to 1 also includes deleted assurances

    .. php:function:: check_date_limit ($userid,$age)

        Checks if the user with the passed userid has reached a given age. Uses :php:func:`query_init`, :php:func:`query_get_number_of_rows`.

        :param int $userid: id of a user
        :param int $age: the age to be checked against
        :return: * (int) - 1: if the given age is reached; 0 else

    .. php:function:: max_points($userid)

        Determin, how many points the user can issue at most. Uses :php:func:`output_summary_content`.

        :param int $userid: id of a user
        :return: * (int) - max to issue points

    .. php:function:: output_summary_content($userid,$display_output)

        Calculate points and render them for output. Uses :php:func:`check_date_limit`, :php:func:`get_received_assurances_summary`, :php:func:`calc_awarded`, :php:func:`get_given_assurances_summary`, :php:func:`get_cats_state`, :php:func:`output_summary_row`.

        :param int $userid: id of a user
        :param int $display_output: flag if to display (1) or not (0)
        :retur: * (int) - max to issue points

    .. php:function:: output_given_assurances($userid, $support=0, $ticketno='', $log=0)

        Render assurances given by the user. Uses :php:func:`output_assurances_header`, :php:func:`output_given_assurances_content`, :php:func:`output_assurances_footer`.

        :param int $userid: id of a user
        :param int $support: set to 1 if the output is for the support interface
        :param string $ticketno: the ticket number set in the support interface
        :param int $log: if set to 1 also includes deleted assurances

    .. php:function:: output_received_assurances($userid, $support=0, $ticketno='', $log=0)

        Render assurances received by the user. Uses :php:func:`output_assurances_header`, :php:func:`output_received_assurances_content`, :php:func:`output_assurances_footer`.

        :param int $userid: id of a user
        :param int $support: set to 1 if the output is for the support interface
        :param string $ticketno: the ticket number set in the support interface
        :param int $log: if set to 1 also includes deleted assurances

    .. php:function:: output_summary($userid)

        Render the page output for a user. Uses :php:func:`output_summary_header`, :php:func:`output_summary_content`, :php:func:`output_summary_footer`.

        :param int $userid: id of a user

    .. php:function:: output_end_of_page()

        Adds a goBack-button to the page.

    .. php:function:: write_user_agreement($memid, $document, $method, $comment, $active=1, $secmemid=0)

        Writes a new record to the table user_agreement.

        :param mixed $memid: id of a user
        :param mixed $document:
        :param mixed $method:
        :param mixed $comment:
        :param integer $active:
        :param integer $secmemid:
        :return: 

    .. php:function:: get_user_agreement_status($memid, $type="CCA")

        Returns 1 if the user has an entry for the given type in user_agreement, 0 if no entry is recorded

        :param mixed $memid: userid
        :param string $type: "CCA"
        :return: * (int) - 1 if the user has an entry for the given type in user_agreement, 0 if no entry is recorded

    .. php:function:: get_first_user_agreement($memid, $type=null, $active=null)

        Get the first user_agreement entry of the requested type

        :param int $memid:
        :param string $type: the type of user agreement, by default all agreements are listed
        :param int $active: whether to get active or passive agreements: 

            * 0 := passive
            * 1 := active
            * null := both

        :return: * (array(string=>mixed)) - an associative array containing 'document', 'date', 'method', 'comment', 'active'.

    .. php:function:: get_last_user_agreement($memid, $type=null, $active=null)

        Get the last user_agreement entry of the requested type

        :param int $memid:
        :param string $type: the type of user agreement, by default all agreements are listed
        :param int $active: whether to get active or passive agreements: 

            * 0 := passive
            * 1 := active
            * null := both

        :return: * (array(string=>mixed)) - an associative array containing 'document', 'date', 'method', 'comment', 'active'.

    .. php:function:: get_user_agreements($memid, $type=null, $active=null)

        Get all user_agreement entrys of the requested type

        :param int $memid:
        :param string $type: the type of user agreement, by default all agreements are listed
        :param int $active: whether to get active or passive agreements: 

            * 0 := passive
            * 1 := active
            * null := both

        :return: * (resource) - a mysql result set containing all agreements

    .. php:function:: delete_user_agreement($memid, $type=false)

        Deletes all entries for a given type from user_agreement of a given user, if type is not given, delete all all

        :param mixed $memid: Member-id 
        :param string $type: the type of user agreement ; if false all

    .. :php:function:: AssureHead($confirmation,$checkname)

        Render the header for assurance-page /pages/wot/6.php

        :param string $confirmation: text of title
        :param string $checkname: textline including then ame of the person to be assured

    .. php:function:: AssureTextLine($field1,$field2)

        Prepares a text line for assurance-page /pages/wot/6.php; two cells in a row

        :param string $field1: text string
        :param string $field2: text string

    .. php:function:: AssureBoxLine($type,$text,$checked)

        Prepares a box line for assurance-page /pages/wot/6.php; two cells in a row, a checkbox with stats and a text

        :param string $type: type/name of checkbox
        :param string $text: text to present
        :param string $checked: status of the ceckbox

    .. php:function:: AssureMethodLine($text,$methods,$remark)

        Prepares another row for assurance-page /pages/wot/6.php containing the methods of the assurance

        :param string $text$: text
        :param array(string) $methods: possible methods of assurance
        :param string $remark: a possible remark to the assurance

    .. php:function:: AssureInboxLine($type,$field,$value,$description)

        Prepare an inBox line.

        :param string $type: name of the information shown in line
        :param string $field: readable name of the information of the line
        :param string $value: value of the information
        :param string $description: description/remarks to displayed the information

    .. php:function:: AssureFoot($oldid,$confirm)

        Prepares the footer of the assurance page /pages/wot/6.php.

        :param int $oldid: field to hide containing the actual id of the dialog
        :param string $confirm: text for confirmation

    .. php:function:: account_email_delete($mailid)

        Deletes an email entry from an acount, revolkes all certifcates for that email address. Uses :php:func:`revoke_all_client_cert`.

        :param int $mailid: Id of the email address to be deleted

    .. php:function:: account_domain_delete($domainid)

        Deletes an domain entry from an acount, revolkes all certifcates for that domain address. Uses :php:func:`revoke_all_server_cert`.

        :param int $domainid: Id of the domain to be deleted

    .. php:function:: account_delete($id, $arbno, $adminid)

        Deletes an account following the deleted account routnie V3 and change password (arbitration). Uses :php:func:`account_email_delete`, :php:func:`account_domain_delete`, 

        :param int $id: Id of the account to be deleted
        :param string $arbno: Arbitrationnumber that justifies the deletion.
        :param int $adminid: ID of the administrator who fullfilled the deletion

    .. php:function:: check_email_exists($email)

        Checks if an email address exists.

        :param string $email: Email address to be checked
        :returns: * (bool): true if email exists; else false

    .. php:function:: check_gpg_cert_running($uid,$cca=0)

        Checks if a non-expired gpg certificatation exists.

        :param int $uid: account ID to be checked for gpg certification
        :param int $cca: 0 if just expired, =1 if CCA retention +3 month should be obeyed
        :returns: * (bool) - true if a gpg certification exists; else false

    .. php:function:: check_client_cert_running($uid,$cca=0)

        Checks if a non-expired, non-revoked client certificate exists for an account.

        :param int $uid: account ID to be checked for client certificates
        :param int $cca: 0 if just expired, =1 if CCA retention +3 month should be obeyed
        :returns: * (bool) - true if a client certificate exists; else false

    .. php:function:: check_server_cert_running($uid,$cca=0)

        Checks if a non-expired, non-revoked server certificate exists for an account.

        :param int $uid: account ID to be checked for server certificates
        :param int $cca: 0 if just expired, =1 if CCA retention +3 month should be obeyed
        :returns: * (bool) - true if a server certificate exists; else false

    .. php:function:: check_is_orgadmin($uid)

        Checks if a given account is an organisation administrator.

        :param int $uid: account ID to be checked as organisation administrator
        :returns: * (bool) - true if the account belongs to an organisation administrator; else false

    .. php:function:: revoke_all_client_cert($mailid)

        Revokes all client certificates for a given email address. 

        :param int $mailid: ID of an email address.

    .. php:function:: function revoke_all_server_cert($domainid)

        Revokes all server certs for an domain.

        :param int $domainid: ID of an domain.

    .. php:function:: revoke_all_private_cert($uid)

        Revokes all certificates linked to a personal accounts, gpg revokation needs to be added to a later point. Uses :php:func:`revoke_all_client_cert`, :php:func:`revoke_all_server_cert`.

        :param int $uid: ID of the account whos certificates have to be rovoked
        
    .. php:function:: check_date_format($date, $year=2000)

        Checks if the date is entered in the right date format YYYY-MM-DD and if the date is after the 1st January of the given year

        :param mixed $date: Date to check
        :param integer $year: Year to check against 
        :returns: * (bool) - true if date is valid; false if not

    .. php:function:: check_date_difference($date, $diff=1)

        Checks if the given date is less or equal then today plus a given time difference

        :param mixed $date: Date to be checked
        :param integer $diff: difference in days (positive future, negative past) to add to the current date
        :returns: * (bool) - returns false if the date is larger then today + time difference

    .. php:function:: write_se_log($uid, $adminid, $type, $info)

        Records all support engineer actions changing a user account writing the information to the adminlog. 

        :param int $uid: id of the user account
        :param int $adminid: id of the admin
        :param string $type: the operation that was performed on the user account
        :param string $info: the ticket / arbitration number or other information
        :returns: * (bool) - true := success, false := error

    .. php:function:: valid_ticket_number($ticketno)

        Check if the entered information is a valid ticket or arbitration number.

        :param string $ticketno:
        :returns: * (bool) - 

    .. php:function:: get_user_data($userid, $deleted=0)

        Get all data of an account given by the id from the `users` table (function for handling account/43.php)

        :param int $userid:  account id
        :param int $deleted:  states if deleted data should be visible , default = 0 - not visible
        :returns: * (resource) - a mysql result set

    .. php:function:: get_alerts($userid)

        Get the alert settings for a user (function for handling account/43.php)

        :param int $userid: for the requested account
        :returns: * (array) - associative array

    .. php:function:: get_email_addresses($userid, $exclude, $deleted=0)

        Get all email addresses linked to the account (should be entered in account/2.php)

        :param int    $userid:
        :param string $exclude: if given the email address will be excluded
        :param int    $deleted: states if deleted data should be visible, default = 0 - not visible
        :returns: * (resource) - a mysql result set

    .. php:function:: get_domains($userid, $deleted=0)

        Get all domains linked to the account (should be entered in account/9.php).

        :param int $userid:
        :param int $deleted: states if deleted data should be visible, default = 0 - not visible
        :returns: * (resource) - a mysql result set
 
    .. php:function:: get_training_results($userid)

        Get all training results for the account (should be entered in account/55.php)

        :param int $userid:
        :returns: * (resource) - a mysql result set

    .. php:function:: get_se_log($userid)

        Get all SE log entries for the account

        :param int $userid:
        :returns: * (resource) - a mysql result set

    .. php:function:: get_client_certs($userid, $viewall=0)

        Get all client certificates linked to the account (add to account/5.php)

        :param int $userid:
        :param int $viewall: states if expired certs should be visible, default = 0 - not visible
        :returns: * (resource) - a mysql result set

    .. php:function:: get_server_certs($userid, $viewall=0)

        Get all server certs linked to the account (add to account/12.php)

        :param int $userid:
        :param int $viewall: states if expired certs should be visible, default = 0 - not visible
        :returns: * (resource - a mysql result set)

    .. php:function:: get_gpg_certs($userid, $viewall=0)

        Get all gpg certs linked to the account (add to gpg/2.php)

        :param int $userid:
        :param int $viewall: states if expired certs should be visible, default = 0 - not visible
        :returns: * (resource) - a mysql result set

    .. php:function:: output_log_email_header()

        Show the table header to the email table for the admin log

    .. php:function::  output_log_email($row, $primary)

        Show all email data for the admin log

        :param array  $row: associative array containing the column data
        :param string $primary: if given the primary address is highlighted

    .. php:function:: output_log_domains_header()

        Show the table header to the domains table for the admin log.

    .. php:function:: output_log_domains($row)

        Show the domain data for the admin log

        :param array $row: associative array containing the column data

    .. php:function:: output_log_agreement_header()

        Show the table header to the user agreement table for the admin log.

    .. php:function:: output_log_agreement($row)

        Show the agreement data for the admin log.

        :param array $row: associative array containing the column data

    .. php:function:: output_log_training_header()

        Show the table header to the training table (should be entered in account/55.php).

    .. php:function:: output_log_training($row)

        Show the training data (should be entered in account/55.php).

        :param array $row: associative array containing the column data

    .. php:function:: output_log_se_header($support=0)

        Show the table header to the SE log table for the admin log.

        :param int $support: if support = 1 more information is visible

    .. php:function:: output_log_se($row, $support=0)

        Show the SE log data for the admin log (should be entered in account/55.php)

        :param array $row: associative array containing the column data
        :param int   $support: if support = 1 more information is visible

    .. php:function:: output_client_cert_header($support=0, $readonly=true)

        Shows the table header to the client cert table (should be added to account/5.php)

        :param int  $support: if support = 1 some columns ar not visible
        :param bool $readonly: whether elements to modify data should be hidden, default is `true`

    .. php:function:: output_client_cert($row, $support=0, $readonly=true)

        Show the client cert data (should be entered in account/5.php)

        :param array $row: associative array containing the column data
        :param int   $support: if support = 1 some columns are not visible
        :param bool  $readonly: whether elements to modify data should be hidden, default is `true`

    .. php:function:: output_server_certs_header($support=0, $readonly=true)

        Show the table header to the server cert table (should be entered in account/12.php)

        :param int  $support: if support = 1 some columns ar not visible
        :param bool $readonly: whether elements to modify data should be hidden, default is `true`

    .. php:function:: output_server_certs($row, $support=0, $readonly=true)

        Show the server cert data (should be entered in account/12.php)

        :param array $row: associative array containing the column data
        :param int   $support: if support = 1 some columns are not visible
        :param bool  $readonly: whether elements to modify data should be hidden, default is `true`

    .. php:function:: output_gpg_certs_header($support=0, $readonly=true)

        Show the table header to the gpg cert table.

        :param int  $support: if support = 1 some columns ar not visible
        :param bool $readonly: whether elements to modify data should be hidden, default is `true` ($readonly is currently ignored but kept for consistency)

    .. php:function:: output_gpg_certs($row, $support=0, $readonly=true)

        Show the gpg cert data (should be entered in account/55.php)

        :param array $row: associative array containing the column data
        :param int   $support: if support = 1 some columns are not visible
        :param bool  $readonly: whether elements to modify data should be hidden, default is `true`

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

    :file:`includes/lib/general.php` provides the system with three functions.
    
    .. php:function:: get_user_id_from_cert($serial, $issuer_cn)

        Checks if the user may log in and retrieve the user id. Usually called with $_SERVER['SSL_CLIENT_M_SERIAL'] and $_SERVER['SSL_CLIENT_I_DN_CN']

        :param string $serial: usually $_SERVER['SSL_CLIENT_M_SERIAL']
        :param string $issuer_cn: usually $_SERVER['SSL_CLIENT_I_DN_CN']
        :return: * (int) - the user id, -1 in case of error

    .. php:function:: failWithId($errormessage)

        Produces a log entry with the error message with log level E_USER_WARN and a random ID an returns a message that can be displayed to the user including the generated ID
        
        :param $errormessage string: The error message that should be logged
        :return: * (string) - containing the generated ID that can be displayed to the user

    .. php:function:: runCommand($command, $input = "", &$output = null, &$errors = true)

        Runs a command on the shell and return it's exit code and output

        :param string $command: The command to run. Make sure that you escapeshellarg() any non-constant parts as this is executed on a shell!
        :param string|bool $input: The input that is passed to the command via STDIN, if true the real STDIN is passed through 
        :param string|bool $output: The output the command wrote to STDOUT (this is passed as reference), if true the output will be written to the real STDOUT. Output is ignored by default 
        :param string|bool $errors: The output the command wrote to STDERR (this is passed as reference), if true (default) the output will be written to the real STDERR 
        :return: * (int|bool) - The exit code of the command, true if the execution of the command failed (true because then <code>if (runCommand('echo "foo"')) handle_error();</code> will work) 

    .. php:function:: get_assurer_status($userID)

        Determine if the user with the passed userid is an assurer.
        
        :param int $userid: id of the user to be checked.
        :return: * (int) - 0 if user is an assurer; 3,7,11,15 if 100 ssurance points not reached; 5,7,13,15 if assurer test is missing; 9,11,13,15 if not allowed to b an assurer. 


.. sourcefile:: includes/lib/l10n.php

    :file:`includes/lib/l10n.php` defines the class L10n. Some methods use and manipulate the global variables:

    .. php:global:: $_SESSION['_config']['language']

    .. php:global:: $_SESSION['_config']['recode']

    .. php:class:: L10n

        Allowed/possible translations are "ar", "bg", "cs", "da", "de", "el", "en", "es", "fi", "fr", "hu", "it", "ja", "lv", "nl", "pl", "pt", "pt-br", "ru", "sv", "tr", "zh-cn", "zh-tw".

        Allowed locales are "ar_JO", "bg_BG", "cs_CZ", "da_DK", "de_DE", "el_GR", "en_US", "es_ES", "fa_IR", "fi_FI", "fr_FR", "he_IL", "hr_HR", "hu_HU", "id_ID", "is_IS", "it_IT", "ja_JP", "ka_GE", "ko_KR", "lv_LV", "nb_NO", "nl_NL", "pl_PL", "pt_PT", "pt_BR", "ro_RO", "ru_RU", "sl_SI", "sv_SE", "th_TH", "tr_TR", "uk_UA", "zh_CN", "zh_TW".

    .. php:staticmethod:: detect_language()

        It auto-detects the language that should be used and sets it. Only works for HTTP, not in a command line script. Priority: 

            #. explicit parameter "lang" passed in HTTP (e.g. via GET) 
            #. existing setting in the session (stick to the setting we had before)
            #. auto-detect via the HTTP Accept-Language header sent by the user agent

        Uses the global variables :php:global:`$_REQUEST["lang"]`, :php:global:`$_SERVER['HTTP_ACCEPT_LANGUAGE']`.

    .. php:staticmethod:: normalise_translation($translation_code)

        Normalise the translation code (e.g. from the old codes to the new)

        :param string $translation_code: the translation code as specified in the keys of $translations
        :return: * (string) - a translation code or the empty string if it can't be normalised

    .. php:staticmethod:: get_translation()

        Get the set translation. The method uses :php:global:`$_SESSION['_config']['language']`

        :returns: * (string) - a translation code or the empty string if not set

    .. php:staticmethod:: set_translation($translation_code)

        Set the translation to use. Sets also the :php:global:`ENV LANG=` and if run in a session :php:global:`$_SESSION['_config']['language']` and :php:global:`$_SESSION['_config']['recode']`.

        :param string $translation_code: the translation code as specified in the keys of {@link $translations}
        :returns: * (bool) - true if the translation has been set successfully; false if the $translation_code was not contained in the white list or could not be set for other reasons (e.g. setlocale() failed because the locale has not been set up on the system - details will be logged)

    .. php:staticmethod:: init_gettext($domain = 'messages')

        Sets up the text domain used by gettext. Uses :php:global:`$_SESSION['_config']['filepath']` and appends '/locale'.

        :param string $domain: the gettext domain that should be used, defaults to "messages"

    .. php:staticmethod:: set_recipient_language($accountid)

        Returns the language of a recipient to make sure that the language is correct

        :param int $accountid: accountnumber of the recipient
        
        
        
        
        
        
