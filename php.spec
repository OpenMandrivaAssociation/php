%define _build_pkgcheck_set %{nil}
%define _build_pkgcheck_srpm %{nil}

# For empty debugsource package
%global _debugsource_template %{nil}

%define build_test 0
%{?_with_test: %{expand: %%global build_test 1}}
%{?_without_test: %{expand: %%global build_test 0}}

%define build_libmagic 0
%{?_with_libmagic: %{expand: %%global build_libmagic 1}}
%{?_without_libmagic: %{expand: %%global build_libmagic 0}}

%define php8_common_major 5
%define libname %mklibname php8_common %{php8_common_major}

%define __noautoreq '.*/bin/awk|.*/bin/gawk'

%ifarch %{aarch64}
# Workaround for link time bug in lld 13.0.0
%global optflags %{optflags} -fuse-ld=bfd
%endif

#define beta RC4

Summary:	The PHP scripting language
Name:		php
Version:	8.2.1
%if 0%{?beta:1}
Release:	0.%{beta}.1
Source0:	https://github.com/php/php-src/archive/refs/tags/php-%{version}%{beta}.tar.gz
%else
Release:	1
Source0:	http://ch1.php.net/distributions/php-%{version}.tar.xz
%endif
Group:		Development/PHP
License:	PHP License
URL:		http://www.php.net
Source2:	maxlifetime
Source3:	php.crond
Source5:	php-fpm.sysconf
Source6:	php-fpm.logrotate
Source9:	php-fpm-tmpfiles.conf
Source10:	php.ini
Patch0:		php-8.0.0-rc1-allow-newer-bdb.patch
Patch1:		php-8.1.0-systzdata-v21.patch
#Patch2:		php-8.0.0-rc1-libtool-2.4.6.patch
# Based on https://wiki.php.net/rfc/socketactivation
Patch3:		php-fpm-socket-activation.patch

BuildRequires:	autoconf
BuildRequires:	autoconf-archive
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	byacc
BuildRequires:	file
BuildRequires:	flex
BuildRequires:	lemon
BuildRequires:	libtool
BuildRequires:	openssl
BuildRequires:	systemd
BuildRequires:	re2c >= 0.13.4

BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(libzip)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(libxcrypt)
BuildRequires:	pkgconfig(libpcre2-posix)
BuildRequires:	pkgconfig(libpcre2-8)
BuildRequires:	pkgconfig(libpcre2-16)
BuildRequires:	pkgconfig(libpcre2-32)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(xmlrpc)
BuildRequires:	pkgconfig(libacl)
BuildRequires:	apache-base

BuildRequires:	apache-devel >= 2.2.0
BuildRequires:	aspell-devel
BuildRequires:	bzip2-devel
BuildRequires:	c-client-devel >= 2007
BuildRequires:	db-devel
BuildRequires:	elfutils-devel
BuildRequires:	freetds-devel >= 0.63
BuildRequires:	gdbm-devel
BuildRequires:	gd-devel >= 2.0.33
BuildRequires:	gettext-devel
BuildRequires:	gmp-devel
BuildRequires:	gpm-devel
BuildRequires:	icu-devel >= 49.0
BuildRequires:	jpeg-devel
BuildRequires:	openldap-devel
BuildRequires:	sasl-devel
BuildRequires:	libtool-devel
BuildRequires:	mbfl-devel >= 1.2.0
BuildRequires:	mysql-devel >= 4.1.7
BuildRequires:	lm_sensors-devel
BuildRequires:	net-snmp-devel
BuildRequires:	net-snmp-mibs
BuildRequires:	onig-devel >= 5.9.2
BuildRequires:	pam-devel
BuildRequires:	postgresql-devel
BuildRequires:	readline-devel
BuildRequires:	recode-devel
BuildRequires:	t1lib-devel
BuildRequires:	tidy-devel
BuildRequires:	unixODBC-devel >= 2.2.1
BuildRequires:	xmlrpc-epi-devel
# For _pre_useradd
BuildRequires:	rpm-helper
%if %{build_libmagic}
BuildRequires:	magic-devel
%endif
Epoch: 3

# stupid postgresql... stupid build system...
# this is needed due to the postgresql packaging and due to bugs like this:
# https://qa.mandriva.com/show_bug.cgi?id=52527
%define postgresql_version %(pg_config &>/dev/null && pg_config 2>/dev/null | grep "^VERSION" | awk '{ print $4 }' 2>/dev/null |sed -E 's,(alpha|beta|rc).*,,' || echo 0)

%description
PHP is an HTML-embeddable scripting language. PHP offers built-in database
integration for several commercial and non-commercial database management
systems, so writing a database-enabled script with PHP is fairly simple. The
most common use of PHP coding is probably as a replacement for CGI scripts.

%package	cli
Summary:	PHP CLI interface
Group:		Development/Other
Requires:	%{libname} >= %{EVRD}
Requires:	php-ctype >= %{EVRD}
Requires:	php-filter >= %{EVRD}
Requires:	php-ftp >= %{EVRD}
Requires:	php-gettext >= %{EVRD}
# As of 7.4, php-hash seems to be builtin-only
%rename 	php-hash
Requires:	php-ini >= %{version}
Requires:	php-openssl >= %{EVRD}
Requires:	php-posix >= %{EVRD}
Requires:	php-session >= %{EVRD}
Requires:	php-sysvsem >= %{EVRD}
Requires:	php-sysvshm >= %{EVRD}
Requires:	php-timezonedb >= 3:2009.10
Requires:	php-tokenizer >= %{EVRD}
Requires:	php-xmlreader >= %{EVRD}
Requires:	php-xmlwriter >= %{EVRD}
Requires:	php-zlib >= %{EVRD}
Requires:	php-xml >= %{EVRD}
Obsoletes:	php-json < %{EVRD}
Provides:	php = %{EVRD}
Provides:	/usr/bin/php

%description	cli
PHP is an HTML-embeddable scripting language. PHP offers built-in database
integration for several commercial and non-commercial database management
systems, so writing a database-enabled script with PHP is fairly simple. The
most common use of PHP coding is probably as a replacement for CGI scripts.

This package contains a command-line (CLI) version of php. You must also
install libphp8_common. If you need apache module support, you also need to
install the apache-mod_php package.

%package	dbg
Summary:	Debugging version of the PHP CLI interface
Group:		Development/Other
Requires:	%{libname} >= %{EVRD}
Requires:	php-ctype >= %{EVRD}
Requires:	php-filter >= %{EVRD}
Requires:	php-ftp >= %{EVRD}
Requires:	php-gettext >= %{EVRD}
Requires:	php-ini >= %{version}
Requires:	php-openssl >= %{EVRD}
Requires:	php-posix >= %{EVRD}
Requires:	php-session >= %{EVRD}
Requires:	php-sysvsem >= %{EVRD}
Requires:	php-sysvshm >= %{EVRD}
Requires:	php-timezonedb >= 3:2009.10
Requires:	php-tokenizer >= %{EVRD}
Requires:	php-xmlreader >= %{EVRD}
Requires:	php-xmlwriter >= %{EVRD}
Requires:	php-zlib >= %{EVRD}
Requires:	php-xml >= %{EVRD}
Provides:	php = %{EVRD}

%description	dbg
PHP is an HTML-embeddable scripting language. PHP offers built-in database
integration for several commercial and non-commercial database management
systems, so writing a database-enabled script with PHP is fairly simple. The
most common use of PHP coding is probably as a replacement for CGI scripts.

This package contains a debugging version of php. You must also
install libphp8_common. If you need apache module support, you also need to
install the apache-mod_php package.

%package	cgi
Summary:	PHP CGI interface
Group:		Development/Other
Requires:	%{libname} >= %{EVRD}
Requires:	php-ctype >= %{EVRD}
Requires:	php-filter >= %{EVRD}
Requires:	php-ftp >= %{EVRD}
Requires:	php-gettext >= %{EVRD}
Requires:	php-ini >= %{version}
Requires:	php-openssl >= %{EVRD}
Requires:	php-posix >= %{EVRD}
Requires:	php-session >= %{EVRD}
Requires:	php-sysvsem >= %{EVRD}
Requires:	php-sysvshm >= %{EVRD}
Requires:	php-timezonedb >= 3:2009.10
Requires:	php-tokenizer >= %{EVRD}
Requires:	php-xmlreader >= %{EVRD}
Requires:	php-xmlwriter >= %{EVRD}
Requires:	php-zlib >= %{EVRD}
Requires:	php-xml >= %{EVRD}
Provides:	php = %{EVRD}
Obsoletes:	php-json < %{EVRD}

