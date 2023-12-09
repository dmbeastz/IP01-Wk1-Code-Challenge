def convert_to_24_hour(hour, minute, period):
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0
    
    return f"{hour:02d}{minute:02d}" 

# Test cases
print(convert_to_24_hour(8, 30, "am"))  # Output: 0830
print(convert_to_24_hour(8, 30, "pm"))  # Output: 2030
