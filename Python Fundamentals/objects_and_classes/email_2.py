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
    sender, receiver, content = entry.split()
    email = Email(sender, receiver, content)
    emails.append(email)
    entry = input()

emails_to_send = list(map(int, input().split(', ')))

emails_sent = [emails[i].send() for i in emails_to_send]

for email in emails:
    print(email.get_info())