%description	cgi
PHP is an HTML-embeddable scripting language. PHP offers built-in database
integration for several commercial and non-commercial database management
systems, so writing a database-enabled script with PHP is fairly simple. The
most common use of PHP coding is probably as a replacement for CGI scripts.

This package contains a standalone (CGI) version of php with FastCGI support.
You must also install libphp8_common. If you need apache module support, you
also need to install the apache-mod_php package.

%package openlitespeed
Summary:	PHP module for the Openlitespeed web server
Group:		Servers
Requires:	openlitespeed
Requires:	%{libname} >= %{EVRD}
Requires:	php-ctype >= %{EVRD}
Requires:	php-filter >= %{EVRD}
Requires:	php-ftp >= %{EVRD}
Requires:	php-gettext >= %{EVRD}
Requires:	php-ini >= %{version}
Requires:	php-openssl >= %{EVRD}
Requires:	php-posix >= %{EVRD}
Requires:	php-session >= %{EVRD}
Requires:	php-sysvsem >= %{EVRD}
Requires:	php-sysvshm >= %{EVRD}
Requires:	php-timezonedb >= 3:2009.10
Requires:	php-tokenizer >= %{EVRD}
Requires:	php-xmlreader >= %{EVRD}
Requires:	php-xmlwriter >= %{EVRD}
Requires:	php-zlib >= %{EVRD}
Requires:	php-xml >= %{EVRD}

%description openlitespeed
PHP is an HTML-embeddable scripting language. PHP offers built-in database
integration for several commercial and non-commercial database management
systems, so writing a database-enabled script with PHP is fairly simple. The
most common use of PHP coding is probably as a replacement for CGI scripts.

This package contains a PHP module for the openlitespeed web server.

%package -n	%{libname}
Summary:	Shared library for PHP
Group:		Development/Other
Provides:	php-pcre = %{EVRD}
Provides:	php-simplexml = %{EVRD}
Requires:	systemd-units
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description -n	%{libname}
This package provides the common files to run with different implementations of
PHP. You need this package if you install the php standalone package or a
webserver with php support (ie: apache-mod_php).

%package	devel
Summary:	Development package for PHP
Group:		Development/C
Requires:	%{libname} >= %{EVRD}
Requires:	autoconf automake libtool
Requires:	bison
Requires:	byacc
Requires:	chrpath
Requires:	dos2unix
Requires:	flex
Requires:	openssl
Requires:	re2c >= 0.9.11
Requires:	tcl
Requires:	pam-devel
Requires:	pkgconfig(libpcre)
Requires:	pkgconfig(libxml-2.0)
Requires:	pkgconfig(libxslt)
Requires:	pkgconfig(openssl)


%description	devel
The php-devel package lets you compile dynamic extensions to PHP. Included
here is the source for the php extensions. Instead of recompiling the whole php
binary to add support for, say, oracle, install this package and use the new
self-contained extensions support. For more information, read the file
SELF-CONTAINED-EXTENSIONS.

%package	openssl
Summary:	OpenSSL extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	openssl
This is a dynamic shared object (DSO) for PHP that will add OpenSSL support.

%package	zlib
Summary:	Zlib extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	zlib
This is a dynamic shared object (DSO) for PHP that will add zlib compression
support to PHP.

%package	doc
Summary:	Documentation for PHP
Group:		Development/PHP

%description	doc
Documentation for php.

%package	bcmath
Summary:	The bcmath module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	bcmath
This is a dynamic shared object (DSO) for PHP that will add bc style precision
math functions support.

For arbitrary precision mathematics PHP offers the Binary Calculator which
supports numbers of any size and precision, represented as strings.

%package	bz2
Summary:	Bzip2 extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	bz2
This is a dynamic shared object (DSO) for PHP that will add bzip2 compression
support to PHP.

The bzip2 functions are used to transparently read and write bzip2 (.bz2)
compressed files.

%package	calendar
Summary:	Calendar extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	calendar
This is a dynamic shared object (DSO) for PHP that will add calendar support.

The calendar extension presents a series of functions to simplify converting
between different calendar formats. The intermediary or standard it is based on
is the Julian Day Count. The Julian Day Count is a count of days starting from
January 1st, 4713 B.C. To convert between calendar systems, you must first
convert to Julian Day Count, then to the calendar system of your choice. Julian
Day Count is very different from the Julian Calendar! For more information on
Julian Day Count, visit http://www.hermetic.ch/cal_stud/jdn.htm. For more
information on calendar systems visit
http://www.boogle.com/info/cal-overview.html. Excerpts from this page are
included in these instructions, and are in quotes.

%package	ctype
Summary:	Ctype extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	ctype
This is a dynamic shared object (DSO) for PHP that will add ctype support.

The functions provided by this extension check whether a character or string
falls into a certain character class according to the current locale (see also
setlocale()).

%package	curl
Summary:	Curl extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	curl
This is a dynamic shared object (DSO) for PHP that will add curl support.

PHP supports libcurl, a library created by Daniel Stenberg, that allows you to
connect and communicate to many different types of servers with many different
types of protocols. libcurl currently supports the http, https, ftp, gopher,
telnet, dict, file, and ldap protocols. libcurl also supports HTTPS
certificates, HTTP POST, HTTP PUT, FTP uploading (this can also be done with
PHP's ftp extension), HTTP form based upload, proxies, cookies, and
user+password authentication.

%package	dba
Summary:	DBA extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	dba
This is a dynamic shared object (DSO) for PHP that will add flat-file databases
(DBA) support.

These functions build the foundation for accessing Berkeley DB style databases.

This is a general abstraction layer for several file-based databases. As such,
functionality is limited to a common subset of features supported by modern
databases such as Sleepycat Software's DB2. (This is not to be confused with
IBM's DB2 software, which is supported through the ODBC functions.)

%package	dom
Summary:	Dom extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	dom
This is a dynamic shared object (DSO) for PHP that will add dom support.

The DOM extension is the replacement for the DOM XML extension from PHP 4. The
extension still contains many old functions, but they should no longer be used.
In particular, functions that are not object-oriented should be avoided.

The extension allows you to operate on an XML document with the DOM API.

%package	enchant
Summary:	Libenchant binder, support near all spelling tools
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	enchant
Enchant is a binder for libenchant. Libenchant provides a common API for many
spell libraries:

 - aspell/pspell (intended to replace ispell)
 - hspell (hebrew)
 - ispell 
 - myspell (OpenOffice project, mozilla)
 - uspell (primarily Yiddish, Hebrew, and Eastern European languages)
   A plugin system allows to add custom spell support.
   see www.abisource.com/enchant/

%package	filter
Summary:	Extension for safely dealing with input parameters
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	filter
The Input Filter extension is meant to address this issue by implementing a set
of filters and mechanisms that users can use to safely access their input data.

%package	ftp
Summary:	FTP extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	ftp
This is a dynamic shared object (DSO) for PHP that will add FTP support.

The functions in this extension implement client access to file servers
speaking the File Transfer Protocol (FTP) as defined in
http://www.faqs.org/rfcs/rfc959. This extension is meant for detailed access to
an FTP server providing a wide range of control to the executing script. If you
only wish to read from or write to a file on an FTP server, consider using the
ftp:// wrapper  with the filesystem functions  which provide a simpler and more
intuitive interface.

%package	gd
Summary:	GD extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	gd
This is a dynamic shared object (DSO) for PHP that will add GD support,
allowing you to create and manipulate images with PHP using the gd library.

PHP is not limited to creating just HTML output. It can also be used to create
and manipulate image files in a variety of different image formats, including
gif, png, jpg, wbmp, and xpm. Even more convenient, PHP can output image
streams directly to a browser. You will need to compile PHP with the GD library
of image functions for this to work. GD and PHP may also require other
libraries, depending on which image formats you want to work with.

You can use the image functions in PHP to get the size of JPEG, GIF, PNG, SWF,
TIFF and JPEG2000 images.

%package	gettext
Summary:	Gettext extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	gettext
This is a dynamic shared object (DSO) for PHP that will add gettext support.

The gettext functions implement an NLS (Native Language Support) API which can
be used to internationalize your PHP applications. Please see the gettext
documentation for your system for a thorough explanation of these functions or
view the docs at http://www.gnu.org/software/gettext/manual/gettext.html.

%package	gmp
Summary:	Gmp extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	gmp
This is a dynamic shared object (DSO) for PHP that will add arbitrary length
number support using the GNU MP library.

%package	hash
Summary:	HASH Message Digest Framework
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	hash
Native implementations of common message digest algorithms using a generic
factory method.

Message Digest (hash) engine. Allows direct or incremental processing of
arbitrary length messages using a variety of hashing algorithms.

%package	iconv
Summary:	Iconv extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	iconv
This is a dynamic shared object (DSO) for PHP that will add iconv support.

This module contains an interface to iconv character set conversion facility.
With this module, you can turn a string represented by a local character set
into the one represented by another character set, which may be the Unicode
character set. Supported character sets depend on the iconv implementation of
your system. Note that the iconv function on some systems may not work as you
expect. In such case, it'd be a good idea to install the GNU libiconv library.
It will most likely end up with more consistent results.

%package	imap
Summary:	IMAP extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	imap
This is a dynamic shared object (DSO) for PHP that will add IMAP support.

These functions are not limited to the IMAP protocol, despite their name. The
underlying c-client library also supports NNTP, POP3 and local mailbox access
methods.

%package	intl
Summary:	Internationalization extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	intl
This is a dynamic shared object (DSO) for PHP that will add
Internationalization support.

Internationalization extension implements ICU library functionality in PHP.

%package	ldap
Summary:	LDAP extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	ldap
This is a dynamic shared object (DSO) for PHP that will add LDAP support.

LDAP is the Lightweight Directory Access Protocol, and is a protocol used to
access "Directory Servers". The Directory is a special kind of database that
holds information in a tree structure.

The concept is similar to your hard disk directory structure, except that in
this context, the root directory is "The world" and the first level
subdirectories are "countries". Lower levels of the directory structure contain
entries for companies, organisations or places, while yet lower still we find
directory entries for people, and perhaps equipment or documents.

%package	mbstring
Summary:	MBstring extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}
# To make it easier to find for e.g. Roundcube requesting php-multibyte
Provides:	%{name}-multibyte = %{EVRD}

