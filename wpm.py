from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
import config
import feedparser

#authenticate
wp_url = config.wordpressURL
wp_username = config.username
wp_password = config.password
wp = Client(wp_url, wp_username, wp_password)

# grab rss item
d = feedparser.parse('http://newsrss.bbc.co.uk/rss/newsonline_uk_edition/technology/rss.xml')
print(d.feed.title)
print(d.entries[0].title)
print(d.entries[0].description)

#post and activate new post
post = WordPressPost()
post.title = (d.entries[0].title)
post.content = (d.entries[0].description)
post.enclosure = (d.entries[0].media_content)
post.post_status = 'publish'
post.terms_names = {
  'post_tag': ['test', 'firstpost'],
  'category': ['Introductions', 'Tests']
}
wp.call(NewPost(post))

print("Done!")