import setuptools


setuptools.setup(
    name="calendar_project_plugin",
    description="calendar_project_plugin or generating ics files",
    packages=setuptools.find_packages("src"),
    package_dir={"":"src"},
    entry_points={
    "demo_reader.compression_plugins"
    }

)

