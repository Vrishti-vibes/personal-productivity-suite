import pytest
from modules.calculator import Calculator
from modules.notes_manager import NotesManager
from modules.file_organizer import FileOrganizer
from modules.backup_manager import BackupManager
from modules.timer import Timer
from modules.unit_converter import UnitConverter
from modules.utils import some_util_function  # replace with actual utils

# ---------------- Calculator Tests ----------------
def test_calculator_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0

def test_calculator_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(3, 5) == -2

# Add multiply/divide tests if applicable
def test_calculator_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)

# ---------------- NotesManager Tests ----------------
@pytest.fixture
def notes():
    return NotesManager()

def test_add_note(notes):
    notes.add_note(content="Test Note", title="Sample")
    all_contents = [note['content'] for note in notes.get_all_notes()]
    assert "Test Note" in all_contents

def test_remove_note(notes):
    notes.add_note(content="Temp Note", title="Temp")
    notes.remove_note("Temp Note")
    all_contents = [note['content'] for note in notes.get_all_notes()]
    assert "Temp Note" not in all_contents

# ---------------- FileOrganizer Tests ----------------
@pytest.fixture
def organizer(tmp_path):
    return FileOrganizer(base_path=tmp_path)

def test_create_file(organizer, tmp_path):
    file_name = "sample.txt"
    organizer.create_file(file_name, content="Hello")
    assert (tmp_path / file_name).exists()

def test_delete_file(organizer, tmp_path):
    file_name = "delete_me.txt"
    organizer.create_file(file_name, content="Bye")
    organizer.delete_file(file_name)
    assert not (tmp_path / file_name).exists()

# ---------------- BackupManager Tests ----------------
def test_backup(tmp_path):
    manager = BackupManager()
    test_file = tmp_path / "backup.txt"
    test_file.write_text("Backup data")
    manager.backup_file(test_file)
    # check if backup exists in backup folder (update path according to your code)
    backup_path = tmp_path / "backup" / "backup.txt"
    assert backup_path.exists()

# ---------------- Timer Tests ----------------
def test_timer_start_stop():
    t = Timer()
    t.start()
    t.stop()
    assert t.elapsed >= 0

# ---------------- UnitConverter Tests ----------------
def test_length_conversion():
    converter = UnitConverter()
    assert converter.meters_to_km(1000) == 1
    assert converter.km_to_meters(1) == 1000

def test_weight_conversion():
    converter = UnitConverter()
    assert converter.kg_to_g(2) == 2000
    assert converter.g_to_kg(2000) == 2

# ---------------- Utils Tests ----------------
def test_some_util_function():
    # replace with actual function test
    result = some_util_function("input")
    assert result is not None