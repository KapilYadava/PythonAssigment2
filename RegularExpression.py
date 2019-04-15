import re

line = "From abc.xyz@pqr.com Mon Dec 29 01:12:15 2016"
domain_re = r"(@[a-z]+.[a-z]+)"
email_re = r"([a-z]+.[a-z]+@[a-z]+.[a-z]+)"
time_re = r"([0-9]+:[0-9]+:[0-9]+)"

match = re.search(domain_re, line, re.M | re.I)
print(match.group())

match = re.search(email_re, line, re.M | re.I)
print(match.group())

match = re.search(time_re, line, re.M | re.I)
print(match.group())
