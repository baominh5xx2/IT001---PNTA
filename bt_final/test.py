rounded_number = 2.12123
decimal_places = 3

formatted_result = "{:.{precision}f}".format(rounded_number, precision=decimal_places)

print(formatted_result)
