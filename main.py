from flask import Flask
from janome.tokenizer import Tokenizer

my_app = Flask(__name__)

tokenizer = Tokenizer()
word = 'JanomeはPythonの形態素解析エンジン。日本語のテキストを形態素ごとに分割して品詞を判定したり分かち書きしたりすることができる。'

tokens = tokenizer.tokenize(word)

ans = ''

for token in tokens:
    ans +=  f"{str(token.surface)}({token.part_of_speech.split(',')[0]}) "

@my_app.route('/')
def home():
    return f"<p>{ans}</p>"

if __name__ == '__main__':
    my_app.run(debug = True)