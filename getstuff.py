import imports

class Getter():
    '''Get some stuff from subreddits. Required params:
    (str): <Subreddit name>, (int): <number of posts>'''
    reddit = imports.praw.Reddit(   # initialize the reddit variable
        client_id='UctJAJCE-8-nvA',
        client_secret='1FsIcCXLLrKqxcAU3bRISfzuUrI',
        user_agent = 'my user agent'

    )
    def __init__(self, subreddit , number):
        self.sb = subreddit
        self.n = number

    def content(self):
        '''Get the content . ie , the posts in the subreddit,
         followed by the link contained in them , if any.
         Now , send them to a contents.txt file date wise '''
        with open('Contents.txt', 'a') as f :
            f.write("On:")
            f.write(str(imports.dt.today()))
            f.write('\n')
            i = 1
            for submission in self.reddit.subreddit(self.sb).hot(limit=self.n):
                comment = submission.comments.list()
                t = comment[0].body
                f.write(str(i))
                i += 1
                f.write("\t")
                f.write(submission.title)
                f.write('\n')
                f.write('=========================\n')
                f.write(submission.selftext)
                f.write('\n')
                f.write('*************************\n')
                f.write("URL to the full article:\t ")
                f.write(submission.url)
                f.write('\n')
                f.write("Comments:")
                f.write(t)
                f.write('\n')
                f.write('CCCCCCCCCCCCCCCCCCCCC')
                f.write('\n')

    def main(self):
        '''Calls all needed methods.'''
        self.content()

    def doc(self):
        '''Used to get the docstring for a function.'''
        for sub in self.reddit.subreddit(self.sb).hot(limit = 1):
            print(sub.__doc__)
if __name__ == '__main__':
    get = Getter('news', 5)  # get 5 news bits
    get.main()