import praw,requests,re

r = praw.Reddit(client_id='UctJAJCE-8-nvA',
        client_secret='1FsIcCXLLrKqxcAU3bRISfzuUrI',
        user_agent = 'my user agent')
subreddit = r.subreddit('news')

for post in subreddit.new(limit=5):
    url = (post.url)
    file_name = url.split("/")
    if len(file_name) == 0:
        file_name = re.findall("/(.*?)", url)
    file_name = file_name[-1]
    if "." not in file_name:
        file_name += ".png"
    print(file_name)
    r = requests.get(url)
    with open(file_name,"wb") as f:
        f.write(r.content)