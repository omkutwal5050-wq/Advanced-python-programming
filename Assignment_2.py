"""
Experiment 2: Advanced Class Concepts - Decorators and Magic Methods
Dynamic Report Generator - Menu Driven Version
"""


# Decorator for formatting text in bold (markdown-style ** **)
def bold_text(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"**{result}**"
    return wrapper


# Decorator for formatting text in uppercase, boxed style
def boxed_text(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        line = "=" * (len(result) + 4)
        return f"{line}\n| {result.upper()} |\n{line}"
    return wrapper


class Report:
    # Class variable for storing templates shared across all instances
    templates = {}

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def add_template(cls, name, template_func):
        """Add a template function to the class-level template registry."""
        cls.templates[name] = template_func
        print(f"Template '{name}' added.")

    @classmethod
    def get_template(cls, name):
        """Retrieve a template function from the registry."""
        return cls.templates.get(name)

    @classmethod
    def list_templates(cls):
        """List all available template names."""
        if not cls.templates:
            print("No templates available.")
        else:
            print("Available templates:", ", ".join(cls.templates.keys()))

    def __call__(self, template_name):
        """Generate the report using the given template name."""
        template_func = self.get_template(template_name)
        if template_func is None:
            return f"Template '{template_name}' not found."
        return template_func(self.title, self.content)

    def __str__(self):
        return f"Report(title='{self.title}', content='{self.content}')"


# ---------------- Built-in template functions ----------------
def simple_template(title, content):
    return f"{title}\n{'-' * len(title)}\n{content}"


@bold_text
def fancy_template(title, content):
    return f"{title}: {content}"


@boxed_text
def alert_template(title, content):
    return f"{title}: {content}"


def register_default_templates():
    Report.add_template("simple", simple_template)
    Report.add_template("fancy", fancy_template)
    Report.add_template("alert", alert_template)


def print_menu():
    print("\n===== DYNAMIC REPORT GENERATOR =====")
    print("1. Create a new report")
    print("2. Generate report using a template")
    print("3. List available templates")
    print("4. Show report details (__str__)")
    print("5. Exit")
    print("======================================")


def main():
    register_default_templates()
    current_report = None

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            title = input("Enter report title: ").strip()
            content = input("Enter report content: ").strip()
            current_report = Report(title, content)
            print(f"Report '{title}' created.")

        elif choice == "2":
            if current_report is None:
                print("No report created yet. Please create one first (option 1).")
                continue
            Report.list_templates()
            template_name = input("Enter template name to use: ").strip()
            # Calling the report instance directly invokes __call__
            output = current_report(template_name)
            print("\n--- Generated Report ---")
            print(output)

        elif choice == "3":
            Report.list_templates()

        elif choice == "4":
            if current_report is None:
                print("No report created yet. Please create one first (option 1).")
            else:
                print(str(current_report))

        elif choice == "5":
            print("Exiting the Report Generator. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()

