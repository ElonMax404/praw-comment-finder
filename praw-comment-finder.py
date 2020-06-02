import praw
from praw.models import MoreComments

reddit = praw.Reddit(client_id="",
                     client_secret="",
                     user_agent="",
                     username = "",
                     password = "")

sub = input("Enter name of the subreddit to search: ")
limit = int(input('Enter the limit of posts to search: '))
word = input('Enter the targeted word to search: ')

subreddit = reddit.subreddit(sub)


postsWithThisWord = 0
for submission in subreddit.hot(limit=limit):
	submission.comments.replace_more(limit=None)
	ContainingWord = False
	for comment in submission.comments.list():
		if ContainingWord == False:
			if word in str(comment.body).lower():
				print(submission.title)
				print("Post link: " + "https://www.reddit.com/r/" + str(subreddit) + '/comments/' + str(submission.id))
				print()
				postsWithThisWord = postsWithThisWord + 1
				ContainingWord = True
		else:
			break


print(str(postsWithThisWord) + " posts, in limit of " + str(limit) + " , are containing comments with targeted word -  " + str(word))