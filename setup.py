from setuptools import setup

setup(
    name='anonftp',
    version='1.0',
    license='GPL',
    url='https://github.com/setsid/anonftp',
    author='Vadim Kuznetsov',
    author_email='vimusov@gmail.com',
    description='Insecure anonymous FTP server',
    scripts=['anonftp'],
    install_requires=['pyftpdlib'],
)
