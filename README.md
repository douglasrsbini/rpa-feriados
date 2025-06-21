# RPA - Coleta de Feriados Municipais, Estaduais, Nacionais e Facultativos

Este projeto é um RPA (Robotic Process Automation) desenvolvido em **Python** para capturar informações de feriados (data, descrição e tipo) de municípios brasileiros no site [**feriados.com.br**](https://www.feriados.com.br/) e exportá-las em um arquivo JSON.

## Finalidade

Este projeto foi desenvolvido para atender uma demanda real em uma **cooperativa de crédito**, onde surgiu a necessidade de obter os feriados **municipais, estaduais, nacionais e facultativos** das cidades onde a instituição possui agências. Essas informações são essenciais para um novo sistema de **Business Intelligence (BI)** que está sendo criado, com o objetivo de fornecer esses dados de forma centralizada e estruturada para os departamentos de **endomarketing, departamento pessoal e marketing**.

## Funcionalidades

- Coleta de feriados **Nacionais, Estaduais, Municipais e Facultativos**.
- Exportação organizada dos dados em arquivo **feriados_YYYY.json**.
- Parâmetro configurável de lista de municípios e ano.

## Tecnologias Utilizadas

- **Python 3.12.4**
- **requests** — para realizar requisições HTTP.
- **BeautifulSoup4** — para fazer parsing do HTML.
- **json** — para manipulação e gravação de arquivos JSON.
- **time** — para controle de intervalo entre requisições.

## Instalação e Execução

### Clone o repositório

```bash
git clone https://github.com/douglasrsbini/rpa-feriados.git
cd rpa-feriados
```

### Pré-requisitos

- Python 3.12.4 instalado ou superior.

### Instalação das bibliotecas

```bash
pip install requests beautifulsoup4
```

### Execução

1. Configure a lista de municípios e o ano no script `rpa_feriados.py`.
2. Execute o script:

```bash
python rpa_feriados.py
```

3. Verifique o arquivo `feriados_2025.json` gerado na mesma pasta.

## 📂 Estrutura do Projeto

```bash
📁 rpa-feriados/
├── 📄 rpa_feriados.py
├── 📄 feriados_2025.json
├── 📄 README.md
├── 📄 LICENSE
├── 📄 .gitignore
```

## Como funciona

- Para cada município configurado:
  - Monta a URL de consulta.
  - Faz requisição HTTP.
  - Extrai feriados Nacionais, Estaduais e Municipais de `<div>` com `title`.
  - Extrai feriados Facultativos de `<span>` com classe `style_lista_facultativos`.
  - Organiza as informações e exporta para JSON.

## Exemplos de JSON Gerado

```json
{
  "data": "20/11/2025",
  "descricao": "Consciência Negra",
  "tipo": "Feriado Nacional",
  "municipio": "Primavera Do Leste",
  "uf": "MT"
}
```

## Licença

Este projeto está sob a licença **MIT** — sinta-se livre para usar, modificar e compartilhar.

## Autor

**Douglas Richard Soares Bini**
[LinkedIn](https://www.linkedin.com/in/douglasbini)

## Contato

Caso tenha interesse em colaborar ou conhecer mais projetos meus:

- [LinkedIn Douglas Bini](https://www.linkedin.com/in/douglasbini)

---

Se quiser contribuir ou sugerir melhorias, fique à vontade para abrir um Pull Request ou Issue!
