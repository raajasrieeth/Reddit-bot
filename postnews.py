import imports
import getstuff
# webbrowser.open('http://thisisraaj.unaux.com/wp-admin/post.php?post=48&action=edit')  # news page in my website.

if __name__ == '__main__':
    items = getstuff.Getter('news', 5)  # get 5 news bits daily!
    items.content()
