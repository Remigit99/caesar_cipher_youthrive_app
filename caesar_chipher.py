import streamlit as st


#CSS(Cascading Style Sheet)
with open("style.css") as styles:
    st.markdown(f"<style> {styles.read()} </style>", unsafe_allow_html=True) 


# Function to perform Caesar Cipher encryption and decryption
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    shift = shift if mode == 'encrypt' else -shift
    
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result

# Streamlit app
st.title("Caesar Cipher Encryption App")

# Input text
text = st.text_area("Enter the text to be encrypted or decrypted", "")

# Shift value
shift = st.number_input("Enter the shift value", min_value=1, max_value=25, value="min")

# Mode selection
mode = st.radio("Select mode", ('Encrypt', 'Decrypt'))

# Perform encryption or decryption based on the selected mode
if st.button("Submit"):
    if text:  # Check if the text is not empty
        if mode == 'Encrypt':
            result = caesar_cipher(text, shift, mode='encrypt')
            st.write("Encrypted Text:", result)
        else:
            result = caesar_cipher(text, shift, mode='decrypt')
            st.write("Decrypted Text:", result)
    else:
        st.write("Please enter text to be encrypted or decrypted.")


