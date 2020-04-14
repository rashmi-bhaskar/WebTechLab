from os import path
from wordcloud import WordCloud


def wcloud(filename):
    d = path.dirname(__file__)

    # Read the whole text.
    text = open(path.join(d, filename)).read()

    # Generate a word cloud image
    wordcloud = WordCloud(collocations=False, min_font_size=7, width=1600, height=900).generate(text)

    # Display the generated image:
    # the matplotlib way:
    import matplotlib.pyplot as plt
    plt.figure( figsize=(16,9) )
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()