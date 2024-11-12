# simple_lms.py
from datetime import datetime
import re

class User:
    def __init__(self, user_id, name, role, email, password):
        self.user_id = user_id
        self.name = name
        self.role = role  # 'student' or 'instructor'
        self.email = email
        self.password = password
        self.enrolled_courses = []

class Course:
    def __init__(self, course_id, title, instructor):
        self.course_id = course_id
        self.title = title
        self.instructor = instructor
        self.students = []
        self.assignments = []
        self.materials = []

class Assignment:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.submissions = {}  # student_id: submission

class LearningManagementSystem:
    def __init__(self):
        self.users = {}
        self.courses = {}
        self.next_student_id = 1
        self.next_instructor_id = 1

    def generate_user_id(self, role):
        if role == 'student':
            user_id = f"S{str(self.next_student_id).zfill(3)}"
            self.next_student_id += 1
        else:
            user_id = f"I{str(self.next_instructor_id).zfill(3)}"
            self.next_instructor_id += 1
        return user_id

    def validate_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

    def validate_password(self, password):
        return len(password) >= 6

    def add_user(self, name, role, email, password):
        if not self.validate_email(email):
            return None, "Invalid email format"
        
        if not self.validate_password(password):
            return None, "Password must be at least 6 characters long"

        # Check if email already exists
        for user in self.users.values():
            if user.email == email:
                return None, "Email already exists"

        user_id = self.generate_user_id(role)
        user = User(user_id, name, role, email, password)
        self.users[user_id] = user
        return user, "User created successfully"

    # ... (previous methods remain the same)

class LMSInterface:
    def __init__(self):
        self.lms = LearningManagementSystem()

    def clear_screen(self):
        print("\n" * 50)

    def print_header(self, title):
        print("=" * 50)
        print(f"{title:^50}")
        print("=" * 50)

    def get_user_input(self):
        while True:
            print("\nAdd New User")
            print("-" * 20)
            
            # Get role
            print("\nSelect Role:")
            print("1. Student")
            print("2. Instructor")
            
            role_choice = input("Enter choice (1-2): ").strip()
            if role_choice not in ['1', '2']:
                print("Invalid choice. Please try again.")
                continue
            
            role = 'student' if role_choice == '1' else 'instructor'

            # Get name
            name = input("\nEnter full name: ").strip()
            if not name:
                print("Name cannot be empty. Please try again.")
                continue

            # Get email
            email = input("Enter email: ").strip().lower()

            # Get password
            password = input("Enter password (min 6 characters): ").strip()

            return role, name, email, password

    def add_user_interface(self):
        self.clear_screen()
        self.print_header("Add New User")

        role, name, email, password = self.get_user_input()
        user, message = self.lms.add_user(name, role, email, password)

        if user:
            print("\nUser added successfully!")
            print(f"User ID: {user.user_id}")
            print(f"Name: {user.name}")
            print(f"Role: {user.role}")
            print(f"Email: {user.email}")
        else:
            print(f"\nError: {message}")

        input("\nPress Enter to continue...")

    def display_all_users(self):
        self.clear_screen()
        self.print_header("All Users")

        if not self.lms.users:
            print("\nNo users found in the system.")
        else:
            print("\nStudents:")
            print("-" * 60)
            for user in self.lms.users.values():
                if user.role == 'student':
                    print(f"ID: {user.user_id} | Name: {user.name:<20} | Email: {user.email}")
            
            print("\nInstructors:")
            print("-" * 60)
            for user in self.lms.users.values():
                if user.role == 'instructor':
                    print(f"ID: {user.user_id} | Name: {user.name:<20} | Email: {user.email}")

        input("\nPress Enter to continue...")

    def main_menu(self):
        while True:
            self.clear_screen()
            self.print_header("LMS Main Menu")
            
            print("\n1. Add New User")
            print("2. Display All Users")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                self.add_user_interface()
            elif choice == '2':
                self.display_all_users()
            elif choice == '3':
                print("\nThank you for using the LMS. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")
                input("Press Enter to continue...")

def main():
    interface = LMSInterface()
    interface.main_menu()

if __name__ == "__main__":
    main()