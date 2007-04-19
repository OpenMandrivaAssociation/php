%define _requires_exceptions BEGIN\\|mkinstalldirs\\|pear(\\|/usr/bin/tclsh

%define epoch 3
%define major 5
%define libname %mklibname php5_common %{major}

%define suhosin_version 0.9.6.2

Summary:	The PHP5 scripting language
Name:		php
Version:	5.2.1
Release:	%mkrel 5
Group:		Development/PHP
License:	PHP License
URL:		http://www.php.net
Source0:	http://se.php.net/distributions/php-%{version}.tar.gz
Patch0:		php-4.3.0-init.patch
Patch1:		php-5.2.0-shared.diff
Patch2:		php-4.3.0-imap.patch
Patch3:		php-4.3.4RC3-64bit.patch
Patch4:		php-5.1.2-lib64.diff
Patch6:		php-4.3.11-libtool.diff
Patch7:		php-5.2.0-no_egg.diff
Patch8:		php-5.1.2-phpize.diff
Patch9:		php-5.1.0RC4-remove_bogus_iconv_deps.diff
Patch10:	php-5.1.0RC1-phpbuilddir.diff
# for kolab2
Patch11:	php-5.1.3-imap-annotation.diff
Patch12:	php-5.0.4-imap-status-current.diff
# http://www.outoforder.cc/projects/apache/mod_transform/
# http://www.outoforder.cc/projects/apache/mod_transform/patches/php5-apache2-filters.patch
Patch13:	php5-apache2-filters.diff
# P14 fixes the way we package the extensions to not check if the dep are installed or compiled in
Patch14:	php-5.1.3-extension_dep_macro_revert.diff
# remove libedit once and for all
Patch15:	php-5.1.2-no_libedit.diff
#####################################################################
# Stolen from PLD
Patch20:	php-4.3.0-mail.patch
Patch21:	php-sybase-fix.patch
Patch23:	php-5.2.0-mdv_logo.diff
Patch25:	php-dba-link.patch
Patch27:	php-zlib-for-getimagesize.patch
Patch28:	php-zlib.patch
# http://choon.net/opensource/php/php-5.0.5-mail-header.patch
Patch29:	php-5.1.2-mail-header.diff
# stolen from debian
Patch30:	php-5.1.4-session.save_path.diff
Patch31:	php-5.1.4-recode_size_t.diff
Patch32:	php-5.1.4-exif_nesting_level.diff
#####################################################################
# Stolen from fedora
Patch101:	php-5.1.0b1-cxx.diff
Patch102:	php-4.3.3-install.patch
Patch103:	php-5.0.4-norpath.patch
Patch105:	php-umask.diff
Patch106:	php-5.2.1-strreplace.patch
# Fixes for extension modules
Patch111:	php-4.3.1-odbc.patch
Patch112:	php-4.3.11-shutdown.patch
Patch113:	php-5.2.0-libc-client-php.diff
# Functional changes
Patch115:	php-5.0.4-dlopen.patch
# Fixes for tests
Patch120:	php-5.1.0RC4-tests-dashn.diff
Patch121:	php-5.1.0b1-tests-wddx.diff
# Fix bugs
Patch200:	php-bug-22414.patch
# http://bugs.php.net/bug.php?id=29119
Patch201:	php-5.0.4-bug29119.diff
Patch202:	php-5.1.0RC6-CVE-2005-3388.diff
Patch208:	php-extraimapcheck.diff
Patch210:	php-CVE-2007-0455.diff
Patch211:	php-5.1.6-CVE-2007-1001.patch
Patch212:	php-5.2.1-CVE-2007-1285.patch
Patch213:	php-5.1.6-CVE-2007-1583.patch
Patch214:	php-5.1.6-CVE-2007-1718.patch
Patch215:	php-5.2.1-CVE-2007-1454.patch
# http://www.suhosin.org/
Patch300:	suhosin-patch-%{version}-%{suhosin_version}.patch.gz
Source4:	suhosin-patch-%{version}-%{suhosin_version}.patch.gz.sig
BuildRequires:	apache-devel >= 2.0.54
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7
BuildRequires:	bison
BuildRequires:	byacc
BuildRequires:	dos2unix
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
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
PHP5 is an HTML-embeddable scripting language. PHP5 offers built-in
database integration for several commercial and non-commercial
database management systems, so writing a database-enabled script
with PHP5 is fairly simple.  The most common use of PHP5 coding is
probably as a replacement for CGI scripts.

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
Requires(post):	php-simplexml >= %{version}
Requires(post):	php-suhosin >= 0.9.10
Requires(post):	php-filter >= 0.11.0
Requires(post):	php-json >= 1.2.1
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
Requires(preun): php-simplexml >= %{version}
Requires(preun): php-suhosin >= 0.9.10
Requires(preun): php-filter >= 0.11.0
Requires(preun): php-json >= 1.2.1
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
Requires:	php-simplexml >= %{version}
Requires:	php-suhosin >= 0.9.10
Requires:	php-filter >= 0.11.0
Requires:	php-json >= 1.2.1
Requires:	php-timezonedb >= 2007.3
Provides:	php php3 php4
Obsoletes:	php php3 php4
Epoch:		%{epoch}

%description	cli
PHP5 is an HTML-embeddable scripting language. PHP5 offers built-in
database integration for several commercial and non-commercial
database management systems, so writing a database-enabled script
with PHP5 is fairly simple.  The most common use of PHP5 coding is
probably as a replacement for CGI scripts.

This package contains a command-line (CLI) version of php. You must
also install libphp5_common. If you need apache module support, you
also need to install the apache-mod_php package.

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
Requires(post):	php-simplexml >= %{version}
Requires(post):	php-suhosin >= 0.9.10
Requires(post):	php-filter >= 0.11.0
Requires(post):	php-json >= 1.2.1
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
Requires(preun): php-simplexml >= %{version}
Requires(preun): php-suhosin >= 0.9.10
Requires(preun): php-filter >= 0.11.0
Requires(preun): php-json >= 1.2.1
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
Requires:	php-simplexml >= %{version}
Requires:	php-suhosin >= 0.9.10
Requires:	php-filter >= 0.11.0
Requires:	php-json >= 1.2.1
Requires:	php-timezonedb >= 2007.3
Provides:	php php3 php4
Obsoletes:	php php3 php4
Epoch:		%{epoch}

%description	cgi
PHP5 is an HTML-embeddable scripting language. PHP5 offers built-in
database integration for several commercial and non-commercial
database management systems, so writing a database-enabled script
with PHP5 is fairly simple.  The most common use of PHP5 coding is
probably as a replacement for CGI scripts.

This package contains a standalone (CGI) version of php. You must
also install libphp5_common. If you need apache module support, you
also need to install the apache-mod_php package.

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
Requires(post):	php-simplexml >= %{version}
Requires(post):	php-suhosin >= 0.9.10
Requires(post):	php-filter >= 0.11.0
Requires(post):	php-json >= 1.2.1
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
Requires(preun): php-simplexml >= %{version}
Requires(preun): php-suhosin >= 0.9.10
Requires(preun): php-filter >= 0.11.0
Requires(preun): php-json >= 1.2.1
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
Requires:	php-simplexml >= %{version}
Requires:	php-suhosin >= 0.9.10
Requires:	php-filter >= 0.11.0
Requires:	php-json >= 1.2.1
Requires:	php-timezonedb >= 2007.3
Provides:	php php3 php4
Obsoletes:	php php3 php4
Epoch:		%{epoch}

%description	fcgi
PHP5 is an HTML-embeddable scripting language. PHP5 offers built-in
database integration for several commercial and non-commercial
database management systems, so writing a database-enabled script
with PHP5 is fairly simple.  The most common use of PHP5 coding is
probably as a replacement for CGI scripts.

This package contains a standalone (CGI) version of php with FastCGI
support. You must also install libphp5_common. If you need apache
module support, you also need to install the apache-mod_php
package.

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
Epoch:		%{epoch}

%description -n	%{libname}
This package provides the common files to run with different
implementations of PHP5. You need this package if you install the
php standalone package or a webserver with php support (ie: 
apache-mod_php).

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
Requires:	apache-base >= 2.0.54
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
The php-devel package lets you compile dynamic extensions to
PHP5. Included here is the source for the php extensions. Instead
of recompiling the whole php binary to add support for, say,
oracle, install this package and use the new self-contained
extensions support. For more information, read the file
SELF-CONTAINED-EXTENSIONS.

This version of php has the suhosin patch %{suhosin_version} applied. Please
report bugs here: http://qa.mandriva.com/ so that the official maintainer of
this Mandriva package can help you. More information regarding the
suhosin patch %{suhosin_version} here: http://www.suhosin.org/

%package	openssl
Summary:	OpenSSL extension module for PHP
Group:		Development/PHP
Epoch:		%{epoch}

%description	openssl
This is a dynamic shared object (DSO) for PHP that will add OpenSSL support.

%package	zlib
Summary:	Zlib extension module for PHP
Group:		Development/PHP
Epoch:		%{epoch}

%description	zlib
This is a dynamic shared object (DSO) for PHP that will add zlib compression
support to PHP.

%prep

%setup -q -n php-%{version}

# the ".droplet" suffix is here to nuke the backups later..., we don't want those in php-devel
%patch0 -p1 -b .init.droplet
%patch1 -p1 -b .shared.droplet
%patch2 -p0 -b .imap.droplet
%patch3 -p1 -b .64bit.droplet
%patch4 -p1 -b .lib64.droplet
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

#####################################################################
# Stolen from PLD
%patch20 -p1 -b .mail.droplet
%patch21 -p1 -b .sybase-fix.droplet
%patch25 -p1 -b .dba-link.droplet

%patch27 -p1 -b .zlib-for-getimagesize.droplet
%patch28 -p1 -b .zlib.droplet
%patch29 -p0 -b .mail-header.droplet
# stolen from debian
%patch30 -p0 -b .session.save_path.droplet
%patch31 -p0 -b .recode_size_t.droplet
%patch32 -p0 -b .exif_nesting_level.droplet

#####################################################################
# Stolen from fedora
%patch101 -p0 -b .cxx.droplet
%patch102 -p1 -b .install.droplet
%patch103 -p1 -b .norpath.droplet
%patch105 -p0 -b .umask.droplet
%patch106 -p1 -b .strreplace
%patch111 -p1 -b .odbc.droplet
%patch112 -p1 -b .shutdown.droplet
%patch113 -p0 -b .libc-client-php.droplet
%patch115 -p1 -b .dlopen.droplet
#
#%patch120 -p1 -b .tests-dashn.droplet
%patch121 -p1 -b .tests-wddx.droplet

# make the tests worky
%patch200 -p1 -b .bug-22414.droplet
%patch201 -p0 -b .bug29119.droplet

# security fixes
%patch202 -p0 -b .CVE-2005-3388.droplet

%patch208 -p0 -b .open_basedir_and_safe_mode_checks.droplet
%patch210 -p0 -b .php-CVE-2007-0455.droplet
%patch211 -p1 -b .php-CVE-2007-1001.droplet
%patch212 -p1 -b .php-CVE-2007-1285.droplet
%patch213 -p1 -b .php-CVE-2007-1583.droplet
%patch214 -p1 -b .php-CVE-2007-1718.droplet
%patch215 -p1 -b .php-CVE-2007-1454.droplet

%patch300 -p1 -b .suhosin.droplet
%patch7 -p1 -b .no_egg.droplet
%patch23 -p1 -b .mdv_logo.droplet

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
rm -rf php-devel/extensions/com
rm -rf php-devel/extensions/dotnet
rm -rf php-devel/extensions/printer
rm -rf php-devel/extensions/w32api

# likewise with these:
find php-devel -name "*.dsp" | xargs rm -f
find php-devel -name "*.mak" | xargs rm -f
find php-devel -name "*.w32" | xargs rm

# strip away annoying ^M
find -type f | \
    grep -v "\.gif" | \
    grep -v "\.gz" | \
    grep -v "\.jpeg" | \
    grep -v "\.jpg" | \
    grep -v "\.png" | \
    grep -v "\.psd" | \
    grep -v "\.tgz" | \
    grep -v "\.ttf" | \
    grep -v "\.zip" | \
    xargs dos2unix -U

cat > php-devel/buildext <<EOF
#!/bin/bash
gcc -Wall -fPIC -shared %{optflags} \\
    -I. \`%{_bindir}/php-config --includes\` \\
    -I%{_includedir}/libxml2 \\
    -I%{_includedir}/freetype \\
    -I%{_includedir}/openssl \\
    -I%{_usrsrc}/php-devel/ext \\
    -I%{_includedir}/\$1 \\
    \$4 \$2 -o \$1.so \$3 -lc
EOF

chmod 755 php-devel/buildext

%build
# this _has_ to be executed!
#export WANT_AUTOCONF_2_5=1

rm -f configure; libtoolize --copy --force; aclocal-1.7; autoconf --force; autoheader
#./buildconf --force

# Do this patch with a perl hack...
perl -pi -e "s|'\\\$install_libdir'|'%{_libdir}'|" ltmain.sh

export oldstyleextdir=yes
export EXTENSION_DIR="%{_libdir}/php/extensions"
export PROG_SENDMAIL="%{_sbindir}/sendmail"
export CFLAGS="%{optflags} -fPIC -L%{_libdir}"

# never use "--disable-rpath", it does the opposite

# Configure php5
for i in cgi cli fcgi apxs; do
./configure \
    `[ $i = fcgi ] && echo --enable-fastcgi --with-fastcgi=%{_prefix} --disable-cli --enable-force-cgi-redirect` \
    `[ $i = cgi ] && echo --enable-discard-path --disable-cli --enable-force-cgi-redirect` \
    `[ $i = apxs ] && echo --with-apxs2=%{_sbindir}/apxs` \
    `[ $i = cli ] && echo --disable-cgi --enable-cli` \
    --cache-file=config.cache \
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
    --localstatedir=%{_localstatedir} \
    --mandir=%{_mandir} \
    --enable-shared=yes \
    --enable-static=no \
    --with-libdir=%{_lib} \
    --disable-all \
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
    --with-mod_charset \
    --without-pear

cp -f Makefile Makefile.$i

# left for debugging purposes
cp -f main/php_config.h php_config.h.$i

# when all else failed...
perl -pi -e "s|-prefer-non-pic -static||g" Makefile.$i

done

# remove all confusion...
perl -pi -e "s|^#define CONFIGURE_COMMAND .*|#define CONFIGURE_COMMAND \"This is irrelevant, look inside the %{_docdir}/libphp5_common%{major}-%{version}/configure_command file. urpmi is your friend, use it to install extensions not shown below.\"|g" main/build-defs.h
cp config.nice configure_command; chmod 644 configure_command

%make

# make php-fcgi
cp -af php_config.h.fcgi main/php_config.h
%make -f Makefile.fcgi sapi/cgi/php
cp -rp sapi/cgi sapi/fcgi
perl -pi -e "s|sapi/cgi|sapi/fcgi|g" sapi/fcgi/php
rm -rf sapi/cgi/.libs; rm -f sapi/cgi/*.lo sapi/cgi/php

# make php-cgi
cp -af php_config.h.cgi main/php_config.h
%make -f Makefile.cgi sapi/cgi/php

cp -af php_config.h.apxs main/php_config.h

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sysconfdir}/php.d
install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_usrsrc}/php-devel
install -d %{buildroot}%{_mandir}/man1

#perl -pi -e "s|^libdir=.*|libdir='%{_libdir}'|g" .libs/*.la*

make -f Makefile.apxs install \
	INSTALL_ROOT=%{buildroot} \
	INSTALL_IT="\$(LIBTOOL) --mode=install install libphp5_common.la %{buildroot}%{_libdir}/" \
	INSTALL_CLI="\$(LIBTOOL) --silent --mode=install install sapi/cli/php %{buildroot}%{_bindir}/php"

./libtool --silent --mode=install install sapi/fcgi/php %{buildroot}%{_bindir}/php-fcgi
./libtool --silent --mode=install install sapi/cgi/php %{buildroot}%{_bindir}/php-cgi

cp -dpR php-devel/* %{buildroot}%{_usrsrc}/php-devel/
install -m0644 run-tests*.php %{buildroot}%{_usrsrc}/php-devel/
install -m0644 main/internal_functions.c %{buildroot}%{_usrsrc}/php-devel/

install -m0644 sapi/cli/php.1 %{buildroot}%{_mandir}/man1/
install -m0644 scripts/man1/phpize.1 %{buildroot}%{_mandir}/man1/
install -m0644 scripts/man1/php-config.1 %{buildroot}%{_mandir}/man1/

ln -snf extensions %{buildroot}%{_usrsrc}/php-devel/ext

# extensions
echo "extension = openssl.so" > %{buildroot}%{_sysconfdir}/php.d/21_openssl.ini
echo "extension = zlib.so" > %{buildroot}%{_sysconfdir}/php.d/21_zlib.ini

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

# fix one strange weirdo
%{__perl} -pi -e "s|^libdir=.*|libdir='%{_libdir}'|g" %{buildroot}%{_libdir}/*.la

%multiarch_includes %{buildroot}%{_includedir}/php/main/build-defs.h
%multiarch_includes %{buildroot}%{_includedir}/php/main/config.w32.h
%multiarch_includes %{buildroot}%{_includedir}/php/main/php_config.h

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

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
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/*_openssl.ini
%attr(0755,root,root) %{_libdir}/php/extensions/openssl.so

%files zlib
%defattr(-,root,root)
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/*_zlib.ini
%attr(0755,root,root) %{_libdir}/php/extensions/zlib.so