%description	mbstring
This is a dynamic shared object (DSO) for PHP that will add multibyte string
support.

mbstring provides multibyte specific string functions that help you deal with
multibyte encodings in PHP. In addition to that, mbstring handles character
encoding conversion between the possible encoding pairs. mbstring is designed
to handle Unicode-based encodings such as UTF-8 and UCS-2 and many single-byte
encodings for convenience.

%package	mysqli
Summary:	MySQL database module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}
%rename	%{name}-mysql
Requires:	%{name}-mysqlnd = %{EVRD}

%description	mysqli
This is a dynamic shared object (DSO) for PHP that will add MySQL database
support.

The mysqli extension allows you to access the functionality provided by MySQL
4.1 and above. It is an improved version of the older PHP MySQL driver,
offering various benefits. The developers of the PHP programming language
recommend using MySQLi when dealing with MySQL server versions 4.1.3 and newer
(takes advantage of new functionality)

More information about the MySQL Database server can be found at
http://www.mysql.com/

Documentation for MySQL can be found at http://dev.mysql.com/doc/.

Documentation for MySQLi can be found at http://www.php.net/manual/en/mysqli.overview.php.

%package	mysqlnd
Summary:	MySQL native database module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	mysqlnd
This is a dynamic shared object (DSO) for PHP that will add MySQL native
database support.

These functions allow you to access MySQL database servers. More information
about MySQL can be found at http://www.mysql.com/.

Documentation for MySQL can be found at http://dev.mysql.com/doc/.

%package	odbc
Summary:	ODBC extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	odbc
This is a dynamic shared object (DSO) for PHP that will add ODBC support.

In addition to normal ODBC support, the Unified ODBC functions in PHP allow you
to access several databases that have borrowed the semantics of the ODBC API to
implement their own API. Instead of maintaining multiple database drivers that
were all nearly identical, these drivers have been unified into a single set of
ODBC functions.

%package	opcache
Summary:	Opcode cache for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	opcache
Opcode cache for PHP

%package	pcntl
Summary:	Process Control extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	pcntl
This is a dynamic shared object (DSO) for PHP that will add process spawning
and control support. It supports functions like fork(), waitpid(), signal()
etc.

Process Control support in PHP implements the Unix style of process creation,
program execution, signal handling and process termination. Process Control
should not be enabled within a webserver environment and unexpected results may
happen if any Process Control functions are used within a webserver
environment.

%package	pdo
Summary:	PHP Data Objects Interface
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	pdo
PDO provides a uniform data access interface, sporting advanced features such
as prepared statements and bound parameters. PDO drivers are dynamically
loadable and may be developed independently from the core, but still accessed
using the same API.

Read the documentation at http://www.php.net/pdo for more information.

%package	pdo_dblib
Summary:	Sybase Interface driver for PDO
Group:		Development/PHP
Requires:	   freetds >= 0.63
Requires:	php-pdo >= %{EVRD}
Requires:	%{libname} >= %{EVRD}

%description	pdo_dblib
PDO_DBLIB is a driver that implements the PHP Data Objects (PDO) interface to
enable access from PHP to Microsoft SQL Server and Sybase databases through the
FreeTDS libary.

%package	pdo_mysql
Summary:	MySQL Interface driver for PDO
Group:		Development/PHP
Requires:	php-pdo >= %{EVRD}
Requires:	%{libname} >= %{EVRD}

%description	pdo_mysql
PDO_MYSQL is a driver that implements the PHP Data Objects (PDO) interface to
enable access from PHP to MySQL 3.x and 4.x databases.
 
PDO_MYSQL will take advantage of native prepared statement support present in
MySQL 4.1 and higher. If you're using an older version of the mysql client
libraries, PDO will emulate them for you.

%package	pdo_odbc
Summary:	ODBC v3 Interface driver for PDO
Group:		Development/PHP
Requires:	php-pdo >= %{EVRD}
Requires:	%{libname} >= %{EVRD}

%description	pdo_odbc
PDO_ODBC is a driver that implements the PHP Data Objects (PDO) interface to
enable access from PHP to databases through ODBC drivers or through the IBM DB2
Call Level Interface (DB2 CLI) library. PDO_ODBC currently supports three
different "flavours" of database drivers:
 
 o ibm-db2  - Supports access to IBM DB2 Universal Database, Cloudscape, and
			  Apache Derby servers through the free DB2 client.

 o unixODBC - Supports access to database servers through the unixODBC driver
			  manager and the database's own ODBC drivers.

 o generic  - Offers a compile option for ODBC driver managers that are not
			  explicitly supported by PDO_ODBC.

%package	pdo_pgsql
Summary:	PostgreSQL interface driver for PDO
Group:		Development/PHP
Requires:	php-pdo >= %{EVRD}
Requires:	%{libname} >= %{EVRD}
Requires:	postgresql-libs >= %{postgresql_version}

%description	pdo_pgsql
PDO_PGSQL is a driver that implements the PHP Data Objects (PDO) interface to
enable access from PHP to PostgreSQL databases.

%package	pdo_sqlite
Summary:	SQLite v3 Interface driver for PDO
Group:		Development/PHP
Requires:	php-pdo >= %{EVRD}
Requires:	%{libname} >= %{EVRD}

%description	pdo_sqlite
PDO_SQLITE is a driver that implements the PHP Data Objects (PDO) interface to
enable access to SQLite 3 databases.

This extension provides an SQLite v3 driver for PDO. SQLite V3 is NOT
compatible with the bundled SQLite 2 in PHP 7, but is a significant step
forwards, featuring complete utf-8 support, native support for blobs, native
support for prepared statements with bound parameters and improved concurrency.

%package	pgsql
Summary:	PostgreSQL database module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}
Requires:	postgresql-libs >= %{postgresql_version}

%description	pgsql
This is a dynamic shared object (DSO) for PHP that will add PostgreSQL database
support.

PostgreSQL database is Open Source product and available without cost.
Postgres, developed originally in the UC Berkeley Computer Science Department,
pioneered many of the object-relational concepts now becoming available in some
commercial databases. It provides SQL92/SQL99 language support, transactions,
referential integrity, stored procedures and type extensibility. PostgreSQL is
an open source descendant of this original Berkeley code.

%package	phar
Summary:	Allows running of complete applications out of .phar files
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}
Requires:	php-bz2

%description	phar
This is the extension version of PEAR's PHP_Archive package. Support for
zlib, bz2 and crc32 is achieved without any dependency other than the external
zlib or bz2 extension.

