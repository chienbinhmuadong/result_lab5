import requests
website='https://www.geeksforgeeks.org/python-programming-language/'
response=requests.get(website)
print(response.status_code, response.reason,'\n',response.headers["Content-Type"])