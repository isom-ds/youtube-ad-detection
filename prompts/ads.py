find_ad = """Find the ad.
Return in format the following format:
[
    {   'text': str,
        'start': float,
        'duration': float
    },
    ...
]
IF THE AD IS SPLIT ACROSS MULTIPLE DICTIONARIES, RETURN A LIST OF DICTIONARIES. ONLY RETURN THE DICTIONARIES IF THE AD IS PRESENT.
If there is no ad, return None."""