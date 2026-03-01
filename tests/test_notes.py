import pytest
from modules.notes_manager import NotesManager

def test_add_note():
    notes = NotesManager()
    notes.add_note(content="Test Note", title="Sample")   # <-- content argument fix
    assert "Test Note" in [note['content'] for note in notes.get_all_notes()]

def test_remove_note():
    notes = NotesManager()
    notes.add_note(content="Temp Note", title="Temp")     # <-- content argument fix
    notes.remove_note("Temp Note")
    assert "Temp Note" not in [note['content'] for note in notes.get_all_notes()]