# DeepSeek - Narzędzie do streszczania stron internetowych

## Opis
DeepSeek to narzędzie wiersza poleceń do automatycznego streszczania zawartości stron internetowych. Wykorzystuje model DeepSeek-1 (8B) do analizy treści stron i generowania zwięzłych streszczeń w języku polskim.

## Funkcjonalność
- Automatyczne wykrywanie głównej treści artykułu na stronie internetowej
- Usuwanie elementów niepotrzebnych (menu, stopki, bannery itd.)
- Generowanie zwięzłych streszczeń (3-5 zdań) w języku polskim
- Obsługa zawartości w różnych językach (automatyczne tłumaczenie do polskiego)

## Wymagania
- Python 3.6+
- Biblioteki:
  - ollama
  - requests
  - beautifulsoup4 (bs4)
  - re

## Instalacja
```bash
git clone https://github.com/lowcyai/DeepSeek.git
cd DeepSeek
pip install -r requirements.txt
```

## Użycie
```bash
python main.py <adres_strony>
```

### Przykład
```bash
python main.py https://example.com/article
```

## Jak to działa
1. Program pobiera stronę internetową z podanego URL
2. Analizuje strukturę HTML, próbując znaleźć główną treść artykułu
3. Usuwa niepotrzebne elementy (menu, stopki, skrypty itp.)
4. Wysyła treść do modelu DeepSeek-1 (8B) z odpowiednim promptem
5. Wyświetla wygenerowane streszczenie

## Projekt dla [lowcyai.pl](https://lowcyai.pl)
Narzędzie stanowi część projektów opisywanych na blogu lowcyai.pl, poświęconym sztucznej inteligencji i jej praktycznym zastosowaniom.

## Licencja
MIT
