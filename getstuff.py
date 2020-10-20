import imports

class Getter():
    reddit = praw.Reddit(   # initialize the reddit variable
        client_id='UctJAJCE-8-nvA',
        client_secret='1FsIcCXLLrKqxcAU3bRISfzuUrI',
        user_agent = 'my user agent'

    )
    def __init__(self, subreddit , number):
        self.sb = subreddit
        self.n = number

    def content(self):
        '''Get the content . ie , the posts in the subreddit,
         followed by the link contained in them , if any. '''
        for submission in self.reddit.subreddit(self.sb).hot(limit=self.n):
            print(submission.title)
            print('=========================')
            print(submission.selftext)
            print('*************************')
            print("URL to the full article: " , submission.url)

    def comments(self):
        '''Get the top comments in the subreddit'''
        for comment in self.reddit.subreddit(self.sb).comments(limit=5):
            print("++++++++++++++++++++++")
            print(comment.body) # get the body of the comment
            print("######################")

    def main(self):
        '''get the content '''
        print(self.content())
    def doc(self):
        '''Used to get the docstring for a function.'''
        for sub in self.reddit.subreddit(self.sb).hot(limit = 1):
            print(sub.__doc__)
if __name__ == '__main__':
    get = Getter('news', 5)  # get 5 news bits
    get.main()