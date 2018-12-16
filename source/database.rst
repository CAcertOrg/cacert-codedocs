==================
Database structure
==================

This part of the documentation describes the database schema of the CAcert
web application.


Miscellaneous Tables
====================


.. _schema_version:

--------------------
table schema_version
--------------------

This table holds the current webdb revision. This table was introduced in Nov 2011 by Software-Assessment project https://bugs.cacert.org/view.php?id=976. Current revision:  '1' , November 23, 2011

.. csv-table:: 
    :header-rows: 1
    :align: left
    :widths: 1,1,2

    "Field", "Type", "Comment"
    "id", "int(11)",   "PRIMARY KEY auto_increment"
    version,    int(11),   "NOT NULL UNIQUE"    
    when,        datetime,  "NOT NULL"


.. _AdminLog:

--------------
table AdminLog
--------------

Records changes of the DOB or the name executed by Support Engineers.
A record is also written when an account is "deleted" as a result of an Arbitration.

.. csv-table:: 
    :header-rows: 1
    :align: left

    Field, Type, NULL, Key, Default, Extras
    when, datetime , NO , , ,   
    old-lname, varchar(255), NO,  ,  ,   
    old-dob, date, NO, , , , 
    new-lname, varchar(255), NO, , , 
    new-dob, date, NO, , , ,
    uid, int(11), NO, , , ,
    adminid, int(11), NO, ,  ,
    type, varchar(50), NO,   ,NULL, See https://bugs.cacert.org/view.php?id=1135. New in Schema Version 4 (or 3?) 
    information, varchar(50), NO, , NULL, See https://bugs.cacert.org/view.php?id=1135. New in Schema Version 4 (or 3?) 
    actiontypeid, int(11), NO ?, , 1 ?, "Found this in notary.inc.php of commit 00f5b2872a, write_se_log. Nore documentation needed! Added this manually to testserver database."


.. _Advertising:

-----------------
table Advertising 
-----------------

Holds information about the advertising data, used for the Advertising on the WebDB

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","NULL","Key","Default","Extras"
    "id","int(10) unsigned","NO","auto_increment, primary","",""
    "replaceid","int(10) unsigned","NO","","",""
    "replaced","tinyint(3) unsigned","NO","","",""
    "orderid","tinyint(3) unsigned","NO","","",""
    "link","varchar(255)","NO","","",""
    "title","varchar(255)","NO","","",""
    "months","tinyint(3) unsigned","NO","","",""
    "who","int(10) unsigned","NO","","",""
    "when","datetime","NO","","",""
    "active","tinyint(3) unsigned","NO","","",""
    "approvedby","int(10) unsigned","NO","","",""
    "expires","datetime","NO","","",""


.. _Alerts:

------------
table Alerts
------------

Stores information about the alert settings of a user

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","NULL","Key","Default","Extras"
    "memid","int(11)","NO","primary key","0",""
    "general","tinyint(1)","NO","","0",""
    "country","tinyint(1)","NO","","0",""
    "regional","tinyint(1)","NO","","0",""
    "radius","tinyint(1)","NO","","0",""

    
.. _BadDomains:

----------------
table BadDomains
----------------

Should store information about domains that are not allowed to be used to add domains to a personal account

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","NULL","Key","Default","Extras"
    "domain","varchar(255)","NO","","",""


.. _DisputeDomain:

-------------------
table DisputeDomain
-------------------

An entry in this table is created if a user selects the menu item "Disputes/Abuses -> Domain Dispute".

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","NULL","Key","Default","Extras"
    "memid","int(11)","NO","","0",""
    "oldmemid","int(11)","NO","","0",""
    "domain","varchar(255)","NO","","",""
    "created","datetime","NO","","'0000-00-00 00:00:00'",""
    "hash","varchar(50)","NO","","‘’",""
    "attempts","int(1)","NO","","0",""
    "action","enum('accept','reject','failed')","NO","","accept",""


.. _DisputeEmail:

------------------
table DisputeEmail
------------------

