import streamlit as st

def main():
    st.title("Welcome to My Streamlit App")
    st.write("This is a simple Streamlit application.")

    if st.button("Click Me"):
        st.write("Button clicked!")

    user_input = st.text_input("Enter some text:")
    if user_input:
        st.write(f"You entered: {user_input}")
    st.sidebar.title("Sidebar")
    st.sidebar.write("This is a sidebar.")
    st.sidebar.button("Sidebar Button")
    st.sidebar.text_input("Sidebar Input", "Type here...")

if __name__ == "__main__":
    main()