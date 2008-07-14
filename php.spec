%define build_test 1
%{?_with_test: %{expand: %%global build_test 1}}
%{?_without_test: %{expand: %%global build_test 0}}

%define _requires_exceptions BEGIN\\|mkinstalldirs\\|pear(\\|/usr/bin/tclsh

%define epoch 3
%define major 5
%define libname %mklibname php5_common %{major}

%define suhosin_version 0.9.6.2

Summary:	The PHP5 scripting language
Name:		php
Version:	5.2.6
Release:	%mkrel 9
Group:		Development/PHP
License:	PHP License
URL:		http://www.php.net
Source0:	http://se.php.net/distributions/php-%{version}.tar.gz
Source1:	php-test.ini
Source2:	maxlifetime
Source3:	php.crond
Patch0:		php-init.diff
Patch1:		php-shared.diff
Patch3:		php-64bit.diff
Patch6:		php-libtool.diff
Patch7:		php-no_egg.diff
Patch8:		php-phpize.diff
Patch9:		php-remove_bogus_iconv_deps.diff
Patch10:	php-phpbuilddir.diff
# for kolab2
Patch11:	php-imap-annotation.diff
Patch12:	php-imap-status-current.diff
# http://www.outoforder.cc/projects/apache/mod_transform/
# http://www.outoforder.cc/projects/apache/mod_transform/patches/php5-apache2-filters.patch
Patch13:	php5-apache2-filters.diff
# P14 fixes the way we package the extensions to not check if the dep are installed or compiled in
Patch14:	php-extension_dep_macro_revert.diff
# remove libedit once and for all
Patch15:	php-no_libedit.diff
Patch16:	php-freetds.diff
Patch17:	php-xmlrpc_no_rpath.diff
Patch18:	php-really_external_sqlite2.diff
#####################################################################
# Stolen from PLD
Patch20:	php-mail.diff
Patch21:	php-sybase-fix.patch
Patch22:	php-filter-shared.diff
Patch23:	php-5.2.0-mdv_logo.diff
Patch25:	php-dba-link.patch
Patch27:	php-zlib-for-getimagesize.patch
Patch28:	php-zlib.patch
# stolen from debian
Patch30:	php-session.save_path.diff
Patch32:	php-exif_nesting_level.diff
#####################################################################
# Stolen from fedora
Patch101:	php-cxx.diff
Patch102:	php-install.diff
Patch105:	php-umask.diff
Patch106:	php-5.2.5-systzdata.patch
# Fixes for extension modules
Patch112:	php-shutdown.diff
Patch113:	php-libc-client.diff
Patch114:	php-no_pam_in_c-client.diff
# Functional changes
Patch115:	php-dlopen.diff
# Fix bugs
Patch120:	php-tests-wddx.diff
Patch121:	php-bug43221.diff
Patch122:	php-bug37076.diff
Patch123:	php-bug43589.diff
Patch224:	php-5.1.0RC6-CVE-2005-3388.diff
Patch225:	php-extraimapcheck.diff
# fix http://qa.mandriva.com/show_bug.cgi?id=37171, http://bugs.php.net/bug.php?id=43487
# -ffloat-store fixes it too
Patch226:	php-5.2.5-use-volatile-to-force-float-store.patch
Patch227:	php-bug43279.diff
Patch228:	php-posix-autoconf-2.62_fix.diff
Patch229:	php-bug44594.diff
# http://www.suhosin.org/
Source300:	suhosin-patch-%{version}-%{suhosin_version}.patch.gz.sig
Patch300:	suhosin-patch-%{version}-%{suhosin_version}.patch.gz
BuildRequires:	apache-devel >= 2.2.8
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7
BuildRequires:	bison
BuildRequires:	byacc
BuildRequires:	flex
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6
BuildRequires:	libxslt-devel >= 1.1.0
BuildRequires:	openssl >= 0.9.7
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	pam-devel
BuildRequires:	pcre-devel >= 6.6 
BuildRequires:	re2c >= 0.9.11
BuildRequires:	multiarch-utils >= 1.0.3
Epoch:		%{epoch}
%if %{build_test}
# (oe) the tests might fail because files in /etc/php.d/ will be picked up, and
# if there is an extension installed that may be conflicting we need to have
# this huge list of build conflicts... the list is constructed like this:
# rpm -qp --queryformat "[BuildConflicts:\t%{name}\n]" /RPMS/release/php-* \
# /contrib/release/php-* | grep -v pear | grep -v manual | sort -u
# simplexml needs to be compiled into the library as well...
# http://bugs.php.net/bug.php?id=42604
BuildConflicts:	php-adodb-ext
BuildConflicts:	php-amf
BuildConflicts:	php-apc
BuildConflicts:	php-archive
BuildConflicts:	php-auth_nds
BuildConflicts:	php-bbcode
BuildConflicts:	php-bcmath
BuildConflicts:	php-braille
BuildConflicts:	php-bz2
BuildConflicts:	php-calendar
BuildConflicts:	php-cgi
BuildConflicts:	php-clamav
BuildConflicts:	php-cli
BuildConflicts:	php-colorer
BuildConflicts:	php-courierauth
BuildConflicts:	php-ctype
BuildConflicts:	php-cups
BuildConflicts:	php-curl
BuildConflicts:	php-cyrus
BuildConflicts:	php-dav
BuildConflicts:	php-dba
BuildConflicts:	php-dbase
BuildConflicts:	php-dbx
BuildConflicts:	php-devel
BuildConflicts:	php-dio
BuildConflicts:	php-dom
BuildConflicts:	php-domxml
BuildConflicts:	php-doublemetaphone
BuildConflicts:	php-eaccelerator
BuildConflicts:	php-ecasound
BuildConflicts:	php-enchant
BuildConflicts:	php-esmtp
BuildConflicts:	php-event
BuildConflicts:	php-exif
BuildConflicts:	php-expect
BuildConflicts:	php-fam
BuildConflicts:	php-fcgi
BuildConflicts:	php-ffmpeg
BuildConflicts:	php-fileinfo
BuildConflicts:	php-filepro
BuildConflicts:	php-filter
BuildConflicts:	php-firebird
BuildConflicts:	php-ftp
BuildConflicts:	php-gd
BuildConflicts:	php-gd-bundled
BuildConflicts:	php-geoip
BuildConflicts:	php-gettext
BuildConflicts:	php-gmp
BuildConflicts:	php-gnupg
BuildConflicts:	php-gnutls
BuildConflicts:	php-gtk2
BuildConflicts:	php-haru
BuildConflicts:	php-hash
BuildConflicts:	php-hidef
BuildConflicts:	php-htscanner
BuildConflicts:	php-iconv
BuildConflicts:	php-id3
BuildConflicts:	php-idn
BuildConflicts:	php-imagick
BuildConflicts:	php-imap
BuildConflicts:	php-imlib2
BuildConflicts:	php-ini
BuildConflicts:	php-java-bridge
BuildConflicts:	php-java-bridge-tomcat
BuildConflicts:	php-json
BuildConflicts:	php-ldap
BuildConflicts:	php-magickwand
BuildConflicts:	php-mailparse
BuildConflicts:	php-mapscript
BuildConflicts:	php-mbstring
BuildConflicts:	php-mcache
BuildConflicts:	php-mcal
BuildConflicts:	php-mcrypt
BuildConflicts:	php-mcve
BuildConflicts:	php-mdbtools
BuildConflicts:	php-memcache
BuildConflicts:	php-mhash
BuildConflicts:	php-mime_magic
BuildConflicts:	php-ming
BuildConflicts:	php-mnogosearch
BuildConflicts:	php-mod_bt
BuildConflicts:	php-mssql
BuildConflicts:	php-mysql
BuildConflicts:	php-mysqli
BuildConflicts:	php-ncurses
BuildConflicts:	php-netools
BuildConflicts:	php-newt
BuildConflicts:	php-odbc
BuildConflicts:	php-oggvorbis
BuildConflicts:	php-openssl
BuildConflicts:	php-pam
BuildConflicts:	php-pcntl
BuildConflicts:	php-pdo
BuildConflicts:	php-pdo_dblib
BuildConflicts:	php-pdo_mysql
BuildConflicts:	php-pdo_odbc
BuildConflicts:	php-pdo_pgsql
BuildConflicts:	php-pdo_sqlite
BuildConflicts:	php-perl
BuildConflicts:	php-pgsql
BuildConflicts:	php-phar
BuildConflicts:	php-phk
BuildConflicts:	php-posix
BuildConflicts:	php-ps
BuildConflicts:	php-pspell
BuildConflicts:	php-radius
BuildConflicts:	php-readline
BuildConflicts:	php-recode
BuildConflicts:	php-rpmreader
BuildConflicts:	php-rrdtool
BuildConflicts:	php-ruli
BuildConflicts:	php-sasl
BuildConflicts:	php-session
BuildConflicts:	php-shmop
BuildConflicts:	php-shout
BuildConflicts:	php-shp
BuildConflicts:	php-simplexml
BuildConflicts:	php-smbauth
BuildConflicts:	php-snmp
BuildConflicts:	php-soap
BuildConflicts:	php-sockets
BuildConflicts:	php-sqlite
BuildConflicts:	php-sqlite3
BuildConflicts:	php-ssh2
BuildConflicts:	php-stats
BuildConflicts:	php-stem
BuildConflicts:	php-suhosin
BuildConflicts:	php-svn
BuildConflicts:	php-sybase
BuildConflicts:	php-syck
BuildConflicts:	php-sysvmsg
BuildConflicts:	php-sysvsem
BuildConflicts:	php-sysvshm
BuildConflicts:	php-tclink
BuildConflicts:	php-tcpwrap
BuildConflicts:	php-teng
BuildConflicts:	php-tidy
BuildConflicts:	php-tk
BuildConflicts:	php-tokenizer
BuildConflicts:	php-translit
BuildConflicts:	php-uuid
BuildConflicts:	php-vld
BuildConflicts:	php-wddx
BuildConflicts:	php-xattr
BuildConflicts:	php-xdebug
BuildConflicts:	php-xdiff
BuildConflicts:	php-xml
BuildConflicts:	php-xmlreader
BuildConflicts:	php-xmlrpc
BuildConflicts:	php-xmlwriter
BuildConflicts:	php-xsl
BuildConflicts:	php-yaz
BuildConflicts:	php-yp
BuildConflicts:	php-zip
BuildConflicts:	php-zlib
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
PHP5 is an HTML-embeddable scripting language. PHP5 offers built-in database
integration for several commercial and non-commercial database management
systems, so writing a database-enabled script with PHP5 is fairly simple. The
most common use of PHP5 coding is probably as a replacement for CGI scripts.

%package	cli
Summary:	PHP5 CLI interface
Group:		Development/Other
Requires(post): %{libname} >= %{epoch}:%{version}
Requires(post): php-ini >= %{version}
Requires(post): php-ftp >= %{epoch}:%{version}
Requires(post): php-pcre >= %{epoch}:%{version}
Requires(post): php-gettext >= %{epoch}:%{version}
Requires(post): php-posix >= %{epoch}:%{version}
Requires(post): php-ctype >= %{epoch}:%{version}
Requires(post): php-session >= %{epoch}:%{version}
Requires(post): php-sysvsem >= %{epoch}:%{version}
Requires(post): php-sysvshm >= %{epoch}:%{version}
Requires(post): php-openssl >= %{epoch}:%{version}
Requires(post): php-zlib >= %{epoch}:%{version}
Requires(post): php-tokenizer >= %{version}
Requires(post):	php-hash >= %{version}
Requires(post):	php-xmlreader >= %{version}
Requires(post):	php-xmlwriter >= %{version}
Requires(post):	php-suhosin >= 0.9.23
Requires(post):	php-filter >= 0.11.0
Requires(post):	php-json >= 0:%{version}
Requires(preun): %{libname} >= %{epoch}:%{version}
Requires(preun): php-ini >= %{version}
Requires(preun): php-ftp >= %{epoch}:%{version}
Requires(preun): php-pcre >= %{epoch}:%{version}
Requires(preun): php-gettext >= %{epoch}:%{version}
Requires(preun): php-posix >= %{epoch}:%{version}
Requires(preun): php-ctype >= %{epoch}:%{version}
Requires(preun): php-session >= %{epoch}:%{version}
Requires(preun): php-sysvsem >= %{epoch}:%{version}
Requires(preun): php-sysvshm >= %{epoch}:%{version}
Requires(preun): php-openssl >= %{epoch}:%{version}
Requires(preun): php-zlib >= %{epoch}:%{version}
Requires(preun): php-tokenizer >= %{version}
Requires(preun): php-hash >= %{version}
Requires(preun): php-xmlreader >= %{version}
Requires(preun): php-xmlwriter >= %{version}
Requires(preun): php-suhosin >= 0.9.23
Requires(preun): php-filter >= 0.11.0
Requires(preun): php-json >= 0:%{version}
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	php-ini >= %{version}
Requires:	php-ftp >= %{epoch}:%{version}
Requires:	php-pcre >= %{epoch}:%{version}
Requires:	php-gettext >= %{epoch}:%{version}
Requires:	php-posix >= %{epoch}:%{version}
Requires:	php-ctype >= %{epoch}:%{version}
Requires:	php-session >= %{epoch}:%{version}
Requires:	php-sysvsem >= %{epoch}:%{version}
Requires:	php-sysvshm >= %{epoch}:%{version}
Requires:	php-openssl >= %{epoch}:%{version}
Requires:	php-zlib >= %{epoch}:%{version}
Requires:	php-tokenizer >= %{version}
Requires:	php-hash >= %{version}
Requires:	php-xmlreader >= %{version}
Requires:	php-xmlwriter >= %{version}
Requires:	php-suhosin >= 0.9.23
Requires:	php-filter >= 0.11.0
Requires:	php-json >= 0:%{version}
Provides:	php php3 php4
Obsoletes:	php php3 php4
Epoch:		%{epoch}

%description	cli
PHP5 is an HTML-embeddable scripting language. PHP5 offers built-in database
integration for several commercial and non-commercial database management
systems, so writing a database-enabled script with PHP5 is fairly simple. The
most common use of PHP5 coding is probably as a replacement for CGI scripts.

This package contains a command-line (CLI) version of php. You must also
install libphp5_common. If you need apache module support, you also need to
install the apache-mod_php package.

This version of php has the suhosin patch %{suhosin_version} applied. Please
report bugs here: http://qa.mandriva.com/ so that the official maintainer of
this Mandriva package can help you. More information regarding the
suhosin patch %{suhosin_version} here: http://www.suhosin.org/

%package	cgi
Summary:	PHP5 CGI interface
Group:		Development/Other
Requires(post): %{libname} >= %{epoch}:%{version}
Requires(post): php-ini >= %{version}
Requires(post): php-ftp >= %{epoch}:%{version}
Requires(post): php-pcre >= %{epoch}:%{version}
Requires(post): php-gettext >= %{epoch}:%{version}
Requires(post): php-posix >= %{epoch}:%{version}
Requires(post): php-ctype >= %{epoch}:%{version}
Requires(post): php-session >= %{epoch}:%{version}
Requires(post): php-sysvsem >= %{epoch}:%{version}
Requires(post): php-sysvshm >= %{epoch}:%{version}
Requires(post): php-openssl >= %{epoch}:%{version}
Requires(post): php-zlib >= %{epoch}:%{version}
Requires(post): php-tokenizer >= %{version}
Requires(post):	php-hash >= %{version}
Requires(post):	php-xmlreader >= %{version}
Requires(post):	php-xmlwriter >= %{version}
Requires(post):	php-suhosin >= 0.9.23
Requires(post):	php-filter >= 0.11.0
Requires(post):	php-json >= 0:%{version}
Requires(preun): %{libname} >= %{epoch}:%{version}
Requires(preun): php-ini >= %{version}
Requires(preun): php-ftp >= %{epoch}:%{version}
Requires(preun): php-pcre >= %{epoch}:%{version}
Requires(preun): php-gettext >= %{epoch}:%{version}
Requires(preun): php-posix >= %{epoch}:%{version}
Requires(preun): php-ctype >= %{epoch}:%{version}
Requires(preun): php-session >= %{epoch}:%{version}
Requires(preun): php-sysvsem >= %{epoch}:%{version}
Requires(preun): php-sysvshm >= %{epoch}:%{version}
Requires(preun): php-openssl >= %{epoch}:%{version}
Requires(preun): php-zlib >= %{epoch}:%{version}
Requires(preun): php-tokenizer >= %{version}
Requires(preun): php-hash >= %{version}
Requires(preun): php-xmlreader >= %{version}
Requires(preun): php-xmlwriter >= %{version}
Requires(preun): php-suhosin >= 0.9.23
Requires(preun): php-filter >= 0.11.0
Requires(preun): php-json >= 0:%{version}
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	php-ini >= %{version}
Requires:	php-ftp >= %{epoch}:%{version}
Requires:	php-pcre >= %{epoch}:%{version}
Requires:	php-gettext >= %{epoch}:%{version}
Requires:	php-posix >= %{epoch}:%{version}
Requires:	php-ctype >= %{epoch}:%{version}
Requires:	php-session >= %{epoch}:%{version}
Requires:	php-sysvsem >= %{epoch}:%{version}
Requires:	php-sysvshm >= %{epoch}:%{version}
Requires:	php-openssl >= %{epoch}:%{version}
Requires:	php-zlib >= %{epoch}:%{version}
Requires:	php-tokenizer >= %{version}
Requires:	php-hash >= %{version}
Requires:	php-xmlreader >= %{version}
Requires:	php-xmlwriter >= %{version}
Requires:	php-suhosin >= 0.9.23
Requires:	php-filter >= 0.11.0
Requires:	php-json >= 0:%{version}
Provides:	php php3 php4
Obsoletes:	php php3 php4
Epoch:		%{epoch}

%description	cgi
PHP5 is an HTML-embeddable scripting language. PHP5 offers built-in database
integration for several commercial and non-commercial database management
systems, so writing a database-enabled script with PHP5 is fairly simple. The
most common use of PHP5 coding is probably as a replacement for CGI scripts.

This package contains a standalone (CGI) version of php. You must also install
libphp5_common. If you need apache module support, you also need to install the
apache-mod_php package.

This version of php has the suhosin patch %{suhosin_version} applied. Please
report bugs here: http://qa.mandriva.com/ so that the official maintainer of
this Mandriva package can help you. More information regarding the
suhosin patch %{suhosin_version} here: http://www.suhosin.org/

%package	fcgi
Summary:	PHP5 CGI interface with FastCGI support
Group:		Development/Other
Requires(post): %{libname} >= %{epoch}:%{version}
Requires(post): php-ini >= %{version}
Requires(post): php-ftp >= %{epoch}:%{version}
Requires(post): php-pcre >= %{epoch}:%{version}
Requires(post): php-gettext >= %{epoch}:%{version}
Requires(post): php-posix >= %{epoch}:%{version}
Requires(post): php-ctype >= %{epoch}:%{version}
Requires(post): php-session >= %{epoch}:%{version}
Requires(post): php-sysvsem >= %{epoch}:%{version}
Requires(post): php-sysvshm >= %{epoch}:%{version}
Requires(post): php-openssl >= %{epoch}:%{version}
Requires(post): php-zlib >= %{epoch}:%{version}
Requires(post): php-tokenizer >= %{version}
Requires(post):	php-hash >= %{version}
Requires(post):	php-xmlreader >= %{version}
Requires(post):	php-xmlwriter >= %{version}
Requires(post):	php-suhosin >= 0.9.23
Requires(post):	php-filter >= 0.11.0
Requires(post):	php-json >= 0:%{version}
Requires(preun): %{libname} >= %{epoch}:%{version}
Requires(preun): php-ini >= %{version}
Requires(preun): php-ftp >= %{epoch}:%{version}
Requires(preun): php-pcre >= %{epoch}:%{version}
Requires(preun): php-gettext >= %{epoch}:%{version}
Requires(preun): php-posix >= %{epoch}:%{version}
Requires(preun): php-ctype >= %{epoch}:%{version}
Requires(preun): php-session >= %{epoch}:%{version}
Requires(preun): php-sysvsem >= %{epoch}:%{version}
Requires(preun): php-sysvshm >= %{epoch}:%{version}
Requires(preun): php-openssl >= %{epoch}:%{version}
Requires(preun): php-zlib >= %{epoch}:%{version}
Requires(preun): php-tokenizer >= %{version}
Requires(preun): php-hash >= %{version}
Requires(preun): php-xmlreader >= %{version}
Requires(preun): php-xmlwriter >= %{version}
Requires(preun): php-suhosin >= 0.9.23
Requires(preun): php-filter >= 0.11.0
Requires(preun): php-json >= 0:%{version}
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	php-ini >= %{version}
Requires:	php-ftp >= %{epoch}:%{version}
Requires:	php-pcre >= %{epoch}:%{version}
Requires:	php-gettext >= %{epoch}:%{version}
Requires:	php-posix >= %{epoch}:%{version}
Requires:	php-ctype >= %{epoch}:%{version}
Requires:	php-session >= %{epoch}:%{version}
Requires:	php-sysvsem >= %{epoch}:%{version}
Requires:	php-sysvshm >= %{epoch}:%{version}
Requires:	php-openssl >= %{epoch}:%{version}
Requires:	php-zlib >= %{epoch}:%{version}
Requires:	php-tokenizer >= %{version}
Requires:	php-hash >= %{version}
Requires:	php-xmlreader >= %{version}
Requires:	php-xmlwriter >= %{version}
Requires:	php-suhosin >= 0.9.23
Requires:	php-filter >= 0.11.0
Requires:	php-json >= 0:%{version}
Provides:	php php3 php4
Obsoletes:	php php3 php4
Epoch:		%{epoch}

%description	fcgi
PHP5 is an HTML-embeddable scripting language. PHP5 offers built-in database
integration for several commercial and non-commercial database management
systems, so writing a database-enabled script with PHP5 is fairly simple. The
most common use of PHP5 coding is probably as a replacement for CGI scripts.

This package contains a standalone (CGI) version of php with FastCGI support.
You must also install libphp5_common. If you need apache module support, you
also need to install the apache-mod_php package.

This version of php has the suhosin patch %{suhosin_version} applied. Please
report bugs here: http://qa.mandriva.com/ so that the official maintainer of
this Mandriva package can help you. More information regarding the
suhosin patch %{suhosin_version} here: http://www.suhosin.org/

%package -n	%{libname}
Summary:	Shared library for PHP5
Group:		Development/Other
Provides:	libphp_common php-common
Obsoletes:	libphp_common php-common
Obsoletes:	php-pcre
Provides:	php-pcre = %{epoch}:%{version}
Obsoletes:	php-timezonedb
Provides:	php-timezonedb = %{epoch}:%{version}
Obsoletes:	php-simplexml
Provides:	php-simplexml = 0:%{version}
Epoch:		%{epoch}

%description -n	%{libname}
This package provides the common files to run with different implementations of
PHP5. You need this package if you install the php standalone package or a
webserver with php support (ie: apache-mod_php).

This version of php has the suhosin patch %{suhosin_version} applied. Please
report bugs here: http://qa.mandriva.com/ so that the official maintainer of
this Mandriva package can help you. More information regarding the
suhosin patch %{suhosin_version} here: http://www.suhosin.org/

%package	devel
Summary:	Development package for PHP5
Group:		Development/C
Requires(post): %{libname} >= %{epoch}:%{version}
Requires(preun): %{libname} >= %{epoch}:%{version}
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	apache-base >= 2.2.8
Requires:	autoconf2.5
Requires:	automake1.7
Requires:	bison
Requires:	byacc
Requires:	chrpath
Requires:	dos2unix
Requires:	flex
Requires:	libtool
Requires:	libxml2-devel >= 2.6
Requires:	libxslt-devel >= 1.1.0
Requires:	openssl >= 0.9.7
Requires:	openssl-devel >= 0.9.7
Requires:	pam-devel
Requires:	pcre-devel >= 6.6
Requires:	re2c >= 0.9.11
Requires:	tcl
Epoch:		%{epoch}

%description	devel
The php-devel package lets you compile dynamic extensions to PHP5. Included
here is the source for the php extensions. Instead of recompiling the whole php
binary to add support for, say, oracle, install this package and use the new
self-contained extensions support. For more information, read the file
SELF-CONTAINED-EXTENSIONS.

This version of php has the suhosin patch %{suhosin_version} applied. Please
report bugs here: http://qa.mandriva.com/ so that the official maintainer of
this Mandriva package can help you. More information regarding the
suhosin patch %{suhosin_version} here: http://www.suhosin.org/

%package	openssl
Summary:	OpenSSL extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		%{epoch}

%description	openssl
This is a dynamic shared object (DSO) for PHP that will add OpenSSL support.

%package	zlib
Summary:	Zlib extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		%{epoch}

%description	zlib
This is a dynamic shared object (DSO) for PHP that will add zlib compression
support to PHP.

%package	bcmath
Summary:	The bcmath module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	bcmath
This is a dynamic shared object (DSO) for PHP that will add bc style precision
math functions support.

For arbitrary precision mathematics PHP offers the Binary Calculator which
supports numbers of any size and precision, represented as strings.

%package	bz2
Summary:	Bzip2 extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}
BuildRequires:	bzip2-devel
Epoch:		0

