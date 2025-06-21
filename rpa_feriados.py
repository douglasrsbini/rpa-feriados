import requests
from bs4 import BeautifulSoup
import json
import time

#Lista de municípios e UF para serem captados
municipios = [
    {"uf":"MT","municipio":"primavera_do_leste"},
    {"uf":"MT","municipio":"campo_verde"},
    {"uf":"MT","municipio":"jaciara"},
    {"uf":"MT","municipio":"canarana"},
    {"uf":"MT","municipio":"paranatinga"},
    {"uf":"MT","municipio":"dom_aquino"},
    {"uf":"MT","municipio":"poxoreu"},
    {"uf":"MT","municipio":"jardim_paraiso"},
    {"uf":"MT","municipio":"bom_jesus_do_araguaia"},
    {"uf":"MT","municipio":"gaucha_do_norte"},
    {"uf":"MT","municipio":"juscimeira"},
    {"uf":"MT","municipio":"nova_brasilandia"},
    {"uf":"PA","municipio":"dom_eliseu"},
    {"uf":"PA","municipio":"rondon_do_para"},
    {"uf":"PA","municipio":"ulianopolis"},
    {"uf":"PA","municipio":"mae_do_rio"},
    {"uf":"PA","municipio":"sao_miguel"},
    {"uf":"PA","municipio":"belem"},
    {"uf":"PA","municipio":"ananindeua"},
    {"uf":"PA","municipio":"abaetetuba"},
    {"uf":"PA","municipio":"barcarena"},
    {"uf":"PA","municipio":"marituba"},
    {"uf":"PA","municipio":"santa_isabel"},
    {"uf":"PA","municipio":"capanema"},
    {"uf":"PA","municipio":"braganca"},
    {"uf":"PA","municipio":"paragominas"},
    {"uf":"MT","municipio":"santo_antonio_do_leste"},
    {"uf":"PA","municipio":"maraba"},
    {"uf":"PA","municipio":"tailandia"},
    {"uf":"PA","municipio":"tome-acu"},
    {"uf":"PA","municipio":"canaa_dos_carajas"},
    {"uf":"PA","municipio":"parauapebas"},
    {"uf":"PA","municipio":"tucurui"}
]

ano = 2025  # Ano de referência

todos_feriados = []  # Armazena todos os feriados coletados

def coletar_feriados(municipio, uf, ano):
    url = f"https://www.feriados.com.br/feriados-{municipio.lower()}-{uf.lower()}.php?ano={ano}"
    print(f"Coletando: {municipio}/{uf} - {ano}")

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
    except Exception as e:
        print(f"Erro ao acessar {url}: {e}")
        return []

    soup = BeautifulSoup(resposta.content, 'html.parser')

    feriados_municipio = []

    #Coleta os feriados Nacionais, Estaduais, Municipais
    divs_feriados = soup.find_all('div', id=True, title=True)

    for div in divs_feriados:
        tipo_html = div.get('title')
        tipo = BeautifulSoup(tipo_html, 'html.parser').text.strip() if tipo_html else "Não identificado"

        span = div.find('span', class_='style_lista_feriados')
        if span:
            conteudo = span.text.strip()
            if ' - ' in conteudo:
                data, descricao = conteudo.split(' - ', 1)
            else:
                data, descricao = "Não identificado", conteudo

            feriado = {
                "data": data,
                "descricao": descricao,
                "tipo": tipo,
                "municipio": municipio.replace("_", " ").title(),
                "uf": uf
            }

            feriados_municipio.append(feriado)

    #Coleta os feriados Facultativos
    spans_facultativos = soup.find_all('span', class_='style_lista_facultativos')

    for span in spans_facultativos:
        conteudo = span.text.strip()
        if ' - ' in conteudo:
            data, descricao = conteudo.split(' - ', 1)
        else:
            data, descricao = "Não identificado", conteudo

        feriado_facultativo = {
            "data": data,
            "descricao": descricao,
            "tipo": "Feriado Facultativo",
            "municipio": municipio.replace("_", " ").title(),
            "uf": uf
        }

        feriados_municipio.append(feriado_facultativo)

    return feriados_municipio


#Laço para percorrer os municípios
for item in municipios:
    municipio = item['municipio']
    uf = item['uf']

    feriados = coletar_feriados(municipio, uf, ano)
    todos_feriados.extend(feriados)

    time.sleep(1)

#Salvar no arquivo JSON
with open(f"feriados_{ano}.json", "w", encoding="utf-8") as arquivo:
    json.dump(todos_feriados, arquivo, ensure_ascii=False, indent=4)

print(f"\nFeriados coletados e salvos em 'feriados_{ano}.json'")
