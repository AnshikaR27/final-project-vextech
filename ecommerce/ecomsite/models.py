from mongoengine import Document, StringField, EmailField

class EmailSubscriber(Document):
    email = EmailField(unique=True, required=True)
    
    def __str__(self):
        return self.email
