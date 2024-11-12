const noteList = document.getElementById('note-list');
const noteEditor = document.getElementById('note-editor');
const viewNote = document.getElementById('view-note');
const newNoteBtn = document.getElementById('new-note-btn');
const saveNoteBtn = document.getElementById('save-note-btn');
const deleteNoteBtn = document.getElementById('delete-note-btn');
const closeNoteBtn = document.getElementById('close-note-btn');
const noteTitleInput = document.getElementById('note-title');
const noteContentInput = document.getElementById('note-content');
const noteTagsInput = document.getElementById('note-tags');
const viewNoteTitle = document.getElementById('view-note-title');
const viewNoteContent = document.getElementById('view-note-content');

// Initialize notes array
let notes = [];

// Load notes from local storage
if (localStorage.getItem('notes')) {
    notes = JSON.parse(localStorage.getItem('notes'));
    renderNoteList();
}

// Render note list
function renderNoteList() {
    noteList.innerHTML = '';
    notes.forEach((note, index) => {
        const noteListItem = document.createElement('li');
        noteListItem.textContent = note.title;
        noteListItem.addEventListener('click', () => {
            openNote(index);
        });
        noteList.appendChild(noteListItem);
    });
}

// Open note
function openNote(index) {
    viewNote.style.display = 'block';
    viewNoteTitle.textContent = notes[index].title;
    viewNoteContent.textContent = notes[index].content;
}

// Close note
closeNoteBtn.addEventListener('click', () => {
    viewNote.style.display = 'none';
});

// Save note
saveNoteBtn.addEventListener('click', () => {
    const note = {
        title: noteTitleInput.value,
        content: noteContentInput.value,
        tags: noteTagsInput.value
    };
    notes.push(note);
    localStorage.setItem('notes', JSON.stringify(notes));
    renderNoteList();
    noteTitleInput.value = '';
    noteContentInput.value = '';
    noteTagsInput.value = '';
});

// Delete note
deleteNoteBtn.addEventListener('click', () => {
    const index = noteList.selectedIndex;
    notes.splice(index, 1);
    localStorage.setItem('notes', JSON.stringify(notes));
    renderNoteList();
});

// New note
newNoteBtn.addEventListener('click', () => {
    noteEditor.style.display = 'block';
    noteTitleInput.focus();
});

// Event listeners
noteTitleInput.addEventListener('input', () => {
    saveNoteBtn.disabled = !noteTitleInput.value;
});

noteContentInput.addEventListener('input', () => {
    saveNoteBtn.disabled = !noteContentInput.value;
});

noteTagsInput.addEventListener('input', () => {
    saveNoteBtn.disabled = !noteTagsInput.value;
});