from setuptools import setup, find_packages

setup(
    name='google-site-verification',
    version='0.0.4',
    url='https://github.com/lotrekagency/django-google-site-verification',
    install_requires=[],
    description="django-google-site-verification",
    long_description=open('README.rst', 'r').read(),
    license="MIT",
    author="Lotrek",
    author_email="dimmitutto@lotrek.it",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
)