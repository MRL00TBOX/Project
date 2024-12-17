import streamlit as st
import nbformat
from nbconvert import PythonExporter

# Заголовок приложения
st.title("Загрузка Jupyter Notebook")

# Загрузка файла
uploaded_file = st.file_uploader("Project_main.ipynb", type=["ipynb"])

if uploaded_file is not None:
    # Чтение содержимого загрузки
    notebook_content = uploaded_file.read()

    # Преобразование .ipynb в Python код
    notebook = nbformat.reads(notebook_content.decode("utf-8"), as_version=4)
    exporter = PythonExporter()
    python_code, _ = exporter.from_notebook_node(notebook)

    # Отображение кода
    st.subheader("Содержимое вашего Notebook:")
    st.code(python_code, language='python')

    # Выполнение кода (не рекомендуется без проверки)
    try:
        exec(python_code)
    except Exception as e:
        st.error("Ошибка при выполнении кода.")
        st.error(e)
