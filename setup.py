from distutils.core import setup

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='django-receipt',
    version='1.0.0',
    packages=['receipt', 'receipt.templates', 'receipt.templatetags'],
    package_dir={'': 'project_receipt'},
    url='https://github.com/Guilouf/django-receipt',
    license='Apache 2.0',
    author='Guilouf',
    description='Django app for storing receipts from purchases',
    install_requires=['django-filter'],
    long_description=long_description,  # will be included in METADATA file in dist-info folder
    long_description_content_type='text/markdown',
    include_package_data=True  # for non python files, e.g html templates or static css
)
