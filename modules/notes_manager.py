import json
import os
import uuid
from datetime import datetime

class NotesManager:
    def __init__(self):
        self.notes = []

    def add_note(self, content, title=None):
        self.notes.append({"title": title, "content": content})

    def remove_note(self, content):
        self.notes = [note for note in self.notes if note["content"] != content]

    def get_all_notes(self):
        return self.notes