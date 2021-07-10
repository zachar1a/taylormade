from setuptools import setup
from Scrappers import writeData


setup(
        name='taylormade',
        include_package_data=True,
        py_modules=['Scrappers.writeData', 'Scrappers.expandData'],
        entry_points={
            'console_scripts':[
                'nike=Nike:main',
                'hibbett=Scrappers.hibbett:main',
                'stockx=Scrappers.stockX:main',
                'dicks=Scrappers.dicksSportingGoods:main',
                'main=Scrappers.Nike:main'
                ]
        },
     )
