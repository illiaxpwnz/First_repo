import streamlit as st
from streamlit.components.v1 import html

# Function to display a "Copy to Clipboard" button and script
def copy_to_clipboard_button(text_to_copy):
    # HTML + JS code to create a button and copy text to clipboard
    button_uuid = "copy_button_" + text_to_copy
    button_html = f"""
        <button onclick='navigator.clipboard.writeText("{text_to_copy}")' id='{button_uuid}'>
            Copy to Clipboard
        </button>
        <script>
            document.querySelector("#{button_uuid}").onclick = function() {{
                navigator.clipboard.writeText("{text_to_copy}").then(() => {{
                    // Optional: Change the button text on click to indicate success
                    document.getElementById('{button_uuid}').innerText = 'Copied!';
                }});
            }};
        </script>
    """
    html(button_html)

# Your main application code
st.title("Percentage Calculator")

# Entry widget for user input
base_value = st.number_input("Ціна:", min_value=0.0, format="%f")

# Placeholder for displaying results and the copy button
result_placeholder = st.empty()

# Action buttons and display result
if st.button("15%"):
    result = calculate_increase(base_value, 0.15)
    result_text = f"Результат: {result}"
    result_placeholder.write(result_text)
    copy_to_clipboard_button(result_text)

if st.button("20%"):
    result = calculate_increase(base_value, 0.20)
    result_text = f"Результат: {result}"
    result_placeholder.write(result_text)
    copy_to_clipboard_button(result_text)

if st.button("25%"):
    result = calculate_increase(base_value, 0.25)
    result_text = f"Результат: {result}"
    result_placeholder.write(result_text)
    copy_to_clipboard_button(result_text)
