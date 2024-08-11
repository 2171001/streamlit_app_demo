import streamlit as st

from forms.contact import contact_form



@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profile_image.png", width=200)
with col2:
    st.title("Abel Benedict", anchor=False)
    st.write("Aspiring Bug Hunter passionate about Penetration Testing, AI and Cybersecurity.")
    if st.button("Contact Me"):
        show_contact_form()

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - Proficient in Linux, Python and Powershell
    - Solid grasp of security principles and ethics
    - Strong team player with proactive initiative
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming: Python, C
    - Automation: Experience with scripting and automation
    - VAPT: Proficient in Vulnerability Assessment and Penetration Testing
    - Tools: Experience with Wireshark, CAIDO, Metasploit and other security tools.
    """
)