An entry in this table is created if a user selects the menu item "Disputes/Abuses -> Email Dispute".

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Comment"
    "ID","int(11)","Primary Key"
    "memid","int(11)","ID of the user account that initiated the 'dispute'"
    "oldmemid","int(11)","ID of the user account owning the disputed mail address"
    "email","varchar(255)","Mail address which is disputed"
    "created","datetime",""
    "hash","varchar(50)","Hash used to identify this dispute in deep links. This will be cleared if the dispute is answered by the owner of the disputed address"
    "attempts","int(1)",""
    "action","enum('accept','reject','failed')","Reply of the owner to the dispute, initialized to 'accept'"
    "IP","varchar(20)","Remote IP address of machine from where the dispute was initiated"


.. _GPG:

---------
table GPG
---------

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","NULL","Key","Default","Extra"
    "id","int(11)","NO","","auto_increment",""
    "memid","int(11)","NO","","'0'",""
    "email","varchar(255)","NO","","''",""
    "level","int(1)","NO","","'0'",""
    "multiple","tinyint(1)","NO","","'0'",""
    "expires","tinyint(1)","NO","","'0'",""
    "csr","varchar(255)","NO","","''",""
    "crt","varchar(255)","NO","","''",""
    "issued","datetime","NO","","'0000-00-00 00:00:00'",""
    "expire","datetime","NO","","'0000-00-00 00:00:00'",""
    "keyid","char(18)","","","NULL",""
    "warning","tinyint(1)","NO","","'0'",""
    "description","varchar(100)","NO","","''","[[https://bugs.cacert.org/view.php?id=782|bug #782]]"


.. _LocAlias:

--------------
table LocAlias 
--------------


.. _News:

----------
table News
----------


.. _OrgAdminLog:

-----------------
table OrgAdminLog
-----------------

