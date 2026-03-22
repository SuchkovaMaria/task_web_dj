import requests

def request_post():

    url = 'http://localhost:8080/'

    data = "тест запроса do_POST"

    response = requests.post(url, data=data)
    response_status = response.status_code

    return  response.content.decode('utf-8'), response_status


if __name__ == '__main__':
    print(request_post())
