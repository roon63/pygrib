from distutils.core import setup, Extension
import numpy
import os

grib_api_dir = os.environ.get('GRIBAPI_DIR')
grib_api_libdir = os.environ.get('GRIBAPI_LIBDIR')
grib_api_incdir = os.environ.get('GRIBAPI_INCDIR')
jasper_dir = os.environ.get('JASPER_DIR')
jasper_libdir = os.environ.get('JASPER_LIBDIR')
jasper_incdir = os.environ.get('JASPER_INCDIR')
png_dir = os.environ.get('PNG_DIR')
png_libdir = os.environ.get('PNG_LIBDIR')
png_incdir = os.environ.get('PNG_INCDIR')
zlib_dir = os.environ.get('ZLIB_DIR')
zlib_libdir = os.environ.get('ZLIB_LIBDIR')
zlib_incdir = os.environ.get('ZLIB_INCDIR')
openjpeg_dir = os.environ.get('OPENJPEG_DIR')
openjpeg_libdir = os.environ.get('OPENJPEG_LIBDIR')
openjpeg_incdir = os.environ.get('OPENJPEG_INCDIR')

libdirs=[]
incdirs=[numpy.get_include()]
libraries=['grib_api']

if grib_api_libdir is None and grib_api_dir is not None: 
    libdirs.append(os.path.join(grib_api_dir,'lib'))
    libdirs.append(os.path.join(grib_api_dir,'lib64'))
if grib_api_incdir is None and grib_api_dir is not None: 
    incdirs.append(os.path.join(grib_api_dir,'include'))

if jasper_dir is not None or jasper_libdir is not None:
    libraries.append("jasper")
if jasper_libdir is None and jasper_dir is not None: 
    libdirs.append(os.path.join(jasper_dir,'lib'))
    libdirs.append(os.path.join(jasper_dir,'lib64'))
if jasper_incdir is None and jasper_dir is not None: 
    incdirs.append(os.path.join(jasper_dir,'include'))
    incdirs.append(os.path.join(jasper_dir,'include/jasper'))

if openjpeg_dir is not None or openjpeg_libdir is not None:
    libraries.append("openjpeg")
if openjpeg_libdir is None and openjpeg_dir is not None: 
    libdirs.append(os.path.join(openjpeg_dir,'lib'))
    libdirs.append(os.path.join(openjpeg_dir,'lib64'))
if openjpeg_incdir is None and openjpeg_dir is not None: 
    incdirs.append(os.path.join(openjpeg_dir,'include'))

if png_dir is not None or png_libdir is not None:
    libraries.append("png")
if png_libdir is None and png_dir is not None: 
    libdirs.append(os.path.join(png_dir,'lib'))
    libdirs.append(os.path.join(png_dir,'lib64'))
if png_incdir is None and png_dir is not None: 
    incdirs.append(os.path.join(png_dir,'include'))

if zlib_dir is not None or zlib_libdir is not None:
    libraries.append("z")
if zlib_libdir is None and zlib_dir is not None: 
    libdirs.append(os.path.join(zlib_dir,'lib'))
    libdirs.append(os.path.join(zlib_dir,'lib64'))
if zlib_incdir is None and zlib_dir is not None: 
    incdirs.append(os.path.join(zlib_dir,'include'))

setup(name = "pygrib",
      version = "1.7.1",
      description       = "Python module for reading GRIB files",
      author            = "Jeff Whitaker",
      author_email      = "jeffrey.s.whitaker@noaa.gov",
      url               = "http://code.google.com/p/pygrib",
      download_url      = "http://code.google.com/p/pygrib/downloads/list",
      scripts = ['utils/grib_list','utils/grib_repack'],
      ext_modules = [Extension(
        "pygrib",
        ["pygrib.c"],
	include_dirs=incdirs,
        library_dirs=libdirs,
        libraries=libraries
      )])
