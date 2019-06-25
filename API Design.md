# API Design

## Overview

This document details the high-level API routes that will need to be built out for the WWDTM Stats Page API Service.

- [API Design](#API-Design)
  - [Overview](#Overview)
  - [JSON Response Format](#JSON-Response-Format)
    - [Success](#Success)
    - [Fail](#Fail)
    - [Error](#Error)
  - [Endpoints](#Endpoints)
    - [Guests](#Guests)
    - [Hosts](#Hosts)
    - [Locations](#Locations)
    - [Panelists](#Panelists)
    - [Scorekeepers](#Scorekeepers)
    - [Shows](#Shows)
    - [Miscellaneous Endpoints](#Miscellaneous-Endpoints)

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

All of the endpoints listed below only accept the `GET` HTTP request method. Other methods are not implemented and will return `405 Method Not Allowed` when such requests are attempted.

### Guests

* /v1.0/guests

  Retrieve guest ID, slug and name for all available guests

* /v1.0/guests/`:id`

  Retrieve guest ID, slug and name for the requested guest ID

* /v1.0/guests/`:id`/details

  Retrieve guest ID, slug, name and list of appearances for the requested guest ID

* /v1.0/guests/details

  Retrieve guest ID, slug, name and list of appearances for all available guests

* /v1.0/guests/slug/`:slug`

  Retrieve guest ID, slug and name for the requested guest slug

* /v1.0/guests/slug/`:slug`/details

  Retrieve guest ID, slug, name and list of appearances for the requested guest ID

### Hosts

* /v1.0/hosts

  Retrieve host ID, slug, name and gender for all available hosts

* /v1.0/hosts/`:id`

  Retrieve host ID, slug, name and gender for the requested host ID

* /v1.0/hosts/`:id`/details

  Retrieve host ID, slug, name, gender and list of appearances for the requested host ID

* /v1.0/hosts/details

  Retrieve host ID, slug, name, gender and list of appearances for all available hosts

* /v1.0/hosts/slug/`:slug`

  Retrieve host ID, slug, name and gender for the requested host slug

* /v1.0/hosts/slug/`:slug`/details

  Retrieve host ID, slug, name, gender and list of appearances for the requested host slug

### Locations

* /v1.0/locations

  Retrieve location ID, city, state and venue for all available locations

* /v1.0/locations/`:id`

  Retrieve location ID, city, state and venue for the requested location ID

* /v1.0/locations/`:id`/recordings

  Retrieve location ID, city, state, venue and list of shows recorded at that location

* /v1.0/locations/recordings

  Retrieve location ID, city, state, venue and shows recorded for all available locations

### Panelists

* /v1.0/panelists

  Retrieve panelist ID, slug, name and gender for all available panelists

* /v1.0/panelists/`:id`

  Retrieve panelist ID, slug, name and gender for the requested panelist ID

* /v1.0/panelists/`:id`/details

  Retrieve panelist ID, slug, name, gender, statistics and appearances for the requested panelist ID

* /v1.0/panelists/`:id`/scores

  Retrieve panelist scores with show dates in one list and corresponding scores in another list for the requested panelist ID

* /v1.0/panelists/details

  Retrieve panelist ID, slug, name, gender, statistics and appearances for all available panelists

* /v1.0/panelists/`:id`/scores/ordered-pair

  Retrieve panelist scores as a list of ordered pairs (show date, score) for the requested panelist ID

* /v1.0/panelists/slug/`:slug`

  Retrieve panelist ID, slug, name and gender for the requested panelist slug

* /v1.0/panelists/slug/`:slug`/details

  Retrieve panelist ID, slug, name, gender, statistics and appearances for the requested panelist slug

* /v1.0/panelists/slug/`:slug`/scores

  Retrieve panelist scores with show dates in one list and corresponding scores in another list for the requested panelist ID

* /v1.0/panelists/slug/`:slug`/scores/ordered-pair

  Retrieve panelist scores as a list of ordered pairs (show date, score) for the requested panelist slug

### Scorekeepers

* /v1.0/scorekeepers

  Retrieve scorekeeper ID, slug, name and gender for all available scorekeepers

* /v1.0/scorekeepers/`:id`

  Retrieve scorekeeper ID, slug, name and gender for the requested scorekeeper ID

* /v1.0/scorekeepers/`:id`/details

  Retrieve scorekeeper ID, slug, name, gender and appearances for the requested scorekeeper ID

* /v1.0/scorekeepers/all/details

  Retrieve scorekeeper ID, slug, name, gender and appearances for all available scorekeepers

* /v1.0/scorekeepers/slug/`:slug`

  Retrieve scorekeeper ID, slug, name and gender for the requested scorekeeper slug

* /v1.0/scorekeepers/slug/`:slug`/details

  Retrieve scorekeeper ID, slug, name, gender and appearances for the requested scorekeeper slug

### Shows

* /v1.0/shows

  Retrieve a list of all shows along with their corresponding show IDs, show dates and repeat show/Best Of information

* /v1.0/shows/`:id`

  Retrieve show ID, date and repeat show/Best Of information for the requested show

* /v1.0/shows/`:id`/details

  Retrieve detailed show information, including: location, host, scorekeeper, panelists and guests for the requested show

* /v1.0/shows/date/`:year`

  Retrieve a list of show IDs, dates and repeat show/Best Of information for shows from `year`.
  
  `year` needs to be provided as a four-digit year

* /v1.0/shows/date/`:year`/details

  Retrieve a list of all shows from `year` along with their corresponding show IDs, show dates and repeat show/Best Of information
  
  `year` needs to be provided as a four-digit year

* /v1.0/shows/date/`:year`/`:month`

  Retrieve a list of show IDs, dates and repeat show/Best Of information for shows from `year`/`month`
  
  `year` needs to be provided as a four-digit year

* /v1.0/shows/date/`:year`/`:month`/details

  Retrieve a list of all shows from `year`/`month` along with their full details: location, host, scorekeeper, panelists and guests
  
  `year` needs to be provided as a four-digit year

* /v1.0/shows/date/`:year`/`:month`/`:day`

  Retrieve show ID, date and repeat show/Best Of information for the show from `year`/`month`/`day`

  `year` needs to be provided as a four-digit year

* /v1.0/shows/date/`:year`/`:month`/`:day`/details

  Retrieve show information for the show from `year`/`month`/`day` along with their full details: location, host, scorekeeper, panelists and guests

  `year` needs to be provided as a four-digit year

* /v1.0/shows/date/iso/`:year`-`:month`-`:day`

  Retrieve show ID, date and repeat show/Best Of information for the show from `year`-`month`-`day`

  `year` needs to be provided as a four-digit year

* /v1.0/shows/date/iso/`:year`-`:month`-`:day`/details

  Retrieve show information for the show from `year`-`month`-`day` along with their full details: location, host, scorekeeper, panelists and guests

  `year` needs to be provided as a four-digit year

* /v1.0/shows/details

  Retrieve a list of all shows with their full details, including: location, host, scorekeeper, panelists and guests

* /v1.0/shows/recent

  Retrieve a list of recent show IDs, dates, repeat show/Best Of information for shows that fall within the past `X` days and upcoming `Y` days

* /v1.0/shows/recent/details

  Retrieve a detailed list of recent shows that fall within the past `X` days and upcoming `Y` days. The detailed information would include panelist, guest and bluff information

### Miscellaneous Endpoints

 * /v1.0/version

  Returns the version number of the libwwdtm `wwdtm` library used by the API