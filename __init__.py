#!/usr/bin/env python
# coding: utf-8

# In[96]:


from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2
import urllib.request
from flask import Flask, render_template, request, redirect
import os



# In[97]:


app = Flask(__name__)
app.config["img_width"] = 224
app.config["img_height"] = 224


# In[98]:


@app.route("/")
def index():
    return render_template("index.html")


# In[99]:


@app.route("/result")
def result():
    model = load_model('covid2model')
    model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    
    path = "https://corvir.000webhostapp.com/upload/image.jpg"
    req = urllib.request.urlopen(path)
    img = image.load_img(req, target_size=(app.config["img_width"], app.config["img_height"]))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])

    classes = model.predict(images/255, batch_size=10)

    if np.argmax(classes, axis=1) == 0:
        out = "Positive"
        acc = str(round(classes[0][0] * 100))
    else:
        out = "Negative"
        acc = str(round(classes[0][1] * 100))
    
    return render_template("result.html", out = out, acc = acc)


# In[100]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:




