import re
import sys
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.util import ngrams

def verificar_dependencias():
    """
    Verifica se os recursos do NLTK e Spacy estão instalados
    Se não estiverem tenta baixar/avisa o usuário
    """
    print("Verificando dependências...........")
    
    # Verifica stopwords do NLTK
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        print("   -> Baixando stopwords do NLTK..........")
        nltk.download('stopwords', quiet=True)
    
    #Tenta carregar o Spacy
    try:
        nlp = spacy.load('pt_core_news_sm')
        return nlp
    except OSError:
        print("   Erro: O modelo de português do Spacy não foi encontrado.")
        print("   Por favor, execute o comando abaixo no terminal antes de rodar o script:")
        print("   python -m spacy download pt_core_news_sm")
        sys.exit(1)

def main():
    #Configuração inicial
    nlp = verificar_dependencias()
    print("Todas as dependências estão ok!!!\n")

    # Escolhi um texto do Machado de Assis para testar pontuação e acentuação
    corpus = """
    Uma noite destas, vindo da cidade para o Engenho Novo, encontrei no trem da Central um rapaz aqui do bairro, que eu conheço de vista e de chapéu. 
    Cumprimentou-me, sentou-se ao meu lado, falou da lua e dos ministros, e acabou recitando-me versos. A viagem era curta, e os versos pode ser que não fossem inteiramente maus. 
    Sucedeu, porém, que, como eu estava cansado, fechei os olhos três ou quatro vezes; tanto bastou para que ele interrompesse a leitura e metesse os versos no bolso.
    """
    
    print("TEXTO ORIGINAL")
    print(corpus.strip())
    print("-" * 50)

    #Tokenização e normalização
    #Convertemos para minúsculas 
    #Isso já elimina vírgulas, pontos finais e aspas
    texto_lower = corpus.lower()
    tokens = re.findall(r'\w+', texto_lower)
    
    print(f"\n1. TOKENIZAÇÃO E NORMALIZAÇÃO")
    print(f"Total de tokens brutos: {len(tokens)}")
    print(f"Primeiros 15 tokens: {tokens[:15]}")

    #Remoção de stop words
    #carrega a lista de palavras "vazias" (artigos, preposições) em português
    stop_words_pt = set(stopwords.words('portuguese'))
    tokens_filtrados = [token for token in tokens if token not in stop_words_pt]
    
    print(f"\n2. REMOÇÃO DE STOP WORDS")
    print(f"Total após limpeza: {len(tokens_filtrados)}")
    print(f"Exemplo sem stop words: {tokens_filtrados[:15]}")

    #Geração dos n-gramas
    #bigramas  e trigramas ajudam a entender contexto 
    bigramas = list(ngrams(tokens_filtrados, 2))
    trigrams = list(ngrams(tokens_filtrados, 3))
    
    print(f"\n3. N-GRAMAS (Contexto)")
    print(f"Exemplo de Bigramas: {bigramas[:5]}")
    print(f"Exemplo de Trigramas: {trigrams[:5]}")

    #Lematização com Spacy
    doc = nlp(" ".join(tokens_filtrados))
    lemas = [token.lemma_ for token in doc]

    print(f"\n4. LEMATIZAÇÃO (Raiz das palavras)")
    print(f"Resultado final: {lemas}")
    
    print("\nProcessamento concluído com sucesso!")

if __name__ == "__main__":
    main()
