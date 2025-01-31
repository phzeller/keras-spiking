# Automatically generated by nengo-bones, do not edit this file directly

# pylint: disable=consider-using-f-string

"""KerasSpiking version information.

We use semantic versioning (see http://semver.org/)
and conform to PEP440 (see https://www.python.org/dev/peps/pep-0440/).
'.dev0' will be added to the version unless the code base represents
a release version. Release versions are git tagged with the version.
"""

version_info = (0, 3, 1)

name = "keras-spiking"
dev = 0

# use old string formatting, so that this can still run in Python <= 3.5
# (since this file is parsed in setup.py, before python_requires is applied)
version = ".".join(str(v) for v in version_info)
if dev is not None:
    version += ".dev%d" % dev

copyright = "Copyright (c) 2020-2022 Applied Brain Research"
