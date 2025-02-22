class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False


    def send(self):
        self.is_sent = True


    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

all_emails = []

while True:
    command = input().split()

    if command[0] == "Stop":
        break

    sender, receiver, content = command
    instance = Email(sender, receiver, content)

    all_emails.append(instance)



indexes = list(map(int, input().split(", ")))

for index in indexes:
    all_emails[index].send()

for mail in all_emails:
    print(mail.get_info())



