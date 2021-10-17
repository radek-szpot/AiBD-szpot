# Laboratorium 2 

Wykonał: Radosław Szpot
Ćwiczenie mające za zadanie zapozanie się z portokołem TIER i zasadami "tidy data".

1. Zawartość folderów zgodnych z portokołem TIER.
 * Zgodnie z numerem datasetu (5 mod 5) + 1 = 1 zaimportowano dane "weather.txt" z * [link](https://raw.githubusercontent.com/KAIR-ISZ/public_lectures/master/Analiza%20i%20Bazy%20Danych%202021/Lab%202/Datasets/weather.txt) do folderu Oryginal-data. Dane te zawierają dzienne dane pogodowe z Global Historical Climatology Network.
 * Skrypt wykonujący operacje na danych "lab2.ipynb" umieszczono w folderze Command-files.
 * Dokumentacja, w tym przypadku plik readme.md umieszczono w folderze Documents
 * Dodatkowo utworzono folder Analisys-data do przechowania wyczyszczonych danych ze skryptu.
 
2. Modyfikacje wykonane na danych.
 * Skrypt odczytuje dane z pliku z rozszerzeniem .txt i przetwarza je tak, aby można nad nimi operować:
	* Dzieli dane ze względu na spacje.
	* Przetwarza tylko dane z 2010 roku (zgodnie z poleceniem ćwiczenia).
	* Usuwa litere "I".
	* Łączy flagę "S" z odpowiadającą jej daną wartością, po to aby zachować tą informację.
	* Sprawdza czy danych nie ma za mało (musi być odpowiednia ilość danych, ponieważ dane uszkodzone są nadpisywane wartością -9999).
	* Sprawdza czy element 1 nie połączył się z 2 i jeśli tak to rozdziela je zostawiając w odpowiednich miejscach.
	* Zastępuje błędne dane "-9999" wartością np.nan (dzięki temu można potem dokonać operacji .dropna()).
	* Dzieli pierwszy element na: id stacji, rok, miesiąc, nazwę zmiennych.
 * Po tej długiej obróbce danych utworzono pierwszy DataFrame bez żadnych reguł, w celu zapoznania się z danymi całościowo.
 * Niestety od razu widać że danych błędnych jest zdecydowanie więcej i cięzko będzie z nich uzyskać sensowne wnioski. Nie da się też ich odtworzyć.
 * Aby nie powtarzać obserwacji w jenym rzędzie podzielono tabelę tak aby każdy dzień miał dopasowane wszystkie swoje zmienne, w tym oddzielono flagę "S" od wartości.
 * Wygenerowano DataFrame  zawierający powyższą poprawkę i zapisano do pliku "all_data_data_with_nan" w folderze Analisys-data.
 * Następnie usunięto zmienne ID i YEAR, ponieważ odczyt jest ograniczony do tego samego roku i tej samej stacji, tak poprawiony DataFrame zapisano do pliku "data_with_nan" w folderze Analisys-data.
 * Dodatkowo usunięto błędne wartości NaN wykorzystując komendę .dropna() te dane również zapisano w folderze Analisys-data w pliku "data_without_nan"
