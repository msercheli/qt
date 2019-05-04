name = "qt"

version = "4.8.7"

description = \
    """
    Qt
    """

build_requires = [
    "python-2.7"
]

def commands():
    # export CMAKE_MODULE_PATH=$CMAKE_MODULE_PATH:!ROOT!/cmake
    # export QTDIR=!ROOT!
    # export QT_INCLUDE_DIR=!ROOT!/include
    # export QT_LIB_DIR=!ROOT!/lib
    # export LD_LIBRARY_PATH=!ROOT!/lib:$LD_LIBRARY_PATH
    # export QTLIB=!ROOT!/lib
    # export QT_QMAKE_EXECUTABLE=!ROOT!/bin/qmake
    # export PATH=!ROOT!/bin:$PATH
    # export CMAKE_MODULE_PATH=$CMAKE_MODULE_PATH:!ROOT!/cmake
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.QT_ROOT = '{root}'
    if building:
        env.CMAKE_MODULE_PATH.append("{root}/cmake")

uuid = "repository.qt"
