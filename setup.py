from setuptools import setup
from Scrappers import Nike
from Scrappers import writeData


setup(
        name='taylormade',
        include_package_data=True,
        enty_points={
            'console_scripts':[
                'Nike=Nike:main'
                ]
        },
     )
