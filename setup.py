from setuptools import setup, find_packages
 
version = '0.1'
 
LONG_DESCRIPTION = """
This app implements threaded discussions.
"""
 
setup(
    name='django-topics',
    version=version,
    description="django-topics",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Other/Nonlisted Topic",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='topics,django',
    author='James Tauber',
    author_email='jtauber@jtauber.com',
    url='http://github.com/RockHoward/django-topics/tree/master',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)
