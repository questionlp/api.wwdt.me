# API Design

## Overview

This document details the high-level API routes that will need to be built out for the WWDTM Stats Page API Service. Unless otherwise noted, all API calls will be available with requiring authentication.

API calls that require authentication are done so due to the volume of data and the compute requirements to serve them at volume. This may change as request caching is implemented across the board at a later date.

* [JSON Response Format](#json-response-format)
  * [Success](#success)
  * [Fail](#fail)
  * [Error](#error)
* [Endpoints](#endpoints)
  * [Guests](#guests)
  * [Hosts](#hosts)
  * [Locations](#locations)
  * [Panelists](#panelists)
  * [Scorekeepers](#scorekeepers)
  * [Shows](#shows)

## JSON Response Format

The JSON repsonse format used to return data, failure details and error messages is based on the [JSend](https://github.com/omniti-labs/jsend) specification for its simplicity.

All responses will include a status key with either `success`, `fail` or `error` as its value. See the following sections for more information.

### Success

For successful responses, a `success` status will be returned and the response object will be returned as part of the `data` key.

    {
        status: "success",
        data: {
            response-object
        }
    }

In addition to the JSON response being returned in the response body, a status code of `200` will be returned in the HTTP header(s).

### Fail

For responses that fail due to issues with the user input or where a requested object cannot be located, a `fail` status will be returned with a reason included in the `data` key.

    {
        status: "fail",
        data: {
            fail-details
        }
    }

In addition to the JSON response being returned in the response body, a status code of `404` will be returned when a requested object cannot be located. Other fail conditions will return a `400`.

### Error

For responses that fail during the processing of the request, an `error` status will be returned and a description of the error will be returned within the `message` key.

    {
        status: "error",
        message: error-message
    }

In addition to the JSON response being returned in the response body, a status code of `500` will be returned when an error occurs.

## Endpoints

### Guests

* /guests

  Retrieve guest ID, slug and name for all available guests

* /guests/`:id`

  Retrieve guest ID, slug and name for the requested guest ID

* /guests/`:id`/details

  Retrieve guest ID, slug, name and list of appearances for the requested guest ID

* /guests/details

  **(Authenticated)** Retrieve guest ID, slug, name and list of appearances for all available guests

* /guests/slug/`:slug`

  Retrieve guest ID, slug and name for the requested guest slug

* /guests/slug/`:slug`/details

  Retrieve guest ID, slug, name and list of appearances for the requested guest ID

### Hosts

* /hosts

  Retrieve host ID, slug, name and gender for all available hosts

* /hosts/`:id`

  Retrieve host ID, slug, name and gender for the requested host ID

* /hosts/`:id`/details

  Retrieve host ID, slug, name, gender and list of appearances for the requested host ID

* /hosts/details

  **(Authenticated)** Retrieve host ID, slug, name, gender and list of appearances for all available hosts

* /hosts/slug/`:slug`

  Retrieve host ID, slug, name and gender for the requested host slug

* /hosts/slug/`:slug`/details

  Retrieve host ID, slug, name, gender and list of appearances for the requested host slug

### Locations

* /locations

  Retrieve location ID, city, state and venue for all available locations

* /locations/`:id`

  Retrieve location ID, city, state and venue for the requested location ID

* /locations/`:id`/recordings

  Retrieve location ID, city, state, venue and list of shows recorded at that location

* /locations/recordings

  **(Authenticated)** Retrieve location ID, city, state, venue and shows recorded for all available locations

### Panelists

* /panelists

  Retrieve panelist ID, slug, name and gender for all available panelists

* /panelists/`:id`

  Retrieve panelist ID, slug, name and gender for the requested panelist ID

* /panelists/`:id`/details

  Retrieve panelist ID, slug, name, gender, statistics and appearances for the requested panelist ID

* /panelists/`:id`/scores

  Retrieve panelist scores with show dates in one list and corresponding scores in another list for the requested panelist ID

* /panelists/details

  **(Authenticated)** Retrieve panelist ID, slug, name, gender, statistics and appearances for all available panelists

* /panelists/`:id`/scores/ordered-pair

  Retrieve panelist scores as a list of ordered pairs (show date, score) for the requested panelist ID

* /panelists/slug/`:slug`

  Retrieve panelist ID, slug, name and gender for the requested panelist slug

* /panelists/slug/`:slug`/details

  Retrieve panelist ID, slug, name, gender, statistics and appearances for the requested panelist slug

* /panelists/slug/`:slug`/scores

  Retrieve panelist scores with show dates in one list and corresponding scores in another list for the requested panelist ID

* /panelists/slug/`:slug`/scores/ordered-pair

  Retrieve panelist scores as a list of ordered pairs (show date, score) for the requested panelist slug

### Scorekeepers

* /scorekeepers

  Retrieve scorekeeper ID, slug, name and gender for all available scorekeepers

* /scorekeepers/`:id`

  Retrieve scorekeeper ID, slug, name and gender for the requested scorekeeper ID

* /scorekeepers/`:id`/details

  Retrieve scorekeeper ID, slug, name, gender and appearances for the requested scorekeeper ID

* /scorekeepers/all/details

  **(Authenticated)** Retrieve scorekeeper ID, slug, name, gender and appearances for all available scorekeepers

* /scorekeepers/slug/`:slug`

  Retrieve scorekeeper ID, slug, name and gender for the requested scorekeeper slug

* /scorekeepers/slug/`:slug`/details

  Retrieve scorekeeper ID, slug, name, gender and appearances for the requested scorekeeper slug

### Shows

* /shows

  Retrieve a list of all shows along with their corresponding show IDs, show dates and repeat show/Best Of information

* /shows/`:id`

  Retrieve show ID, date and repeat show/Best Of information for the requested show

* /shows/`:id`/details

  Retrieve detailed show information, including: location, host, scorekeeper, panelists and guests for the requested show

* /shows/date/`:year`

  Retrieve a list of show IDs, dates and repeat show/Best Of information for shows from `year`

* /shows/date/`:year`/details

  **(Authenticated)** Retrieve a list of all shows from `year` along with their corresponding show IDs, show dates and repeat show/Best Of information

* /shows/date/`:year`/`:month`

  Retrieve a list of show IDs, dates and repeat show/Best Of information for shows from `year`/`month`

* /shows/date/`:year`/`:month`/details

  Retrieve a list of all shows from `year`/`month` along with their full details: location, host, scorekeeper, panelists and guests

* /shows/date/`:year`/`:month`/`:day`

  Retrieve show ID, date and repeat show/Best Of information for the show from `year`/`month`/`day`

* /shows/date/`:year`/`:month`/`:day`/details

  Retrieve show information for the show from `year`/`month`/`day` along with their full details: location, host, scorekeeper, panelists and guests

* /shows/details

  **(Authenticated)** Retrieve a list of all shows with their full details, including: location, host, scorekeeper, panelists and guests

* /shows/recent

  Retrieve a list of recent show IDs, dates, repeat show/Best Of information for shows that fall within the past `X` days and upcoming `Y` days

* /shows/recent/details

  Retrieve a detailed list of recent shows that fall within the past `X` days and upcoming `Y` days. The detailed information would include panelist, guest and bluff information
