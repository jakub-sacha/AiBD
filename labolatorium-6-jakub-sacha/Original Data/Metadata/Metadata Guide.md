# Metadata Guide dla zbioru danych 10_POMORSKIE.csv

## Kolumna 1: ID wiersza.
- typ danych: liczba całkowita - int
- zakres danych: od 0 do 553
- opis: informacja o ID wiersza z danymi 

## Kolumna 2: Dni od zakupu.
- typ danych: liczba całkowita - int
- zakres danych: od 2 do 17 
- opis: czas, który minął od zakupu odkurzacza do wystawienia oceny 

## Kolumna 3: Marka.
- typ danych: ciąg znaków - string 
- zakres danych: ciąg znaków ze zbioru dostępnych w sklepie marek odkurzaczy ('Beko', 'Tefal', 'Electrolux', 'Samsung', 'Dyson').
- opis: nazwa marki zakupionego odkurzacza

## Kolumna 4: Wiek kupujacego.
- typ danych: liczba całkowita - int
- zakres danych: minimum 18
- opis: wiek osoby, która zakupila odkurzacz

## Kolumna 5: płeć kupującego.
- typ danych: znak - string 
- zakres danych: wartość ze zbioru ('K', 'M', 'bd.')
- opis: pleć osoby, która zakupiła odkurzacz 

## Kolumna 6: Ocena.
- typ danych: liczba rzeczywsita - float
- zakres danych: liczba od 0 do 5 
- opis: ocena odkurzacza według osoby, która go zakupiła 