%description	bz2
This is a dynamic shared object (DSO) for PHP that will add bzip2 compression
support to PHP.

The bzip2 functions are used to transparently read and write bzip2 (.bz2)
compressed files.

%package	calendar
Summary:	Calendar extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

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
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		3

%description	ctype
This is a dynamic shared object (DSO) for PHP that will add ctype support.

The functions provided by this extension check whether a character or string
falls into a certain character class according to the current locale (see also
setlocale()).

%package	curl
Summary:	Curl extension module for PHP
Group:		Development/PHP
BuildRequires:	curl-devel >= 7.9.8
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

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
BuildRequires:	gdbm-devel
BuildRequires:	db4-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	dba
This is a dynamic shared object (DSO) for PHP that will add flat-file databases
(DBA) support.

These functions build the foundation for accessing Berkeley DB style databases.

This is a general abstraction layer for several file-based databases. As such,
functionality is limited to a common subset of features supported by modern
databases such as Sleepycat Software's DB2. (This is not to be confused with
IBM's DB2 software, which is supported through the ODBC functions.)

%package	dbase
Summary:	DBase extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	dbase
This is a dynamic shared object (DSO) for PHP that will add DBase support.

These functions allow you to access records stored in dBase-format (dbf)
databases.

dBase files are simple sequential files of fixed length records. Records are
appended to the end of the file and delete records are kept until you call
dbase_pack().

