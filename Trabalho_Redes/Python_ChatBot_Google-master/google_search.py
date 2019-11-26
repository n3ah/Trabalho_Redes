import requests
import string
from lxml import html
from googlesearch import search
from bs4 import BeautifulSoup


def chatbot_query(query, index=0):
    msgErro = 'Desculpe, não consigo pensar em uma resposta para isso.'
    resultado = ''

    try:

        #instancia query passando parametro de busca
        resultado_pesquisa = list(search(query, tld="co.in", num=10, stop=3, pause=1))

        #vetoriza o retorno
        page = requests.get(resultado_pesquisa[index])

        tree = html.fromstring(page.content)

        #chama o beatiful soup para a leitura da resposta da requisição como o endereço de busca
        soup = BeautifulSoup(page.content, features="lxml")

        #instancia a variavel que recebera o artigo
        article_text = ''
        article = soup.findAll('p')

        #Corre o artigo pelos elementos quebrando as strngs
        for element in article:
            article_text += '\n' + ''.join(element.findAll(text = True))
        article_text = article_text.replace('\n', '')
        first_sentence = article_text.split('.')
        first_sentence = first_sentence[0].split('?')[0]

        chars_without_whitespace = first_sentence.translate(
            { ord(c): None for c in string.whitespace }
        )

        if len(chars_without_whitespace) > 0:
            resultado = first_sentence
        else:
            resultado = msgErro

        return resultado
    except:
        if len(resultado) == 0: resultado = msgErro
        return resultado
