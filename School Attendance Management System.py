# import tkinter as tk
# from tkinter import ttk, messagebox
# import sqlite3
# from datetime import datetime
# import re

# class AttendanceSystem:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("SNJ Higher Secondary School - Attendance System")
#         self.root.geometry("1000x600")
#         self.root.configure(bg="#f0f2f5")

#         # Initialize database
#         self.create_database()
        
#         # Variables
#         self.name_var = tk.StringVar()
#         self.email_var = tk.StringVar()
#         self.phone_var = tk.StringVar()
#         self.role_var = tk.StringVar()
#         self.status_var = tk.StringVar()

#         # Main Header
#         header_frame = tk.Frame(root, bg="#1a73e8", height=60)
#         header_frame.pack(fill=tk.X)
#         tk.Label(
#             header_frame,
#             text="SNJ Higher Secondary School - Attendance Management",
#             font=("Helvetica", 18, "bold"),
#             bg="#1a73e8",
#             fg="white",
#             pady=10
#         ).pack()

#         # Create main content area
#         self.create_content_area()

#     def create_database(self):
#         conn = sqlite3.connect('school_attendance.db')
#         cursor = conn.cursor()
        
#         # Create tables for attendance records
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS users (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT NOT NULL,
#                 email TEXT UNIQUE NOT NULL,
#                 phone TEXT NOT NULL,
#                 role TEXT NOT NULL
#             )
#         ''')
        
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS attendance (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 user_id INTEGER,
#                 date TEXT NOT NULL,
#                 status TEXT NOT NULL,
#                 FOREIGN KEY (user_id) REFERENCES users (id)
#             )
#         ''')
        
#         conn.commit()
#         conn.close()

#     def create_content_area(self):
#         # Input Frame
#         input_frame = tk.Frame(self.root, bg="#ffffff", pady=20)
#         input_frame.pack(fill=tk.X, padx=20)

#         # Style configuration
#         style = ttk.Style()
#         style.configure("Custom.TEntry", padding=5)

#         # Input fields
#         labels = ["Name:", "Email:", "Phone:", "Role:"]
#         variables = [self.name_var, self.email_var, self.phone_var, self.role_var]
        
#         for i, (label, var) in enumerate(zip(labels, variables)):
#             tk.Label(
#                 input_frame,
#                 text=label,
#                 font=("Helvetica", 10, "bold"),
#                 bg="#ffffff"
#             ).grid(row=i, column=0, padx=10, pady=5, sticky="e")
            
#             if label == "Role:":
#                 role_combo = ttk.Combobox(
#                     input_frame,
#                     textvariable=var,
#                     values=["Student", "Teacher"],
#                     state="readonly",
#                     width=30
#                 )
#                 role_combo.grid(row=i, column=1, padx=10, pady=5, sticky="w")
#             else:
#                 ttk.Entry(
#                     input_frame,
#                     textvariable=var,
#                     style="Custom.TEntry",
#                     width=30
#                 ).grid(row=i, column=1, padx=10, pady=5, sticky="w")

#         # Attendance Status
#         tk.Label(
#             input_frame,
#             text="Attendance:",
#             font=("Helvetica", 10, "bold"),
#             bg="#ffffff"
#         ).grid(row=4, column=0, padx=10, pady=5, sticky="e")
        
#         status_combo = ttk.Combobox(
#             input_frame,
#             textvariable=self.status_var,
#             values=["Present", "Absent", "Late"],
#             state="readonly",
#             width=30
#         )
#         status_combo.grid(row=4, column=1, padx=10, pady=5, sticky="w")

#         # Buttons
#         btn_frame = tk.Frame(input_frame, bg="#ffffff")
#         btn_frame.grid(row=5, column=0, columnspan=2, pady=20)

#         ttk.Button(
#             btn_frame,
#             text="Mark Attendance",
#             command=self.mark_attendance,
#             style="Accent.TButton",
#             padding=10
#         ).pack(side=tk.LEFT, padx=5)

#         ttk.Button(
#             btn_frame,
#             text="View Records",
#             command=self.view_records,
#             style="Accent.TButton",
#             padding=10
#         ).pack(side=tk.LEFT, padx=5)

#         # Create custom style for buttons
#         style.configure(
#             "Accent.TButton",
#             background="#1a73e8",
#             foreground="white",
#             font=("Helvetica", 10)
#         )

#     def validate_inputs(self):
#         # Email validation
#         email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#         if not re.match(email_pattern, self.email_var.get()):
#             messagebox.showerror("Error", "Please enter a valid email address")
#             return False

#         # Phone validation
#         phone_pattern = r'^\d{10}$'
#         if not re.match(phone_pattern, self.phone_var.get()):
#             messagebox.showerror("Error", "Please enter a valid 10-digit phone number")
#             return False

#         # Check if all fields are filled
#         if not all([
#             self.name_var.get(),
#             self.email_var.get(),
#             self.phone_var.get(),
#             self.role_var.get(),
#             self.status_var.get()
#         ]):
#             messagebox.showerror("Error", "Please fill all fields")
#             return False

#         return True

#     def mark_attendance(self):
#         if not self.validate_inputs():
#             return

#         try:
#             conn = sqlite3.connect('school_attendance.db')
#             cursor = conn.cursor()

#             # First insert or get user
#             cursor.execute('''
#                 INSERT OR IGNORE INTO users (name, email, phone, role)
#                 VALUES (?, ?, ?, ?)
#             ''', (
#                 self.name_var.get(),
#                 self.email_var.get(),
#                 self.phone_var.get(),
#                 self.role_var.get()
#             ))

#             # Get user_id
#             cursor.execute('SELECT id FROM users WHERE email = ?', (self.email_var.get(),))
#             user_id = cursor.fetchone()[0]

#             # Mark attendance
#             cursor.execute('''
#                 INSERT INTO attendance (user_id, date, status)
#                 VALUES (?, ?, ?)
#             ''', (
#                 user_id,
#                 datetime.now().strftime('%Y-%m-%d'),
#                 self.status_var.get()
#             ))

#             conn.commit()
#             messagebox.showinfo("Success", "Attendance marked successfully!")
            
#             # Clear fields
#             for var in [self.name_var, self.email_var, self.phone_var, self.role_var, self.status_var]:
#                 var.set('')

#         except sqlite3.IntegrityError:
#             messagebox.showerror("Error", "Email already exists!")
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred: {str(e)}")
#         finally:
#             conn.close()

#     def view_records(self):
#         # Create new window for records
#         records_window = tk.Toplevel(self.root)
#         records_window.title("Attendance Records")
#         records_window.geometry("800x600")

#         # Create Treeview
#         tree = ttk.Treeview(records_window, columns=("Name", "Email", "Role", "Date", "Status"), show="headings")
        
#         # Define headings
#         for col in tree["columns"]:
#             tree.heading(col, text=col)
#             tree.column(col, width=150)

#         # Add scrollbar
#         scrollbar = ttk.Scrollbar(records_window, orient=tk.VERTICAL, command=tree.yview)
#         tree.configure(yscrollcommand=scrollbar.set)

#         # Pack elements
#         tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#         scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#         # Fetch and display records
#         try:
#             conn = sqlite3.connect('school_attendance.db')
#             cursor = conn.cursor()
            
#             cursor.execute('''
#                 SELECT users.name, users.email, users.role, attendance.date, attendance.status
#                 FROM users
#                 JOIN attendance ON users.id = attendance.user_id
#                 ORDER BY attendance.date DESC
#             ''')
            
#             for row in cursor.fetchall():
#                 tree.insert("", tk.END, values=row)

#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred: {str(e)}")
#         finally:
#             conn.close()

# if __name__ == "__main__":
#     root = tk.Window()
#     app = AttendanceSystem(root)
#     root.mainloop()


# import tkinter as tk
# from tkinter import ttk, messagebox
# from datetime import datetime
# import csv
# import os
# import re

# class AttendanceSystem:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("SNJ Higher Secondary School - Attendance System")
#         self.root.geometry("900x600")
#         self.root.configure(bg="#f0f2f5")
        
#         # Create CSV files if they don't exist
#         self.initialize_files()
        
#         # Variables
#         self.name_var = tk.StringVar()
#         self.email_var = tk.StringVar()
#         self.phone_var = tk.StringVar()
#         self.role_var = tk.StringVar()
#         self.status_var = tk.StringVar()
        
#         self.setup_ui()
    
#     def initialize_files(self):
#         # Create attendance.csv if it doesn't exist
#         if not os.path.exists('attendance.csv'):
#             with open('attendance.csv', 'w', newline='') as file:
#                 writer = csv.writer(file)
#                 writer.writerow(['Date', 'Name', 'Email', 'Phone', 'Role', 'Status'])
    
#     def setup_ui(self):
#         # Main Header
#         header = tk.Frame(self.root, bg="#1a73e8", pady=15)
#         header.pack(fill=tk.X)
        
#         tk.Label(
#             header,
#             text="SNJ Higher Secondary School",
#             font=("Helvetica", 20, "bold"),
#             bg="#1a73e8",
#             fg="white"
#         ).pack()
        
#         tk.Label(
#             header,
#             text="Attendance Management System",
#             font=("Helvetica", 12),
#             bg="#1a73e8",
#             fg="white"
#         ).pack()

#         # Main Content Frame
#         content = tk.Frame(self.root, bg="white", pady=20)
#         content.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
#         # Input Fields
#         input_frame = tk.LabelFrame(content, text="Mark Attendance", bg="white", font=("Helvetica", 10, "bold"))
#         input_frame.pack(padx=20, pady=10, fill=tk.X)
        
#         # Grid for input fields
#         labels = ["Name:", "Email:", "Phone:", "Role:", "Status:"]
#         variables = [self.name_var, self.email_var, self.phone_var, self.role_var, self.status_var]
        
#         for i, (label, var) in enumerate(zip(labels, variables)):
#             tk.Label(
#                 input_frame,
#                 text=label,
#                 bg="white",
#                 font=("Helvetica", 10)
#             ).grid(row=i, column=0, padx=10, pady=8, sticky="e")
            
#             if label == "Role:":
#                 ttk.Combobox(
#                     input_frame,
#                     textvariable=var,
#                     values=["Student", "Teacher"],
#                     state="readonly",
#                     width=30
#                 ).grid(row=i, column=1, padx=10, pady=8, sticky="w")
#             elif label == "Status:":
#                 ttk.Combobox(
#                     input_frame,
#                     textvariable=var,
#                     values=["Present", "Absent", "Late"],
#                     state="readonly",
#                     width=30
#                 ).grid(row=i, column=1, padx=10, pady=8, sticky="w")
#             else:
#                 ttk.Entry(
#                     input_frame,
#                     textvariable=var,
#                     width=32
#                 ).grid(row=i, column=1, padx=10, pady=8, sticky="w")
        
#         # Buttons Frame
#         button_frame = tk.Frame(content, bg="white")
#         button_frame.pack(pady=20)
        
#         ttk.Button(
#             button_frame,
#             text="Mark Attendance",
#             command=self.mark_attendance,
#             style="Accent.TButton",
#             padding=10
#         ).pack(side=tk.LEFT, padx=5)
        
#         ttk.Button(
#             button_frame,
#             text="View Records",
#             command=self.view_records,
#             style="Accent.TButton",
#             padding=10
#         ).pack(side=tk.LEFT, padx=5)
        
#         # Style Configuration
#         style = ttk.Style()
#         style.configure("Accent.TButton", font=("Helvetica", 10))
        
#         # Records Frame
#         self.records_frame = tk.Frame(content, bg="white")
#         self.records_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
#         # Create Treeview for records
#         self.create_treeview()
        
#         # Load initial records
#         self.load_records()
    
#     def create_treeview(self):
#         columns = ("Date", "Name", "Email", "Phone", "Role", "Status")
#         self.tree = ttk.Treeview(self.records_frame, columns=columns, show="headings", height=10)
        
#         # Configure columns and headings
#         for col in columns:
#             self.tree.heading(col, text=col)
#             self.tree.column(col, width=100)
        
#         # Add scrollbar
#         scrollbar = ttk.Scrollbar(self.records_frame, orient=tk.VERTICAL, command=self.tree.yview)
#         self.tree.configure(yscrollcommand=scrollbar.set)
        
#         # Pack elements
#         self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#         scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
#     def validate_inputs(self):
#         # Email validation
#         email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#         if not re.match(email_pattern, self.email_var.get()):
#             messagebox.showerror("Error", "Please enter a valid email address")
#             return False
        
#         # Phone validation
#         phone_pattern = r'^\d{10}$'
#         if not re.match(phone_pattern, self.phone_var.get()):
#             messagebox.showerror("Error", "Please enter a valid 10-digit phone number")
#             return False
        
#         # Check if all fields are filled
#         if not all([
#             self.name_var.get(),
#             self.email_var.get(),
#             self.phone_var.get(),
#             self.role_var.get(),
#             self.status_var.get()
#         ]):
#             messagebox.showerror("Error", "Please fill all fields")
#             return False
        
#         return True
    
#     def mark_attendance(self):
#         if not self.validate_inputs():
#             return
        
#         # Get current date
#         current_date = datetime.now().strftime('%Y-%m-%d')
        
#         # Prepare record
#         record = [
#             current_date,
#             self.name_var.get(),
#             self.email_var.get(),
#             self.phone_var.get(),
#             self.role_var.get(),
#             self.status_var.get()
#         ]
        
#         # Save to CSV
#         with open('attendance.csv', 'a', newline='') as file:
#             writer = csv.writer(file)
#             writer.writerow(record)
        
#         # Clear fields
#         for var in [self.name_var, self.email_var, self.phone_var, self.role_var, self.status_var]:
#             var.set('')
        
#         messagebox.showinfo("Success", "Attendance marked successfully!")
        
#         # Reload records
#         self.load_records()
    
#     def load_records(self):
#         # Clear existing items
#         for item in self.tree.get_children():
#             self.tree.delete(item)
        
#         # Load records from CSV
#         try:
#             with open('attendance.csv', 'r') as file:
#                 reader = csv.reader(file)
#                 next(reader)  # Skip header row
#                 for row in reader:
#                     self.tree.insert('', 'end', values=row)
#         except FileNotFoundError:
#             pass
    
#     def view_records(self):
#         # Records are already visible in the main window
#         # Just scroll to the bottom to see the latest entries
#         if self.tree.get_children():
#             last_item = self.tree.get_children()[-1]
#             self.tree.see(last_item)
#             self.tree.selection_set(last_item)

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = AttendanceSystem(root)
#     root.mainloop()


import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import csv
import os
import re

class ModernAttendanceSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("SNJ Higher Secondary School - Attendance System")
        self.root.geometry("1200x800")
        self.root.configure(bg="#f0f2f5")
        
        # Initialize files
        self.initialize_files()
        
        # Variables
        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.role_var = tk.StringVar()
        self.status_var = tk.StringVar()
        
        # Setup theme
        self.setup_theme()
        self.setup_ui()
    
    def initialize_files(self):
        if not os.path.exists('attendance.csv'):
            with open('attendance.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Date', 'Name', 'Email', 'Phone', 'Role', 'Status'])
    
    def setup_theme(self):
        # Configure styles for modern look
        style = ttk.Style()
        
        # Configure main theme colors
        style.configure("MainFrame.TFrame", background="#f0f2f5")
        
        # Configure entry style
        style.configure("Modern.TEntry", padding=10)
        
        # Configure button styles
        style.configure("Primary.TButton",
                       padding=15,
                       font=("Helvetica", 10, "bold"))
        
        style.configure("Secondary.TButton",
                       padding=15,
                       font=("Helvetica", 10))
        
        # Configure combobox style
        style.configure("Modern.TCombobox", padding=5)
        
        # Configure treeview style
        style.configure("Modern.Treeview",
                       rowheight=30,
                       font=("Helvetica", 10))
        style.configure("Modern.Treeview.Heading",
                       font=("Helvetica", 10, "bold"))
    
    def setup_ui(self):
        # Main container with padding
        main_container = ttk.Frame(self.root, style="MainFrame.TFrame")
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header Section with gradient-like effect
        header_frame = tk.Frame(main_container, bg="#1a73e8")
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        # School name with shadow effect
        tk.Label(
            header_frame,
            text="SNJ Higher Secondary School",
            font=("Helvetica", 24, "bold"),
            bg="#1a73e8",
            fg="white",
            pady=10
        ).pack()
        
        tk.Label(
            header_frame,
            text="Attendance Management System",
            font=("Helvetica", 14),
            bg="#1a73e8",
            fg="#e8f0fe",
            pady=5
        ).pack()
        
        # Create two columns using PanedWindow
        paned = ttk.PanedWindow(main_container, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True)
        
        # Left Panel - Input Form
        left_panel = ttk.Frame(paned)
        paned.add(left_panel, weight=1)
        
        # Stylish form header
        form_header = tk.Frame(left_panel, bg="#ffffff")
        form_header.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(
            form_header,
            text="Mark Attendance",
            font=("Helvetica", 16, "bold"),
            bg="#ffffff",
            fg="#1a73e8",
            pady=10
        ).pack()
        
        # Form container with white background
        form_container = tk.Frame(left_panel, bg="#ffffff", padx=20, pady=20)
        form_container.pack(fill=tk.BOTH, expand=True)
        
        # Input fields with better spacing
        fields = [
            ("Name", self.name_var, "entry"),
            ("Email", self.email_var, "entry"),
            ("Phone", self.phone_var, "entry"),
            ("Role", self.role_var, ["Student", "Teacher"]),
            ("Status", self.status_var, ["Present", "Absent", "Late"])
        ]
        
        for i, (label_text, variable, field_type) in enumerate(fields):
            # Container for each field
            field_frame = tk.Frame(form_container, bg="#ffffff")
            field_frame.pack(fill=tk.X, pady=10)
            
            # Label
            tk.Label(
                field_frame,
                text=label_text,
                font=("Helvetica", 10, "bold"),
                bg="#ffffff",
                fg="#666666"
            ).pack(anchor="w")
            
            # Input field
            if field_type == "entry":
                ttk.Entry(
                    field_frame,
                    textvariable=variable,
                    style="Modern.TEntry",
                    width=30
                ).pack(fill=tk.X, pady=(5, 0))
            else:
                ttk.Combobox(
                    field_frame,
                    textvariable=variable,
                    values=field_type,
                    state="readonly",
                    style="Modern.TCombobox",
                    width=27
                ).pack(fill=tk.X, pady=(5, 0))
        
        # Buttons container
        button_frame = tk.Frame(form_container, bg="#ffffff")
        button_frame.pack(fill=tk.X, pady=20)
        
        ttk.Button(
            button_frame,
            text="Mark Attendance",
            command=self.mark_attendance,
            style="Primary.TButton"
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="Clear Form",
            command=self.clear_form,
            style="Secondary.TButton"
        ).pack(side=tk.LEFT, padx=5)
        
        # Right Panel - Records View
        right_panel = ttk.Frame(paned)
        paned.add(right_panel, weight=2)
        
        # Records header
        tk.Label(
            right_panel,
            text="Attendance Records",
            font=("Helvetica", 16, "bold"),
            fg="#1a73e8",
            bg="#ffffff",
            pady=10
        ).pack(fill=tk.X)
        
        # Create modern Treeview
        self.create_treeview(right_panel)
        
        # Load initial records
        self.load_records()
    
    def create_treeview(self, parent):
        # Create container for treeview
        tree_frame = ttk.Frame(parent)
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        # Configure columns
        columns = ("Date", "Name", "Email", "Phone", "Role", "Status")
        self.tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings",
            style="Modern.Treeview"
        )
        
        # Configure column widths and headings
        column_widths = {
            "Date": 100,
            "Name": 150,
            "Email": 200,
            "Phone": 100,
            "Role": 100,
            "Status": 100
        }
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=column_widths.get(col, 100))
        
        # Add scrollbars
        y_scroll = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        x_scroll = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
        
        # Pack elements
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        x_scroll.pack(side=tk.BOTTOM, fill=tk.X)
    
    def clear_form(self):
        for var in [self.name_var, self.email_var, self.phone_var, self.role_var, self.status_var]:
            var.set('')
    
    def validate_inputs(self):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, self.email_var.get()):
            messagebox.showerror("Error", "Please enter a valid email address")
            return False
        
        phone_pattern = r'^\d{10}$'
        if not re.match(phone_pattern, self.phone_var.get()):
            messagebox.showerror("Error", "Please enter a valid 10-digit phone number")
            return False
        
        if not all([
            self.name_var.get(),
            self.email_var.get(),
            self.phone_var.get(),
            self.role_var.get(),
            self.status_var.get()
        ]):
            messagebox.showerror("Error", "Please fill all fields")
            return False
        
        return True
    
    def mark_attendance(self):
        if not self.validate_inputs():
            return
        
        current_date = datetime.now().strftime('%Y-%m-%d')
        record = [
            current_date,
            self.name_var.get(),
            self.email_var.get(),
            self.phone_var.get(),
            self.role_var.get(),
            self.status_var.get()
        ]
        
        with open('attendance.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(record)
        
        self.clear_form()
        messagebox.showinfo("Success", "Attendance marked successfully!")
        self.load_records()
    
    def load_records(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        try:
            with open('attendance.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    self.tree.insert('', 'end', values=row)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernAttendanceSystem(root)
    root.mainloop()