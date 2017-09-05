def sillycase(string):
    half = round(len(string)/2)                                 // Find the half index
    return string[:half].lower() + string[half:].upper()        // If you only want certain letters to be upper case //
