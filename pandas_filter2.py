import pandas as pd

# Читаем Excel-файл
file_path = 'credit_portfile.xlsx'
df = pd.read_excel(file_path)
print(df.columns)
# Основные ключевые слова для поиска
keywords = ['ИП', 'индивидуальный предприниматель', 'самозанят', 'индивид']
product_keyword = 'Старт'

# Дополнительное условие (например, должно содержаться слово 'юрлицо')
additional_condition = 'предпри'
product_column = 'Вид кредита'
product_table = 'Старт'
# Название столбца с признаком
column_name = 'Должность заемщика'

# Фильтруем строки без учёта регистра
filtered_df = df[
    (df[product_column].astype(str).str.contains(product_table, case=False, regex=True, na=False)) |
    (
          df[column_name].astype(str).apply(
              lambda cell: any(kw.lower() in cell.lower() for kw in keywords)
          )
      )
]
# Или можно сохранить результат в новом файле
output_file = 'filtered_subject_types_without_case2.xlsx'
filtered_df.to_excel(output_file, index=False)
print(f"Отфильтрованные строки сохранены в файле {output_file}.")
#####
