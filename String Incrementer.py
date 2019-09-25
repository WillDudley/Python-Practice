#Testing re.split
import re
import unittest

# string = 'hi'
# #newstring = re.split(r'(\d*)$', string2, maxsplit=2)
# newstring = re.search('(\d*)$', string)
#
# end_number = int((newstring.group(1)) + 1 if newstring.group(1) else 1)
# print(re.split('(\d*)$', string)[0] + str(end_number))
# #newstring[1] = int(newstring[1]) + 1
# #finish = newstring[0] + str(newstring[1])
# #print finish
#
# # def my_func(string):
# #     return re.split('(\d*)$', string)[0] + str(int(re.search('(\d*)$', string).group(1)) + 1)
# #
# # print my_func('2345this7is.a!string123')
# # print my_func('1234')
# # print my_func('hi')

# newstring = re.search('(\d*)$', string)
# end_number = int((newstring.group(1)) + 1 if newstring.group(1) else 1)
# print(re.split('(\d*)$', string)[0] + str(end_number))

import re
def increment_string(string):
    newstring = re.search('(\d*)$', string)
    end_number = str(int(newstring.group(1)) + 1 if newstring.group(1) else 1).zfill(len(newstring.group(1)))
    rest = str(re.split('(\d*)$', string)[0])
    print type(end_number)
    print type(rest)
    print rest + end_number

#increment_string("foo")
increment_string("foobar001")
# increment_string("foobar1")
# increment_string("foobar00")
# increment_string("foobar99")
increment_string("foobar099")
# increment_string("")