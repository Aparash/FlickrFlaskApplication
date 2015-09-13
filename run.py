from flask import Flask, Markup, request, render_template
import feedparser

app = Flask(__name__)

# Route for Displaying Feed from Flickr API
@app.route('/', methods=['GET', 'POST'])
def get_images():
        query = ''
        if request.method == 'POST':
                query = request.form['searchtag']
                print query

        feed = get_feed(query)
        print str(feed)
        return render_template('index.html',
                                feed = feed)

def get_feed(tags=''):
        url = 'https://api.flickr.com/services/feeds/photos_public.gne'
        if tags != '':
                url += '?tags=' + ','.join(tags.split(' '))
        print url
        return map(lambda x: Markup(x.content[0].value.encode('ascii', 'ignore')),
                   feedparser.parse(url).entries)


if __name__ == '__main__':
        app.run()