from flask import Flask,render_template, json,request,url_for
from werkzeug.utils import redirect


app = Flask(__name__)

def arquivoNaoExiste(): 
        try:
            arquivoTxt = open("arquivoListaArray.txt")
            arquivoTxt.close()
            print('arquivo existe')
            return False
        except:
            print('Arquivo nao existe')
            return True
def criaArquivo():
    arquivoTxt = open("arquivoListaArray.txt","w")
    arquivoTxt.write('[]')
    arquivoTxt.close()

@app.route("/" ,methods=["POST","GET"])
def index():
    if(arquivoNaoExiste()):
        criaArquivo()
    else:
        try:

            arquivoTxt = open('arquivoListaArray.txt','r')
            
        except:
            print('bbbbbbbbbbbbbbbbbbbbbb')
            criaArquivo()
            arquivoTxt = open('arquivoListaArray.txt','r')
            listaTxt = json.loads(arquivoTxt.read())
            arquivoTxt.close()

        listaTxt = json.loads(arquivoTxt.read())
        lista_array = listaTxt
        lista_array = json.dumps(lista_array)  
        return render_template("tabela_main.html", lista_array = lista_array)

    arquivoTxt = open('arquivoListaArray.txt','r')
    listaTxt = json.loads(arquivoTxt.read())
    return render_template("tabela_main.html", lista_array = listaTxt)
    
@app.route("/tabela", methods= ["POST","GET"])
def tabelaLibelula():
    if(request.method == "POST"):
        
        arquivoTxt = open('arquivoListaArray.txt',"w")
        listaInput = request.form.get('lista_array')
        arquivoTxt.write(f"{listaInput}")
    return redirect(url_for('index'))

app.run(debug=True)
