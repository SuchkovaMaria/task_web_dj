import requests

def request_post():

    url = 'http://localhost:8080'

    data = {"тест запроса do_POST":1}

    response = requests.post(url, data=data)
    response_status = response.status_code

    return response.text, response_status


if __name__ == '__main__':
    print(request_post())
