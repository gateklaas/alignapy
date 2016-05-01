from setuptools import setup, find_packages
setup(
    name = "Alignapy",
    version = "0.2",
    packages = find_packages(),
    namespace_packages=['alignapy'],
    include_package_data=True,
    install_requires=[
                'rdflib>=4.0.1',
                'nltk>=2.0',
                'requests>=2.0.0',
    ],
    author = "Klaas Schuijtemaker",
    author_email = "klaas_schuijtemaker@hotmail.com",
    description = "Basic ontology matching",
    license = "LGPL",
    keywords = "rdf ontology matching linked data semantic web alignment",
    url = "https://github.com/gateklaas/alignapy",   # project home page, if any
)

