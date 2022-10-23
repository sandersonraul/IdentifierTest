def identifier(data):
    if  data.isalnum() and data[0].isalpha() and len(data) >= 1 and len(data) <= 6:
        return "Valid"
    else:
        return "Invalid"
