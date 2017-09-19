
# coding: utf-8

# In[7]:


from PIL import Image, ImageDraw, ImageFont


# In[30]:


def meme(filename,fulltext,textsize=32,color=(0,0,0,255)): 
    image = Image.open('./img/'+filename+'.jpg')
    width, height = image.size
    draw = ImageDraw.Draw(image)
    text = fulltext
    font = ImageFont.truetype('./font/msjh.ttc', textsize)
    textwidth, textheight = draw.textsize(text, font)
    margin = 5
    x = (width - textwidth - margin)/2
    y = height - textheight - margin
    draw.text((x, y), text, font=font, fill=color)
    return image


# In[33]:


#meme("64","我佛你!!",color=(255,255,255,255))

