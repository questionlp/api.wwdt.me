# -*- coding: utf-8 -*-
# Copyright (c) 2018-2019 Linh Pham
# wwdtm is relased under the terms of the Apache License 2.0
"""Package setup file"""

from setuptools import setup

setup(name="api_wwdtm",
      version="0.9.1",
      description="Wait Wait... Don't Tell Me! API Service",
      long_description=("Provides API service to request show, host, "
                        "scorekeeper, panelist and guest details from an "
                        "instance of the Wait Wait... Don't Tell Me! Stats "
                        "Page databse"),
      classifiers=[
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: Apache Software License 2.0",
          "Programming Language :: Python :: 3.6",
      ],
      url="http://linhpham.org/",
      author="Linh Pham",
      author_email="dev@wwdt.me",
      license="Apache License 2.0",
      project_urls={
          "Source": "https://github.com/questionlp/libwwdtm/",
      },
      python_requires=">=3.6",
      install_requires=[
          "Flask",
          "mysql-connector-python",
          "numpy",
          "python-dateutil",
          "python-slugify",
          "uWSGI",
      ],
      include_package_data=True
     )
