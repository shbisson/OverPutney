# OverPutney
[OverPutney](https://twitter.com/overputney) is an ADS-B Twitter Bot running on a Raspberry Pi 4.  It tracks airplanes and then tweets whenever an airplane flies overhead. It is a fork of the original AboveTustin bot, moidified to work on a Piaware with Flightaware's fork of dump1090 and adding support for [Josh Douch's free ICAO lookup APIs](https://api.joshdouch.me/).

 * Uses [dump1090-fa](https://github.com/flightaware/dump1090) for ADSB message decoding, airplane tracking, and webserving.
 * Works with Chromium chromedriver webdriver on Raspberry Pi
 * It tweets an image of a map with the airplane's track.
 * It displays the flight name if available, or the reported icao code.
 * It displays altitude, ground speed and heading information of the airplane at it's closest point to the bot.
 * Gives different hashtags depending on altitude, speed and time of day.
 
## Dependencies
* Uses [dump1090-mutability](https://github.com/flightaware/dump1090) for ADSB message decoding, airplane tracking, and webserving.
* Uses [twitter](https://pypi.python.org/pypi/twitter) for tweeting.
* Uses [selenium](https://pypi.python.org/pypi/selenium) for screenshots

## Forked from AboveTustin originally written by
* [Kevin Brandon](https://github.com/kevinabrandon)
* [Joseph Prochazka](https://github.com/jprochazka)