.phar files can be read using the phar stream, or with the Phar class. If the
SPL extension is available, a Phar object can be used as an array to iterate
over a phar's contents or to read files directly from the phar.

Phar archives can be created using the streams API or with the Phar class, if
the phar.readonly ini variable is set to false.

Full support for MD5 and SHA1 signatures is possible. Signatures can be
required if the ini variable phar.require_hash is set to true. When PECL
extension hash is avaiable then SHA-256 and SHA-512 signatures are supported as
well.

%package	posix
Summary:	POSIX extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	posix
This is a dynamic shared object (DSO) for PHP that will add POSIX functions
support to PHP.

This module contains an interface to those functions defined in the IEEE 1003.1
(POSIX.1) standards document which are not accessible through other means.
POSIX.1 for example defined the open(), read(), write() and close() functions,
too, which traditionally have been part of PHP 3 for a long time. Some more
system specific functions have not been available before, though, and this
module tries to remedy this by providing easy access to these functions.

%package	pspell
Summary:	Pspell extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	pspell
This is a dynamic shared object (DSO) for PHP that will add pspell support to
PHP.

These functions allow you to check the spelling of a word and offer
suggestions.

%package	readline
Summary:	Readline extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	readline
This PHP module adds support for readline functions (only for cli and cgi
SAPIs).

The readline() functions implement an interface to the GNU Readline library.
These are functions that provide editable command lines. An example being the
way Bash allows you to use the arrow keys to insert characters or scroll
through command history. Because of the interactive nature of this library, it
will be of little use for writing Web applications, but may be useful when
writing scripts used from a command line.

%package	recode
Summary:	Recode extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	recode
This is a dynamic shared object (DSO) for PHP that will add recode support
using the recode library.

This module contains an interface to the GNU Recode library. The GNU Recode
library converts files between various coded character sets and surface
encodings. When this cannot be achieved exactly, it may get rid of the
offending characters or fall back on approximations. The library recognises or
produces nearly 150 different character sets and is able to convert files
between almost any pair. Most RFC 1345 character sets are supported.

%package	session
Summary:	Session extension module for PHP
Group:		Development/PHP
Requires(pre,postun): rpm-helper
Requires:	%{libname} >= %{EVRD}

%description	session
This is a dynamic shared object (DSO) for PHP that will add session support.

Session support in PHP consists of a way to preserve certain data across
subsequent accesses. This enables you to build more customized applications and
increase the appeal of your web site.

A visitor accessing your web site is assigned a unique id, the so-called
session id. This is either stored in a cookie on the user side or is propagated
in the URL.

%package	shmop
Summary:	Shared Memory Operations extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	shmop
This is a dynamic shared object (DSO) for PHP that will add Shared Memory
Operations support.

Shmop is an easy to use set of functions that allows PHP to read, write, create
and delete Unix shared memory segments.

%package	snmp
Summary:	NET-SNMP extension module for PHP
Group:		Development/PHP
Requires:	net-snmp-mibs
Requires:	%{libname} >= %{EVRD}

%description	snmp
This is a dynamic shared object (DSO) for PHP that will add SNMP support using
the NET-SNMP libraries.

In order to use the SNMP functions you need to install the NET-SNMP package.

%package	soap
Summary:	Soap extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	soap
This is a dynamic shared object (DSO) for PHP that will add soap support.

The SOAP extension can be used to write SOAP Servers and Clients. It supports
subsets of SOAP 1.1, SOAP 1.2 and WSDL 1.1 specifications.

%package	sockets
Summary:	Sockets extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	sockets
This is a dynamic shared object (DSO) for PHP that will add sockets support.

The socket extension implements a low-level interface to the socket
communication functions based on the popular BSD sockets, providing the
possibility to act as a socket server as well as a client.

%package	sqlite3
Summary:	SQLite database bindings for PHP
Group:		Development/PHP
Requires:	php-pdo >= %{EVRD}
Requires:	%{libname} >= %{EVRD}
Obsoletes:	%name-sqlite

%description	sqlite3
This is an extension for the SQLite Embeddable SQL Database Engine. SQLite is a
C library that implements an embeddable SQL database engine. Programs that link
with the SQLite library can have SQL database access without running a separate
RDBMS process.

SQLite is not a client library used to connect to a big database server. SQLite
is the server. The SQLite library reads and writes directly to and from the
database files on disk.

%package	sysvmsg
Summary:	SysV msg extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	sysvmsg
This is a dynamic shared object (DSO) for PHP that will add SysV message queues
support.

%package	sysvsem
Summary:	SysV sem extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	sysvsem
This is a dynamic shared object (DSO) for PHP that will add SysV semaphores
support.

%package	sysvshm
Summary:	SysV shm extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	sysvshm
This is a dynamic shared object (DSO) for PHP that will add SysV Shared Memory
support.

%package	tidy
Summary:	Tidy HTML Repairing and Parsing for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	tidy
Tidy is a binding for the Tidy HTML clean and repair utility which allows you
to not only clean and otherwise manipluate HTML documents, but also traverse
the document tree using the Zend Engine 2 OO semantics.

%package	tokenizer
Summary:	Tokenizer extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	tokenizer
This is a dynamic shared object (DSO) for PHP that will add Tokenizer support.

The tokenizer functions provide an interface to the PHP tokenizer embedded in
the Zend Engine. Using these functions you may write your own PHP source
analyzing or modification tools without having to deal with the language
specification at the lexical level.

%package	xml
Summary:	XML extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	xml
This is a dynamic shared object (DSO) for PHP that will add XML support. This
extension lets you create XML parsers and then define handlers for different
XML events.

%package	xmlreader
Summary:	Xmlreader extension module for PHP
Group:		Development/PHP
Requires:	php-dom
Requires:	%{libname} >= %{EVRD}

%description	xmlreader
XMLReader represents a reader that provides non-cached, forward-only access to
XML data. It is based upon the xmlTextReader api from libxml

%package	xmlwriter
Summary:	Provides fast, non-cached, forward-only means to write XML data
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	xmlwriter
This extension wraps the libxml xmlWriter API. Represents a writer that
provides a non-cached, forward-only means of generating streams or files
containing XML data.

%package	xsl
Summary:	Xsl extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{EVRD}

%description	xsl
This is a dynamic shared object (DSO) for PHP that will add xsl support.

The XSL extension implements the XSL standard, performing XSLT transformations
using the libxslt library

%package	zip
Summary:	A zip management extension for PHP
Group:		Development/PHP

%description	zip
This is a dynamic shared object (DSO) for PHP that will add zip support to
create and read zip files using the libzip library.

%package	fpm
Summary:	PHP FastCGI Process Manager
Group:		Development/Other
Requires(post): rpm-helper
Requires(preun): rpm-helper
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires:	%{libname} >= %{EVRD}
Requires:	php-ctype >= %{EVRD}
Requires:	php-filter >= %{EVRD}
Requires:	php-ftp >= %{EVRD}
Requires:	php-gettext >= %{EVRD}
Requires:	php-ini >= %{version}
Requires:	php-openssl >= %{EVRD}
Requires:	php-posix >= %{EVRD}
Requires:	php-session >= %{EVRD}
Requires:	php-sysvsem >= %{EVRD}
Requires:	php-sysvshm >= %{EVRD}
Requires:	php-timezonedb >= 3:2009.10
Requires:	php-tokenizer >= %{EVRD}
Requires:	php-xmlreader >= %{EVRD}
Requires:	php-xmlwriter >= %{EVRD}
Requires:	php-zlib >= %{EVRD}
Requires:	php-xml >= %{EVRD}
Provides:	php = %{EVRD}
%rename php-fcgi

%description	fpm
PHP is an HTML-embeddable scripting language. PHP offers built-in database
integration for several commercial and non-commercial database management
systems, so writing a database-enabled script with PHP is fairly simple. The
most common use of PHP coding is probably as a replacement for CGI scripts.

This package contains the FastCGI Process Manager. You must also install
libphp8_common.

