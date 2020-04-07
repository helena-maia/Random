import urllib.request as ur
import ssl
import argparse

def baixaEsalva(url, arquivo, context=""):
    url_completa = url+arquivo

    with ur.urlopen(url_completa, context=context) as response:
      #print(response.headers['content-type'])
      conteudo = response.read().decode('utf-8')
 
      with open(arquivo, 'w') as f:
        f.write(conteudo)
        f.close()

parser = argparse.ArgumentParser(description='Programa para baixar arquivos .in e .res do SuSy')
parser.add_argument('-t', default="mc102w", help="Turma (Default: mc102w)")
parser.add_argument('-l', default="01-Entrega", help="Lab (Default: 01-Entrega)")
parser.add_argument('-n', type=int, default=15, help="Numero de testes (Default:15)")
parser.add_argument('-f', default="arq{:02d}.in", help="Formato entrada (Default:arq{:02d}.in)")
args = parser.parse_args()

context = ssl._create_unverified_context()
url = "https://susy.ic.unicamp.br:9999/"+args.t+"/"+args.l+"/dados/"
num_teste = args.n
fmt_entrada = args.f

for i in range(num_teste):
    baixaEsalva(url, fmt_entrada.format(i+1), context)
    baixaEsalva(url, "arq{:02d}.res".format(i+1), context)