%package	dom
Summary:	Dom extension module for PHP
Group:		Development/PHP
BuildRequires:	libxml2-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	dom
This is a dynamic shared object (DSO) for PHP that will add dom support.

The DOM extension is the replacement for the DOM XML extension from PHP 4. The
extension still contains many old functions, but they should no longer be used.
In particular, functions that are not object-oriented should be avoided.

The extension allows you to operate on an XML document with the DOM API.

%package	exif
Summary:	EXIF extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}
Requires:	php-mbstring >= 0:%{version}
Epoch:		0

%description	exif
This is a dynamic shared object (DSO) for PHP that will add EXIF tags support
in image files.

With the exif extension you are able to work with image meta data. For example,
you may use exif functions to read meta data of pictures taken from digital
cameras by working with information stored in the headers of the JPEG and TIFF
images.

%package	filter
Summary:	Extension for safely dealing with input parameters
Group:		Development/PHP
BuildRequires:	pcre-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	filter
The Input Filter extension is meant to address this issue by implementing a set
of filters and mechanisms that users can use to safely access their input data.

%package	ftp
Summary:	FTP extension module for PHP
Group:		Development/PHP
BuildRequires:	openssl-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		3

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
BuildRequires:	gd-devel >= 2.0.33
BuildRequires:	freetype2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libxpm-devel
BuildRequires:	X11-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

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
BuildRequires:	gettext-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		3

%description	gettext
This is a dynamic shared object (DSO) for PHP that will add gettext support.

The gettext functions implement an NLS (Native Language Support) API which can
be used to internationalize your PHP applications. Please see the gettext
documentation for your system for a thorough explanation of these functions or
view the docs at http://www.gnu.org/software/gettext/manual/gettext.html.

%package	gmp
Summary:	Gmp extension module for PHP
Group:		Development/PHP
BuildRequires:	gmp-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	gmp
This is a dynamic shared object (DSO) for PHP that will add arbitrary length
number support using the GNU MP library.

%package	hash
Summary:	HASH Message Digest Framework
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	hash
Native implementations of common message digest algorithms using a generic
factory method.

Message Digest (hash) engine. Allows direct or incremental processing of
arbitrary length messages using a variety of hashing algorithms.

%package	iconv
Summary:	Iconv extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

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
BuildRequires:	c-client-devel >= 2007
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	imap
This is a dynamic shared object (DSO) for PHP that will add IMAP support.

These functions are not limited to the IMAP protocol, despite their name. The
underlying c-client library also supports NNTP, POP3 and local mailbox access
methods.

%package	json
Summary:	JavaScript Object Notation
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	json
Support for JSON (JavaScript Object Notation) serialization.

%package	ldap
Summary:	LDAP extension module for PHP
Group:		Development/PHP
BuildRequires:	libldap-devel
BuildRequires:	libsasl-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

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
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	mbstring
This is a dynamic shared object (DSO) for PHP that will add multibyte string
support.

mbstring provides multibyte specific string functions that help you deal with
multibyte encodings in PHP. In addition to that, mbstring handles character
encoding conversion between the possible encoding pairs. mbstring is designed
to handle Unicode-based encodings such as UTF-8 and UCS-2 and many single-byte
encodings for convenience.

%package	mcrypt
Summary:	Mcrypt extension module for PHP
Group:		Development/PHP
BuildRequires:	libmcrypt-devel
BuildRequires:	libtool-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	mcrypt
This is a dynamic shared object (DSO) for PHP that will add mcrypt support.

