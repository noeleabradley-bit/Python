import requests

url = 'https://w3schools.com/python/demopage.htm'
#'https://example.com'
response = requests.get(url)

# Check if the request was successful
print("status Code "
"" + str(response.status_code))
if response.status_code == 200:
    print(response.text)  # For text files
    # print(response.content)  # For binary files (images, PDFs, etc.)