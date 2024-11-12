# Application Name: RiseNote
# Features:
# Note Creation
# Note Editing
# Note Deletion
# Note Searching
# Tag-based Note Organization
# Note Saving and Loading
# Required Libraries:
# tkinter for UI
# tkinter.ttk for themed widgets
# sqlite3 for database management

# import tkinter as tk
# from tkinter import ttk
# import sqlite3

# class RiseNote:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("RiseNote")
#         self.root.geometry("800x600")

#         # Create database connection
#         self.conn = sqlite3.connect("risenote.db")
#         self.cursor = self.conn.cursor()
#         self.cursor.execute("""
#             CREATE TABLE IF NOT EXISTS notes (
#                 id INTEGER PRIMARY KEY,
#                 title TEXT,
#                 content TEXT,
#                 tags TEXT
#             )
#         """)
#         self.conn.commit()

#         # Create UI components
#         self.notebook = ttk.Notebook(self.root)
#         self.notebook.pack(fill="both", expand=True)

#         self.note_frame = ttk.Frame(self.notebook)
#         self.notebook.add(self.note_frame, text="Notes")

#         self.tag_frame = ttk.Frame(self.notebook)
#         self.notebook.add(self.tag_frame, text="Tags")

#         self.search_frame = ttk.Frame(self.notebook)
#         self.notebook.add(self.search_frame, text="Search")

#         # Note frame components
#         self.title_label = ttk.Label(self.note_frame, text="Title:")
#         self.title_label.pack()
#         self.title_entry = ttk.Entry(self.note_frame)
#         self.title_entry.pack()

#         self.content_text = tk.Text(self.note_frame)
#         self.content_text.pack(fill="both", expand=True)

#         self.save_button = ttk.Button(self.note_frame, text="Save", command=self.save_note)
#         self.save_button.pack()

#         self.delete_button = ttk.Button(self.note_frame, text="Delete", command=self.delete_note)
#         self.delete_button.pack()

#         # Tag frame components
#         self.tag_label = ttk.Label(self.tag_frame, text="Tags:")
#         self.tag_label.pack()
#         self.tag_entry = ttk.Entry(self.tag_frame)
#         self.tag_entry.pack()

#         self.tag_listbox = tk.Listbox(self.tag_frame)
#         self.tag_listbox.pack(fill="both", expand=True)

#         # Search frame components
#         self.search_label = ttk.Label(self.search_frame, text="Search:")
#         self.search_label.pack()
#         self.search_entry = ttk.Entry(self.search_frame)
#         self.search_entry.pack()

#         self.search_button = ttk.Button(self.search_frame, text="Search", command=self.search_notes)
#         self.search_button.pack()

#         self.search_results = tk.Text(self.search_frame)
#         self.search_results.pack(fill="both", expand=True)

#     def save_note(self):
#         title = self.title_entry.get()
#         content = self.content_text.get("1.0", "end-1c")
#         tags = self.tag_entry.get()
#         self.cursor.execute("INSERT INTO notes (title, content, tags) VALUES (?, ?, ?)", (title, content, tags))
#         self.conn.commit()
#         self.title_entry.delete(0, "end")
#         self.content_text.delete("1.0", "end")
#         self.tag_entry.delete(0, "end")

#     def delete_note(self):
#         note_id = self.cursor.lastrowid
#         self.cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
#         self.conn.commit()

#     def search_notes(self):
#         query = self.search_entry.get()
#         self.cursor.execute("SELECT * FROM notes WHERE title LIKE ? OR content LIKE ?", ("%" + query + "%", "%" + query + "%"))
#         results = self.cursor.fetchall()
#         self.search_results.delete("1.0", "end")
#         for result in results:
#             self.search_results.insert("end", f"Title: {result[1]}\nContent: {result[2]}\nTags: {result[3]}\n\n")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = RiseNote(root)
#     root.mainloop()

# adding sidebar

# import tkinter as tk
# from tkinter import ttk
# import sqlite3

# class RiseNote:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("RiseNote")
#         self.root.geometry("1000x600")

#         # Create database connection
#         self.conn = sqlite3.connect("risenote.db")
#         self.cursor = self.conn.cursor()
#         self.cursor.execute("""
#             CREATE TABLE IF NOT EXISTS notes (
#                 id INTEGER PRIMARY KEY,
#                 title TEXT,
#                 content TEXT,
#                 tags TEXT
#             )
#         """)
#         self.conn.commit()

