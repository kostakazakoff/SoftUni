from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.documents = []
        self.topics = []

    def add_category(self, category:Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic:Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document:Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name:str):
        category = [x for x in self.categories if x.id == category_id][0]
        if category: category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = [x for x in self.topics if x.id == topic_id][0]
        if topic: topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = [x for x in self.documents if x.id == document_id][0]
        if document: document.edit(new_file_name)

    def delete_category(self, category_id):
        category = [x for x in self.categories if x.id == category_id][0]
        if category: self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = [x for x in self.topics if x.id == topic_id][0]
        if topic: self.topics.remove(topic)

    def delete_document(self, document_id):
        document = [x for x in self.documents if x.id == document_id][0]
        if document: self.documents.remove(document)

    def get_document(self, document_id):
        document = [x for x in self.documents if x.id == document_id][0]
        return document

    def __repr__(self):
        return '\n'.join(repr(x) for x in self.documents)

