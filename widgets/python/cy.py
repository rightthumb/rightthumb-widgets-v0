from setuptools import setup
from Cython.Build import cythonize
import platform

setup(
    ext_modules=cythonize("files.ob.py", compiler_directives={"language_level": "3"}),
    options={"build_ext": {"plat_name": "win-amd64" if platform.system() == "Windows" else None}}
)

