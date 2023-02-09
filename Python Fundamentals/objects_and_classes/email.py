class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


entry = input()
emails = []
while entry != 'Stop':
    email = entry.split()
    emails.append(email)
    entry = input()
sent_indexes = list(map(int, input().split(', ')))

for i in range(len(emails)):
    sender, receiver, content = emails[i]
    email = Email(sender, receiver, content)
    if i in sent_indexes:
        email.send()
    print(email.get_info())