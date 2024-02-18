import streamlit as st

# Function to calculate the increase
def calculate_increase(base_value, percent):
    result = base_value + (base_value * percent)
    return int(result)  # Convert to integer for simplicity

# Streamlit UI setup
st.title("Percentage Calculator")

# Entry widget for user input
base_value = st.number_input("Ціна:", min_value=0.0, format="%f")

# Action buttons and display result
if st.button("15%"):
    result = calculate_increase(base_value, 0.15)
    st.write(f"Результат: {result}")

if st.button("20%"):
    result = calculate_increase(base_value, 0.20)
    st.write(f"Результат: {result}")

if st.button("25%"):
    result = calculate_increase(base_value, 0.25)
    st.write(f"Результат: {result}")

# Copy to clipboard is not directly supported in Streamlit as it is in desktop applications.
# However, you can allow users to manually copy the result or use JavaScript integrations to facilitate this.
