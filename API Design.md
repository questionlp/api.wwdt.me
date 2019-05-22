# API Design

## Overview

This document details the high-level API routes that will need to be built out for the WWDTM Stats Page API Service. Unless otherwise noted, all API calls will be available with requiring authentication.

API calls that require authentication are done so due to the volume of data and the compute requirements to serve them at volume. This may change as request caching is implemented across the board at a later date.

## Shows

* /shows/`:id`

  Retrieve show ID, date and repeat show/Best Of information for the requested show

* /shows/`:id`/details

  Retrieve detailed show information, including: location, host, scorekeeper, panelists and guests for the requested show

* /shows/all

  Retrieve a list of all shows along with their corresponding show IDs, show dates and repeat show/Best Of information

* /shows/all/details

  **(Authenticated)** Retrieve a list of all shows with their full details, including: location, host, scorekeeper, panelists and guests

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

* /shows/recent

  Retrieve a list of recent show IDs, dates, repeat show/Best Of information for shows that fall within the past `X` days and upcoming `Y` days

* /shows/recent/details

  Retrieve a detailed list of recent shows that fall within the past `X` days and upcoming `Y` days. The detailed information would include panelist, guest and bluff information.

## Guests

 * /guests/all


 * /guests/`guest-slug`


 * /guests/id/`guest-id`


## Hosts

 * /hosts/all


 * /hosts/`host-slug`


 * /hosts/id/`host-id`


## Locations

 * /locations/all


 * /location/id/`location-id`

## Panelists

 * /panelists/all


 * /panelists/`panelist-slug`


 * /panelists/id/`panelist-id`


## Scorekeepers

 * /scorekeepers/all


 * /scorekeepers/`scorekeeper-slug`


 * /scorekeepers/id/`scorekeeper-id`