Structure identical to [[#AdminLog|AdminLog]], see [[https://bugs.cacert.org/view.php?id=1135|Bug#1135]].


.. _OTPHashes:

---------------
table OTPHashes
---------------


.. _PingLog:

-------------
table PingLog
-------------


.. _Root_Certs:

----------------
table Root_Certs
----------------

Just a simple list connecting the root cert's CN to an ID for efficient storage and reference. This table is needed in translations from certs serial numbers to user accounts. Also a request to this table is required in certs login procedure.

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Comment"
    "ID","int(2)","Primary Key"
    "Cert_Text","varchar(255)","CN as stored in the certificate"


.. _StampCache:

----------------
table StampCache
----------------


.. _Tickets:

-------------
table Tickets
-------------


Language related Tables 
=======================


.. _AddLang:

-------------
table AddLang
-------------

secondary languages list (account.php?id=41), a few rows

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Comment"
    "ID","int(?)","Primary Key"
    "userid","int(?)","a Users Id, who selected a secondary language"
    "lang","varchar(?)","language code, relates to table Languages locale, i.e. en_US, de_AT"

    
.. _Languages:

---------------
table Languages
---------------

primary languages list (account.php?id=41), approx 99 records, fixed content
 
.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Comment"
    "locale","varchar(?)","i.e. en_US, de_AT, de_CH"
    "en_co","varchar(?)","i.e. Austria, Germany, Switzerland"
    "en_lang","varchar(?)","i.e. German, Danish, German"
    "country","varchar(?)","i.e. &Ouml;sterreich, Danmark, Schweiz"
    "lang","varchar(?)","i.e. Deutsch, dansk, Deutsch"

 
Geographical Tables
===================


.. _Countries:

---------------
table Countries
---------------

List of Countries, fixed content

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Comment"
    "id","int(3)","Primary Key"
    "name","varchar(50)","country name"
    "acount","integer","how many assurers in this country?"

    
.. _Locations:

---------------
table Locations
---------------

List of Cities

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Comment"
    "id","int(7)","Primary Key"
    "regid","int(4)","city relates to this region"
    "ccid","int(3)","city relates to this country"
    "name","varchar(50)","city name"
    "lat","double(6,3)","latitude of the city"
    "long","double(6,3)","longitude of the city"
    "acount","integer","how many assurers in this city?"
    
    
.. _Regions:

-------------
table Regions
-------------

List of Regions, fixed content

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Comment"
    "id","int(5)","Primary Key"
    "ccid","int(3)","region relates to this country"
    "name","varchar(50)","region name"
    "acount","integer","how many assurers in this region?"

    
User Data
=========


.. _DomainCerts:

-----------------
table DomainCerts
-----------------

contains server certificates

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Null","Key","Default","Extra"
    "id","int(11)","NO","PRI","NULL","auto_increment"
    "domid","int(11)","NO","","0","reference to table domain.id"
    "serial","varchar(50)","NO","","",""
    "CN","varchar(255)","NO","","",""
    "subject","text","NO","","",""
    "csr_name","varchar(255)","NO","","",""
    "crt_name","varchar(255)","NO","","","contains the filename of the certificate (see pages/account/15.php)"
    "created","datetime","NO","","0000-00-00 00:00:00",""
    "modified","datetime","NO","","0000-00-00 00:00:00",""
    "revoked","datetime","NO","","0000-00-00 00:00:00","Is set to '1970-01-01 10:00:01' if the certificate shall be revoked. Acts as trigger for server process to do the revocation and to insert the current timestamp here."
    "expire","datetime","NO","","0000-00-00 00:00:00",""
    "warning","tinyint(1)","NO","","0",""
    "renewed","tinyint(1)","NO","","0",""
    "rootcert","int(2)","NO","","1",""
    "md","enum('md5','sha1','sha256','sha512')","NO","","sha512","[[https://bugs.cacert.org/view.php?id=1237|bug#1237]]"
    "type","tinyint(4)","YES","","NULL",""
    "pkhash","varchar(40)","YES","MUL","NULL",""
    "certhash","varchar(40)","YES","","NULL",""
    "coll_found","tinyint(1)","NO","","0",""
    "description","varchar(100)","NO","","''","[[https://bugs.cacert.org/view.php?id=782|bug #782]]"

    
.. _Domains:

-------------
table Domains
-------------

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Null","Key","Default","Extra"
    "id","int(11)","NO","PRI","NULL","auto_increment"
    "memid","int(11)","NO","MUL","0","reference to owner of the domain (users.id)"
    "domain","varchar(255)","NO","","",""
    "created","datetime","NO","","0000-00-00 00:00:00",""
    "modified","datetime","NO","","0000-00-00 00:00:00",""
    "deleted","datetime","NO","","0000-00-00 00:00:00",""
    "hash","varchar(50)","NO","","",""
    "attempts","int(1)","NO","","0",""

    
.. _DomLink:

-------------
table DomLink
-------------

similiar to !EmailLink

This one seems to link !DomainCerts to Domains.

There is an N:M relation between Domains and !DomainCerts, that is a certificate can contain multiple Domains (???) and there also can be multiple !DomainCerts for each Domain.

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Null","Key","Default","Extra"
    "certid","int(11)","NO","","0",""
    "domid","int(11)","NO","","0",""

    
.. _EmailCerts:

----------------
table EmailCerts
----------------

contains client certificates? Details to be verified!

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Null","Key","Default","Extra"
    "id","int(11)","NO","PRI","NULL","auto_increment"
    "memid","int(11)","NO","","0",""
    "serial","varchar(50)","NO","","",""
    "CN","varchar(255)","NO","","",""
    "subject","text","NO","","",""
    "keytype","char(2)","NO","","NS",""
    "codesign","tinyint(1)","NO","","0",""
    "csr_name","varchar(255)","NO","","",""
    "crt_name","varchar(255)","NO","","",""
    "created","datetime","NO","","0000-00-00 00:00:00",""
    "modified","datetime","NO","","0000-00-00 00:00:00",""
    "revoked","datetime","NO","","0000-00-00 00:00:00","Is set to '1970-01-01 10:00:01' if the certificate shall be revoked.  Acts as trigger for server process to do the revocation and to insert the current timestamp here."
    "expire","datetime","NO","","0000-00-00 00:00:00",""
    "warning","tinyint(1)","NO","","0",""
    "renewed","tinyint(1)","NO","","0",""
    "rootcert","int(2)","NO","","1",""
    "md","enum('md5','sha1','sha256','sha512')","NO","","sha512","[[https://bugs.cacert.org/view.php?id=1237|bug#1237]]"
    "type","tinyint(4)","YES","","NULL",""
    "disablelogin","int(1)","NO","","0","If set to 0 login using this certificate is allowed, checked in get_user_id_from_cert(). Set to 1 if login is not allowed."
    "pkhash","varchar(40)","YES","MUL","NULL",""
    "certhash","varchar(40)","YES","","NULL",""
    "coll_found","tinyint(1)","NO","","0",""
    "description","varchar(100)","NO","","''","[[https://bugs.cacert.org/view.php?id=782|bug #782]]"


.. _EmailLink:

---------------
table EmailLink
---------------

This one seems to link !EmailCerts to Emails.

There is an N:M relation between Emails and !EmailCerts, that is a certificate can contain multiple emails and there also can be multiple !EmailCerts for each Email.

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Null","Key","Default","Extra"
    "emailcertsid","int(11)","NO","MUL","0",""
    "emailid","int(11)","NO","","0",""

    
.. _Email:

-----------
table Email
-----------

Contains a list of all mail adresses (including the primary one named in the Users table) associated to user accounts.

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Comment"
    "ID","int(11)","Primary Key, autoincrement"
    "memid","int(11)","Foreign key to table Users, associated account"
    "email","varchar(255)",""
    "created","datetime",""
    "modified","datetime",""
    "deleted","datetime","timestamp of deletion, is set if the user deletes the mail address from his/her account."
    "hash","varchar(50)","If a new mail address is added the verification hash is stored here until the mail address has been verified. So ''email.hash = ' ' '' is a restriction that finds only verified mails."
    "attempts","int(1)","for verification process?"

    
.. _notary:

------------
table notary
------------

This table contains all data for events which award Trust Points: Assurances, TTP, Thawte Point transfers etc.

.. csv-table::
    :header-rows: 1
    :align: left
    :widths: 1,1,2

    Field,Type,Comment
    ID,int(11),"Primary Key, autoincrement"
    From,int(11),"Foreign key to users, user awarding the Trust Points"
    To,int(11),"Foreign key to users, user receiving the Trust Points"
    Awarded,int(3),Number of points the Assurer awarded
    Points,int(3),"Number of points credited to the receiver, may be less than awarded if receiver already has 100 points. With bug-1042 (new point calculation) installed, points will normally be set to 0 and ignored in calculation of assurance/experience points" 
    Method,enum,"Kind of event, definitions see below"
    Location,varchar(255),Free text
    Date,varchar(255),Date as entered in the Assure Someone application (free text)
    When,datetime,"Timestamp of form completion, recorded automatically"
    Expire,datetime,? Expiry timestamp of temporary awarded points?
    Sponsor,int(11),is Sponsor if value != 0 and Points=200 
    deleted ,datetime ,"NOT NULL, DEFAULT '0000-00-00 00:00:00'" 

methods
-------

  * '''[Face to Face Meeting]''' (Default) (Common Assurance)
  * '''[Trusted Third Parties]''' (Trusted 3rd Parties /pages/wot/6.php definition (https://bugs.cacert.org/view.php?id=855)), see comment below and https://bugs.cacert.org/view.php?id=1207!
  * '''[Thawte Points Transfer]'''
  * '''[Administrative Increase]''' 2 points for assuring someone else ("old" points counting) -or- "old" Super-Assurer increase
  * '''[CT Magazine - Germany]''' (deprecated)
  * '''[Temporary Increase]''' (raise +x experience points to give 35 pts)
  * '''[Unknown]''' ("old" undef state)
  * '''[TOPUP]''' (new TTP TOPUP program, https://bugs.cacert.org/view.php?id=863, https://bugs.cacert.org/view.php?id=864, https://bugs.cacert.org/view.php?id=888)
  * '''[TTP-Assisted]''', TTP assisted assurance according to new policy, the different name to [Trusted Third Party] from above is chosen to separate the two TTP programm from each other.


.. _Cats_Passed:

-----------------
table Cats_Passed
-----------------

Lists all the tests passed by a user.

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Comment"
    "id","int(11)","Primary Key, autoincrement"
    "user_id","int(11)","Foreign key to table users. User that has passed this test"
    "variant_id","int(11)","Foreign key to table Cats_variant. Exact kind of test passed."
    "pass_date","timestamp","Timestamp of passing the test"


.. _Cats_Type:

---------------
table Cats_Type
---------------

Contains all the different kind of tests, currently the Assurer Challenge.
Another planned type is the Test for Organisation Assurers.
This defines what a test is good for.

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Comment"
    "id","int(11)","Primary Key, autoincrement"
    "type_text","varchar(255)","Short description of the test type"


.. _Cats_Variant:

------------------
table Cats_Variant
------------------

Describes the variants of each cats_type, like translation in different languages.
This defines exactly which test has been passed.

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Comment"
    "id","int(11)","Primary Key, autoincrement"
    "type_id","int(11)","Foreign key to Cats_type"
    "test_text","varchar(255)","Short description of the test variant"


.. _TVerify:

-------------
table TVerify
-------------

Tables TVerify and TVerify-Vote are related to the TVerify program, which now is history since the Thawte Freemal program has been canceled quite some time ago.

TVerify contains one record per user request to be TVerified.

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Comment"
    "id","int(11)","Primary Key, autoincrement"
    "memid","int(11)","Foreign key to table Users, identifying the user which has submitted the contained data for review by TVerify Admins"
    "photoid","varchar(255)","Path to uploaded image of a photo id by the user"
    "URL","text","URL of the user in Thawte Freemail's Notary directory"
    "CN","text","(probably)The Common Name contained in the requesting user's Thawte Freemail certificate"
    "created","datetime","Timestamp when the request was initiated"
    "modified","datetime","Timestamp when the request is completed, that is, has 8 positive or 4 negative votes"


.. _TVerify-Vote:

------------------
table TVerify-Vote
------------------

Table contains one record for each vote made by a TVerify Admin

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Comment"
    "tverify","int(11)","Foreign key to table TVerify, identifying the record that's voted"
    "memid","int(11)","Foreign key to table Users, identifying the TVerify Admin who has made this vote"
    "when","datetime","Timestamp when the vote was made"
    "vote","tinyint(1)","Result of the vote, 1 for agree, -1 for disagree"
    "comment","varchar255","A free text comment by the TVerify Admin. It is included in the notification mail to the requesting user if the request is accepted or rejected."


.. _UserLocations:

-------------------
table UserLocations
-------------------

... seems to store the user's location...

Currently it is not used anywhere in the code, but it seems to be prepared to hold multiple locations per user.

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Null","Key","Default","Extra"
    "id","int(11)","NO","PRI","NULL","auto_increment"
    "memid","int(11)","NO","","0",""
    "ccid","int(11)","NO","","0",""
    "regid","int(11)","NO","","0",""
    "locid","int(11)","NO","","0",""


.. _users:

-----------
table users
-----------

Contains one record for each registered user.

.. csv-table::
    :header-rows: 1
    :align: left
    :widths: 1,1,2

    Field,Type,Comment
    id,int(11),"Primary Key, autoincrement"
    email,varchar(255),primary email address of the account
    password,varchar(255),encrypted
    fname,varchar(255),first name
    mname,varchar(255),middle name
    lname,varchar(255),last name
    suffix,varchar(50),name suffix
    dob,date,Date of Birth
    verified,int(1),1 if probe mail answered
    ccid,int(3),country: pointer to countries.id
    regid,int(5),region: pointer to regions.id
    locid,int(7),location: pointer to locations.id
    listme,int(1),1 if published in Assurer List
    codesign,int(1),1 if allowed to request code signing certs
    1024bit,tinyint(1),?
    contactinfo,varchar(255),?
    admin,tinyint(1),1 if user is admin
    ttpadmin,tinyint(1),"1 if user is TTP admin, it allows to set the Assurance Method to 'Trusted 3rd Parties' and leave some of those checkboxes on the Assurance page unchecked. It does not allow to issue more than the usual maximum points"
    orgadmin,tinyint(1),1 if user is Org admin
    board,tinyint(1),"1 if user has additional privileged of CAcert's board. In addition with ttpadmin allows to set all Assurance methods ('Face to Face Meeting', 'Trusted 3rd Parties', 'Thawte Points Transfer', 'Administrative Increase', 'CT Magazine - Germany'). Allows issuance of temporary increases if a sponsor (another user with board-flag set) is named."
    tverify,tinyint(1),1 if user is tverify admin (?)
    locadmin,tinyint(1),1 if user can administer the location database
    language,varchar(5),preferred language (?)
    Q1,varchar(255),Lost Password Question 1
    Q2,varchar(255),Lost Password Question 2
    Q3,varchar(255),Lost Password Question 3
    Q4,varchar(255),Lost Password Question 4
    Q5,varchar(255),Lost Password Question 5
    A1,varchar(255),Lost Password Answer 1
    A2,varchar(255),Lost Password Answer 2
    A3,varchar(255),Lost Password Answer 3
    A4,varchar(255),Lost Password Answer 4
    A5,varchar(255),Lost Password Answer 5
    created,datetime,timestamp of account creation (?)
    modified,datetime,timestamp of last account modification (?)
    deleted,datetime,"timestamp of account deletion, is set when the account is 'deleted' from the support interface"
    locked,tinyint(1),"1 if account is locked; prevents user to login with this account, to create, revoke or update certs, to do assurances" 
    otppin,smallint(4),something with OneTimePassword? (eg http://www.freeauth.org/ (WIP))
    uniqueID,varchar(255),"This is the 'SSO-ID' which is included in client certificates if the 'Add Single Sign On ID Information' button is selected during certificate creation. This ID is calculated during account creation (INSERT INTO Users) as a hash of the creation time and 64 byes of random. It is not guaranteed to be unique, but de facto collisions are extremly improbable."
    orphash,varchar(16),something with OneTimePassword?
    adadmin,tinyint(1), "0 = none, 1 = submit, 2 = approve" 
    assurer,int(2),"1 if user is Assurer (100 Assurance Points plus Challenge). This field is caching only, if performance does not forbid try to select the underlying data instead."
    assurer_blocked,tinyint(1),1 if user may not become assurer
    lastLoginAttempt,datetime,when the last failed login attempt for this user was


.. _User_Agreements:

---------------------
table User_Agreements
---------------------

Table to record instances when a user agreed to a specific agreement, currently only the CCA.

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Comment"
    "ID","int(11) NOT NULL","Primary Key, autoincrement"
    "memid","int(11)","Member for which the agreement is recorded"
    "secmemid","int(11)","user that is involved in the agreement (e.g. Assurer) / ID of another member involved, like the counterpart in an Assurance"
    "document","varchar(50)","Kind of agreement which got accepted, e.g. 'CCA'"
    "date","datetime","Time the agreement was recorded"
    "active","int(1)","whether the user actively agreed or if the agreement took place via an indirect process (e.g. Assurance)"
    "method","varchar(100)","in which process did the agreement take place (e.g. certificate issuance, account creation, assurance)"
    "comment","varchar(100)","user comment, Describes the circumstances, currently one of 'Assuring', 'Being assured', 'GPG', 'called from ...', depending on which action the user wanted to do when accepting the agreement."


Organisations Data
==================


.. _OrgDomainCerts:

--------------------
table OrgDomainCerts
--------------------

Contains Org server certificates

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Null","Key","Default","Extra"
    "id","int(11)","NO","PRI","NULL","auto_increment"
    "orgid","int(11)","NO","","0",""
    "subject","text","NO","","",""
    "serial","varchar(50)","NO","","",""
    "CN","varchar(255)","NO","","",""
    "csr_name","varchar(255)","NO","","",""
    "crt_name","varchar(255)","NO","","",""
    "created","datetime","NO","","0000-00-00 00:00:00",""
    "modified","datetime","NO","","0000-00-00 00:00:00",""
    "revoked","datetime","NO","","0000-00-00 00:00:00","Is set to '1970-01-01 10:00:01' if the certificate shall be revoked.  Acts as trigger for server process to do the revocation and to insert the current timestamp here."
    "expire","datetime","NO","","0000-00-00 00:00:00",""
    "renewed","tinyint(1)","NO","","0",""
    "rootcert","int(2)","NO","","1",""
    "md","enum('md5','sha1','sha256','sha512')","NO","","sha512","[[https://bugs.cacert.org/view.php?id=1237|bug#1237]]"
    "type","tinyint(4)","YES","","NULL",""
    "warning","tinyint(1)","NO","","0",""
    "pkhash","varchar(40)","YES","MUL","NULL",""
    "certhash","varchar(40)","YES","","NULL",""
    "coll_found","tinyint(1)","NO","","0",""
    "description","varchar(100)","NO","","''","[[https://bugs.cacert.org/view.php?id=782|bug #782]]"


.. _OrgDomains:

----------------
table OrgDomains
----------------

The domains associated to an Organisation (?)

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Null","Key","Default","Extra"
    "id","int(11)","NO","PRI","NULL","auto_increment"
    "orgid","int(11)","NO","","0",""
    "domain","varchar(255)","NO","","",""


.. _OrgDomLink:

----------------
table OrgDomLink
----------------

Cross-table linking Org(server?)certs with corresponding domain (?)

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Null","Key","Default","Extra"
    "orgcertid","int(11)","NO","PRI","0",""
    "orgdomid","int(11)","NO","PRI","0",""


.. _OrgEmailCerts:

-------------------
table OrgEmailCerts
-------------------

Contains Org client certificates

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Null","Key","Default","Extra"
    "id","int(11)","NO","PRI","NULL","auto_increment"
    "orgid","int(11)","NO","","0",""
    "serial","varchar(50)","NO","","",""
    "CN","varchar(255)","NO","","",""
    "subject","text","NO","","",""
    "keytype","char(2)","NO","","NS",""
    "csr_name","varchar(255)","NO","","",""
    "crt_name","varchar(255)","NO","","",""
    "created","datetime","NO","","0000-00-00 00:00:00",""
    "modified","datetime","NO","","0000-00-00 00:00:00",""
    "revoked","datetime","NO","","0000-00-00 00:00:00","Is set to '1970-01-01 10:00:01' if the certificate shall be revoked.  Acts as trigger for server process to do the revocation and to insert the current timestamp here."
    "expire","datetime","NO","","0000-00-00 00:00:00",""
    "renewed","tinyint(1)","NO","","0",""
    "rootcert","int(2)","NO","","1",""
    "md","enum('md5','sha1','sha256','sha512')","NO","","sha512","[[https://bugs.cacert.org/view.php?id=1237|bug#1237]]"
    "type","tinyint(4)","YES","","NULL",""
    "codesign","tinyint(1)","NO","","0",""
    "warning","tinyint(1)","NO","","0",""
    "pkhash","varchar(40)","YES","MUL","NULL",""
    "certhash","varchar(40)","YES","","NULL",""
    "coll_found","tinyint(1)","NO","","0",""
    "description","varchar(100)","NO","","''","[[https://bugs.cacert.org/view.php?id=782|bug #782]]"


.. _OrgEmailLink:

------------------
table OrgEmailLink
------------------

Cross-table linking Org(client?)certs with corresponding OrgDomain (?)

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Null","Key","Default","Extra"
    "emailcertsid","int(11)","NO","MUL","0",""
    "domid","int(11)","NO","","0",""


.. _OrgInfo:

-------------
table OrgInfo
-------------

One record for every registered organisation.

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Null","Key","Default","Extra"
    "id","int(11)","NO","PRI","NULL","auto_increment"
    "contact","varchar(255)","NO","","","email address"
    "O","varchar(255)","NO","","","Org name"
    "L","varchar(255)","NO","","","Org location (City)"
    "ST","varchar(255)","NO","","","Org state (?)"
    "C","char(2)","NO","","","Org country (e.g. 'DE') ISO-Alpha-2-Code?"
    "comments","text","NO","","",""
    "creator_id","int(11)","NO","","'0'","which Organisation Assurer entered the organisation?"
    "created","datetime","NO","","'0000-00-00 00:00:00'","when was the organisation entered?"
    "deleted","datetime","NO","","'0000-00-00 00:00:00'","allow for marking as deleted instead of really deleting"


.. _Org:

---------
table Org
---------

Links Organisations and corresponding OrgAdmins

.. csv-table:: 
    :header-rows: 1
    :align: left

    "Field","Type","Null","Key","Default","Extra"
    "orgid","int(11)","NO","PRI","0","References OrgInfo.id"
    "memid","int(11)","NO","PRI","0","References Users.id"
    "OU","varchar(255)","NO","","",""
    "masteracc","int(1)","NO","","0",""
    "comments","text","NO","","",""
    "creator_id","int(11)","NO","","'0'","which Organisation Assurer assigned the Organisation Admin?"
    "created","datetime","NO","","'0000-00-00 00:00:00'","when was the Organisation Admin assigned?"
    "deleted","datetime","NO","","'0000-00-00 00:00:00'","allow for marking as deleted instead of really deleting"

