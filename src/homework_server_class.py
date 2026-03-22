import os

from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost" # Адрес для доступа по сети
serverPort = 8080 # Порт для доступа по сети

class HWServer(BaseHTTPRequestHandler):
    """Класс обработки запросов"""

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов"""

        self.send_response(200)  # Отправка кода ответа
        self.send_header("Content-type", "text/html")
        self.end_headers()  # Завершение формирования заголовков ответа
        dir = os.getcwd()
        absolute_path = os.path.join(dir, "..")
        os.chdir(absolute_path)
        path_to_direct = os.path.dirname(__file__)
        path_to_file = os.path.join(path_to_direct, "..", "file_html", "contacts.html")
        with open(path_to_file, 'r', encoding='utf-8') as file:
            html_content = file.read()
        self.wfile.write(bytes(html_content.encode('utf-8')))  # Тело ответа


    def do_POST(self):
        """ Метод для обработки входящих POST-запросов"""
        print("do_POST called")
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print(body)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        write = "POST запрос обработан"
        self.wfile.write(bytes(write.encode('utf-8')))


if __name__ == '__main__':

    webServer = HTTPServer((hostName, serverPort), HWServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass


    webServer.server_close()
    print("Server stopped.")

    webServer= HTTPServer((hostName, serverPort), HWServer)
    print("Server is running on port 8080")
    webServer.serve_forever()

