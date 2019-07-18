from setuptools import setup


setup(
    name="azureml-custom-module-import-data",
    version="0.0.2",
    description="Import data custom modules.",
    packages=["import_data_torchvision", "import_data_generic_folder"],
    author="Heyi Tang",
    license="MIT",
    include_package_data=True,
)
