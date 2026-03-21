# =========================================================
# 📦 MODULE + PIP DEMO (PYJOKES)
# =========================================================

# Step 0:
# Make sure you installed pyjokes using:
# pip install pyjokes


# ---------------------------------------------------------
# Step 1: Importing the module
# ---------------------------------------------------------
import pyjokes   # external module


# ---------------------------------------------------------
# Step 2: Using functions from module
# ---------------------------------------------------------

# Get a single joke
joke = pyjokes.get_joke()

# Print the joke
print("😂 Random Joke:")
print(joke)


# ---------------------------------------------------------
# Step 3: Using parameters (optional)
# ---------------------------------------------------------

# You can specify category & language
# Categories: 'neutral', 'chuck', 'all'
# Language: 'en'

joke2 = pyjokes.get_joke(language='en', category='neutral')

print("\n😂 Another Joke:")
print(joke2)


# ---------------------------------------------------------
# Step 4: Get multiple jokes
# ---------------------------------------------------------

jokes_list = pyjokes.get_jokes()

print("\n😂 Multiple Jokes:")
for j in jokes_list[:3]:   # print first 3 jokes
    print("-", j)


# ---------------------------------------------------------
# Step 5: What is happening?
# ---------------------------------------------------------

# pyjokes = module (installed using pip)
# get_joke() = function inside module
# pip = tool used to install this module


# =========================================================
# 🎯 END
# =========================================================