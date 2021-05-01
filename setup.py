from setuptools import setup
from Scrappers import writeData


setup(
        name='taylormade',
        include_package_data=True,
        packages=['Scrappers.writeData', 'Scrappers.expandData'],
        entry_points={
            'console_scripts':[
                'nike=Nike:main',
                'main=Scrappers.Nike:main'
                ]
        },
     )
