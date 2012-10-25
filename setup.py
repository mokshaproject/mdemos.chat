
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name="mdemos.chat",
    version="0.1.2",
    url="http://moksha.fedorahosted.org",
    description="Moksha Chat App",
    long_description="",
    author="Luke Macken",
    author_email="lmacken@redhat.com",
    license="ASL 2.0",
    packages=['mdemos', 'mdemos.chat'],
    namespace_packages=['mdemos'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "moksha>=0.7.0a",
    ],
    entry_points={
        'moksha.application': (
            'chat = mdemos.chat.controllers:ChatController',
        ),
        'moksha.widget': (
            'chat = mdemos.chat:LiveChatWidget',
        ),
    }
)
