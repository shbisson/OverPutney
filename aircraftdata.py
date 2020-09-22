# Using the api.joshdouche.me calls to get data from ICAO hex

import requests

def regis(hex):
        """
        Gets registration from hex
        """
        if hex == None:
                 return None
        return requests.get("https://api.joshdouch.me/hex-reg.php?hex={hex}")

def plane(hex):
        """
        Gets plane from hex
        """
        if hex == None:
                 return None
        return requests.get("https://api.joshdouch.me/hex-type.php?hex={hex}")

def oper(hex):
        """
        Gets plane from hex
        """
        if hex == None:
                 return None
        return requests.get("https://api.joshdouch.me/hex-airline.php?hex={hex}")