%package -n	apache-mod_php
Summary:	The PHP HTML-embedded scripting language for use with apache
Group:		System/Servers
Requires(pre,postun):	rpm-helper
Requires:	%{libname} = %{EVRD}
Requires:	apache-base >= 2.4.0
Requires:	apache-modules >= 2.4.0
Requires:	apache-mpm >= 2.4.0
Requires:	%{name}-ctype = %{EVRD}
Requires:	%{name}-filter = %{EVRD}
Requires:	%{name}-ftp = %{EVRD}
Requires:	%{name}-gettext = %{EVRD}
Requires:	%{name}-ini >= %{version}
Requires:	%{name}-openssl = %{EVRD}
Requires:	%{name}-pcre = %{EVRD}
Requires:	%{name}-posix = %{EVRD}
Requires:	%{name}-session = %{EVRD}
Requires:	%{name}-sysvsem = %{EVRD}
Requires:	%{name}-tokenizer = %{EVRD}
Requires:	%{name}-xmlreader = %{EVRD}
Requires:	%{name}-xmlwriter = %{EVRD}
Requires:	%{name}-zlib = %{EVRD}
Requires:	%{name}-xml = %{EVRD}
Requires:	%{name}-timezonedb >= 3:2009.10
Obsoletes:	php-json < %{EVRD}
Conflicts:	%{name}-suhosin < 0.9.29
Conflicts:	apache-mpm-worker >= 2.4.0
# mod_php with the event mpm is not an recommended by php devs, but
# is (at least somewhat) working. Let's not do a hard conflict.
# Conflicts:	apache-mpm-event >= 2.4.0
Provides:	mod_php = %{EVRD}
BuildRequires:	dos2unix

%description -n apache-mod_php
PHP is an HTML-embedded scripting language. PHP attempts to make it easy for
developers to write dynamically generated web pages. PHP also offers built-in
database integration for several commercial and non-commercial database
management systems, so writing a database-enabled web page with PHP is fairly
simple. The most common use of PHP coding is probably as a replacement for CGI
scripts. The %{name} module enables the apache web server to understand
and process the embedded PHP language in web pages.

This package contains PHP version 8. You'll also need to install the apache web
server.


%package -n	php-ini
Summary:	INI files for PHP
Group:		Development/Other

%description -n	php-ini
The php-ini package contains the ini file required for PHP.


%prep
export LC_ALL=en_US.utf-8
export LANG=en_US.utf-8
export LANGUAGE=en_US.utf-8
export LANGUAGES=en_US.utf-8
%autosetup -p1 -n %{name}-%{?beta:src-php-}%{version}%{?beta:%{beta}}

%if %{build_libmagic}
if ! [ -f %{_datadir}/misc/magic.mgc ]; then
	echo "ERROR: the %{_datadir}/misc/magic.mgc file is needed"
	exit 1
fi
%endif

# nuke bogus checks becuase i fixed this years ago in our recode package
rm -f ext/recode/config9.m4

# Change perms otherwise rpm would get fooled while finding requires
find -name "*.inc" | xargs chmod 644
# Can't use xargs here because of spaces in filenames
find -name "*.php*" -exec chmod 644 {} \;
find -name "*README*" | xargs chmod 644

