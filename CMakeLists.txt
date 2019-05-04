CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

set(qt_version ${QT_VERSION})
set(qt_short_version ${QT_MAJOR_VERSION}.${QT_MINOR_VERSION})

rez_set_archive(
    url_qt qt/qt-everywhere-opensource-src-${qt_version}.tar.gz
    http://download.qt.io/official_releases/qt/${qt_short_version}/${qt_version}/qt-everywhere-opensource-src-${qt_version}.tar.gz
)

set(make_args -j$ENV{REZ_BUILD_THREAD_COUNT})

if(${REZ_BUILD_INSTALL})
    set(install_cmd gmake install ${make_args})
else()
    set(install_cmd "")
endif()

ExternalProject_add(
    qt
    URL ${url_qt}
    PREFIX qt
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ./configure --prefix=${CMAKE_INSTALL_PREFIX} -opensource -confirm-license -no-phonon -no-phonon-backend -no-dbus -no-qt3support -no-rpath -no-webkit -fast
    INSTALL_COMMAND "${install_cmd}"
    BUILD_IN_SOURCE 1
    BUILD_COMMAND gmake ${make_args}
)

install(
    FILES cmake/qt.cmake
    DESTINATION cmake
)
