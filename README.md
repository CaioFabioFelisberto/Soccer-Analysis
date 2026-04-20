# ⚽ Football Data Scouting Dashboard

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)

Este projeto é um painel de **Data Scouting** interativo que transforma dados brutos das Top 5 Ligas Europeias em inteligência tática. Utilizando Python e Flask, a aplicação processa estatísticas avançadas para identificar perfis de jogadores, talentos promissores e padrões táticos entre as ligas.

## 🚀 Funcionalidades (Módulos Analíticos)

O dashboard está dividido em 6 desafios técnicos de ciência de dados aplicados ao futebol:

1.  **🧬 DNA dos Criadores:** Gráfico de dispersão comparando Passes Progressivos vs. Conduções, identificando maestros e infiltradores.
2.  **🎯 Raio-X da Artilharia:** Análise de eficiência isolando gols de bola rolando de penalidades.
3.  **💎 Wonderkid Scouting:** Filtro de eficiência (métricas por 90 min) focado em jogadores Sub-21.
4.  **🕸️ Comparador de Radar:** Ferramenta visual polar para sobreposição de perfis de dois jogadores distintos.
5.  **⚖️ Realidade do xG:** Comparação entre Gols Reais e Gols Esperados (xG) para medir a frieza na finalização.
6.  **📊 DNA das Ligas:** Distribuição estatística (Boxplots) das ligas para identificar estilos de jogo e *outliers* geracionais.

## 🛠️ Tecnologias Utilizadas

-   **Python:** Linguagem base para processamento de dados.
-   **Pandas:** Manipulação de DataFrames, limpeza e normalização (métricas por 90').
-   **Flask:** Micro-framework web para criação de rotas e servidor.
-   **Plotly Express:** Biblioteca de visualização de dados dinâmica e interativa.
-   **Jinja2:** Engine de templates para integração entre o back-end Python e o front-end HTML.

## 📂 Estrutura do Projeto

```text
├── app.py              # Servidor Flask e gerenciamento de rotas
├── processamento.py    # Lógica de Data Science e geração de gráficos
├── top5-players.csv    # Dataset base (Estatísticas de jogadores)
├── templates/          # Arquivos HTML (UI/UX)
│   ├── index.html      # Página principal
│   ├── scatter.html    # Visualização de DNA
│   ├── radar.html      # Comparador de jogadores
│   └── ...             # Outros templates
└── static/             # (Opcional) Arquivos CSS e imagens

git clone [[https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)](https://github.com/CaioFabioFelisberto/Soccer-Analysis)
pip install flask pandas plotly
python app.py
python app.py
http://127.0.0.1:5000