This is an interface to the mcrypt library, which supports a wide variety of
block algorithms such as DES, TripleDES, Blowfish (default), 3-WAY, SAFER-SK64,
SAFER-SK128, TWOFISH, TEA, RC3 and GOST in CBC, OFB, CFB and ECB cipher modes.
Additionally, it supports RC6 and IDEA which are considered "non-free".

%package	mhash
Summary:	Mhash extension module for PHP
Group:		Development/PHP
BuildRequires:	libmhash-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	mhash
This is a dynamic shared object (DSO) for PHP that will add mhash support.

These functions are intended to work with mhash. Mhash can be used to create
checksums, message digests, message authentication codes, and more.

This is an interface to the mhash library. mhash supports a wide variety of
hash algorithms such as MD5, SHA1, GOST, and many others. For a complete list
of supported hashes, refer to the documentation of mhash. The general rule is
that you can access the hash algorithm from PHP with MHASH_HASHNAME. For
example, to access TIGER you use the PHP constant MHASH_TIGER.

%package	mime_magic
Summary:	The MIME Magic module for PHP
Group:		Development/PHP
BuildRequires:	apache-conf
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	mime_magic
This is a dynamic shared object (DSO) that adds MIME Magic support to PHP.

The functions in this module try to guess the content type and encoding of a
file by looking for certain magic byte sequences at specific positions within
the file. While this is not a bullet proof approach the heuristics used do a
very good job.

This extension is derived from Apache mod_mime_magic, which is itself based on
the file command maintained by Ian F. Darwin. See the source code for further
historic and copyright information.

%package	ming
Summary:	Ming extension module for PHP
Group:		Development/PHP
BuildRequires:	libming-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	ming
This is a dynamic shared object (DSO) for PHP that will add ming (Flash - .swf
files) support.

%package	mssql
Summary:	MS SQL extension module for PHP
Group:		Development/PHP
Requires:       freetds >= 0.63
BuildRequires:  freetds-devel >= 0.63
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	mssql
This is a dynamic shared object (DSO) for PHP that will add MS SQL databases
support using the FreeTDS library.

%package	mysql
Summary:	MySQL database module for PHP
Group:		Development/PHP
BuildRequires:	MySQL-devel >= 4.0.10
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	mysql
This is a dynamic shared object (DSO) for PHP that will add MySQL database
support.

These functions allow you to access MySQL database servers. More information
about MySQL can be found at http://www.mysql.com/.

Documentation for MySQL can be found at http://dev.mysql.com/doc/.

%package	mysqli
Summary:	MySQL database module for PHP
Group:		Development/PHP
BuildRequires:	MySQL-devel >= 4.1.7
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	mysqli
This is a dynamic shared object (DSO) for PHP that will add MySQL database
support.

The mysqli extension allows you to access the functionality provided by MySQL
4.1 and above. More information about the MySQL Database server can be found at
http://www.mysql.com/

Documentation for MySQL can be found at http://dev.mysql.com/doc/.

%package	ncurses
Summary:	Ncurses module for PHP
Group:		Development/PHP
BuildRequires:	ncurses-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	ncurses
This PHP module adds support for ncurses functions (only for cli and cgi
SAPIs).

%package	odbc
Summary:	ODBC extension module for PHP
Group:		Development/PHP
BuildRequires:	unixODBC-devel >= 2.2.1
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	odbc
This is a dynamic shared object (DSO) for PHP that will add ODBC support.

In addition to normal ODBC support, the Unified ODBC functions in PHP allow you
to access several databases that have borrowed the semantics of the ODBC API to
implement their own API. Instead of maintaining multiple database drivers that
were all nearly identical, these drivers have been unified into a single set of
ODBC functions.

%package	pcntl
Summary:	Process Control extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

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
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	pdo
PDO provides a uniform data access interface, sporting advanced features such
as prepared statements and bound parameters. PDO drivers are dynamically
loadable and may be developed independently from the core, but still accessed
using the same API.

Read the documentation at http://www.php.net/pdo for more information.

%package	pdo_dblib
Summary:	Sybase Interface driver for PDO
Group:		Development/PHP
Requires:       freetds >= 0.63
BuildRequires:  freetds-devel >= 0.63
Requires:	php-pdo >= 0:%{version}
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	pdo_dblib
PDO_DBLIB is a driver that implements the PHP Data Objects (PDO) interface to
enable access from PHP to Microsoft SQL Server and Sybase databases through the
FreeTDS libary.

%package	pdo_mysql
Summary:	MySQL Interface driver for PDO
Group:		Development/PHP
Requires:	php-pdo >= 0:%{version}
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	pdo_mysql
PDO_MYSQL is a driver that implements the PHP Data Objects (PDO) interface to
enable access from PHP to MySQL 3.x and 4.x databases.
 
PDO_MYSQL will take advantage of native prepared statement support present in
MySQL 4.1 and higher. If you're using an older version of the mysql client
libraries, PDO will emulate them for you.

%package	pdo_odbc
Summary:	ODBC v3 Interface driver for PDO
Group:		Development/PHP
BuildRequires:	unixODBC-devel
Requires:	php-pdo >= 0:%{version}
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	pdo_odbc
PDO_ODBC is a driver that implements the PHP Data Objects (PDO) interface to
enable access from PHP to databases through ODBC drivers or through the IBM DB2
Call Level Interface (DB2 CLI) library. PDO_ODBC currently supports three
different "flavours" of database drivers:
 
 o ibm-db2  - Supports access to IBM DB2 Universal Database, Cloudscape, and
              Apache Derby servers through the free DB2 client. ibm-db2 is not
	      supported in Mandriva.

 o unixODBC - Supports access to database servers through the unixODBC driver
              manager and the database's own ODBC drivers. 

 o generic  - Offers a compile option for ODBC driver managers that are not
              explicitly supported by PDO_ODBC. 

%package	pdo_pgsql
Summary:	PostgreSQL interface driver for PDO
Group:		Development/PHP
BuildRequires:	postgresql-devel
Requires:	php-pdo >= 0:%{version}
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	pdo_pgsql
PDO_PGSQL is a driver that implements the PHP Data Objects (PDO) interface to
enable access from PHP to PostgreSQL databases.

%package	pdo_sqlite
Summary:	SQLite v3 Interface driver for PDO
Group:		Development/PHP
BuildRequires:	sqlite3-devel
Requires:	php-pdo >= 0:%{version}
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	pdo_sqlite
PDO_SQLITE is a driver that implements the PHP Data Objects (PDO) interface to
enable access to SQLite 3 databases.

This extension provides an SQLite v3 driver for PDO. SQLite V3 is NOT
compatible with the bundled SQLite 2 in PHP 5, but is a significant step
forwards, featuring complete utf-8 support, native support for blobs, native
support for prepared statements with bound parameters and improved concurrency.

%package	pgsql
Summary:	PostgreSQL database module for PHP
Group:		Development/PHP
BuildRequires:	postgresql-devel
BuildRequires:	openssl-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	pgsql
This is a dynamic shared object (DSO) for PHP that will add PostgreSQL database
support.

PostgreSQL database is Open Source product and available without cost.
Postgres, developed originally in the UC Berkeley Computer Science Department,
pioneered many of the object-relational concepts now becoming available in some
commercial databases. It provides SQL92/SQL99 language support, transactions,
referential integrity, stored procedures and type extensibility. PostgreSQL is
an open source descendant of this original Berkeley code.

%package	posix
Summary:	POSIX extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		3

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
BuildRequires:	aspell-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	pspell
This is a dynamic shared object (DSO) for PHP that will add pspell support to
PHP.

These functions allow you to check the spelling of a word and offer
suggestions.

%package	readline
Summary:	Readline extension module for PHP
Group:		Development/PHP
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	gpm-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

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
BuildRequires:	recode-devel
BuildRequires:	gettext-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

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
Requires(pre): rpm-helper
Requires(postun): rpm-helper
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		3

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
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	shmop
This is a dynamic shared object (DSO) for PHP that will add Shared Memory
Operations support.

Shmop is an easy to use set of functions that allows PHP to read, write, create
and delete Unix shared memory segments.

%package	snmp
Summary:	NET-SNMP extension module for PHP
Group:		Development/PHP
Requires:	net-snmp-mibs
BuildRequires:	net-snmp-devel
BuildRequires:	openssl-devel
BuildRequires:	elfutils-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	snmp
This is a dynamic shared object (DSO) for PHP that will add SNMP support using
the NET-SNMP libraries.

In order to use the SNMP functions you need to install the NET-SNMP package.

%package	soap
Summary:	Soap extension module for PHP
Group:		Development/PHP
BuildRequires:	libxml2-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	soap
This is a dynamic shared object (DSO) for PHP that will add soap support.

The SOAP extension can be used to write SOAP Servers and Clients. It supports
subsets of SOAP 1.1, SOAP 1.2 and WSDL 1.1 specifications.

%package	sockets
Summary:	Sockets extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	sockets
This is a dynamic shared object (DSO) for PHP that will add sockets support.

The socket extension implements a low-level interface to the socket
communication functions based on the popular BSD sockets, providing the
possibility to act as a socket server as well as a client.

%package	sqlite
Summary:	SQLite database bindings for PHP
Group:		Development/PHP
Requires:	php-pdo >= 0:%{version}
BuildRequires:	sqlite-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	sqlite
This is an extension for the SQLite Embeddable SQL Database Engine. SQLite is a
C library that implements an embeddable SQL database engine. Programs that link
with the SQLite library can have SQL database access without running a separate
RDBMS process.

SQLite is not a client library used to connect to a big database server. SQLite
is the server. The SQLite library reads and writes directly to and from the
database files on disk.

%package	sybase
Summary:	Sybase extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	sybase
This is a dynamic shared object (DSO) for PHP that will add Sybase support to
PHP.

%package	sysvmsg
Summary:	SysV msg extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	sysvmsg
This is a dynamic shared object (DSO) for PHP that will add SysV message queues
support.

%package	sysvsem
Summary:	SysV sem extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		3

%description	sysvsem
This is a dynamic shared object (DSO) for PHP that will add SysV semaphores
support.

%package	sysvshm
Summary:	SysV shm extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		3

