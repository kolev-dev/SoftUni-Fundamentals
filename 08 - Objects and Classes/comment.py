class Comment:
    def __init__(self, username, content, likes = 0):
        self.username = username
        self.content = content
        self.likes = likes


comment1 = Comment("user1", "I like this book")
print(comment1.username)
print(comment1.content)
print(comment1.likes)