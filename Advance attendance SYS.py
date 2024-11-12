import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import csv
import os
import re
import socket
import platform
from collections import Counter

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
        
        # System info variables
        self.timestamp_var = tk.StringVar()
        self.server_info_var = tk.StringVar()
        self.stats_var = tk.StringVar()
        
        # Update system info
        self.update_system_info()
        
        # Setup theme and UI
        self.setup_theme()
        self.setup_ui()
        
        # Start timestamp updates
        self.update_timestamp()
    
    def initialize_files(self):
        if not os.path.exists('attendance.csv'):
            with open('attendance.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Date', 'Time', 'Name', 'Email', 'Phone', 'Role', 'Status'])
    
    def update_system_info(self):
        # Get server information
        hostname = socket.gethostname()
        os_info = platform.system() + " " + platform.release()
        self.server_info_var.set(f"Server: {hostname} | OS: {os_info}")
        
        # Update attendance statistics
        self.update_statistics()
    
    def update_timestamp(self):
        # Update timestamp every second
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.timestamp_var.set(f"Current Time: {current_time}")
        self.root.after(1000, self.update_timestamp)
    
    def update_statistics(self):
        try:
            with open('attendance.csv', 'r') as file:
                reader = csv.DictReader(file)
                today = datetime.now().strftime('%Y-%m-%d')
                
                # Count today's attendance
                today_records = [row for row in reader if row['Date'] == today]
                status_counts = Counter(row['Status'] for row in today_records)
                role_counts = Counter(row['Role'] for row in today_records)
                
                stats = f"Today's Attendance: Present: {status_counts['Present']} | "
                stats += f"Absent: {status_counts['Absent']} | "
                stats += f"Late: {status_counts['Late']} | "
                stats += f"Students: {role_counts['Student']} | "
                stats += f"Teachers: {role_counts['Teacher']}"
                
                self.stats_var.set(stats)
        except FileNotFoundError:
            self.stats_var.set("No attendance records found")
    
    def setup_theme(self):
        style = ttk.Style()
        style.configure("MainFrame.TFrame", background="#f0f2f5")
        style.configure("Modern.TEntry", padding=10)
        style.configure("Primary.TButton", padding=15, font=("Helvetica", 10, "bold"))
        style.configure("Secondary.TButton", padding=15, font=("Helvetica", 10))
        style.configure("Modern.TCombobox", padding=5)
        style.configure("Modern.Treeview", rowheight=30, font=("Helvetica", 10))
        style.configure("Modern.Treeview.Heading", font=("Helvetica", 10, "bold"))
        style.configure("Info.TLabel", font=("Helvetica", 9), padding=5)
    
    def setup_ui(self):
        main_container = ttk.Frame(self.root, style="MainFrame.TFrame")
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # System Info Bar
        info_frame = tk.Frame(main_container, bg="#e3f2fd")
        info_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Timestamp
        ttk.Label(
            info_frame,
            textvariable=self.timestamp_var,
            style="Info.TLabel",
            background="#e3f2fd"
        ).pack(side=tk.LEFT, padx=10)
        
        # Server Info
        ttk.Label(
            info_frame,
            textvariable=self.server_info_var,
            style="Info.TLabel",
            background="#e3f2fd"
        ).pack(side=tk.RIGHT, padx=10)
        
        # Header Section
        header_frame = tk.Frame(main_container, bg="#1a73e8")
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
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
        
        # Statistics Bar
        stats_frame = tk.Frame(main_container, bg="#f5f5f5")
        stats_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(
            stats_frame,
            textvariable=self.stats_var,
            style="Info.TLabel",
            background="#f5f5f5"
        ).pack(pady=5)
        
        # Main Content
        paned = ttk.PanedWindow(main_container, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True)
        
        # Left Panel - Input Form
        left_panel = self.create_input_panel(paned)
        paned.add(left_panel, weight=1)
        
        # Right Panel - Records View
        right_panel = self.create_records_panel(paned)
        paned.add(right_panel, weight=2)
    
    def create_input_panel(self, parent):
        panel = ttk.Frame(parent)
        
        # Form header
        tk.Label(
            panel,
            text="Mark Attendance",
            font=("Helvetica", 16, "bold"),
            bg="#ffffff",
            fg="#1a73e8",
            pady=10
        ).pack(fill=tk.X)
        
        # Form container
        form_container = tk.Frame(panel, bg="#ffffff", padx=20, pady=20)
        form_container.pack(fill=tk.BOTH, expand=True)
        
        # Input fields
        fields = [
            ("Name", self.name_var, "entry"),
            ("Email", self.email_var, "entry"),
            ("Phone", self.phone_var, "entry"),
            ("Role", self.role_var, ["Student", "Teacher"]),
            ("Status", self.status_var, ["Present", "Absent", "Late"])
        ]
        
        for label_text, variable, field_type in fields:
            field_frame = tk.Frame(form_container, bg="#ffffff")
            field_frame.pack(fill=tk.X, pady=10)
            
            tk.Label(
                field_frame,
                text=label_text,
                font=("Helvetica", 10, "bold"),
                bg="#ffffff",
                fg="#666666"
            ).pack(anchor="w")
            
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
        
        # Buttons
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
        
        return panel
    
    def create_records_panel(self, parent):
        panel = ttk.Frame(parent)
        
        tk.Label(
            panel,
            text="Attendance Records",
            font=("Helvetica", 16, "bold"),
            fg="#1a73e8",
            bg="#ffffff",
            pady=10
        ).pack(fill=tk.X)
        
        # Create Treeview
        tree_frame = ttk.Frame(panel)
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        columns = ("Date", "Time", "Name", "Email", "Phone", "Role", "Status")
        self.tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show="headings",
            style="Modern.Treeview"
        )
        
        column_widths = {
            "Date": 100,
            "Time": 100,
            "Name": 150,
            "Email": 200,
            "Phone": 100,
            "Role": 100,
            "Status": 100
        }
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=column_widths.get(col, 100))
        
        # Scrollbars
        y_scroll = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        x_scroll = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        x_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Load initial records
        self.load_records()
        
        return panel
    
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
        
        current_datetime = datetime.now()
        record = [
            current_datetime.strftime('%Y-%m-%d'),
            current_datetime.strftime('%H:%M:%S'),
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
        self.update_statistics()
    
    def load_records(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        try:
            with open('attendance.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    self.tree.insert('', 0, values=row)  # Insert at top
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernAttendanceSystem(root)
    root.mainloop()