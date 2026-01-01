import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Tanh Activation Function")

st.markdown("### Mathematical Formula")
st.latex(r"f(x) = \tanh(x)")

x = np.linspace(-10, 10, 100)
tanh = np.tanh(x)

st.markdown("### Visualization")
plt.figure()
plt.plot(x, tanh)
plt.xlabel("Input")
plt.ylabel("Output")
plt.title("Tanh Function")

st.pyplot(plt)
