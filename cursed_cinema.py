# Libraries
import streamlit as st

# -------------------------------
# Title & Introduction
# -------------------------------
st.title('🕯️ 𝐓𝐡𝐞 𝐍𝐢𝐠𝐡𝐭 𝐎𝐟 𝐓𝐡𝐞 𝐂𝐮𝐫𝐬𝐞𝐝 𝐂𝐢𝐧𝐞𝐦𝐚 🎬')

st.sidebar.header('🎃 Welcome, Adventurer')
st.sidebar.write('You stand before the forsaken cinema — the mist thickens, the whispers grow louder...')
st.sidebar.write('To enter, you must decode the cryptic message on the door and enter the correct code.')

st.write("""
In the spirit of Halloween, you find yourself wandering through a forsaken town, its streets cloaked in mist and silence.  
As you turn a corner, an abandoned cinema hall looms before you — its faded marquee flickering with the words:

> “Show in Progress.”

Your curiosity whispers louder than your fear. You step inside.

The seats are empty, the air thick with dust… yet you can feel that you’re not alone.

💀 **Your goal:** Survive the night within the cursed cinema.  
Complete chilling challenges, earn points, and uncover the dark secrets hidden behind the screen.  
But beware... every choice you make brings you closer to the truth — or the curse itself.
""")

st.divider()

# -------------------------------
# Section 1: The Challenge
# -------------------------------
st.subheader('🎬 Decrypt the entrance code: Enter If You Dare')

st.write("""
The adventurers can't enter the movie theater without entering the **door code**.  
You can see a **cryptic message** carved next to the rusty padlock...
""")

st.markdown("""
> ### **Cryptic message next to padlock:**
> ꊰꀨꊰ + ꀷꊿ _ ꃔꊿꋖ _ ꑀꃔꋖꑀꌅ + ꋻꎨꌓ
""")

st.write("Can you decode this and reveal the door code?")

# -------------------------------
# Section 2: Enter Name and Code
# -------------------------------
st.subheader('🔑 Enter Your Details')

player_name = st.text_input('Enter your Discord username:')
door_code = st.text_input('Enter the  door code you discovered:', type='password', max_chars=6)

# Set the correct code (you can modify this)
CORRECT_CODE = "727645"

# -------------------------------
# Section 3: Validation
# -------------------------------
if st.button('Submit Answer'):
    if not player_name:
        st.warning("Please enter your name before submitting!")
    elif door_code == CORRECT_CODE:
        # Custom spooky message when the code is correct
        st.success(f"[SYSTEM ERROR] Code submitted... code accepted... access denied.")
        st.markdown("""
        ---
        “**Get out now…**”
        
        But something pulls you back.  
        You ignore the warning and step forward.
        
        🎟️ **Koro Sensei awaits at the counter — re-redacte-redacted.**
        
        Good luck feller! 💀
        ---
        """)
    else:
        st.error("❌ The symbols shift... The code is incorrect. Try again before the spirits awaken!")

