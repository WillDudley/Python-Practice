import math


def encrypt(encrypted_text, n):
    """
    This function:
        1) Checks for outliers
        2) Creates two lists - one containing the evenly indexed elements and the other containing oddly indexed elements
        3) Joins the mentioned lists to give us the encrypted text

    Kwargs:
        encrypted_text -- the input text we want encrypted
        n -- the number of iterations of encryption we want

    Output: The encrypted text
    """
    if (encrypted_text == (None or [])) or (n <= 0):
        return encrypted_text

    for i in range(n):
        even_elements = [encrypted_text[x] for x in range(len(encrypted_text)) if (x + 1) % 2 == 0]
        odd_elements = [encrypted_text[x] for x in range(len(encrypted_text)) if (x + 1) % 2 != 0]
        encrypted_text = ''.join((even_elements + odd_elements))
    return encrypted_text

'''
def decrypt(text, n):
    """
    This function:
        1) Checks for outliers
        2) Finds the middle of the input text
        3) Sets all characters to the left of the midpoint as the odd elements, and all to the right as the even elements
        4) Makes sure the above two lists are of equal and correct length to avoid index errors
        5) Generates the decrypted text for this iteration
        6) Repeats steps 3-5 n times, with the previous iteration's decrypted text being treated as the current's text
        7) Returns the final iteration's decrypted text

    Kwargs:
        text -- the input text we want decrypted
        n -- the number of iterations of decryption we want

    Output: The decrypted text
    """
    if (text == (None or [])) or (n <= 0):
        return text

    if len(text) % 2 == 0:
        midwaypoint = int(float(len(text)) / 2.)
    else:
        midwaypoint = int(math.ceil(float(len(text)) / 2.))

    decrypted_text = text

    for j in range(n):
        text = decrypted_text

        #even_elements = [decrypted_text[x] for x in range(midwaypoint-1)]
        #odd_elements = [decrypted_text[x] for x in range(midwaypoint-1, len(text))]

        odd_elements = list(decrypted_text[:midwaypoint-1])
        even_elements = list(decrypted_text[midwaypoint-1:])

        while len(odd_elements) < midwaypoint:
            odd_elements.append('')
        while len(even_elements) < midwaypoint:
            even_elements.append('')

        decrypted_text = ''

        i = 0
        while len(decrypted_text) != len(text):
            decrypted_text = decrypted_text + even_elements[i]
            decrypted_text = decrypted_text + odd_elements[i]


            i += 1

    return decrypted_text
'''

def decrypt(text,n): #ie. abcdefg -> a,b,c are the "old" elements taken out to the front -> daebfcg

    midpoint = int(math.floor(float(len(text))) / 2.0) #ie. len=7, midpoint=3

    previous_decrypted_layer = text

    for iteration_j in range(n):

        elements_first_half = previous_decrypted_layer[:midpoint] #ie. abc
        elements_second_half = previous_decrypted_layer[midpoint:] #ie. defg

        #we want daebfg

        current_layer = ''

        count = 0
        while len(current_layer) != len(text):
            current_layer = current_layer + elements_second_half[count]
            try:
                current_layer = current_layer + elements_first_half[count]
            except IndexError:
                break

            count += 1

        previous_decrypted_layer = current_layer

    return current_layer