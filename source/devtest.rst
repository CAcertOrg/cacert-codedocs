=======================================================
Build yourself a CAcert Test Machine for Development
=======================================================

As developers, at some point we all need a machine, whether for raw development,
Unit Testing, Integration or System Testing, so that we can be assured that our
code is ready to submit to the Software Reviewers and Approvers on its way to
deployment in Production.

That machine should be structured and configured to be as close a match
as possible to CAcert's production servers.

I have written this document and prepared scripts and other tools to help other
Developers easily create such a machine for their own purposes.

At present the machine that we are trying to match is a very old Debian machine
with PHP 5 installed.  Since we can no longer install a version of Debian that
is as old as is running in Production, I found that Debian 8 would still install,
at least at present, and PHP 5.7 can still be installed on that version of Debian.


Assumptions and Expectations
----------------------------

This document will describe the use of VirtualBox to create a working copy
of CAcert's Test Server for use in development of bug fixes and other code
intended for deployment to CAcert's servers.

It will describe all of the pieces that were used to create a working Debian 8
system, complete with various helper tools that allow this system to be used in
a stand-alone manner, effectively air-gapped from the Internet and E-Mail.

Since the CAcert code makes use of E-Mail for validating users and other 
internal purposes, this code must trap any outgoing e-mail so that it can
be examined and then returned to the system to fulfil those validation
purposes.

For future code development, much of this instruction can be repeated, with
principally, replacement of the Debian ISO and, therefore, upgrade of the
database server and PHP version within.


Software Development and Code Submission in CAcert
--------------------------------------------------

For those who are unfamiliar, there is a good document in the CAcert code tree, 
describing the process of managing the code involved in a CAcert bug fix or feature
submission.  The current version can be found at `Contributing`_.  Please note that
you should only make the minimum code changes necessary 
for each Pull Request ( PR ), to assist
the people involved in QA and Software Assesment.

Pre-requisites
--------------

* Internet connection
    - Not for testing, but for obtaining the software that we are putting
      into our virtual machine.
* VirtualBox [#f1]_
    - Remember that the OS of the host system does not have to match the OS of the virtual machine.
* ISO of Debian 7 or older, if possible. [#f2]_ [#f4]_
    - I was not able to install Debian 7 from a NetInst ISO, because of its repository requirement. [#f3]_
* Membership in the CAcert Development group and Mailing List: cacert-devel@lists.cacert.org.
* Access to our Bug Tracker `Mantis`_.

Everything else that I installed, I will provide in the instructions.


Create a running Debian
-----------------------

VirtualBox
++++++++++

For those of us familiar with VirtualBox, this is relatively straight-forward.
I will try to ease the path for the others.  If you have any questions, feel free
to contact me and other CAcert developers on the CAcert Developers mailing list
cacert-devel@lists.cacert.org.

VirtualBox can be found as an installable package for most modern systems,
whether Linux, as I run, MacOS ( OS X ) or Windows, as well as Solaris! [#f1]_

For our purposes, most modern machines, including laptops, can run VirtualBox
and our Development VM.  


Debian Versions
+++++++++++++++

Since CAcert's current production systems are running on ten-year-old versions of
Debian, for any bug fixing or enhancements to the current system, we need to try
and reproduce that environment as much as possible.

For that reason, I am specifying Debian 8, Jessie, as our standard Development
Environment, since it is the oldest still supported version of Debian.  If absolutely 
necessary, we could experiment by downloading older CD versions of Debian, but for
now, let us use Jessie.

Creating our Development and Test Platform
++++++++++++++++++++++++++++++++++++++++++

If you have not yet installed VirtualBox, do so now.

Then create a new VM, using the default values offered by VirtualBox.
When asked about memory, allocate at least 1GB, but no more than half
of the memory installed in the host machine.  Disks will normally
be created as compressed devices, so that you will not use as much as
you select for the disk size except under exceptional circumstances.

Mount the Debian ISO, and start the VM.


First Installation Steps
++++++++++++++++++++++++

* Aptitude
    - I prefer the command line version of aptitude to apt-get, so install it on every machine that I build.
    - Once it has been installed, do:
        + aptitude update
        + aptitude safe-upgrade
    - And then install the following tools with "aptitude install vim git rsync"
* Vim
* Git
* Rsync
* Others?
* Create a useful directory
    - mkdir tools
* Create a source directory
    - mkdir cacert


Installing PHP 5
++++++++++++++++++

PHP 5 is a normal part of Debian 7, so does not require any special effort to install.

* Installing PHP
    - aptitude update
    - aptitude install php5 php5-mysql


Installing MySQL 5
++++++++++++++++++

MySQL 5 is a normal part of Debian 7, so does not require any special effort to install.

* Installing MySQL
    - aptitude update
    - aptitude install mysql-5.5-server mysql-client


Installing Mail and MailHog
+++++++++++++++++++++++++++

* Configuring Exim4
    - cd /etc/exim4
    - vim update-exim4.conf.conf
    - find line with *dc_smarthost*
    - insert *localhost::1025* between quotes
    - Save and Exit
    - Restart Exim by *service exim4 restart*
        + This will compile the configuration file
* Downloading MailHog and Installing
* Finishing Configuration


Apache
++++++

* Editing Virtual Host

Installing Required Environment Variables
_________________________________________

* Deciding on values
* Editing Apache Virtual Host

Editing PHP.ini
_______________


Installing Test Manager
+++++++++++++++++++++++


Installing Source Code
++++++++++++++++++++++


Any More Steps
++++++++++++++

Starting Development
--------------------

Starting MailHog
++++++++++++++++

Etc
---



.. rubric:: Footnotes
.. [#f1] VirtualBox can be obtained either from a Linux distribution repository
	or directly from `VirtualBox`_.
.. [#f2] You can download Debian ISOs from `Debian`_, but finding older ones, such
	as the one that we want, can be a bit tricky.  I would normally use the `NetInst version`_
	because it is much smaller, and therefore quicker to download, but might be a bit longer to install than a full
	`DVD copy`_.  Note that while the NetInst version is
	less than 300 MB, there are three DVD images, totalling about 13 GB!  However, only the first DVD is required for most
	purposes.  Since the NetInst version requires a working Debian Mirror, while the DVD does not, for anything older than
	Debian 8, only the DVD ISO will work successfully.
.. [#f3] I did try downloading the DVD image for Debian 6, Squeeze, and created a Virtual Box VM using that.  Each disk image was 4.4 GB, so took a 
	while to download.  I only needed to download DVD-1 for the install, named debian-6.0.10-amd64-DVD-1.iso.
	However, after I created the Debian 6 version, I discovered that the *git* in that version would not work with GitHUB.
.. [#f4] Note that the source for Debian CD and DVD images older that the current version is `Debian Archive`_. The NetInst
	version can be found in the iso-cd directory.


.. _Mantis: https://bugs.cacert.org
.. _VirtualBox:  https://www.virtualbox.org/wiki/Downloads
.. _Debian:  https://debian.org
.. _NetInst version:  https://cdimage.debian.org/cdimage/archive/8.11.1/amd64/iso-cd/debian-8.11.1-amd64-netinst.iso
.. _DVD copy:  https://cdimage.debian.org/cdimage/archive/8.11.1/amd64/iso-dvd/
.. _Contributing: https://github.com/jandd/cacert-devel/blob/contribution-guide/CONTRIBUTING.md
.. _Debian Archive: http://cdimage.debian.org/cdimage/archive/

