"""
From the given string,

pull
IP
DATE
PICS
URL

Expected Output:
---------------
123.123.123.123
26/Apr/2000
wpaper.gif
http://www.jafsoft.com/asctortf/
---------------
"""

print("input_data")
print("-" * 20)
# ----------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(input_data)

print("#" * 40, end="\n\n")
##################################

print("input_data in RAW FORMAT")
print("-" * 20)
# ----------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(repr(input_data))

print("#" * 40, end="\n\n")
##################################

print("input_data type")
print("-" * 20)
# ----------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(type(input_data))

print("#" * 40, end="\n\n")
##################################

print("Extract IP: 1-WAY")
print("-"*20)
# ----------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

ip = input_data[0:16]
print(ip)

print("#"*40, end="\n\n")
##################################

print("Extract IP: 2-WAY")
print("-"*20)
# ----------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'

index_of_1st_space = input_data.index(" ")
ip = input_data[0:index_of_1st_space]
print(ip)

# Example:
# >>> s = "WEL COME"
# >>>
# >>> # About index() method
# >>> # feature-1
# >>> s.index('E') # Index of 1st occurance of 'E'
# 1
# >>>
# >>> # feature-2
# >>> s.index('E', 3) # start searching for 'E' from index-3
# 7
# >>>
# >>> # feature-3
# >>> s.index("COME") # Returns index of 'C'
# 4
#
print("#"*40, end="\n\n")
##################################

print("Extract IP: 3-WAY")
print("-"*20)
# ----------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
sp = input_data.split() # split by space
print("input_data after split:", sp, sep="\n", end="\n\n")

ip = sp[0]
print(ip)

# >>> s = "WEL COME"
# >>> # About split() method
# >>>
# >>> # Feature-1
# >>> s.split() # split by space
# ['WEL', 'COME']
# >>>
# >>> # Feature-2
# >>> s.split('E')
# ['W', 'L COM', '']

print("#"*40, end="\n\n")
##################################

print("Extract DATE:")
print("-"*20)
# ----------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
sp = input_data.split() # split by space
print("input_data after split:", sp, sep="\n", end="\n\n")

raw_date = sp[3] # '[26/Apr/2000:00:23:48'

index_of_colon = raw_date.index(":")
dt = raw_date[1:index_of_colon]
print(dt)

print("#"*40, end="\n\n")
##################################

print("Extract PICS:")
print("-"*20)
# ----------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
sp = input_data.split() # split by space
print("input_data after split:", sp, sep="\n", end="\n\n")

raw_img = sp[6] # '/pics/wpaper.gif'

# 1-WAY to remove '/pics/' from '/pics/wpaper.gif'
img_1 = raw_img[6:]

# 2-WAY to remove '/pics/' from '/pics/wpaper.gif'
img_2 = raw_img.removeprefix("/pics/")

print(img_1, img_2, sep="\n")

print("#"*40, end="\n\n")
##################################

print("Extract URL:")
print("-"*20)
# ----------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
sp = input_data.split() # split by space
print("input_data after split:", sp, sep="\n", end="\n\n")

raw_url = sp[10] # '"http://www.jafsoft.com/asctortf/"'

# 1-WAY to remove " from '"http://www.jafsoft.com/asctortf/"'
url_1 = raw_url[1:-1]

# 2-WAY to remove " from '"http://www.jafsoft.com/asctortf/"'
url_2 = raw_url.removeprefix('"')
url_2 = url_2.removesuffix('"')

# 3-WAY to remove " from '"http://www.jafsoft.com/asctortf/"'
url_3 = raw_url.strip('"')

print(url_1, url_2, url_3, sep="\n")

print("#"*40, end="\n\n")
##################################