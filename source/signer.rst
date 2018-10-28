===================
The Signer Protocol
===================

Communication with the signer is performed via a serial connection. That has
to be established by the client before speaking the protocol defined here.

.. _signer-request-data-format:

Signer request data format specification
========================================

Protocol data is encoded with the following format:

.. table:: signer request message format

   ======= ==============================================================
   Byte    Data
   ======= ==============================================================
   0-2     length of header + data in network byte order
   3-12    action specific header
   13-15   length of first action specific content in network byte order
   15-N    fist action specific content string
   N+1-N+3 length of second action specific content in network byte order
   N+4-M   second action specific content string
   M+1-M+3 lenght of third action specific content in network byte order
   M+4-End third action specific content string
   ======= ==============================================================

Due to the length encoding in 3 bytes the messages can have a maximum length
of 8\ :sup:`3` = 2\ :sup:`24` Bytes which is around 16 MiB.

General header format
---------------------

Every protocol header (bytes 3-12 of protocol message) follows the same 8 byte
structure. The content of bits 3-8 are protocol action specific.

.. table:: general request header format

   ==== =============================================================
   Byte Value
   ==== =============================================================
   0    Version (``0x01``)
   1    Action
   2    System (``0x01`` for :ref:`client.pl <commmodule-client-pl>`)
   3    8 bits root
   4    8 bits configuration
   5    8 bits parameter
   6-7  16 bits parameter
   8    8 bits parameter
   ==== =============================================================

.. _signer-nul-request-format:

Format of NUL Requests
----------------------

NUL requests are sent at the end of each iteration in
:ref:`client.pl <commmodule-client-pl>`'s main loop.

.. table:: NUL request header format

   ==== =========================================================
   Byte Value
   ==== =========================================================
   0    Version (``0x01``)
   1    Action ``0x00``
   2    System (``0x01`` for :ref:`client.pl <commmodule-client-pl>`)
   3    ``0x00``
   4    ``0x00``
   5    ``0x00``
   6-7  ``0x0000``
   8    ``0x00``
   ==== =========================================================

**NUL Request Payload:**

- GMT timestamp in %m%d%H%M%Y.%S format
- ""
- ""

Format of X.509 signing request messages
----------------------------------------

X.509 signing request messages are sent in
:ref:`client.pl <commmodule-client-pl>`'s main loop for each requested
certificate.

.. table:: X.509 certificate signing request header format

   ==== =========================================================
   Byte Value
   ==== =========================================================
   0    Version (0x01)
   1    Action 0x01
   2    System (0x01 for :ref:`client.pl <commmodule-client-pl>`)
   3    Root
   4    Profile (see table :ref:`table-cert-profiles`)
   5    Message Digest Id (see table :ref:`table-md-ids`)
   6-7  Days in big-endian format
   8    Key type (``0x01`` for 'NS', ``0x00`` for others)
   ==== =========================================================

.. todo:: describe which root is identified by which root id

The key type is stored in the column *keytype* of the certificate request
table which is one of

- *domaincerts*
- *emailcerts*
- *orgdomaincerts*
- *orgemailcerts*

.. todo:: describe what 'NS' means for key type


**X.509 Signing Request Payload:**

- "$content"
- "$SAN"
- "$subject"

.. _table-cert-profiles:

.. table:: Certificate profile ids

   == ======================
   Id Profile
   == ======================
   0  Client (personal)
   1  Client (Organization)
   2  Client (Codesigning)
   3  Client (Machine)
   4  Client (ADS)
   5  Server (personal)
   6  Server (Organization)
   7  Server (Jabber)
   8  Server (OCSP)
   9  Server (Timestamp)
   10 Proxy
   11 SubCA
   == ======================

.. note::

   :ref:`client.pl <commmodule-client-pl>` supports profiles 0, 1, 2, 4,
   5, 6, 8 and 9 only.

.. _table-md-ids:

.. table:: Message digest ids

   == ==========
   Id Algorithm
   == ==========
   1  MD5
   2  SHA-1
   3  RIPE-MD160
   8  SHA-256
   9  SHA-384
   10 SHA-512
   == ==========


.. todo:: describe other request types

.. _signer-response-data-format:

Signer response data format specification
=========================================

.. todo:: describe signer response

Protocol messages
=================

.. _signer-message-handshake:

Handshake
---------

#. client sends 1 byte ``0x02`` to serial port
#. client reads 1 byte from serial port (with a 20 second timeout)
#. client checks whether the byte is ``0x10``

.. seqdiag::

   seqdiag handhake {
     client  ->  server [label = "0x02"];
     client <--  server [label = "0x10"];
   }

If anything different is received there was a protocol error and no further
messages should be sent over the serial connection.

Send data
---------

:Preconditions:
  successful :ref:`Handshake <signer-message-handshake>`,
  data is encoded according to the :ref:`signer-request-data-format`

#. client builds byte wise xor of all data bytes into 1 byte $xor
#. client sends concatenated $data string + xor-Byte + "rie4Ech7"
#. client reads 1 byte (with a 5 second timeout)
#. if received byte is ``0x11`` try again
#. if received byte is ``0x10`` the message has been sent successfully

.. seqdiag::

   seqdiag with_retry {
     client  -> client [label = "xor $data"];
     client  -> server [label = "$data . $xor . \"rie4Ech7\""];
     client <-- server [label = "0x11"];
     client  -> server [label = "$data . $xor . \"rie4Ech7\""];
     client <-- server [label = "0x10"];
   }

If anything different is received there was a protocol error and no further
messages should be sent over the serial connection.

