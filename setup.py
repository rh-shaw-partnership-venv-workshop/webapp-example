from setuptools import setup

setup(
    name='webapp-example',
    version='0.0.1',
    description='A flask app!!',
    url='https://github.com/rh-shaw-partnership-venv-workshop/webapp-example',
    install_requires=[
        'flask',
        'requests',
    ],
    python_requires=">=3.0",
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
    ],
)
