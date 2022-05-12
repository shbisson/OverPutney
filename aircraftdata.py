# Using the api.joshdouch.me calls to get data from ICAO hex

import requests

def regis(hex):
        """
        Gets registration from hex
        """
        if hex == None:
                 return None
        regis = requests.get(f"https://api.joshdouch.me/hex-reg.php?hex={hex}")
        if regis.text == "n/a":
                regist.text=""
        return regis.text

def plane(hex):
        """
        Gets plane from hex
        """
        if hex == None:
                 return None
        plane = requests.get(f"https://api.joshdouch.me/hex-type.php?hex={hex}")
        if plane.text == "n/a":
                plane.text=""
        return plane.text

def oper(hex):
        """
        Gets plane from hex
        """
        if hex == None:
                 return None
        oper = requests.get(f"https://api.joshdouch.me/hex-airline.php?hex={hex}")
        if oper.text == "n/a":
                oper.text = ""
        return oper.text

def route(flight):
        """
        Gets route from callsign
        """
        if flight == None:
                         return None
        # ICAOroute = requests.get(f"https://api.joshdouch.me/callsign-route.php?callsign={flight}")
        origin = requests.get(f"https://api.joshdouch.me/callsign-origin_ICAO.php?callsign={flight}")
        destination = requests.get(f"https://api.joshdouch.me/callsign-des_ICAO.php?callsign={flight}")
        origin_IATA = requests.get(f"https://api.joshdouch.me/ICAO-IATA.php?icao={origin.text}")
        destination_IATA = requests.get(f"https://api.joshdouch.me/ICAO-IATA.php?icao={destination.text}")
        origin_name = requests.get(f"https://api.joshdouch.me/ICAO-airport.php?icao={origin.text}")
        destination_name = requests.get(f"https://api.joshdouch.me/ICAO-airport.php?icao={destination.text}")
       
        route = origin_IATA.text + "-" + destination_IATA.text + " " + origin_name.text + " to " + destination_name.text
        # route = destination.text + "-" + origin.text
        # print (route)
        if route == "n/a-n/a n/a to n/a":
                route = ""
        return route