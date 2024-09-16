#!/usr/bin/env python

import random

def tamper(payload, **kwargs):
    """
    Toflav3-like tamper script
    """

    if payload:
        # Example: Split and concatenate the SELECT keyword
        payload = payload.replace("SELECT", "SEL/**/ECT")
        
        # Example: Encode certain characters in hexadecimal
        payload = payload.replace(" ", "%20").replace("=", "%3D")

        # Example: Introduce randomness in keyword obfuscation
        if random.choice([True, False]):
            payload = payload.replace("AND", "A/**/ND")
        
        # Example: Use string concatenation for further obfuscation
        payload = payload.replace("FROM", "FRO" + "M")
        
        # Introduce more complex obfuscation as needed

    return payload

