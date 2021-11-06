import setuptools
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setuptools.setup(
    name="uptime_kuma_monitor",
    version="1.0.0",
    description="Python wrapper around Uptime Kuma /metrics endpoint",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["requests", "prometheus-client"],
    py_modules=["uptime_kuma_monitor"],
)
