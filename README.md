# Wait Wait Don't Tell Me! Stats API

## Note

This version of the Wait Wait Stats API is being deprecated and the API will
be shutdown on January 31, 2023. At that time, this repository will be marked
as archived and read-only.

All development efforts has been directed to Stats API Version 2. The repository
for Stats API Version 2 is available at [api.wwdt.me_v2](https://github.com/questionlp/api.wwdt.me_v2).

## Overview

API service written in Python and using Flask to provide endpoints to query
data from an instance of the
[Wait Wait... Don't Tell Me! Stats Page](http://wwdt.me) database.

## Requirements

- Python 3.6 or newer (Python 2.x is not supported)
- MySQL or MariaDB database containing data from the Wait Wait... Don't Tell
  Me! Stats Page database

## Installation

Refer to [INSTALLING.md](INSTALLING.md) for information on how to set up an
instance of this API service that can be served through NGINX and uWSGI.

## Contributing

If you would like contribute to this project, please make sure to review both
the [Code of Conduct](CODE_OF_CONDUCT.md) and the
[Contributing](CONTRIBUTING.md) documents in this repository.

## License

This library is licensed under the terms of the
[Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0).
