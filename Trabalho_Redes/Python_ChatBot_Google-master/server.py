import http.server
import socketserver
from google_search import chatbot_query


#Definindo Porta #########################Importante nao alterar dando erro
PORT = 8080
DIRECTORY = 'public'
##########################################################################

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


    #Classe para diparar mensagem no console referente ao servidor
    def do_POST(self):
        self.send_response(200)
        content_length = int(self.headers['Content-Length'])
        post_info = self.rfile.read(content_length)
        self.end_headers()
        print('Informacao Pesquisada :', post_info)
        Exemplo_chatBot = chatbot_query(post_info)
        self.wfile.write(str.encode(Exemplo_chatBot))


#informar a porta de utilização, falta colocar pra iniciar no index junto com servidor ... (FELIPE)
with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print('Utilizando a porta :', PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
