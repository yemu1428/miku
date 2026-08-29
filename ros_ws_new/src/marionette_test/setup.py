from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'marionette_test'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'launch'),
         glob(os.path.join('launch','*launch.py')) + glob(os.path.join('launch','*.yaml')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yemu',
    maintainer_email='yemu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': ['publisher=marionette_test.publisher_node:main','subscriber=marionette_test.subscriber_node:main',
        ],
    },
)
