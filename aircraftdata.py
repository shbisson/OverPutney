# Using the api.joshdouche.me calls to get data from ICAO hex

import requests

def regis(hex):
        """
        Gets registration from hex
        """
        if hex == None:
                 return None
        regis = requests.get(f"https://api.joshdouch.me/hex-reg.php?hex={hex}")
        return regis.text

def plane(hex):
        """
        Gets plane from hex
        """
        if hex == None:
                 return None
        plane = requests.get(f"https://api.joshdouch.me/hex-type.php?hex={hex}")
        return plane.text

def oper(hex):
        """
        Gets plane from hex
        """
        if hex == None:
                 return None
        oper = requests.get(f"https://api.joshdouch.me/hex-airline.php?hex={hex}")
        return oper.text