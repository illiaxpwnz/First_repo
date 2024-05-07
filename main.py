import streamlit as st
from streamlit.components.v1 import html

# Function to calculate the increase
def calculate_increase(base_value, percent):
    result = base_value + (base_value * percent)
    return int(result)  # Ensuring result is an integer

# Function to display a "Copy to Clipboard" button for integers
def copy_to_clipboard_button(int_value):
    # Ensuring the value to copy is treated as an integer and converted to string for JS
    text_to_copy = str(int_value)
    button_uuid = f"copy_button_{text_to_copy}"
    button_html = f"""
        <button id='{button_uuid}'>Скопіювати {text_to_copy} </button>
        <script>
        document.querySelector("#{button_uuid}").onclick = function() {{
            navigator.clipboard.writeText("{text_to_copy}").then(() => {{
                document.getElementById('{button_uuid}').innerText = 'Скопійовано!';
            }});
        }};
        </script>
    """
    html(button_html)

st.title("Калькулятор націнки")

base_value = st.number_input("Ціна:", min_value=0.0, format="%f")
result_placeholder = st.empty()

if st.button("15%"):
    result = calculate_increase(base_value, 0.15)
    result_placeholder.write(f"Результат: {result}")
    copy_to_clipboard_button(result)

if st.button("20%"):
    result = calculate_increase(base_value, 0.20)
    result_placeholder.write(f"Результат: {result}")
    copy_to_clipboard_button(result)

if st.button("25%"):
    result = calculate_increase(base_value, 0.25)
    result_placeholder.write(f"Результат: {result}")
    copy_to_clipboard_button(result)

# Adding the 35% button
if st.button("35%"):
    result = calculate_increase(base_value, 0.35)
    result_placeholder.write(f"Результат: {result}")
    copy_to_clipboard_button(result)
