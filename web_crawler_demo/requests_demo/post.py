import requests

data = {
    'name': 'LiHua',
    'age': '23'
}
response = requests.post('https://httpbin.org/post',data=data)
print(response.text)