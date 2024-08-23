# Plano da disciplina

- Etapa 1: estudo de tecnologias que podem ser usadas para montar projeto;
- Etapa 2: criar o protótipo com as tecnologias;
- Etapa 3: testar e apresentar protótipo;

# O que são LLM's?

- Modelos de IA que entendem linguagem humana/ natural;
  - Materiais diversos: texto, áudio, vídeo;
- Priemiros modelos baseados em Transformes (Optimus Prime?);
- GPT = Generative Pretrained Transformer;
  - Gemini, FPT, são construidos sobre arquitetura transformer;
  - Introduzi por Vaswani et al.;
  - Revolucionou legal o campo de NLP (Natural Language Processing);
- Generataive models (modelos que nentedem e geram textos);
  - Analisam chunks/ tokens de dados e aprendem a prever os proximos 
    tokens em sequencias, baseados nos tokens previos;
- Recursos: para treinar você precisa de processamento;
  - Fine tuning = você ajusta modelo pre treinado da IA para você;
    - Para uma finalidade: para programar, reconhecer imagens...;
  - Tokenização: dividr texto em unidades menores, como palavras 
    ou subpalavras, chamadas tokens, que sao usados como entrada;
  - RAG: tipo gerar textos para treinamento a partir de uma base de
    dados como pdf e tals;
  - Embedding: representação de palavras ou farses em um espaço
    vetorial onde palavras com significados semelhantes estão mais
    proximas umas das outras;
  - Zero-shot: mandar uma pergunta sem conhecimento previo do gpt;
- Termos comuns:
  - Prompt: passar prompts que mostrma perguntas comuns e respostas 
    para um determinado prompt;
  - Alucinação: fenomeno onde LLM gera info incorretas ou irrelevantes;
  - Sentiment Analysis: aplicação onde LLMS classficiam textos como 
    positivos negativos ou neutros ajudano empresas a compreender
    emoções dos clientes;
- Modelos:
  - Generalistas: modelos LLMS de grande porte treinados em vastas
    quantidades de dados textusias de codigo permitindo que gerem texto,
    traduzam, etc;
  - Especialistas: focados em certa linguagem de programação, etc;
- Mais informações:
  - Reinforcement Learning from Human Feedback (RLHF):
    - Aprendizado por reforço para gerar respostas mais humanas;

## Trabalhando com a APIs

- gpt4-mini: https://platform.openai.com/playground/chat?models=gpt-4o-mini
- groq: https://groq.com/

## Setup

- criar ambiente: `python3 -m venv .meuAmbienteVirtualRisosRisos`
- ativar ambiente: `.\.venv\Scripts\activate`
- `pip install groq`
- definir e exportar variavel (use o CMD)
  - set GROQ_API_KEY=suachave (NAO USE ASPAS AO REDOR DO VALOR)
  - echo %GROQ_API_KEY%
- só usar