# ---
# title: Eirik tester quarto
# author: Eirik Gallefoss
# jupyter:
#   jupytext:
#     formats: 'ipynb,py:percent,qmd'
#     text_representation:
#       extension: .qmd
#       format_name: quarto
#       format_version: '1.0'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3.10.6 64-bit
#     language: python
#     name: py310
# format:
#   html:
#     theme: dark
#     code-fold: true
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent,qmd
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3.10.5 ('py310')
#     language: python
#     name: python3
# ---

# %%
#| echo: false
import datetime as dt
from IPython.display import display, Markdown
import plotly.express as px

# %% [markdown]
# ## Kode

# %%
dt.datetime.now()

# %% [markdown]
# ## Plotly

# %% [markdown]
# Markdown funker.

# %%
import numpy as np
import matplotlib.pyplot as plt

x = list(range(10))
y = [x**3 for x in x]
fig = plt.figure()
plt.plot(x,y)
plt.grid(True)
plt.show()

# %%
px.bar([1,2,3,4,5]).show()

# %% [markdown]
# ## Bilder
#
# Her er en figur.
#
# ![Feilmelding](images/programlimit.png)
#
# Og en annen figur.
#
# ![Treig spørring](images/treg_sp%C3%B8rring.png)
