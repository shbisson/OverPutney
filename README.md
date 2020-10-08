# OverPutney

[OverPutney](https://twitter.com/overputney) is an ADS-B Twitter Bot running on a Raspberry Pi 4.  It tracks airplanes and then tweets whenever an airplane flies overhead. It is a fork of the original AboveTustin bot, moidified to work on a Piaware with Flightaware's fork of dump1090 and adding support for [Josh Douch's free ICAO lookup APIs](https://api.joshdouch.me/).

 * Uses [tar1090](https://github.com/wiedehopf/tar1090) for ADSB message decoding, airplane tracking, and webserving.
 * Built on the [Flightaware Piaware distribution](https://flightaware.com/adsb/piaware/build).
 * Works with Chromium chromedriver webdriver on Raspberry Pi.
 * It tweets an image of a map with the airplane's track and the decoded aircraft data displayed by tar1090.
 * It displays the flight name if available, or the reported icao code.
 * It displays altitude, ground speed and heading information of the airplane at it's closest point to the bot.
 * Gives different hashtags depending on altitude, speed and time of day.
 * Adds aircraft registration, type, and owner using [Josh Douch's ICAO hex lookup APIs](https://api.joshdouch.me/).

## Dependencies
* Uses [tar1090](https://github.com/wiedehopf/tar1090) for ADSB message decoding, airplane tracking, and webserving.
* Uses [twitter](https://pypi.python.org/pypi/twitter) for tweeting.
* Uses [selenium](https://pypi.python.org/pypi/selenium) for screenshots with Chromedriver and Chromium.
* Uses [pillow](https://python-pillow.org/) for image processing.
* Uses [requests](https://pypi.org/project/requests/) for API calls.
* Uses [Chromedriver](https://chromedriver.chromium.org/) for headless web browsing.
* Builds on a running [Piaware](https://flightaware.com/adsb/piaware/build) Raspberry Pi-based ADS-B receiver and decoder with MLAT support, with web server and local databases.

## Forked from the [AboveTustin](https://github.com/kevinabrandon/AboveTustin) code written by
* [Kevin Brandon](https://github.com/kevinabrandon)
* [Joseph Prochazka](https://github.com/jprochazka)