#         # Create main frame
#         self.main_frame = tk.Frame(self.root)
#         self.main_frame.pack(fill="both", expand=True)

#         # Create sidebar frame
#         self.sidebar_frame = tk.Frame(self.main_frame, width=200, bg="#f0f0f0")
#         self.sidebar_frame.pack(side="left", fill="y")

#         # Create note list frame
#         self.note_list_frame = tk.Frame(self.sidebar_frame)
#         self.note_list_frame.pack(fill="both", expand=True)

#         # Create note list label
#         self.note_list_label = tk.Label(self.note_list_frame, text="Notes", bg="#f0f0f0")
#         self.note_list_label.pack()

#         # Create note list
#         self.note_list = tk.Listbox(self.note_list_frame)
#         self.note_list.pack(fill="both", expand=True)

#         # Create note frame
#         self.note_frame = tk.Frame(self.main_frame)
#         self.note_frame.pack(fill="both", expand=True)

#         # Create title label
#         self.title_label = tk.Label(self.note_frame, text="Title:")
#         self.title_label.pack()

#         # Create title entry
#         self.title_entry = tk.Entry(self.note_frame)
#         self.title_entry.pack()

#         # Create content text
#         self.content_text = tk.Text(self.note_frame)
#         self.content_text.pack(fill="both", expand=True)

#         # Create tag label
#         self.tag_label = tk.Label(self.note_frame, text="Tags:")
#         self.tag_label.pack()

#         # Create tag entry
#         self.tag_entry = tk.Entry(self.note_frame)
#         self.tag_entry.pack()

#         # Create save button
#         self.save_button = tk.Button(self.note_frame, text="Save", command=self.save_note)
#         self.save_button.pack()

#         # Create delete button
#         self.delete_button = tk.Button(self.note_frame, text="Delete", command=self.delete_note)
#         self.delete_button.pack()

#         # Create search frame
#         self.search_frame = tk.Frame(self.main_frame)
#         self.search_frame.pack(fill="x")

#         # Create search label
#         self.search_label = tk.Label(self.search_frame, text="Search:")
#         self.search_label.pack(side="left")

#         # Create search entry
#         self.search_entry = tk.Entry(self.search_frame)
#         self.search_entry.pack(side="left", fill="x", expand=True)

#         # Create search button
#         self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_notes)
#         self.search_button.pack(side="left")

#         # Load notes
#         self.load_notes()

#     def save_note(self):
#         title = self.title_entry.get()
#         content = self.content_text.get("1.0", "end-1c")
#         tags = self.tag_entry.get()
#         self.cursor.execute("INSERT INTO notes (title, content, tags) VALUES (?, ?, ?)", (title, content, tags))
#         self.conn.commit()
#         self.title_entry.delete(0, "end")
#         self.content_text.delete("1.0", "end")
#         self.tag_entry.delete(0, "end")
#         self.load_notes()

#     def delete_note(self):
#         note_id = self.note_list.curselection()[0]
#         note_title = self.note_list.get(note_id)
#         self.cursor.execute("DELETE FROM notes WHERE title = ?", (note_title,))
#         self.conn.commit()
#         self.load_notes()

#     def search_notes(self):
#         query = self.search_entry.get()
#         self.cursor.execute("SELECT * FROM notes WHERE title LIKE ? OR content LIKE ?", ("%" + query + "%", "%" + query + "%"))
#         results = self.cursor.fetchall()
#         self.note_list.delete(0, "end")
#         for result in results:
#             self.note_list.insert("end", result[1])

#     def load_notes(self):
#         self.cursor.execute("SELECT title FROM notes")
#         notes = self.cursor.fetchall()
#         self.note_list.delete(0, "end")
#         for note in notes:
#             self.note_list.insert("end", note[0])

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = RiseNote(root)
#     root.mainloop()

import tkinter as tk
from tkinter import ttk
import sqlite3