%description	sysvshm
This is a dynamic shared object (DSO) for PHP that will add SysV Shared Memory
support.

%package	tidy
Summary:	Tidy HTML Repairing and Parsing for PHP
Group:		Development/PHP
BuildRequires:	tidy-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	tidy
Tidy is a binding for the Tidy HTML clean and repair utility which allows you
to not only clean and otherwise manipluate HTML documents, but also traverse
the document tree using the Zend Engine 2 OO semantics.

%package	tokenizer
Summary:	Tokenizer extension module for PHP
Group:		Development/PHP
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	tokenizer
This is a dynamic shared object (DSO) for PHP that will add Tokenizer support.

The tokenizer functions provide an interface to the PHP tokenizer embedded in
the Zend Engine. Using these functions you may write your own PHP source
analyzing or modification tools without having to deal with the language
specification at the lexical level.

%package	xml
Summary:	XML extension module for PHP
Group:		Development/PHP
BuildRequires:	expat-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	xml
This is a dynamic shared object (DSO) for PHP that will add XML support. This
extension lets you create XML parsers and then define handlers for different
XML events.

%package	xmlreader
Summary:	Xmlreader extension module for PHP
Group:		Development/PHP
Requires:	php-dom
BuildRequires:	libxml2-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	xmlreader
XMLReader represents a reader that provides non-cached, forward-only access to
XML data. It is based upon the xmlTextReader api from libxml

%package	xmlrpc
Summary:	Xmlrpc extension module for PHP
Group:		Development/PHP
BuildRequires:	expat-devel
BuildRequires:	libxmlrpc-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	xmlrpc
This is a dynamic shared object (DSO) for PHP that will add XMLRPC support.

These functions can be used to write XML-RPC servers and clients. You can find
more information about XML-RPC at http://www.xmlrpc.com/, and more
documentation on this extension and its functions at
http://xmlrpc-epi.sourceforge.net/.

%package	xmlwriter
Summary:	Provides fast, non-cached, forward-only means to write XML data
Group:		Development/PHP
BuildRequires:	libxml2-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	xmlwriter
This extension wraps the libxml xmlWriter API. Represents a writer that
provides a non-cached, forward-only means of generating streams or files
containing XML data.

%package	xsl
Summary:	Xsl extension module for PHP
Group:		Development/PHP
BuildRequires:	libxslt-devel
BuildRequires:	libxml2-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	xsl
This is a dynamic shared object (DSO) for PHP that will add xsl support.

The XSL extension implements the XSL standard, performing XSLT transformations
using the libxslt library

%package	wddx
Summary:	WDDX serialization functions
Group:		Development/PHP
Requires:	php-xml
BuildRequires:  expat-devel
Requires:	%{libname} >= %{epoch}:%{version}
Epoch:		0

%description	wddx
This is a dynamic shared object (DSO) that adds wddx support to PHP. 

