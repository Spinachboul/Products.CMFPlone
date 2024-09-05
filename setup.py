from setuptools import find_packages
from setuptools import setup


version = "6.1.0a6.dev0"


setup(
    name="Products.CMFPlone",
    version=version,
    description="The Plone Content Management System (core)",
    long_description=open("README.md").read() + "\n" + open("CHANGES.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: Core",
        "Framework :: Zope :: 5",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    keywords="Plone CMF Python Zope CMS Webapplication",
    author="Plone Foundation",
    author_email="releasemanager@plone.org",
    url="https://plone.org",
    license="GPL version 2",
    project_urls={
        "Homepage": "https://plone.org",
        "Documentation": "https://6.docs.plone.org",
        "Source": "https://github.com/plone/Products.CMFPlone",
        "Issues": "https://github.com/plone/plone.org/Products.CMFPlone",
        "Forum": "https://community.plone.org/",
        "Chat": "https://discord.gg/zFY3EBbjaj",
        "Mastodon": "https://plone.social/@plone",
        "Twitter": "https://twitter.com/plone",
        "Videos": "https://youtube.com/@plonecms",
        "Sponsor": "https://github.com/sponsors/plone",
    },
    packages=find_packages(),
    namespace_packages=["Products"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "borg.localrole",
        "five.customerize",
        "lxml",
        "plone.app.content",
        "plone.app.contentlisting",
        "plone.app.contentmenu >= 2.0.1",
        "plone.app.contentrules",
        "plone.app.contenttypes",
        "plone.app.customerize",
        "plone.app.dexterity",
        "plone.app.i18n",
        "plone.app.layout >= 2.5.15",
        "plone.app.linkintegrity >=1.0.3",
        "plone.app.locales",
        "plone.app.portlets",
        "plone.app.redirector",
        "plone.app.registry",
        "plone.app.theming",
        "plone.app.users",
        "plone.app.uuid",
        "plone.app.viewletmanager",
        "plone.app.vocabularies",
        "plone.app.workflow",
        "plone.app.z3cform >= 4.1.0",
        "plone.base",
        "plone.browserlayer >= 2.1.5",
        "plone.contentrules",
        "plone.folder",
        "plone.i18n >= 4.0.5",
        "plone.indexer",
        "plone.intelligenttext",
        "plone.locking",
        "plone.memoize",
        "plone.outputfilters",
        "plone.portlet.collection",
        "plone.portlet.static",
        "plone.portlets",
        "plone.protect >= 3.0.0",
        "plone.resource",
        "plone.schema",
        "plone.session",
        "plone.staticresources",
        "plone.theme",
        "plonetheme.barceloneta",
        "Products.CMFEditions",
        "Products.DCWorkflow",
        "Products.ExtendedPathIndex",
        "Products.isurlinportal",
        "Products.MimetypesRegistry",
        "Products.PlonePAS",
        "Products.PortalTransforms",
        "Products.SiteErrorLog",
        "Products.statusmessages",
        "setuptools>=36.2",
        "plone.autoinclude",
        "webresource>=1.2",
        "Zope[wsgi] >= 5.0",
        "zope.app.locales >= 3.6.0",
        "zope.cachedescriptors",
        "zope.deferredimport",
        "zope.deprecation",
        "zope.dottedname",
        "zope.i18n",
        "zope.i18nmessageid",
        "zope.structuredtext",
    ],
    extras_require={
        "test": [
            "lxml",
            "plone.app.robotframework>=1.0",
            "robotframework-debuglibrary",
            "plone.app.testing",
            "zope.globalrequest",
            "zope.testing",
            "gunicorn",
        ]
    },
)
