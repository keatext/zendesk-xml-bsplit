from setuptools import setup

setup(
    name="zendesk-xml-bsplit",
    version="0.1.0",
    py_modules=["zendesk_xml_bsplit"],
    install_requires=["humanfriendly"],
    entry_points={
        "console_scripts": [
            "zendesk-xml-bsplit=zendesk_xml_bsplit:main"
        ]
    }
)