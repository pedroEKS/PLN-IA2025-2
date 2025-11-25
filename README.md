# Prática de Processamento de Linguagem Natural (PLN)

Este repositório contém um exercício prático de NLP (Natural Language Processing) desenvolvido para a disciplina de Inteligência Artificial da UniBH visando fixar conceitos fundamentais de manipulação de texto com Python

O projeto implementa um pipeline que recebe um texto bruto (um trecho de Dom Casmurro) e o transforma em dados estruturados prontos para análise

## Funcionalidades

O script app.py executa 5 passos essenciais no processamento de dados textuais:

Tokenização: Segmenta o texto em palavras individuais (tokens)

Normalização: Converte o texto para minúsculas e remove pontuação (vírgulas, pontos, aspas) para padronização

Stop Words: Remove palavras irrelevantes para análise semântica (artigos, preposições, conjunções)

N-Gramas: Agrupa palavras adjacentes para capturar contexto (Bigramas e Trigramas)

Lematização: Transforma palavras flexionadas (verbos conjugados, plurais) em sua forma base ou raiz

## Tecnologias Utilizadas

Python 3

NLTK: Utilizado para tarefas estatísticas, remoção de stop words e geração de n-gramas

Spacy: Utilizado com o modelo em português (pt_core_news_sm) para a lematização baseada em regras gramaticais

## Instalação e Execução

Para executar o projeto, siga os passos abaixo:

1) Preparação do Ambiente

Recomenda-se o uso de um ambiente virtual:

Windows:
```
python -m venv venv
venv\Scripts\activate
```

Linux/Mac:
```
python3 -m venv venv
source venv/bin/activate
```

2) Instalação de Dependências

Instale as bibliotecas necessárias:
```
pip install nltk spacy
```

Baixe o modelo de língua portuguesa do Spacy:
```
python -m spacy download pt_core_news_sm
```

3) Execução

Execute o script principal:
```
python app.py
```

## Exemplo de Saída

Abaixo está o resultado da execução do script no terminal:
```
Verificando dependências...........
Todas as dependências estão ok!!!

TEXTO ORIGINAL
Uma noite destas, vindo da cidade para o Engenho Novo, encontrei no trem da Central um rapaz aqui do bairro, que eu conheço de vista e de chapéu.
    Cumprimentou-me, sentou-se ao meu lado, falou da lua e dos ministros, e acabou recitando-me versos. A viagem era curta, e os versos pode ser que não fossem inteiramente maus.
    Sucedeu, porém, que, como eu estava cansado, fechei os olhos três ou quatro vezes; tanto bastou para que ele interrompesse a leitura e metesse os versos no bolso.  
--------------------------------------------------

1. TOKENIZAÇÃO E NORMALIZAÇÃO
Total de tokens brutos: 88
Primeiros 15 tokens: ['uma', 'noite', 'destas', 'vindo', 'da', 'cidade', 'para', 'o', 'engenho', 'novo', 'encontrei', 'no', 'trem', 'da', 'central']

2. REMOÇÃO DE STOP WORDS
Total após limpeza: 45
Exemplo sem stop words: ['noite', 'destas', 'vindo', 'cidade', 'engenho', 'novo', 'encontrei', 'trem', 'central', 'rapaz', 'aqui', 'bairro', 'conheço', 'vista', 'chapéu']

3. N-GRAMAS (Contexto)
Exemplo de Bigramas: [('noite', 'destas'), ('destas', 'vindo'), ('vindo', 'cidade'), ('cidade', 'engenho'), ('engenho', 'novo')]
Exemplo de Trigramas: [('noite', 'destas', 'vindo'), ('destas', 'vindo', 'cidade'), ('vindo', 'cidade', 'engenho'), ('cidade', 'engenho', 'novo'), ('engenho', 'novo', 'encontrei')]

4. LEMATIZAÇÃO (Raiz das palavras)
Resultado final: ['noite', 'de este', 'vir', 'cidade', 'engenho', 'novo', 'encontrar', 'tr', 'central', 'rapaz', 'aqui', 'bairro', 'conheço', 'vista', 'chapéu', 'cumprimentar', 'sentar', 'lado', 'falar', 'lua', 'ministros', 'acabar', 'recitar', 'verso', 'viagem', 'curto', 'verso', 'poder', 'inteiramente', 'mau', 'suceder', 'porém', 'cansado', 'fechei', 'olho', 'três', 'quatro', 'vez', 'tanto', 'bastar', 'interrompesse', 'leitura', 'meter', 'verso', 'bolso']

Processamento concluído com sucesso!
```
