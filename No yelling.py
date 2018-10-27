def filter_words(st):
    st = st.strip(' ')
    st = st.capitalize( )
    st = st.split()
    st = ' '.join(st)
    return st

