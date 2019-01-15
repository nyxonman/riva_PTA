import pip

# list of libraries to install if necesary
# NOTE: THis file is loaded only for POSIX not for WINDOWS
libs = ["PyQt5"]

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        print("'{}' is not installed. Installing it".format(package))
        pip.main(['install', package])

def pta_setup():
    print("\t - Checking Libraries...",end=' ')
    for lib in libs:
        import_or_install(lib)
    print("OK")

    return 0

pta_setup()