import re


a = '<p>WJZ16421212</p>'

re_vcode = re.compile(r'<p>(WJZ\d+)<')
print(re_vcode.search(a).group(1))