class RiseNote:
    def __init__(self, root):
        self.root = root
        self.root.title("RiseNote")
        self.root.geometry("1000x600")

        # Create database connection
        self.conn = sqlite3.connect("risenote.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY,
                title TEXT,
                content TEXT,
                tags TEXT
            )
        """)
        self.conn.commit()

        # Create main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        # Create sidebar frame
        self.sidebar_frame = tk.Frame(self.main_frame, width=200, bg="#f0f0f0")
        self.sidebar_frame.pack(side="left", fill="y")

        # Create note list frame
        self.note_list_frame = tk.Frame(self.sidebar_frame)
        self.note_list_frame.pack(fill="both", expand=True)

        # Create note list label
        self.note_list_label = tk.Label(self.note_list_frame, text="Notes", bg="#f0f0f0")
        self.note_list_label.pack()

        # Create note list
        self.note_list = tk.Listbox(self.note_list_frame)
        self.note_list.pack(fill="both", expand=True)

        # Create open note button
        self.open_note_button = tk.Button(self.note_list_frame, text="Open Note", command=self.open_note)
        self.open_note_button.pack()

        # Create note frame
        self.note_frame = tk.Frame(self.main_frame)
        self.note_frame.pack(fill="both", expand=True)

        # Create title label
        self.title_label = tk.Label(self.note_frame, text="Title:")
        self.title_label.pack()

        # Create title entry
        self.title_entry = tk.Entry(self.note_frame)
        self.title_entry.pack()

        # Create content text
        self.content_text = tk.Text(self.note_frame)
        self.content_text.pack(fill="both", expand=True)

        # Create tag label
        self.tag_label = tk.Label(self.note_frame, text="Tags:")
        self.tag_label.pack()

        # Create tag entry
        self.tag_entry = tk.Entry(self.note_frame)
        self.tag_entry.pack()

        # Create save button
        self.save_button = tk.Button(self.note_frame, text="Save", command=self.save_note)
        self.save_button.pack()

        # Create delete button
        self.delete_button = tk.Button(self.note_frame, text="Delete", command=self.delete_note)
        self.delete_button.pack()

        # Create search frame
        self.search_frame = tk.Frame(self.main_frame)
        self.search_frame.pack(fill="x")

        # Create search label
        self.search_label = tk.Label(self.search_frame, text="Search:")
        self.search_label.pack(side="left")

        # Create search entry
        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.pack(side="left", fill="x", expand=True)

        # Create search button
        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_notes)
        self.search_button.pack(side="left")

        # Create view note frame
        self.view_note_frame = tk.Frame(self.main_frame)
        self.view_note_frame.pack(fill="both", expand=True)

        # Create view note label
        self.view_note_label = tk.Label(self.view_note_frame, text="View Note:")
        self.view_note_label.pack()

        # Create view note text
        self.view_note_text = tk.Text(self.view_note_frame)
        self.view_note_text.pack(fill="both", expand=True)

        # Create close note button
        self.close_note_button = tk.Button(self.view_note_frame, text="Close Note", command=self.close_note)
        self.close_note_button.pack()

        # Hide view note frame
        self.view_note_frame.pack_forget()

        # Load notes
        self.load_notes()

    def save_note(self):
        title = self.title_entry.get()
        content = self.content_text.get("1.0", "end-1c")
        tags = self.tag_entry.get()
        self.cursor.execute("INSERT INTO notes (title, content, tags) VALUES (?, ?, ?)", (title, content, tags))
        self.conn.commit()
        self.title_entry.delete(0, "end")
        self.content_text.delete("1.0", "end")
        self.tag_entry.delete(0, "end")
        self.load_notes()

    def delete_note(self):
        note_id = self.note_list.curselection()[0]
        note_title = self.note_list.get(note_id)
        self.cursor.execute("DELETE FROM notes WHERE title = ?", (note_title,))
        self.conn.commit()
        self.load_notes()

    def search_notes(self):
        query = self.search_entry.get()
        self.cursor.execute("SELECT * FROM notes WHERE title LIKE ? OR content LIKE ?", ("%" + query + "%", "%" + query + "%"))
        results = self.cursor.fetchall()
        self.note_list.delete(0, "end")
        for result in results:
            self.note_list.insert("end", result[1])

    def load_notes(self):
        self.cursor.execute("SELECT title FROM notes")
        notes = self.cursor.fetchall()
        self.note_list.delete(0, "end")
        for note in notes:
            self.note_list.insert("end", note[0])

    def open_note(self):
        note_id = self.note_list.curselection()[0]
        note_title = self.note_list.get(note_id)
        self.cursor.execute("SELECT content FROM notes WHERE title = ?", (note_title,))
        note_content = self.cursor.fetchone()[0]
        self.view_note_text.delete("1.0", "end")
        self.view_note_text.insert("1.0", note_content)
        self.view_note_frame.pack(fill="both", expand=True)
        self.note_frame.pack_forget()

    def close_note(self):
        self.view_note_frame.pack_forget()
        self.note_frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = RiseNote(root)
    root.mainloop()

   