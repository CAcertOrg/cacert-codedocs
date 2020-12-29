.. index:: ideas

============
Future ideas
============

Some ideas for future implementations have already be written in the
:ref:`conclusions section <general-conclusion>` of the general observations.
This section gives more insight into the rationale behind these ideas.

UTF-8 handling for everything
=============================

The world today is not only made of anglo-american and western european
countries. `Unicode`_ is the solution to support all languages of the world.
UTF-8 is a binary representation of Unicode that is compatible with ASCII and
a subset of ISO-8859-1.

.. _Unicode: https://home.unicode.org/

Implications
------------

- database needs to be migrated but should be straightforward
- reimplementation in the signer, signer_client, web application, test manager
  and probably CATS

Proper ASN.1 handling
=====================

Current PKI standards like :rfc:`5280` or the `CAB forum's baseline requirements`_
mandate the integrity of the :term:`ASN.1` objects in certificates. These standards
move towards UTF8String representation of names and have some strict validation
rules that can only be implemented by handling ASN.1 directly.

.. _CAB forum's baseline requirements: https://cabforum.org/baseline-requirements/

Implications
------------

- database migration or acceptance of old and new data formats
- clean separation of DNs (Subject DN and Issuer DN) and extensions (especially
  SubjectAlternativeName)
- reimplementation in signer, signer_client and web application
- changes to the signer protocol

Cleaner separation between components
=====================================

Separation of components improves the maintainability and reduces hard
dependencies between parts of the system. Each data store (filesystem, database
or message bus) should only belong to one component. All other components should
access required data by using :term:`APIs <API>` provided by the application
that owns the data store.

Implications
------------

- implementation of APIs
- decoupling via messaging (either publish/subscribe, queues or event streaming)
- restrict access to data stores via file system permissions, ACLs in databases
  or network separation

Modern web application standards
================================

To reach less technically affine people we need to implement a more modern web
application. If properly implemented this will also improve access for people
with disabilities.

We should try to implement some functionality as APIs so that they can be used
via both the classical web browser as well es API clients like mobile
applications or command line interfaces.

Implications
------------

- rewrite the web application

Secure development practices
============================

There are some established industry best practices for secure software
development. Implementing security as an afterthought is costly (for us
primarily in terms of time). Some documents that we should consider adopting
are referenced in:

- https://en.wikipedia.org/wiki/Secure_by_design
- https://en.wikipedia.org/wiki/Application_security

Implications
------------

- consider during application rewrite

Continuous integration
======================

We should aim for continuous integration of changes to avoid long living feature
branches. Branches of contributors should be built and tested automatically as
part of the review process. If we implement automated tests we could gain
confidence that changes do not introduce regressions.

Documented and automated deployment
===================================

The deployment of the software should be documented in form of step by step
instructions, test procedure descriptions and checklists.

When these instructions are sufficiently complete we can automate the deployment
and could also implement continuous deployment of test environments.

.. note::
   This would require a more sophisticated version control approach were we have
   integration branches for our test environments

.. note::
   Automated deployment of production environments is out of scope at the moment
   because it would probably break the required separation of responsible teams
   (software development, software assessment, infrastructure admin and critical
   admin).

.. blockdiag::
   :caption: Continous Integration / Deployment
   :desctable:

   blockdiag {
       Checkout -> Build -> Test -> Deploy -> Configure;
       Checkout  [description = "get data from code repository"];
       Build     [description = "build a release artifact including all required resources like static assets, translation files, etc."];
       Test      [description = "run test suite or ask people to manually install and test the release package"];
       Deploy    [description = "put the release bundle on a target test or production environment"];
       Configure [description = "take the necessary steps to make the application work in the target environment"];
   }

Configuration
-------------

Configuration should be separated from the actual code. Ideally configuration is
done via a configuration management system and is stored in version control too.

It is a good practice to have the configuration repository separated from the
code repository.

.. index:: signer
.. index:: protocol

New signer protocol
===================

To fix the shortcomings of the current signer protocol we need a new
implementation with better binary support, strong consistency checks and
testability.

The new signer protocol should:

- use a proper framing mechanism (i.e. `COBS`_) with a clearly recognizable
  frame separation byte (i.e. ``0x00``)
- have strong consistency checks (i.e. CRC32)
- have a well understood / documented payload format (i.e. `msgpack`_)
  with documented message types
- have control messages for resetting the connection, requesting
  redelivery of frames or other control functions (we should look at what
  existing protocols like PPP do)
- support binary payloads (DER encoded :term:`ASN.1`)
- support UTF-8 if necessary
- allow clients to request meta data about the signer

  - supported protocol versions
  - used CA certificates
  - used OpenPGP keys
  - supported certificate profiles (with some information about their
    supported key usages and audience)

- provide a way to communicate changes between signers to allow high
  availability this will need at least

  - announcement of revocations
  - announcement of new CA certificates

.. _COBS: https://en.wikipedia.org/wiki/Consistent_Overhead_Byte_Stuffing
.. _msgpack: https://msgpack.org/

.. index:: signer

New signer features
===================

Signer support for requesting CA certificates and GPG public keys (see
discussion in the previous section) used for signing to allow fully automated
bootstrapping of the signer client and web application.

The signer should support resigning of Sub CA certificates.

Email handling
==============

All email functionality should properly quote message headers and construct
proper MIME messages. This is relevant for both the signer_client and web
application(s).

We should not implement email handling ourselves. If we decide to use
`Go`_ we should look at the `Gomail`_ package.

.. _Go: https://golang.org
.. _Gomail: https://pkg.go.dev/gopkg.in/gomail.v2

New web application features
============================

ACME support
------------

The :term:`ACME` protocol has been standardized in :RFC:`8555` and allows
automated issuing of server certificates. We should provide this functionality
and document its usage with existing ACME client software.

Identity provider
-----------------

Our users provide us with identity information and our community verifies this
information. We already allow to use client certificates issued by our CA to
give users a way to authenticate using there CAcert verified user attributes.

We could also provide our users a way to use their information in modern web
authentication / authorization protocols like `OAuth 2`_ and `OpenID Connect`_.
We would need to implement the necessary endpoints for authentication,
authorization, user information retrieval and probably client registration.
We will also need a user interface to revoke access tokens granted to
applications.

.. _OAuth 2: https://oauth.net/2/
.. _OpenID Connect: https://openid.net/connect/

A rudimentary version of an :term:`IDP` could be implemented separately and
could just use information from the client certificates issued by our CA.

We could use OAuth2 or OpenID Connect for our own infrastructure too.

Cross cutting concerns
======================

.. index:: tests

Automated tests
---------------

All critical functionality should be covered by automated tests. This requires
the code to be testable by using modern software development techniques like
dependency injection. We need to have automated tests for at least the
following:

- signer protocol
- user registration
- verification of domains
- verification of email addresses
- assurance point calculation
- ...

.. index:: logging

Consistent logging
------------------

Our applications should log in a consistent format so that logs can be aggregated
this is especially important with distributed applications.

Log information should consist of at least the following information

- Timestamp (same timezone on all machines, ideally UTC)
- Log level (the level definition should be consistent)
- Source of the log (code file / module and if possible line)
- Error code (if an error occurred)
- Request identifier
- Message
- Traceback / stacktrace in case of unhandled errors
