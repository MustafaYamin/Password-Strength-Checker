import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker" , page_icon="🔐")

st.title("🔐 Password Strength Checker")
st.markdown("### Check how safe your online presence is")
st.write(""" ***
***1. Enter password,***

***2. Check strength,***

***3. Get suggestions.***
*** """)

password = st.text_input("Enter your password" , type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least of 8 characters!") 
    
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]' , password):
        score += 1
    else:
        feedback.append("❌ Password should contain both upper and lower case characters!")

    if re.search(r'\d' , password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least 1 numaric character!")
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 2
    else:
        feedback.append("❌ Password should contain atleast 1 special character from these ( [!@#$%^&*(),.?':}{|<>] )!")
    
    if score == 5 | 4:
        feedback.append("✅ The password is strong.")
    elif score == 3:
        feedback.append("🟡 The password strength is medium. It is suggested to make it stronger.")
    elif score < 3:
        feedback.append("🔴 The password is weak!")

    if feedback:
        st.markdown("### Suggestions: ")
        for tip in feedback:
            st.write(tip)

else:
    st.info("Please enter your password to get started.")