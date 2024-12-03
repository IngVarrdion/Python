import pandas as pd
#Zad. 1
print("Zadanie I")
print(pd.read_csv("demografia.csv",decimal=",",na_values=['NA', 'n/a', 'NaN']))
#Zad. 2
print("Zadanie II")
plik = 'demografia.csv'
dane = pd.read_csv(
    plik,
    decimal=',',
    na_values=['NA', 'n/a', 'NaN']
)
indeks_max = dane['2022'].idxmax(skipna=True)
kraj = dane.loc[indeks_max, 'KRAJE']
print(f"Zadanie II\nNajwiększy przyrost ludności w 2022 roku odnotowano w kraju: {kraj}.\nZadanie III")
#Zad. 3
print("Zadanie III")
plik = "demografia.csv"
dane = pd.read_csv(plik, decimal=",", na_values=["NA", "n/a", "NaN"])
dane_bezkraju = dane.drop(columns=["KRAJE"])
max_przyrost = dane_bezkraju.max().max()
rok_max_przyrost = dane_bezkraju.max().idxmax()
index_max_przyrost = dane_bezkraju[rok_max_przyrost].idxmax()
kraj_zmax_przyrostem = dane.loc[index_max_przyrost, "KRAJE"]
print("Największy przyrost ludności występuje w kraju:", kraj_zmax_przyrostem, "i wyniósł:", max_przyrost, "w roku", rok_max_przyrost,"\nZadanie IV")
#Zad. 4
print("Zadanie IV")
data = {
    'ID': [1, 2, 3, 4, 5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Stanowisko': ['Manager', 'Programista', 'Konsultant', 'Programista', 'Manager'],
    'Wiek': [35, 28, 40, 30, 45],
    'Pensja': [8000, 4500, 6000, 5500, 7000]
}
df = pd.DataFrame(data)
high_salary = df[df['Pensja'] > 5000]
print("Pracownicy z pensją większą niż 5000 PLN:")
print(high_salary)
sorted_by_age = df.sort_values(by='Wiek')
print("\nPracownicy posortowani według wieku:")
print(sorted_by_age)
grouped_by_position = df.groupby('Stanowisko')['Pensja'].mean()
print("\nŚrednia pensja według stanowiska:")
print(grouped_by_position)
promotion_data = {
    'ID': [2, 4],
    'Nowe Stanowisko': ['Senior Programista', 'Senior Programista']
}
promotion_df = pd.DataFrame(promotion_data)
merged_df = pd.merge(df, promotion_df, on='ID', how='left')
print("\nTabela z nowymi stanowiskami:")
print(merged_df)
output_file = 'pracownicy.csv'
merged_df.to_csv(output_file, index=False)
print(f"\nDane zapisane do pliku {output_file}")
loaded_df = pd.read_csv(output_file)
print("\nWczytane dane z pliku CSV:")
print(loaded_df)
#Zad. 5
print("Zadanie V")
data = {
    'Nr_albumu': [1, 2, 3, 4, 5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Ocena': [4.5, 3.0, 5.0, 4.0, 2.5],
    'Wiek': [22, 21, 24, 23, 25]
}
df = pd.DataFrame(data)
high_scores = df[df['Ocena'] > 4]
print("Studenci z oceną większą niż 4:")
print(high_scores)
sorted_by_age = df.sort_values(by='Wiek')
print("\nStudenci posortowani według wieku:")
print(sorted_by_age)
grouped_by_score = df.groupby('Ocena')['Wiek'].mean()
print("\nŚredni wiek według ocen:")
print(grouped_by_score)
retake_data = {
    'Nr_albumu': [2, 5],
    'Poprawiona Ocena': [3.5, 3.0]
}
retake_df = pd.DataFrame(retake_data)
merged_df = pd.merge(df, retake_df, on='Nr_albumu', how='left')
print("\nTabela z protokołem ocen po poprawie:")
print(merged_df)
output_file = 'studenci.csv'
merged_df.to_csv(output_file, index=False)
print(f"\nDane zapisane do pliku {output_file}")
loaded_df = pd.read_csv(output_file)
print("\nWczytane dane z pliku CSV:")
print(loaded_df)
new_student = {'Nr_albumu': 6, 'Imię': 'Ewa', 'Nazwisko': 'Kamińska', 'Ocena': 4.0, 'Wiek': 22}
df = pd.concat([df, pd.DataFrame([new_student])], ignore_index=True)
print("\nTabela z dodanym studentem:")
print(df)
unique_scores = df['Ocena'].unique()
print("\nUnikalne wartości w kolumnie 'Ocena':")
print(unique_scores)
count_score_5 = df[df['Ocena'] == 5].shape[0]
print(f"\nLiczba studentów z oceną równą 5: {count_score_5}")