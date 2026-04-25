url = "<https://www.example.com/page>"

url = url.replace('<https://','')
url = url.replace('<http://','' )

url = url.replace('www.','')

s = url.split("/")

print(s[0])


#split /
#example.com/page>

#[example.com, page>]