# php8_module -> php_module to ease upgrades
# Can't use xargs here because of spaces in filenames
find -type f -exec sed -i -e 's,php8_module,php_module,g' {} \;
sed -i -e 's,APLOG_USE_MODULE(php8,APLOG_USE_MODULE(php,g' sapi/apache2handler/*

mkdir -p php-devel/extensions
mkdir -p php-devel/sapi

# Install test files in php-devel
cp -a tests php-devel

cp -dpR ext/* php-devel/extensions/
rm -f php-devel/extensions/informix/stub.c
rm -f php-devel/extensions/standard/.deps
rm -f php-devel/extensions/skeleton/EXPERIMENTAL

# SAPI
cp -dpR sapi/* php-devel/sapi/ 
rm -f php-devel/sapi/thttpd/stub.c
rm -f php-devel/sapi/cgi/php.sym
rm -f php-devel/sapi/fastcgi/php.sym
rm -f php-devel/sapi/pi3web/php.sym

# cleanup
find php-devel -name "*.droplet" -o -name "*~" | xargs rm -f

# don't ship MS Windows source
rm -rf php-devel/extensions/com_dotnet

# likewise with these:
find php-devel -name "*.dsp" | xargs rm -f
find php-devel -name "*.mak" | xargs rm -f
find php-devel -name "*.w32" | xargs rm

# maek sure using system libs
rm -rf ext/pcre/pcrelib
rm -rf ext/pdo_sqlite/sqlite
rm -rf ext/xmlrpc/libxmlrpc

scripts/dev/genfiles

# Included ltmain.sh is obsolete and breaks lto
#rm -f ltmain.sh build/ltmain.sh build/libtool.m4
# including a local libtool.m4 is just wrong, let aclocal
# pick the right version
#sed -i -e '/libtool.m4/d' configure.ac
libtoolize --force
# Replace outdated crappy force-included versions of auto* macros
cat $(aclocal --print-ac-dir)/{libtool,ltoptions,ltsugar,ltversion,lt~obsolete}.m4 >build/libtool.m4
cp -f %{_datadir}/aclocal/{ax_check_compile_flag,ax_func_which_gethostbyname_r,ax_gcc_func_attribute}.m4 build/
touch configure.ac
./buildconf --force

%build
%serverbuild

#cp -f %{_datadir}/libtool/build-aux/config.* .

export CC=%{__cc}
export CXX=%{__cxx}

# it does not work with -fPIE and someone added that to the serverbuild macro...
CFLAGS=`echo $CFLAGS|sed -e 's|-fPIE||g'`
CXXFLAGS=`echo $CXXFLAGS|sed -e 's|-fPIE||g'`

#export CFLAGS="`echo ${CFLAGS} | sed s/O2/O0/` -fPIC -L%{_libdir} -fno-strict-aliasing"
export CFLAGS="${CFLAGS} -fPIC -L%{_libdir} -fno-strict-aliasing"
export CXXFLAGS="${CFLAGS}"
export RPM_OPT_FLAGS="${CFLAGS}"

cat > php-devel/buildext <<EOF
#!/bin/bash
exec $CC -Wall -fPIC -shared $CFLAGS \\
	-I. \`%{_bindir}/php-config --includes\` \\
	-I%{_includedir}/libxml2 \\
	-I%{_includedir}/freetype \\
	-I%{_includedir}/openssl \\
	-I%{_usrsrc}/php-devel/ext \\
	-I%{_includedir}/\$1 \\
	\$4 \$2 -o \$1.so \$3 -lc
EOF

chmod 755 php-devel/buildext

rm -f configure
rm -rf autom4te.cache
libtoolize --force
cat `aclocal --print-ac-dir`/{libtool,ltoptions,ltsugar,ltversion,lt~obsolete}.m4 >build/libtool.m4
touch configure.ac
#sed -i -e '/PHP_AUTOCONF/iaclocal -I build' buildconf
./buildconf --force
cp -f %{_datadir}/libtool/build-aux/* .
cp -f %{_bindir}/libtool .

if grep LT_INIT configure; then
	echo "autoconf ended up putting a literal LT_INIT into configure, this will break things"
	exit 1
fi

# Do this patch with a perl hack...
perl -pi -e "s|'\\\$install_libdir'|'%{_libdir}'|" ltmain.sh

export oldstyleextdir=yes
export EXTENSION_DIR="%{_libdir}/php/extensions"
export PROG_SENDMAIL="%{_sbindir}/sendmail"
export GD_SHARED_LIBADD="$GD_SHARED_LIBADD -lm"
SAFE_LDFLAGS=`echo %{build_ldflags}|sed -e 's|-Wl,--no-undefined||g'`
export EXTRA_LIBS="-lz"
export LDFLAGS="$SAFE_LDFLAGS"

# never use "--disable-rpath", it does the opposite

# Configure php8
# FIXME switch to external gd (--with-gd=shared,%_prefix) once php bug #60108 is fixed
for i in fpm cgi cli embed apxs litespeed; do
	mkdir build-$i
	cd build-$i
	ln -s %{_bindir}/libtool .
../configure \
	`[ $i = fpm ] && echo --disable-cli --enable-fpm --with-fpm-user=apache --with-fpm-group=apache --with-fpm-systemd --with-fpm-acl ` \
	`[ $i = cgi ] && echo --disable-cli` \
	`[ $i = cli ] && echo --disable-cgi --enable-cli` \
	`[ $i = embed ] && echo --disable-cli --enable-embed=shared` \
	`[ $i = apxs ] && echo --with-apxs2=%{_bindir}/apxs` \
	`[ $i = litespeed ] && echo --enable-litespeed` \
	--build=%{_build} \
	--prefix=%{_prefix} \
	--exec-prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--sbindir=%{_sbindir} \
	--sysconfdir=%{_sysconfdir} \
	--datadir=%{_datadir} \
	--includedir=%{_includedir} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--localstatedir=/var/lib \
	--mandir=%{_mandir} \
	--enable-zts \
	--enable-rtld-now \
	--with-layout=GNU \
	--with-external-pcre \
	--with-libdir=%{_lib} \
	--with-config-file-path=%{_sysconfdir} \
	--with-config-file-scan-dir=%{_sysconfdir}/php.d \
	--disable-debug  \
	--with-zlib=%{_prefix} \
	--with-pdo-odbc=unixODBC \
	--with-zlib=shared,%{_prefix} --with-zlib-dir=%{_prefix} \
	--with-openssl=shared,%{_prefix} \
	--without-pear \
	--enable-bcmath=shared \
	--with-bz2=shared,%{_prefix} \
	--enable-calendar=shared \
	--enable-ctype=shared \
	--with-curl=shared,%{_prefix} \
	--enable-dba=shared --with-gdbm --with-db4 --with-cdb  \
	--enable-dom=shared,%{_prefix} \
	--with-enchant=shared,%{_prefix} \
	--with-exif=shared,%{_prefix} \
	--enable-exif \
	--enable-fileinfo \
	--enable-filter=shared \
	--enable-intl=shared \
	--with-openssl-dir=%{_prefix} --enable-ftp=shared \
	--with-zlib-dir=%{_prefix} \
	--with-gettext=shared,%{_prefix} \
	--with-gmp=shared,%{_prefix} \
	--with-iconv=shared \
	--with-imap=shared,%{_prefix} --with-imap-ssl=%{_prefix} \
	--with-ldap=shared,%{_prefix} --with-ldap-sasl=%{_prefix} \
	--enable-mbstring=shared,%{_prefix} --enable-mbregex \
	--with-mysql-sock=/run/mysqld/mysql.sock --with-zlib-dir=%{_prefix} \
	--with-mysqli=shared,mysqlnd \
	--enable-mysqlnd=shared,%{_prefix} \
	--with-unixODBC=shared,%{_prefix} \
	--enable-pcntl=shared \
	--enable-pdo=shared,%{_prefix} --with-pdo-dblib=shared,%{_prefix} --with-pdo-mysql=shared,%{_prefix} --with-pdo-odbc=shared,unixODBC,%{_prefix} --with-pdo-pgsql=shared,%{_prefix} --with-pdo-sqlite=shared,%{_prefix} \
	--with-pgsql=shared,%{_prefix} \
	--enable-phar=shared \
	--enable-posix=shared \
	--with-pspell=shared,%{_prefix} \
	--with-readline=shared,%{_prefix} \
	--enable-session=shared,%{_prefix} \
	--enable-shmop=shared,%{_prefix} \
	--enable-simplexml \
	--with-snmp=shared,%{_prefix} \
	--enable-soap=shared,%{_prefix} \
	--enable-sockets=shared,%{_prefix} \
	--with-sqlite3=shared,%{_prefix} \
	--enable-sysvmsg=shared,%{_prefix} \
	--enable-sysvsem=shared,%{_prefix} \
	--enable-sysvshm=shared,%{_prefix} \
	--with-tidy=shared,%{_prefix} \
	--enable-tokenizer=shared,%{_prefix} \
	--enable-xml=shared,%{_prefix} \
	--enable-xmlreader=shared,%{_prefix} \
	--with-xmlrpc=shared,%{_prefix} \
	--enable-xmlwriter=shared,%{_prefix} \
	--with-xsl=shared,%{_prefix} \
	--enable-gd=shared --with-external-gd \
	--with-zip=shared,%{_prefix} \
	--with-mhash=shared \
	--with-system-tzdata \
	|| (cat config.log && exit 1)

#cp -f Makefile Makefile.$i
#cp -f %{_bindir}/libtool .

# left for debugging purposes
#cp -f main/php_config.h php_config.h.$i

# when all else failed...
#perl -pi -e "s|-prefer-non-pic -static||g" Makefile.$i
%make_build

cd ..
done

%install

install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sysconfdir}/php.d
install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_usrsrc}/php-devel
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_sysconfdir}/cron.d
install -d %{buildroot}/var/lib/php

# Make apxs great again^H^H^H^H^H^H^H^H^H^H^Hhappy
# during build-apxs install
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf
cp %{_sysconfdir}/httpd/conf/httpd.conf %{buildroot}%{_sysconfdir}/httpd/conf/httpd.conf

for i in fpm cgi cli apxs embed litespeed; do
	make -C build-$i install \
		INSTALL_ROOT=%{buildroot}
done

# This was only needed for make install - so drop it
rm %{buildroot}%{_sysconfdir}/httpd/conf/httpd.conf

# extensions
echo "extension = openssl.so"		> %{buildroot}%{_sysconfdir}/php.d/21_openssl.ini
echo "extension = zlib.so"		> %{buildroot}%{_sysconfdir}/php.d/21_zlib.ini
echo "extension = bcmath.so"		> %{buildroot}%{_sysconfdir}/php.d/66_bcmath.ini
echo "extension = bz2.so"		> %{buildroot}%{_sysconfdir}/php.d/10_bz2.ini
echo "extension = calendar.so"		> %{buildroot}%{_sysconfdir}/php.d/11_calendar.ini
echo "extension = ctype.so"		> %{buildroot}%{_sysconfdir}/php.d/12_ctype.ini
echo "extension = curl.so"		> %{buildroot}%{_sysconfdir}/php.d/13_curl.ini
echo "extension = dba.so"		> %{buildroot}%{_sysconfdir}/php.d/14_dba.ini
echo "extension = dom.so"		> %{buildroot}%{_sysconfdir}/php.d/18_dom.ini
echo "extension = filter.so"		> %{buildroot}%{_sysconfdir}/php.d/81_filter.ini
echo "extension = ftp.so"		> %{buildroot}%{_sysconfdir}/php.d/22_ftp.ini
echo "extension = gd.so"		> %{buildroot}%{_sysconfdir}/php.d/23_gd.ini
echo "extension = gettext.so"		> %{buildroot}%{_sysconfdir}/php.d/24_gettext.ini
echo "extension = gmp.so"		> %{buildroot}%{_sysconfdir}/php.d/25_gmp.ini
#echo "extension = hash.so"		> %{buildroot}%{_sysconfdir}/php.d/54_hash.ini
echo "extension = iconv.so"		> %{buildroot}%{_sysconfdir}/php.d/26_iconv.ini
echo "extension = imap.so"		> %{buildroot}%{_sysconfdir}/php.d/27_imap.ini
echo "extension = intl.so"		> %{buildroot}%{_sysconfdir}/php.d/27_intl.ini
echo "extension = ldap.so"		> %{buildroot}%{_sysconfdir}/php.d/28_ldap.ini
echo "extension = mbstring.so"		> %{buildroot}%{_sysconfdir}/php.d/29_mbstring.ini
echo "extension = mysqlnd.so"		> %{buildroot}%{_sysconfdir}/php.d/37_mysqlnd.ini
echo "extension = enchant.so"		> %{buildroot}%{_sysconfdir}/php.d/38_enchant.ini
echo "extension = odbc.so"		> %{buildroot}%{_sysconfdir}/php.d/39_odbc.ini
echo "extension = pcntl.so"		> %{buildroot}%{_sysconfdir}/php.d/40_pcntl.ini
echo "extension = pdo.so"		> %{buildroot}%{_sysconfdir}/php.d/70_pdo.ini
echo "extension = pdo_dblib.so"		> %{buildroot}%{_sysconfdir}/php.d/71_pdo_dblib.ini
echo "extension = pdo_mysql.so"		> %{buildroot}%{_sysconfdir}/php.d/73_pdo_mysql.ini
echo "extension = pdo_odbc.so"		> %{buildroot}%{_sysconfdir}/php.d/75_pdo_odbc.ini
echo "extension = pdo_pgsql.so"		> %{buildroot}%{_sysconfdir}/php.d/76_pdo_pgsql.ini
echo "extension = pdo_sqlite.so"	> %{buildroot}%{_sysconfdir}/php.d/77_pdo_sqlite.ini
echo "extension = mysqli.so"		> %{buildroot}%{_sysconfdir}/php.d/78_mysqli.ini
echo "extension = pgsql.so"		> %{buildroot}%{_sysconfdir}/php.d/42_pgsql.ini
echo "extension = posix.so"		> %{buildroot}%{_sysconfdir}/php.d/43_posix.ini
echo "extension = pspell.so"		> %{buildroot}%{_sysconfdir}/php.d/44_pspell.ini
echo "extension = readline.so"		> %{buildroot}%{_sysconfdir}/php.d/45_readline.ini
#echo "extension = recode.so"		> %{buildroot}%{_sysconfdir}/php.d/46_recode.ini
echo "extension = session.so"		> %{buildroot}%{_sysconfdir}/php.d/47_session.ini
echo "extension = shmop.so"		> %{buildroot}%{_sysconfdir}/php.d/48_shmop.ini
echo "extension = snmp.so"		> %{buildroot}%{_sysconfdir}/php.d/50_snmp.ini
echo "extension = soap.so"		> %{buildroot}%{_sysconfdir}/php.d/51_soap.ini
echo "extension = sockets.so"		> %{buildroot}%{_sysconfdir}/php.d/52_sockets.ini
echo "extension = sqlite3.so"		> %{buildroot}%{_sysconfdir}/php.d/78_sqlite3.ini
echo "extension = sysvmsg.so"		> %{buildroot}%{_sysconfdir}/php.d/56_sysvmsg.ini
echo "extension = sysvsem.so"		> %{buildroot}%{_sysconfdir}/php.d/57_sysvsem.ini
echo "extension = sysvshm.so"		> %{buildroot}%{_sysconfdir}/php.d/58_sysvshm.ini
echo "extension = tidy.so"		> %{buildroot}%{_sysconfdir}/php.d/59_tidy.ini
echo "extension = tokenizer.so"		> %{buildroot}%{_sysconfdir}/php.d/60_tokenizer.ini
echo "extension = xml.so"		> %{buildroot}%{_sysconfdir}/php.d/62_xml.ini
echo "extension = xmlreader.so"		> %{buildroot}%{_sysconfdir}/php.d/63_xmlreader.ini
echo "extension = xmlwriter.so"		> %{buildroot}%{_sysconfdir}/php.d/64_xmlwriter.ini
echo "extension = xsl.so"		> %{buildroot}%{_sysconfdir}/php.d/63_xsl.ini
echo "extension = zip.so"		> %{buildroot}%{_sysconfdir}/php.d/83_zip.ini
echo "extension = phar.so"		> %{buildroot}%{_sysconfdir}/php.d/84_phar.ini
cat >%{buildroot}%{_sysconfdir}/php.d/85_opcache.ini <<"EOF"
zend_extension = %{_libdir}/php/extensions/opcache.so
opcache.memory_consumption=128
opcache.interned_strings_buffer=8
opcache.max_accelerated_files=4000
opcache.revalidate_freq=60
opcache.fast_shutdown=1
opcache.enable_cli=1
EOF

# Follow naming conventions
mv %{buildroot}%{_libdir}/apache/libphp.so %{buildroot}%{_libdir}/apache/mod_php.so

mkdir -p %{buildroot}%{_sysconfdir}/httpd/modules.d
cat > %{buildroot}%{_sysconfdir}/httpd/modules.d/170_mod_php.conf << EOF
LoadModule php_module %{_libdir}/apache/mod_php.so

AddType application/x-httpd-php .php
AddType application/x-httpd-php .phtml
AddType application/x-httpd-php-source .phps

DirectoryIndex index.php index.phtml
EOF

mkdir -p %{buildroot}/lib/systemd/system \
	%{buildroot}%{_sysconfdir}/logrotate.d \
	%{buildroot}%{_sysconfdir}/sysconfig

install -m0755 %{SOURCE2} %{buildroot}%{_libdir}/php/maxlifetime
install -m0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/cron.d/php
%if "%{_libdir}" != "/usr/lib"
sed -i -e "s|/usr/lib|%{_libdir}|" %{buildroot}%{_sysconfdir}/cron.d/php
%endif

mkdir -p %{buildroot}%{_unitdir}
cp build-fpm/sapi/fpm/php-fpm.service %{buildroot}%{_unitdir}/php-fpm.service
cp %{SOURCE5} %{buildroot}%{_sysconfdir}/sysconfig/php-fpm
cp %{SOURCE6} %{buildroot}%{_sysconfdir}/logrotate.d/php-fpm
mkdir -p %{buildroot}%{_tmpfilesdir}
cp %{SOURCE9} %{buildroot}%{_tmpfilesdir}/php-fpm.conf

cp %{buildroot}%{_sysconfdir}/php-fpm.conf.default %{buildroot}%{_sysconfdir}/php-fpm.conf
cp %{buildroot}%{_sysconfdir}/php-fpm.d/www.conf.default %{buildroot}%{_sysconfdir}/php-fpm.d/www.conf

# /var/lib/log is too weird to exist
mkdir -p %{buildroot}%{_localstatedir}/log/php-fpm
sed -i -e 's,;error_log.*,error_log = %{_localstatedir}/log/php-fpm/php-fpm.log,' %{buildroot}%{_sysconfdir}/php-fpm.conf*

# And a UNIX socket tends to be more secure
sed -i -e 's,^listen.*,listen = /run/php-fpm/php.sock,' %{buildroot}%{_sysconfdir}/php-fpm.d/*.conf*

# Let's try to reduce overhead too...
cat >>%{buildroot}%{_unitdir}/php-fpm.service <<EOF

[Socket]
ListenStream = /run/php-fpm/php.sock
EOF

%post bcmath
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun bcmath
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post bz2
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun bz2
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post calendar
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun calendar
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post cgi
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun cgi
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post cli
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun cli
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post ctype
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun ctype
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post curl
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun curl
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post dba
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun dba
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post devel
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun devel
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post doc
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun doc
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post dom
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun dom
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post enchant
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun enchant
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post filter
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun filter
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post ftp
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun ftp
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post gd
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun gd
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post gettext
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun gettext
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post gmp
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun gmp
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post hash
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun hash
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post iconv
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun iconv
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post imap
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun imap
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post intl
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun intl
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post ldap
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun ldap
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mbstring
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mbstring
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mysqlnd
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mysqlnd
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post mysqli
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun mysqli
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post odbc
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun odbc
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post openssl
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun openssl
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post pcntl
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun pcntl
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post pdo
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun pdo
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post pdo_dblib
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun pdo_dblib
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post pdo_mysql
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun pdo_mysql
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post pdo_odbc
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun pdo_odbc
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post pdo_pgsql
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun pdo_pgsql
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post pdo_sqlite
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun pdo_sqlite
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post pgsql
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun pgsql
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post phar
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun phar
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post posix
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun posix
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post pspell
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun pspell
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post readline
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun readline
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post recode
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun recode
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%pre session
%_pre_useradd apache /var/www /bin/sh

%post session
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun session
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post shmop
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun shmop
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post snmp
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun snmp
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post soap
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun soap
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post sockets
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun sockets
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post sqlite3
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun sqlite3
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post sysvmsg
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun sysvmsg
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post sysvsem
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun sysvsem
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post sysvshm
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun sysvshm
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post tidy
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun tidy
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post tokenizer
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun tokenizer
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post xml
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun xml
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post xmlreader
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun xmlreader
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post xmlwriter
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun xmlwriter
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post xsl
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun xsl
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post zip
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun zip
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post zlib
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun zlib
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post fpm
%tmpfiles_create_package php-fpm %{S:9}
%_post_service php-fpm
if [ $1 = 1 ]; then
	# Initial installation
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%pre fpm
%_preun_service php-fpm
%_pre_useradd apache /var/www /bin/sh

%preun fpm
if [ $1 = 0 ]; then
	# Package removal, not upgrade
	/bin/systemctl --no-reload disable php-fpm.service >/dev/null 2>&1 || :
	/bin/systemctl stop php-fpm.service >/dev/null 2>&1 || :
fi

%postun fpm
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ]; then
	# Package upgrade, not uninstall
	/bin/systemctl try-restart php-fpm.service >/dev/null 2>&1 || :
fi
%_postun_userdel apache

%post -n apache-mod_php
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun -n apache-mod_php
if [ "$1" = "0" ]; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%files doc
%doc php.ini-production php.ini-development

%files -n %{libname}

%files cli
%attr(0755,root,root) %{_bindir}/php
%attr(0644,root,root) %{_mandir}/man1/php.1*

%files dbg
%attr(0755,root,root) %{_bindir}/phpdbg
%attr(0644,root,root) %{_mandir}/man1/phpdbg.1*

%files cgi
%attr(0755,root,root) %{_bindir}/php-cgi
%{_mandir}/man1/php-cgi.1*

%files openlitespeed
%attr(0755,root,root) %{_bindir}/lsphp

%files devel
%doc README.* EXTENSIONS
%attr(0755,root,root) %{_bindir}/php-config
%attr(0755,root,root) %{_bindir}/phpize
%{_includedir}/php
%attr(0644,root,root) %{_mandir}/man1/php-config.1*
%attr(0644,root,root) %{_mandir}/man1/phpize.1*
# FIXME incorrectly versioned, wrong directory
%{_prefix}/lib/libphp.so
%{_libdir}/build

%files openssl
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/21_openssl.ini
%attr(0755,root,root) %{_libdir}/php/extensions/openssl.so

%files zlib
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/21_zlib.ini
%attr(0755,root,root) %{_libdir}/php/extensions/zlib.so

%files bcmath
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/66_bcmath.ini
%attr(0755,root,root) %{_libdir}/php/extensions/bcmath.so

%files bz2
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/10_bz2.ini
%attr(0755,root,root) %{_libdir}/php/extensions/bz2.so

%files calendar
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/11_calendar.ini
%attr(0755,root,root) %{_libdir}/php/extensions/calendar.so

%files ctype
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/12_ctype.ini
%attr(0755,root,root) %{_libdir}/php/extensions/ctype.so

%files curl
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/13_curl.ini
%attr(0755,root,root) %{_libdir}/php/extensions/curl.so

%files dba
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/14_dba.ini
%attr(0755,root,root) %{_libdir}/php/extensions/dba.so

%files dom
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/18_dom.ini
%attr(0755,root,root) %{_libdir}/php/extensions/dom.so

%files enchant
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/38_enchant.ini
%attr(0755,root,root) %{_libdir}/php/extensions/enchant.so

%files filter
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/81_filter.ini
%attr(0755,root,root) %{_libdir}/php/extensions/filter.so

%files ftp
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/22_ftp.ini
%attr(0755,root,root) %{_libdir}/php/extensions/ftp.so

%files gd
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/23_gd.ini
%attr(0755,root,root) %{_libdir}/php/extensions/gd.so

%files gettext
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/24_gettext.ini
%attr(0755,root,root) %{_libdir}/php/extensions/gettext.so

%files gmp
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/25_gmp.ini
%attr(0755,root,root) %{_libdir}/php/extensions/gmp.so

#files hash
#attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/54_hash.ini
#attr(0755,root,root) %{_libdir}/php/extensions/hash.so

%files iconv
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/26_iconv.ini
%attr(0755,root,root) %{_libdir}/php/extensions/iconv.so

%files imap
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/27_imap.ini
%attr(0755,root,root) %{_libdir}/php/extensions/imap.so

%files intl
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/27_intl.ini
%attr(0755,root,root) %{_libdir}/php/extensions/intl.so

%files ldap
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/28_ldap.ini
%attr(0755,root,root) %{_libdir}/php/extensions/ldap.so

%files mbstring
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/29_mbstring.ini
%attr(0755,root,root) %{_libdir}/php/extensions/mbstring.so

%files mysqlnd
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/37_mysqlnd.ini
%attr(0755,root,root) %{_libdir}/php/extensions/mysqlnd.so

%files mysqli
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/78_mysqli.ini
%attr(0755,root,root) %{_libdir}/php/extensions/mysqli.so

%files odbc
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/39_odbc.ini
%attr(0755,root,root) %{_libdir}/php/extensions/odbc.so

%files opcache
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/85_opcache.ini
%attr(0755,root,root) %{_libdir}/php/extensions/opcache.so

%files pcntl
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/40_pcntl.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pcntl.so

%files pdo
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/70_pdo.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pdo.so

%files pdo_dblib
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/71_pdo_dblib.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pdo_dblib.so

%files pdo_mysql
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/73_pdo_mysql.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pdo_mysql.so

%files pdo_odbc
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/75_pdo_odbc.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pdo_odbc.so

%files pdo_pgsql
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/76_pdo_pgsql.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pdo_pgsql.so

%files pdo_sqlite
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/77_pdo_sqlite.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pdo_sqlite.so

%files pgsql
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/42_pgsql.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pgsql.so

%files phar
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/84_phar.ini
%attr(0755,root,root) %{_libdir}/php/extensions/phar.so
%attr(0755,root,root) %{_bindir}/phar.phar
%{_bindir}/phar
%{_mandir}/man1/phar.1*
%{_mandir}/man1/phar.phar.1*

%files posix
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/43_posix.ini
%attr(0755,root,root) %{_libdir}/php/extensions/posix.so

%files pspell
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/44_pspell.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pspell.so

%files readline
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/45_readline.ini
%attr(0755,root,root) %{_libdir}/php/extensions/readline.so

#files recode
#attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/46_recode.ini
#attr(0755,root,root) %{_libdir}/php/extensions/recode.so

%files session
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/47_session.ini
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/cron.d/php
%attr(0755,root,root) %{_libdir}/php/extensions/session.so
%attr(0755,root,root) %{_libdir}/php/maxlifetime
%attr(01733,apache,apache) %dir /var/lib/php

%files shmop
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/48_shmop.ini
%attr(0755,root,root) %{_libdir}/php/extensions/shmop.so

%files snmp
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/50_snmp.ini
%attr(0755,root,root) %{_libdir}/php/extensions/snmp.so

%files soap
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/51_soap.ini
%attr(0755,root,root) %{_libdir}/php/extensions/soap.so

%files sockets
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/52_sockets.ini
%attr(0755,root,root) %{_libdir}/php/extensions/sockets.so

%files sqlite3
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/78_sqlite3.ini
%attr(0755,root,root) %{_libdir}/php/extensions/sqlite3.so

%files sysvmsg
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/56_sysvmsg.ini
%attr(0755,root,root) %{_libdir}/php/extensions/sysvmsg.so

%files sysvsem
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/57_sysvsem.ini
%attr(0755,root,root) %{_libdir}/php/extensions/sysvsem.so

%files sysvshm
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/58_sysvshm.ini
%attr(0755,root,root) %{_libdir}/php/extensions/sysvshm.so

%files tidy
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/59_tidy.ini
%attr(0755,root,root) %{_libdir}/php/extensions/tidy.so

%files tokenizer
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/60_tokenizer.ini
%attr(0755,root,root) %{_libdir}/php/extensions/tokenizer.so

%files xml
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/62_xml.ini
%attr(0755,root,root) %{_libdir}/php/extensions/xml.so

%files xmlreader
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/63_xmlreader.ini
%attr(0755,root,root) %{_libdir}/php/extensions/xmlreader.so

%files xmlwriter
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/64_xmlwriter.ini
%attr(0755,root,root) %{_libdir}/php/extensions/xmlwriter.so

%files xsl
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/63_xsl.ini
%attr(0755,root,root) %{_libdir}/php/extensions/xsl.so

%files zip
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/83_zip.ini
%attr(0755,root,root) %{_libdir}/php/extensions/zip.so

%files fpm
%doc sapi/fpm/LICENSE
%{_unitdir}/php-fpm.service
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php-fpm.conf.default
%attr(0644,root,root) %config %{_sysconfdir}/php-fpm.conf
%dir %{_sysconfdir}/php-fpm.d
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php-fpm.d/www.conf.default
%attr(0644,root,root) %config %{_sysconfdir}/php-fpm.d/www.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/php-fpm
%attr(0644,root,root) %{_sysconfdir}/logrotate.d/php-fpm
%attr(0755,root,root) %{_sbindir}/php-fpm
%attr(0644,root,root) %{_mandir}/man8/php-fpm.8*
#%attr(0711,apache,apache) %dir /var/lib/php-fpm
%attr(0711,apache,apache) %dir %{_localstatedir}/log/php-fpm
#%attr(0711,apache,apache) %dir /run/php-fpm
%{_tmpfilesdir}/php-fpm.conf
%{_datadir}/fpm

%files -n apache-mod_php
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/httpd/modules.d/*.conf
%attr(0755,root,root) %{_libdir}/apache/*.so

%files -n php-ini
# FIXME restore
#%config(noreplace) %{_sysconfdir}/php.ini
#%config(noreplace) %{_sysconfdir}/php-cgi-fcgi.ini
%dir %{_sysconfdir}/php.d
%dir %{_libdir}/php
%dir %{_libdir}/php/extensions
#%dir %{_datadir}/php
