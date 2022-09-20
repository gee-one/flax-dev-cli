from setuptools import setup

if __name__ == '__main__':
    setup(
        name='fd_cli',
        version='0.0.2',
        packages=[
            'fd_cli'
        ],
        url='https://github.com/zqrx/fd-cli',
        license='GNU General Public License v2.0',
        author='zqrx',
        author_email='',
        description='',
        install_requires=[
            'click~=8.1.3',
            'chia-blockchain~=1.5.1',
            'setuptools~=65.3.0',
            'requests~=2.28.1'
        ],
        entry_points={
            'console_scripts': [
                'fd-cli = fd_cli.fd_cli:main',
                'flora-dev-cli = fd_cli.fd_cli:main'
            ]
        }
    )
