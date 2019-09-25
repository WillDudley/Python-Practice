import math


def encrypt(encrypted_text, n):
    for i in range(n):
        even_elements = [encrypted_text[x] for x in range(len(encrypted_text)) if (x+1) % 2 == 0]
        odd_elements = [encrypted_text[x] for x in range(len(encrypted_text)) if (x+1) % 2 != 0]
        encrypted_text = ''.join((even_elements + odd_elements))
    return encrypted_text


#print encrypt('This is a test!', 1)


def decrypt(text, n):
    midwaypoint = int(math.ceil(len(text) / 4.) * 2)
    decrypted_text = text
    for j in range(n):
        #print 'Iteration', j+1
        text = decrypted_text

        odd_elements = [decrypted_text[x] for x in range(midwaypoint-1)]
        even_elements = [decrypted_text[x] for x in range(midwaypoint-1, len(text))]
        #even_elements.insert(0, odd_elements.pop())

        while len(odd_elements) < midwaypoint:
            odd_elements.append('')
        while len(even_elements) < midwaypoint:
            even_elements.append('')

        print 'Midpoint =', midwaypoint

        print len(odd_elements)
        print len(even_elements)

        decrypted_text = ''

        i = 0
        while len(decrypted_text) != len(text):
            #print 'ev: ', even_elements[i]
            #print 'odd: ', odd_elements[i]
            decrypted_text = decrypted_text + even_elements[i]
            decrypted_text = decrypted_text + odd_elements[i]
            i += 1


    return decrypted_text


print decrypt('K&M{edgb8m!A)', 33)
