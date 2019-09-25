def get_colour(digit):
    return {
        '0': 'black ',
        '1': 'brown ',
        '2': 'red ',
        '3': 'orange ',
        '4': 'yellow ',
        '5': 'green ',
        '6': 'blue ',
        '7': 'violet ',
        '8': 'gray ',
        '9': 'white '
    }[digit]


def encode_resistor_colors(ohms_string):
    nws = ohms_string.split(' ', 1)[0].replace('.', '')  # number with suffix, ignoring commas
    s = nws[-1]  # suffix - '', 'k', or 'M'
    suffix_multiplier = {
        'k': 10**3,
        'M': 10**6
    }.get(s, 1)  # converts suffix to respective int
    number = int(nws[:-1] if suffix_multiplier != 1 else nws) * suffix_multiplier  # full number, including suffix
    power = str(len(str(number)) - 2 - ('.' in ohms_string))

    j = nws[1]
    if j == 'k' or j == 'M':
        second_digit = '0'
    else:
        second_digit = j

    return get_colour(nws[0]) + get_colour(second_digit) + get_colour(power) + 'gold'


print(encode_resistor_colors("1k ohms"))
