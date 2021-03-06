from setuptools import setup

setup(
    name='TestBlame',
    version="0.1",
    description="collect the failed tests from junit report and send across report based on there commit history",
    author="Omkar Khatavkar",
    author_email="okhatavkar007@gmail.com",
    py_module=['testblame'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        testblame=testblame:cli
    ''',
)