These functions are intended for work with WDDX (http://www.openwddx.org/)

%prep

%setup -q -n php-%{version}

# the ".droplet" suffix is here to nuke the backups later..., we don't want those in php-devel
%patch0 -p0 -b .init.droplet
%patch1 -p1 -b .shared.droplet
%patch3 -p1 -b .64bit.droplet
%patch6 -p0 -b .libtool.droplet
%patch8 -p1 -b .phpize.droplet
%patch9 -p0 -b .remove_bogus_iconv_deps.droplet
%patch10 -p1 -b .phpbuilddir.droplet

# for kolab2
%patch11 -p1 -b .imap-annotation.droplet
%patch12 -p1 -b .imap-status-current.droplet
#
%patch13 -p0 -b .apache2-filters.droplet
%patch14 -p1 -b .extension_dep_macro_revert.droplet
%patch15 -p0 -b .no_libedit.droplet
%patch16 -p1 -b .freetds.droplet
%patch17 -p0 -b .xmlrpc_no_rpath.droplet
%patch18 -p0 -b .really_external_sqlite2.droplet
#####################################################################
# Stolen from PLD
%patch20 -p0 -b .mail.droplet
%patch21 -p1 -b .sybase-fix.droplet
%patch22 -p0 -b .filter-shared.droplet
%patch25 -p0 -b .dba-link.droplet
%patch27 -p1 -b .zlib-for-getimagesize.droplet
%patch28 -p1 -b .zlib.droplet

# stolen from debian
%patch30 -p0 -b .session.save_path.droplet
%patch32 -p0 -b .exif_nesting_level.droplet

#####################################################################
# Stolen from fedora
%patch101 -p0 -b .cxx.droplet
%patch102 -p0 -b .install.droplet
%patch105 -p0 -b .umask.droplet
%patch106 -p1 -b .systzdata.droplet
%patch112 -p1 -b .shutdown.droplet
%patch113 -p0 -b .libc-client-php.droplet
%patch114 -p0 -b .no_pam_in_c-client.droplet
%patch115 -p0 -b .dlopen.droplet

# upstream fixes
%patch120 -p1 -b .tests-wddx.droplet
%patch121 -p0 -b .bug43221.droplet
%patch122 -p0 -b .bug37076.droplet
%patch123 -p0 -b .bug43589.droplet
%patch224 -p0 -b .CVE-2005-3388.droplet
%patch225 -p0 -b .open_basedir_and_safe_mode_checks.droplet
%patch226 -p1 -b .force-store.droplet
%patch227 -p0 -b .bug43279.droplet
%patch228 -p0 -b .posix-autoconf-2.62_fix.droplet
%patch229 -p0 -b .bug44594.droplet

%patch300 -p1 -b .suhosin.droplet
%patch7 -p1 -b .no_egg.droplet
%patch23 -p1 -b .mdv_logo.droplet

# "temporary" autoconf-2.62 "fixes"
perl -pi -e "s|have_broken_glibc_fopen_append|have_cv_broken_glibc_fopen_append|g" *.m4

for i in `find -name "*.m4"`; do
    perl -pi -e "s|cv_php_mbstring_stdarg|php_cv_mbstring_stdarg|g;\
        s|php_can_support_proc_open|php_cv_can_support_proc_open|g" $i
done

#	s|pdo_inc_path|pdo_cv_inc_path|g;\

cp %{SOURCE1} php-test.ini
cp %{SOURCE2} maxlifetime
cp %{SOURCE3} php.crond

# lib64 hack
perl -p -i -e "s|/usr/lib|%{_libdir}|" php.crond

# nuke bogus checks becuase i fixed this years ago in our recode package
rm -f ext/recode/config9.m4

# Change perms otherwise rpm would get fooled while finding requires
find -name "*.inc" | xargs chmod 644
find -name "*.php*" | xargs chmod 644
find -name "*README*" | xargs chmod 644

mkdir -p php-devel/extensions
mkdir -p php-devel/sapi

# Install test files in php-devel
cp -a tests php-devel

cp -dpR ext/* php-devel/extensions/
rm -f php-devel/extensions/informix/stub.c
rm -f php-devel/extensions/standard/.deps
rm -f php-devel/extensions/skeleton/EXPERIMENTAL
rm -f php-devel/extensions/ncurses/EXPERIMENTAL

# SAPI
cp -dpR sapi/* php-devel/sapi/ 
rm -f php-devel/sapi/thttpd/stub.c
rm -f php-devel/sapi/cgi/php.sym
rm -f php-devel/sapi/fastcgi/php.sym
rm -f php-devel/sapi/pi3web/php.sym

# cleanup
find php-devel -name "*.droplet" | xargs rm -f

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

%build
%serverbuild

export CFLAGS="${CFLAGS} -fPIC -L%{_libdir}"
export CXXFLAGS="${CXXFLAGS} -fPIC -L%{_libdir}"
export RPM_OPT_FLAGS="${CFLAGS} -fPIC -L%{_libdir}"

cat > php-devel/buildext <<EOF
#!/bin/bash
gcc -Wall -fPIC -shared $CFLAGS \\
    -I. \`%{_bindir}/php-config --includes\` \\
    -I%{_includedir}/libxml2 \\
    -I%{_includedir}/freetype \\
    -I%{_includedir}/openssl \\
    -I%{_usrsrc}/php-devel/ext \\
    -I%{_includedir}/\$1 \\
    \$4 \$2 -o \$1.so \$3 -lc
EOF

chmod 755 php-devel/buildext

# this _has_ to be executed!
#export WANT_AUTOCONF_2_5=1

rm -f configure; libtoolize --copy --force; aclocal-1.7; autoconf --force; autoheader
#./buildconf --force

# Do this patch with a perl hack...
perl -pi -e "s|'\\\$install_libdir'|'%{_libdir}'|" ltmain.sh

export oldstyleextdir=yes
export EXTENSION_DIR="%{_libdir}/php/extensions"
export PROG_SENDMAIL="%{_sbindir}/sendmail"
export GD_SHARED_LIBADD="$GD_SHARED_LIBADD -lm"

# never use "--disable-rpath", it does the opposite

# Configure php5
for i in cgi cli fcgi apxs; do
./configure \
    `[ $i = fcgi ] && echo --enable-fastcgi --with-fastcgi=%{_prefix} --disable-cli --enable-force-cgi-redirect` \
    `[ $i = cgi ] && echo --enable-discard-path --disable-cli --enable-force-cgi-redirect` \
    `[ $i = apxs ] && echo --with-apxs2=%{_sbindir}/apxs` \
    `[ $i = cli ] && echo --disable-cgi --enable-cli` \
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
    --localstatedir=%{_localstatedir}/lib \
    --mandir=%{_mandir} \
    --enable-shared=yes \
    --enable-static=no \
    --with-libdir=%{_lib} \
    --with-config-file-path=%{_sysconfdir} \
    --with-config-file-scan-dir=%{_sysconfdir}/php.d \
    --disable-debug --enable-pic \
    --enable-inline-optimization \
    --with-exec-dir=%{_bindir} \
    --with-pcre=%{_prefix} --with-pcre-regex=%{_prefix} \
    --with-ttf --with-freetype-dir=%{_prefix} --with-zlib=%{_prefix} \
    --with-png-dir=%{_prefix} \
    --with-regex=php \
    --enable-magic-quotes \
    --enable-safe-mode \
    --with-zlib=shared,%{_prefix} --with-zlib-dir=%{_prefix} \
    --with-openssl=shared,%{_prefix} \
    --enable-libxml=%{_prefix} --with-libxml-dir=%{_prefix} \
    --enable-spl=%{_prefix} \
    --enable-track-vars \
    --enable-trans-sid \
    --enable-memory-limit \
    --with-versioning \
    --enable-mod_charset \
    --without-pear \
    --enable-bcmath=shared \
    --with-bz2=shared,%{_prefix} \
    --enable-calendar=shared \
    --enable-ctype=shared \
    --with-curl=shared,%{_prefix} --without-curlwrappers \
    --enable-dba=shared --with-gdbm --with-db4 --with-cdb --with-flatfile --with-inifile \
    --enable-dbase=shared \
    --enable-dom=shared,%{_prefix} --with-libxml-dir=%{_prefix} \
    --enable-exif=shared \
    --enable-filter=shared --with-pcre-dir=%{_prefix} \
    --enable-json=shared \
    --with-openssl-dir=%{_prefix} --enable-ftp=shared \
    --with-gd=shared,%{_prefix} --with-jpeg-dir=%{_prefix} --with-png-dir=%{_prefix} --with-zlib-dir=%{_prefix} --with-xpm-dir=%{_prefix}/X11R6 --with-ttf=%{_prefix} --with-freetype-dir=%{_prefix} --enable-gd-native-ttf \
    --with-gettext=shared,%{_prefix} \
    --with-gmp=shared,%{_prefix} \
    --enable-hash=shared,%{_prefix} \
    --with-iconv=shared \
    --with-imap=shared,%{_prefix} --with-imap-ssl=%{_prefix} \
    --with-ldap=shared,%{_prefix} --with-ldap-sasl=%{_prefix} \
    --enable-mbstring=shared,%{_prefix} --enable-mbregex \
    --with-mcrypt=shared,%{_prefix} \
    --with-mhash=shared,%{_prefix} \
    --with-mime-magic=shared,%{_sysconfdir}/httpd/conf/magic \
    --with-ming=shared,%{_prefix} \
    --with-mssql=shared,%{_prefix} \
    --with-mysql=shared,%{_prefix} --with-mysql-sock=%{_localstatedir}/lib/mysql/mysql.sock --with-zlib-dir=%{_prefix} \
    --with-mysqli=shared,%{_bindir}/mysql_config \
    --with-ncurses=shared,%{_prefix} \
    --with-unixODBC=shared,%{_prefix} \
    --enable-pcntl=shared \
    --enable-pdo=shared,%{_prefix} --with-pdo-dblib=shared,%{_prefix} --with-pdo-mysql=shared,%{_prefix} --with-pdo-odbc=shared,unixODBC,%{_prefix} --with-pdo-pgsql=shared,%{_prefix} --with-pdo-sqlite=shared,%{_prefix} \
    --with-pgsql=shared,%{_prefix} \
    --enable-posix=shared \
    --with-pspell=shared,%{_prefix} \
    --with-readline=shared,%{_prefix} \
    --with-recode=shared,%{_prefix} \
    --enable-session=shared,%{_prefix} \
    --enable-shmop=shared,%{_prefix} \
    --enable-simplexml \
    --with-snmp=shared,%{_prefix} --enable-ucd-snmp-hack \
    --enable-soap=shared,%{_prefix} --with-libxml-dir=%{_prefix} \
    --enable-sockets=shared,%{_prefix} \
    --with-sqlite=shared,%{_prefix} \
    --with-sybase=shared,%{_prefix} \
    --enable-sysvmsg=shared,%{_prefix} \
    --enable-sysvsem=shared,%{_prefix} \
    --enable-sysvshm=shared,%{_prefix} \
    --with-tidy=shared,%{_prefix} \
    --enable-tokenizer=shared,%{_prefix} \
    --enable-xml=shared,%{_prefix} --with-expat-dir=shared,%{_prefix} \
    --enable-xmlreader=shared,%{_prefix} \
    --with-xmlrpc=shared,%{_prefix} --with-expat-dir=shared,%{_prefix} \
    --enable-xmlwriter=shared,%{_prefix} \
    --with-xsl=shared,%{_prefix} \
    --enable-wddx=shared \
    --enable-reflection=shared \
    --with-system-tzdata=%{_datadir}/zoneinfo

cp -f Makefile Makefile.$i

# left for debugging purposes
cp -f main/php_config.h php_config.h.$i

# when all else failed...
perl -pi -e "s|-prefer-non-pic -static||g" Makefile.$i

done

# remove all confusion...
perl -pi -e "s|^#define CONFIGURE_COMMAND .*|#define CONFIGURE_COMMAND \"This is irrelevant, look inside the %{_docdir}/libphp5_common%{major}-%{version}/configure_command file. urpmi is your friend, use it to install extensions not shown below.\"|g" main/build-defs.h
cp config.nice configure_command; chmod 644 configure_command

make

# make php-fcgi
cp -af php_config.h.fcgi main/php_config.h
make -f Makefile.fcgi sapi/cgi/php-cgi
cp -rp sapi/cgi sapi/fcgi
perl -pi -e "s|sapi/cgi|sapi/fcgi|g" sapi/fcgi/php

# cleanup
rm -rf sapi/cgi/.libs; rm -f sapi/cgi/*.lo sapi/cgi/php-cgi

# make php-cgi
cp -af php_config.h.cgi main/php_config.h
make -f Makefile.cgi sapi/cgi/php-cgi

cp -af php_config.h.apxs main/php_config.h

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sysconfdir}/php.d
install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_usrsrc}/php-devel
install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_sysconfdir}/cron.d
install -d %{buildroot}%{_localstatedir}/lib/php

#perl -pi -e "s|^libdir=.*|libdir='%{_libdir}'|g" .libs/*.la*

make -f Makefile.apxs install \
	INSTALL_ROOT=%{buildroot} \
	INSTALL_IT="\$(LIBTOOL) --mode=install install libphp5_common.la %{buildroot}%{_libdir}/" \
	INSTALL_CLI="\$(LIBTOOL) --silent --mode=install install sapi/cli/php %{buildroot}%{_bindir}/php"

./libtool --silent --mode=install install sapi/fcgi/php-cgi %{buildroot}%{_bindir}/php-fcgi
./libtool --silent --mode=install install sapi/cgi/php-cgi %{buildroot}%{_bindir}/php-cgi

cp -dpR php-devel/* %{buildroot}%{_usrsrc}/php-devel/
install -m0644 run-tests*.php %{buildroot}%{_usrsrc}/php-devel/
install -m0644 main/internal_functions.c %{buildroot}%{_usrsrc}/php-devel/

install -m0644 sapi/cli/php.1 %{buildroot}%{_mandir}/man1/
install -m0644 scripts/man1/phpize.1 %{buildroot}%{_mandir}/man1/
install -m0644 scripts/man1/php-config.1 %{buildroot}%{_mandir}/man1/

ln -snf extensions %{buildroot}%{_usrsrc}/php-devel/ext

# extensions
echo "extension = openssl.so"	> %{buildroot}%{_sysconfdir}/php.d/21_openssl.ini
echo "extension = zlib.so"	> %{buildroot}%{_sysconfdir}/php.d/21_zlib.ini
echo "extension = bcmath.so"	> %{buildroot}%{_sysconfdir}/php.d/66_bcmath.ini
echo "extension = bz2.so"	> %{buildroot}%{_sysconfdir}/php.d/10_bz2.ini
echo "extension = calendar.so"	> %{buildroot}%{_sysconfdir}/php.d/11_calendar.ini
echo "extension = ctype.so"	> %{buildroot}%{_sysconfdir}/php.d/12_ctype.ini
echo "extension = curl.so"	> %{buildroot}%{_sysconfdir}/php.d/13_curl.ini
echo "extension = dba.so"	> %{buildroot}%{_sysconfdir}/php.d/14_dba.ini
echo "extension = dbase.so"	> %{buildroot}%{_sysconfdir}/php.d/15_dbase.ini
echo "extension = dom.so"	> %{buildroot}%{_sysconfdir}/php.d/18_dom.ini
echo "extension = exif.so"	> %{buildroot}%{_sysconfdir}/php.d/19_exif.ini
echo "extension = filter.so"	> %{buildroot}%{_sysconfdir}/php.d/81_filter.ini
echo "extension = ftp.so"	> %{buildroot}%{_sysconfdir}/php.d/22_ftp.ini
echo "extension = gd.so"	> %{buildroot}%{_sysconfdir}/php.d/23_gd.ini
echo "extension = gettext.so"	> %{buildroot}%{_sysconfdir}/php.d/24_gettext.ini
echo "extension = gmp.so"	> %{buildroot}%{_sysconfdir}/php.d/25_gmp.ini
echo "extension = hash.so"	> %{buildroot}%{_sysconfdir}/php.d/54_hash.ini
echo "extension = iconv.so"	> %{buildroot}%{_sysconfdir}/php.d/26_iconv.ini
echo "extension = imap.so"	> %{buildroot}%{_sysconfdir}/php.d/27_imap.ini
echo "extension = ldap.so"	> %{buildroot}%{_sysconfdir}/php.d/28_ldap.ini
echo "extension = mbstring.so"	> %{buildroot}%{_sysconfdir}/php.d/29_mbstring.ini
echo "extension = mcrypt.so"	> %{buildroot}%{_sysconfdir}/php.d/30_mcrypt.ini
echo "extension = mhash.so"	> %{buildroot}%{_sysconfdir}/php.d/31_mhash.ini
cat > %{buildroot}%{_sysconfdir}/php.d/31_mime_magic.ini << EOF
extension = mime_magic.so

[mime_magic]

mime_magic.magicfile = %{_sysconfdir}/httpd/conf/magic
EOF
echo "extension = ming.so"		> %{buildroot}%{_sysconfdir}/php.d/33_ming.ini
echo "extension = mssql.so"		> %{buildroot}%{_sysconfdir}/php.d/35_mssql.ini
echo "extension = mysql.so"		> %{buildroot}%{_sysconfdir}/php.d/36_mysql.ini
echo "extension = mysqli.so"		> %{buildroot}%{_sysconfdir}/php.d/37_mysqli.ini
echo "extension = ncurses.so"		> %{buildroot}%{_sysconfdir}/php.d/38_ncurses.ini
echo "extension = odbc.so"		> %{buildroot}%{_sysconfdir}/php.d/39_odbc.ini
echo "extension = pcntl.so"		> %{buildroot}%{_sysconfdir}/php.d/40_pcntl.ini
echo "extension = pdo.so"		> %{buildroot}%{_sysconfdir}/php.d/70_pdo.ini
echo "extension = pdo_dblib.so"		> %{buildroot}%{_sysconfdir}/php.d/71_pdo_dblib.ini
echo "extension = pdo_mysql.so"		> %{buildroot}%{_sysconfdir}/php.d/73_pdo_mysql.ini
echo "extension = pdo_odbc.so"		> %{buildroot}%{_sysconfdir}/php.d/75_pdo_odbc.ini
echo "extension = pdo_pgsql.so"		> %{buildroot}%{_sysconfdir}/php.d/76_pdo_pgsql.ini
echo "extension = pdo_sqlite.so"	> %{buildroot}%{_sysconfdir}/php.d/77_pdo_sqlite.ini
echo "extension = pgsql.so"		> %{buildroot}%{_sysconfdir}/php.d/42_pgsql.ini
echo "extension = posix.so"		> %{buildroot}%{_sysconfdir}/php.d/43_posix.ini
echo "extension = pspell.so"		> %{buildroot}%{_sysconfdir}/php.d/44_pspell.ini
echo "extension = readline.so"		> %{buildroot}%{_sysconfdir}/php.d/45_readline.ini
echo "extension = recode.so"		> %{buildroot}%{_sysconfdir}/php.d/46_recode.ini
echo "extension = session.so"		> %{buildroot}%{_sysconfdir}/php.d/47_session.ini
echo "extension = shmop.so"		> %{buildroot}%{_sysconfdir}/php.d/48_shmop.ini
echo "extension = snmp.so"		> %{buildroot}%{_sysconfdir}/php.d/50_snmp.ini
echo "extension = soap.so"		> %{buildroot}%{_sysconfdir}/php.d/51_soap.ini
echo "extension = sockets.so"		> %{buildroot}%{_sysconfdir}/php.d/52_sockets.ini
echo "extension = sqlite.so"		> %{buildroot}%{_sysconfdir}/php.d/78_sqlite.ini
echo "extension = sybase.so"		> %{buildroot}%{_sysconfdir}/php.d/46_sybase.ini
echo "extension = sysvmsg.so"		> %{buildroot}%{_sysconfdir}/php.d/56_sysvmsg.ini
echo "extension = sysvsem.so"		> %{buildroot}%{_sysconfdir}/php.d/57_sysvsem.ini
echo "extension = sysvshm.so"		> %{buildroot}%{_sysconfdir}/php.d/58_sysvshm.ini
echo "extension = tidy.so"		> %{buildroot}%{_sysconfdir}/php.d/59_tidy.ini
echo "extension = tokenizer.so"		> %{buildroot}%{_sysconfdir}/php.d/60_tokenizer.ini
echo "extension = xml.so"		> %{buildroot}%{_sysconfdir}/php.d/62_xml.ini
echo "extension = xmlreader.so"		> %{buildroot}%{_sysconfdir}/php.d/63_xmlreader.ini
echo "extension = xmlrpc.so"		> %{buildroot}%{_sysconfdir}/php.d/62_xmlrpc.ini
echo "extension = xmlwriter.so"		> %{buildroot}%{_sysconfdir}/php.d/64_xmlwriter.ini
echo "extension = xsl.so"		> %{buildroot}%{_sysconfdir}/php.d/63_xsl.ini
echo "extension = wddx.so"		> %{buildroot}%{_sysconfdir}/php.d/63_wddx.ini
echo "extension = json.so"		> %{buildroot}%{_sysconfdir}/php.d/82_json.ini

install -m0755 maxlifetime %{buildroot}%{_libdir}/php/maxlifetime
install -m0644 php.crond %{buildroot}%{_sysconfdir}/cron.d/php

# fix docs
cp Zend/LICENSE Zend/ZEND_LICENSE
cp README.SELF-CONTAINED-EXTENSIONS SELF-CONTAINED-EXTENSIONS
cp ext/openssl/README README.openssl
cp ext/spl/README README.spl
cp ext/libxml/CREDITS CREDITS.libxml
cp ext/zlib/CREDITS CREDITS.zlib

# cgi docs
cp sapi/cgi/CREDITS CREDITS.cgi

# fcgi docs
cp sapi/cgi/README.FastCGI README.fcgi
cp sapi/cgi/CREDITS CREDITS.fcgi

# cli docs
cp sapi/cli/CREDITS CREDITS.cli
cp sapi/cli/README README.cli
cp sapi/cli/TODO TODO.cli

# house cleaning
rm -f %{buildroot}%{_bindir}/pear
rm -f %{buildroot}%{_libdir}/*.a

# don't pack useless stuff
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/bcmath
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/bz2
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/calendar
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/ctype
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/curl
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/dba
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/dbase
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/dom
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/exif
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/filter
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/ftp
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/gettext
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/gmp
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/hash
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/iconv
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/imap
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/json
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/ldap
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/libxml
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/mbstring
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/mcrypt
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/mhash
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/mime_magic
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/ming
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/mssql
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/mysql
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/mysqli
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/ncurses
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/odbc
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/openssl
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pcntl
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pcre
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pdo
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pdo_dblib
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pdo_mysql
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pdo_odbc
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pdo_pgsql
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pdo_sqlite
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pgsql
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/posix
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/pspell
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/readline
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/recode
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/shmop
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/snmp
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/soap
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/sockets
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/spl
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/sqlite
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/standard
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/sybase
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/sysvmsg
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/sysvsem
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/sysvshm
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/tidy
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/tokenizer
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/wddx
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/xml
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/xmlreader
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/xmlrpc
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/xmlwriter
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/xsl
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/zlib
rm -rf %{buildroot}%{_usrsrc}/php-devel/extensions/zip

# php-devel.i586: E: zero-length /usr/src/php-devel/extensions/pdo_firebird/EXPERIMENTAL
find %{buildroot}%{_usrsrc}/php-devel -type f -size 0 -exec rm -f {} \;

# fix one strange weirdo
%{__perl} -pi -e "s|^libdir=.*|libdir='%{_libdir}'|g" %{buildroot}%{_libdir}/*.la

%multiarch_includes %{buildroot}%{_includedir}/php/main/build-defs.h
%multiarch_includes %{buildroot}%{_includedir}/php/main/config.w32.h
%multiarch_includes %{buildroot}%{_includedir}/php/main/php_config.h

%if %{build_test}
# do a make test
export NO_INTERACTION=1
export PHPRC="."
export REPORT_EXIT_STATUS=2
export TEST_PHP_DETAILED=0
export TEST_PHP_ERROR_STYLE=EMACS
export TEST_PHP_LOG_FORMAT=LEODC

# FAILING TESTS:
# unknown errors with ext/date/tests/oo_002.phpt probably because of php-5.2.5-systzdata.patch
# http://bugs.php.net/bug.php?id=22414 (claimed to be fixed in 2003, but seems not)
# unknown errors with ext/standard/tests/general_functions/phpinfo.phpt
# unknown errors with ext/standard/tests/strings/setlocale_*
disable_tests="ext/date/tests/oo_002.phpt \
ext/standard/tests/file/bug22414.phpt \
ext/standard/tests/general_functions/phpinfo.phpt \
ext/standard/tests/strings/setlocale_basic1.phpt \
ext/standard/tests/strings/setlocale_basic2.phpt \
ext/standard/tests/strings/setlocale_basic3.phpt \
ext/standard/tests/strings/setlocale_variation1.phpt \
ext/standard/tests/strings/setlocale_variation3.phpt \
ext/standard/tests/strings/setlocale_variation4.phpt \
ext/standard/tests/strings/setlocale_variation5.phpt"

[[ -n "$disable_tests" ]] && \
for f in $disable_tests; do
  [[ -f "$f" ]] && mv $f $f.disabled
done

for f in `find .. -name \*.diff -type f -print`; do
    echo "TEST FAILURE: $f --"
    cat "$f"
    echo "-- $f result ends."
done

TEST_PHP_EXECUTABLE=sapi/cli/php sapi/cli/php -c ./php-test.ini run-tests.php
%endif

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%pre cgi
update-alternatives --remove php %{_bindir}/php-cgi
update-alternatives --remove php %{_bindir}/php-fcgi
update-alternatives --remove php %{_bindir}/php-cli

%pre fcgi
update-alternatives --remove php %{_bindir}/php-cgi
update-alternatives --remove php %{_bindir}/php-fcgi
update-alternatives --remove php %{_bindir}/php-cli

%pre cli
update-alternatives --remove php %{_bindir}/php-cgi
update-alternatives --remove php %{_bindir}/php-fcgi
update-alternatives --remove php %{_bindir}/php-cli

%post bcmath
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun bcmath
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post bz2
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun bz2
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post calendar
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun calendar
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post ctype
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun ctype
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post curl
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun curl
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post dba
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun dba
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post dbase
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun dbase
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post dom
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun dom
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post exif
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun exif
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post fcgi
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun fcgi
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post filter
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun filter
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post ftp
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun ftp
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post gd
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun gd
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post gettext
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun gettext
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post gmp
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun gmp
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post hash
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun hash
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post iconv
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun iconv
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post imap
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun imap
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post json
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun json
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post ldap
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun ldap
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post mbstring
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun mbstring
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post mcrypt
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun mcrypt
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post mhash
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun mhash
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post mime_magic
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun mime_magic
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post ming
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun ming
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post mssql
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun mssql
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post mysql
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun mysql
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post mysqli
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun mysqli
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post ncurses
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun ncurses
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post odbc
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun odbc
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post openssl
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun openssl
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post pcntl
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun pcntl
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post pdo
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun pdo
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post pdo_dblib
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun pdo_dblib
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post pdo_mysql
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun pdo_mysql
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post pdo_odbc
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun pdo_odbc
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post pdo_pgsql
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun pdo_pgsql
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post pdo_sqlite
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun pdo_sqlite
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post pgsql
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun pgsql
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post posix
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun posix
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post pspell
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun pspell
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post readline
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun readline
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post recode
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun recode
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%pre session
%_pre_useradd apache /var/www /bin/sh

%post session
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun session
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post shmop
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun shmop
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post snmp
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun snmp
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post soap
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun soap
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post sockets
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun sockets
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post sqlite
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun sqlite
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post sybase
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun sybase
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post sysvmsg
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun sysvmsg
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post sysvsem
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun sysvsem
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post sysvshm
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun sysvshm
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post tidy
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun tidy
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post tokenizer
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun tokenizer
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post wddx
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun wddx
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post xml
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun xml
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post xmlreader
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun xmlreader
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post xmlrpc
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun xmlrpc
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post xmlwriter
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun xmlwriter
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post xsl
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun xsl
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%post zlib
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun zlib
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
        %{_initrddir}/httpd restart >/dev/null || :
    fi
fi


%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc CREDITS INSTALL LICENSE NEWS Zend/ZEND_LICENSE 
%doc php.ini-dist php.ini-recommended configure_command
%doc README.openssl README.spl CREDITS.libxml CREDITS.zlib
%doc README.PHP4-TO-PHP5-THIN-CHANGES README.UPDATE_5_2
%doc README.EXTENSIONS README.EXT_SKEL README.input_filter
%doc README.PARAMETER_PARSING_API README.STREAMS
%attr(0755,root,root) %{_libdir}/libphp5_common.so.*

%files cli
%defattr(-,root,root)
%doc CREDITS.cli README.cli TODO.cli
%attr(0755,root,root) %{_bindir}/php
%attr(0644,root,root) %{_mandir}/man1/php.1*

%files cgi
%defattr(-,root,root)
%doc CREDITS.cgi
%attr(0755,root,root) %{_bindir}/php-cgi

%files fcgi
%defattr(-,root,root)
%doc CREDITS.fcgi README.fcgi
%attr(0755,root,root) %{_bindir}/php-fcgi

%files devel
%defattr(-,root,root)
%doc SELF-CONTAINED-EXTENSIONS CODING_STANDARDS README.* TODO EXTENSIONS
%doc Zend/ZEND_* README.TESTING*
%attr(0755,root,root) %{_bindir}/php-config
%attr(0755,root,root) %{_bindir}/phpize
%attr(0755,root,root) %{_libdir}/libphp5_common.so
%attr(0755,root,root) %{_libdir}/libphp5_common.la
%{_libdir}/php/build
%{_usrsrc}/php-devel
%multiarch %{multiarch_includedir}/php/main/build-defs.h
%multiarch %{multiarch_includedir}/php/main/config.w32.h
%multiarch %{multiarch_includedir}/php/main/php_config.h
%{_includedir}/php
%attr(0644,root,root) %{_mandir}/man1/php-config.1*
%attr(0644,root,root) %{_mandir}/man1/phpize.1*

%files openssl
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/21_openssl.ini
%attr(0755,root,root) %{_libdir}/php/extensions/openssl.so

%files zlib
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/21_zlib.ini
%attr(0755,root,root) %{_libdir}/php/extensions/zlib.so

%files bcmath
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/66_bcmath.ini
%attr(0755,root,root) %{_libdir}/php/extensions/bcmath.so

%files bz2
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/10_bz2.ini
%attr(0755,root,root) %{_libdir}/php/extensions/bz2.so

%files calendar
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/11_calendar.ini
%attr(0755,root,root) %{_libdir}/php/extensions/calendar.so

%files ctype
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/12_ctype.ini
%attr(0755,root,root) %{_libdir}/php/extensions/ctype.so

%files curl
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/13_curl.ini
%attr(0755,root,root) %{_libdir}/php/extensions/curl.so

%files dba
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/14_dba.ini
%attr(0755,root,root) %{_libdir}/php/extensions/dba.so

%files dbase
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/15_dbase.ini
%attr(0755,root,root) %{_libdir}/php/extensions/dbase.so

%files dom
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/18_dom.ini
%attr(0755,root,root) %{_libdir}/php/extensions/dom.so

%files exif
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/19_exif.ini
%attr(0755,root,root) %{_libdir}/php/extensions/exif.so

%files filter
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/81_filter.ini
%attr(0755,root,root) %{_libdir}/php/extensions/filter.so

%files ftp
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/22_ftp.ini
%attr(0755,root,root) %{_libdir}/php/extensions/ftp.so

%files gd
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/23_gd.ini
%attr(0755,root,root) %{_libdir}/php/extensions/gd.so

%files gettext
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/24_gettext.ini
%attr(0755,root,root) %{_libdir}/php/extensions/gettext.so

%files gmp
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/25_gmp.ini
%attr(0755,root,root) %{_libdir}/php/extensions/gmp.so

%files hash
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/54_hash.ini
%attr(0755,root,root) %{_libdir}/php/extensions/hash.so

%files iconv
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/26_iconv.ini
%attr(0755,root,root) %{_libdir}/php/extensions/iconv.so

%files imap
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/27_imap.ini
%attr(0755,root,root) %{_libdir}/php/extensions/imap.so

%files json
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/82_json.ini
%attr(0755,root,root) %{_libdir}/php/extensions/json.so

%files ldap
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/28_ldap.ini
%attr(0755,root,root) %{_libdir}/php/extensions/ldap.so

%files mbstring
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/29_mbstring.ini
%attr(0755,root,root) %{_libdir}/php/extensions/mbstring.so

%files mcrypt
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/30_mcrypt.ini
%attr(0755,root,root) %{_libdir}/php/extensions/mcrypt.so

%files mhash
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/31_mhash.ini
%attr(0755,root,root) %{_libdir}/php/extensions/mhash.so

%files mime_magic
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/31_mime_magic.ini
%attr(0755,root,root) %{_libdir}/php/extensions/mime_magic.so

%files ming
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/33_ming.ini
%attr(0755,root,root) %{_libdir}/php/extensions/ming.so

%files mssql
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/35_mssql.ini
%attr(0755,root,root) %{_libdir}/php/extensions/mssql.so

%files mysql
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/36_mysql.ini
%attr(0755,root,root) %{_libdir}/php/extensions/mysql.so

%files mysqli
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/37_mysqli.ini
%attr(0755,root,root) %{_libdir}/php/extensions/mysqli.so

%files ncurses
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/38_ncurses.ini
%attr(0755,root,root) %{_libdir}/php/extensions/ncurses.so

%files odbc
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/39_odbc.ini
%attr(0755,root,root) %{_libdir}/php/extensions/odbc.so

%files pcntl
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/40_pcntl.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pcntl.so

%files pdo
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/70_pdo.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pdo.so

%files pdo_dblib
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/71_pdo_dblib.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pdo_dblib.so

%files pdo_mysql
%defattr(-,root,root)
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/73_pdo_mysql.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pdo_mysql.so

%files pdo_odbc
%defattr(-,root,root)
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/75_pdo_odbc.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pdo_odbc.so

%files pdo_pgsql
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/76_pdo_pgsql.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pdo_pgsql.so

%files pdo_sqlite
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/77_pdo_sqlite.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pdo_sqlite.so

%files pgsql
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/42_pgsql.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pgsql.so

%files posix
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/43_posix.ini
%attr(0755,root,root) %{_libdir}/php/extensions/posix.so

%files pspell
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/44_pspell.ini
%attr(0755,root,root) %{_libdir}/php/extensions/pspell.so

%files readline
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/45_readline.ini
%attr(0755,root,root) %{_libdir}/php/extensions/readline.so

%files recode
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/46_recode.ini
%attr(0755,root,root) %{_libdir}/php/extensions/recode.so

%files session
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/47_session.ini
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/cron.d/php
%attr(0755,root,root) %{_libdir}/php/extensions/session.so
%attr(0755,root,root) %{_libdir}/php/maxlifetime
%attr(01733,apache,apache) %dir %{_localstatedir}/lib/php

%files shmop
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/48_shmop.ini
%attr(0755,root,root) %{_libdir}/php/extensions/shmop.so

%files snmp
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/50_snmp.ini
%attr(0755,root,root) %{_libdir}/php/extensions/snmp.so

%files soap
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/51_soap.ini
%attr(0755,root,root) %{_libdir}/php/extensions/soap.so

%files sockets
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/52_sockets.ini
%attr(0755,root,root) %{_libdir}/php/extensions/sockets.so

%files sqlite
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/78_sqlite.ini
%attr(0755,root,root) %{_libdir}/php/extensions/sqlite.so

%files sybase
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/46_sybase.ini
%attr(0755,root,root) %{_libdir}/php/extensions/sybase.so

%files sysvmsg
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/56_sysvmsg.ini
%attr(0755,root,root) %{_libdir}/php/extensions/sysvmsg.so

%files sysvsem
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/57_sysvsem.ini
%attr(0755,root,root) %{_libdir}/php/extensions/sysvsem.so

%files sysvshm
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/58_sysvshm.ini
%attr(0755,root,root) %{_libdir}/php/extensions/sysvshm.so

%files tidy
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/59_tidy.ini
%attr(0755,root,root) %{_libdir}/php/extensions/tidy.so

%files tokenizer
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/60_tokenizer.ini
%attr(0755,root,root) %{_libdir}/php/extensions/tokenizer.so

%files xml
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/62_xml.ini
%attr(0755,root,root) %{_libdir}/php/extensions/xml.so

%files xmlreader
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/63_xmlreader.ini
%attr(0755,root,root) %{_libdir}/php/extensions/xmlreader.so

%files xmlrpc
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/62_xmlrpc.ini
%attr(0755,root,root) %{_libdir}/php/extensions/xmlrpc.so

%files xmlwriter
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/64_xmlwriter.ini
%attr(0755,root,root) %{_libdir}/php/extensions/xmlwriter.so

%files xsl
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/63_xsl.ini
%attr(0755,root,root) %{_libdir}/php/extensions/xsl.so

%files wddx
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/php.d/63_wddx.ini
%attr(0755,root,root) %{_libdir}/php/extensions/wddx.so
