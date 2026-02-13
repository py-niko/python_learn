import pandas as pd

# Чтение файла Excel
df = pd.read_excel('credit_portfile.xlsx')
column = 'Вид кредита'
column1 = '№  договора'
# Создание фильтра: ищем строки, в которых содержится слово "ипотека"
# И также обязательно должно присутствовать слово "рефин", при этом без учета регистра
mask = (
    ((df[column].str.contains('ипотека', case=False)) &
     (df[column].str.contains('рефин', case=False))) |
    (df[column1].str.contains('КПК', case=False))
)

filtered_df = df.loc[mask]

output_file = 'credit_ref_portfile.xlsx'
filtered_df.to_excel(output_file, index=False)
print(f"Отфильтрованные строки сохранены в файле {output_file}.")

