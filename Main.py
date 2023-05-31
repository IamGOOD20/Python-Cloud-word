import os
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image


### reading text files and creating a dataframe code started
# creating lists for future data frame creation
title_colom = list()
description_colom = list()

# through the cycle (10 times, 10 vacancies) I will read each headline and job description
for i in range(1, 11):
    # specifying the working directory for job files
    os.chdir('E:\TEST FROM COMPANIES\CIVISION\Test-CIVI\Jobs')
    # open text files
    with open(f'vacancy_{i}.txt', encoding='utf-8') as f:
        # read title
        title = f.readlines(1)
        # read description
        description = f.readlines()[0:]
    # saving to the header list while removing the "newline" character
    title_colom.append(''.join(title).rstrip('\n'))
    # saving to the description list while removing the "newline" character
    description_colom.append(''.join(description).replace('\n', ' '))

# dataframe creation
data = {'vacancy': title_colom,
        'description': description_colom}
df_pd = pd.DataFrame(data)

# create .csv file for for further reading
df_pd.to_csv('jobs.csv')
df = pd.read_csv('jobs.csv')
### reading text files and creating a dataframe code finished


# function to check for forbidden characters
# in the future, I will call the final picture of the word cloud the name of the vacancy
def prohibited_signs(text):
    punctuation = '/\<>:*?|"'
    for i in text:
        if i in punctuation:
            text = text.replace(i, ' ')
    return text



### mask code started
# choose a photo for the mask
mask = np.array(Image.open('E:\TEST FROM COMPANIES\CIVISION\Test-CIVI\images\work_2.png'))

# Each number in the mask should be == 255 (white), so if it's != 255 we need to change it. In worst case mask will not working
def transform_format(val):
    # my images numbers == 0 (python.png)
    if val == 0:
        return 255
    else:
        return val

# change the current array by replacing the data type with int32
transformed_python_mask = np.ndarray((mask.shape[0], mask.shape[1]), np.int32)

# use transform_format func for change each line
for i in range(len(mask)):
    transformed_python_mask[i] = list(map(transform_format, mask[i]))
### mask code finished



### word cloud generation code started
# using a loop we get the title and description of the vacancy,
# then we generate a word cloud for each vacancy
for df_info in range(10):
    job, job_desc = df.loc[df_info, ['vacancy', 'description']]

    # Create stop words list:
    stopwords = set(STOPWORDS)
    # stopwords.update([])

    # settings for a word cloud image
    word_cloud = WordCloud(max_font_size=100,
                           max_words=1000,
                           mask=transformed_python_mask,
                           background_color='black',
                           stopwords=stopwords,
                           contour_width=2,
                           contour_color='navy'
                           )

    # generate word cloud
    word_cloud.generate(job_desc)

    # save result
    # use prohibited_signs func fot title file
    word_cloud.to_file(f'E:\TEST FROM COMPANIES\CIVISION\Test-CIVI/result image/{prohibited_signs(job)}.png')

    # Display the generated image:
    plt.figure(figsize=[15, 10])
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
### word cloud generation code finished