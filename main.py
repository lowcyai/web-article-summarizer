import ollama
import requests
import bs4
import sys
import re

def process_website(website):
    response = ""
    try:
        # Sprawdzenie, czy adres URL zaczyna się od http:// lub https://
        if not website.startswith(('http://', 'https://')):
            print(
                "Niepoprawny adres URL. Proszę podać adres zaczynający się od http:// lub https://")
            return
        # Pobranie treści strony
        response = requests.get(website)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Błąd podczas pobierania strony: {e}")
        return
    content = bs4.BeautifulSoup(response.text, features="html.parser")
    
    # Próba znalezienia głównej treści - typowe selektory dla treści artykułów
    main_content = None
    
    # Sprawdzanie typowych selektorów dla treści artykułów
    selectors = [
        'article', 'main', '.content', '.post-content', '.article-content', 
        '.entry-content', '#content', '#main-content', '.main-content'
    ]
    
    for selector in selectors:
        elements = content.select(selector)
        if elements:
            main_content = elements[0]
            break
    
    # Jeśli nie znaleziono treści przez selektory, używamy body jako fallback
    if not main_content:
        main_content = content.find('body')
        
    # Usuwanie typowych elementów niepotrzebnych
    for elem in main_content.select('nav, footer, header, .menu, .footer, .sidebar, .widget, script, style, .comments'):
        if elem:
            elem.extract()
    
    text_content = str(main_content)

    prompt = f"""
    Jako specjalista od analizy treści, masz jedno zadanie: streszczenie treści artykułu/tekstu ze strony internetowej.
    
    WAŻNE INSTRUKCJE:
    1. IGNORUJ wszelkie elementy niebędące treścią: menu, przyciski, bannery, reklamy, stopki, nagłówki, komentarze.
    2. ZIDENTYFIKUJ główny artykuł lub tekst na stronie i TYLKO na nim się skup.
    3. Jeśli zawartość jest w języku obcym, najpierw przetłumacz główny tekst na polski.
    4. Przygotuj ZWIĘZŁE, 3-5 zdaniowe streszczenie TYLKO głównej treści artykułu/strony.
    5. NIE opisuj struktury strony, elementów HTML, ani wyglądu witryny.
    6. NIE wymieniaj autorów, dat, kategorii czy innych metadanych, chyba że są kluczowe dla zrozumienia treści.
    
    Poniżej znajduje się HTML strony internetowej. Znajdź w nim główną treść i ją streszczaj:
    
    {text_content}
    
    STRESZCZENIE TREŚCI PO POLSKU:
    """


    chat_response = ollama.chat(
        model='deepseek-r1:8b',
        messages=[{
            'role': 'user',
            'content': prompt
        }]
    )
    returned_response = chat_response['message']['content']
    cleaned_response = re.sub(r'<think>.*?</think>', '', returned_response, flags=re.DOTALL).strip()

    print(cleaned_response)

    ##Poniżej zaimplementuj dalszą logikę, jeśli chcesz zapisać odpowiedź do pliku lub wykonać inne operacje.

  


def main():
    if len(sys.argv) != 2:
        print("Użycie: python main.py <adres_strony> ")
        sys.exit(1)

    input_website = sys.argv[1]
    process_website(input_website)


if __name__ == "__main__":
    main()
