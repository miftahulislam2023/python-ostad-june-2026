import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class BmiBmrCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI & BMR Calculator")
        self.root.geometry("480x600")
        self.root.resizable(False, False)

        # Style configuration
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Color Palette
        self.primary_color = "#3a86ff"
        self.secondary_color = "#8338ec"
        self.bg_color = "#f8f9fa"
        self.text_color = "#212529"

        self.root.configure(bg=self.bg_color)

        # Configure base styles
        self.style.configure(
            ".",
            background=self.bg_color,
            foreground=self.text_color,
            font=("Helvetica", 10),
        )
        self.style.configure("TLabel", background=self.bg_color, foreground=self.text_color)
        self.style.configure(
            "Header.TLabel",
            font=("Helvetica", 16, "bold"),
            foreground=self.primary_color,
        )
        self.style.configure(
            "SubHeader.TLabel",
            font=("Helvetica", 11, "italic"),
            foreground="#6c757d",
        )
        self.style.configure(
            "Result.TLabel",
            font=("Helvetica", 12, "bold"),
            foreground=self.secondary_color,
        )
        self.style.configure(
            "Category.TLabel",
            font=("Helvetica", 11, "bold"),
            foreground=self.text_color,
        )
        self.style.configure(
            "Calculate.TButton",
            font=("Helvetica", 11, "bold"),
            background=self.primary_color,
            foreground="white",
        )
        self.style.map("Calculate.TButton", background=[("active", "#2a6ed2")])

        # Dynamic styles for BMI categories
        self.style.configure("Underweight.Category.TLabel", foreground="#17a2b8")
        self.style.configure("Normal.Category.TLabel", foreground="#28a745")
        self.style.configure("Overweight.Category.TLabel", foreground="#ffc107")
        self.style.configure("Obese.Category.TLabel", foreground="#dc3545")

        # Title Header
        header_frame = ttk.Frame(self.root, padding=15)
        header_frame.pack(fill="x")

        title_label = ttk.Label(
            header_frame,
            text="Fitness Calculator",
            style="Header.TLabel",
        )
        title_label.pack(anchor="center")

        subtitle_label = ttk.Label(
            header_frame,
            text="Calculate your Body Mass Index (BMI) & Basal Metabolic Rate (BMR)",
            style="SubHeader.TLabel",
            wraplength=400,
            justify="center",
        )
        subtitle_label.pack(anchor="center", pady=(5, 0))

        # Notebook (Tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        # BMI Tab
        self.bmi_tab = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(self.bmi_tab, text=" BMI Calculator ")
        self.setup_bmi_tab()

        # BMR Tab
        self.bmr_tab = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(self.bmr_tab, text=" BMR Calculator ")
        self.setup_bmr_tab()

    def setup_bmi_tab(self):
        # Unit selection
        ttk.Label(
            self.bmi_tab,
            text="Choose Unit System:",
            font=("Helvetica", 10, "bold"),
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

        self.bmi_unit_var = tk.StringVar(value="Metric")

        metric_rb = ttk.Radiobutton(
            self.bmi_tab,
            text="Metric (kg, cm)",
            variable=self.bmi_unit_var,
            value="Metric",
            command=self.update_bmi_labels,
        )
        metric_rb.grid(row=1, column=0, sticky="w", pady=5)

        imperial_rb = ttk.Radiobutton(
            self.bmi_tab,
            text="Imperial (lbs, inches)",
            variable=self.bmi_unit_var,
            value="Imperial",
            command=self.update_bmi_labels,
        )
        imperial_rb.grid(row=1, column=1, sticky="w", pady=5)

        # Input variables
        self.bmi_weight_label = ttk.Label(self.bmi_tab, text="Weight (kg):")
        self.bmi_weight_label.grid(row=2, column=0, sticky="w", pady=10)
        self.bmi_weight_entry = ttk.Entry(self.bmi_tab, width=15)
        self.bmi_weight_entry.grid(row=2, column=1, sticky="w", pady=10)

        self.bmi_height_label = ttk.Label(self.bmi_tab, text="Height (cm):")
        self.bmi_height_label.grid(row=3, column=0, sticky="w", pady=10)
        self.bmi_height_entry = ttk.Entry(self.bmi_tab, width=15)
        self.bmi_height_entry.grid(row=3, column=1, sticky="w", pady=10)

        # Calculate button
        calc_btn = ttk.Button(
            self.bmi_tab,
            text="Calculate BMI",
            style="Calculate.TButton",
            command=self.calculate_bmi,
        )
        calc_btn.grid(row=4, column=0, columnspan=2, pady=20, ipady=5)

        # Result display
        self.bmi_result_frame = ttk.LabelFrame(
            self.bmi_tab,
            text=" Your Results ",
            padding=10,
        )
        self.bmi_result_frame.grid(
            row=5, column=0, columnspan=2, sticky="nsew", pady=10
        )
        self.bmi_tab.rowconfigure(5, weight=1)
        self.bmi_tab.columnconfigure(0, weight=1)
        self.bmi_tab.columnconfigure(1, weight=1)

        self.bmi_val_label = ttk.Label(
            self.bmi_result_frame,
            text="BMI: --",
            style="Result.TLabel",
        )
        self.bmi_val_label.pack(anchor="w", pady=5)

        self.bmi_cat_label = ttk.Label(
            self.bmi_result_frame,
            text="Category: --",
            style="Category.TLabel",
        )
        self.bmi_cat_label.pack(anchor="w", pady=5)

    def update_bmi_labels(self):
        if self.bmi_unit_var.get() == "Metric":
            self.bmi_weight_label.configure(text="Weight (kg):")
            self.bmi_height_label.configure(text="Height (cm):")
        else:
            self.bmi_weight_label.configure(text="Weight (lbs):")
            self.bmi_height_label.configure(text="Height (inches):")

    def calculate_bmi(self):
        try:
            weight = float(self.bmi_weight_entry.get())
            height = float(self.bmi_height_entry.get())
            if weight <= 0 or height <= 0:
                raise ValueError("Values must be positive numbers.")
        except ValueError:
            messagebox.showerror(
                "Input Error",
                "Please enter valid positive numbers for weight and height.",
            )
            return

        if self.bmi_unit_var.get() == "Metric":
            height_m = height / 100.0
            bmi = weight / (height_m**2)
        else:
            bmi = (weight / (height**2)) * 703

        if bmi < 18.5:
            category = "Underweight"
            style_name = "Underweight.Category.TLabel"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
            style_name = "Normal.Category.TLabel"
        elif 24.9 <= bmi < 29.9:
            category = "Overweight"
            style_name = "Overweight.Category.TLabel"
        else:
            category = "Obesity"
            style_name = "Obese.Category.TLabel"

        self.bmi_val_label.configure(text=f"BMI: {bmi:.2f}")
        self.bmi_cat_label.configure(
            text=f"Category: {category}",
            style=style_name,
        )

    def setup_bmr_tab(self):
        # Unit selection
        ttk.Label(
            self.bmr_tab,
            text="Choose Unit System:",
            font=("Helvetica", 10, "bold"),
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

        self.bmr_unit_var = tk.StringVar(value="Metric")

        metric_rb = ttk.Radiobutton(
            self.bmr_tab,
            text="Metric (kg, cm)",
            variable=self.bmr_unit_var,
            value="Metric",
            command=self.update_bmr_labels,
        )
        metric_rb.grid(row=1, column=0, sticky="w", pady=5)

        imperial_rb = ttk.Radiobutton(
            self.bmr_tab,
            text="Imperial (lbs, inches)",
            variable=self.bmr_unit_var,
            value="Imperial",
            command=self.update_bmr_labels,
        )
        imperial_rb.grid(row=1, column=1, sticky="w", pady=5)

        # Gender selection
        ttk.Label(self.bmr_tab, text="Gender:").grid(
            row=2, column=0, sticky="w", pady=10
        )
        self.bmr_gender_var = tk.StringVar(value="Male")
        gender_male = ttk.Radiobutton(
            self.bmr_tab,
            text="Male",
            variable=self.bmr_gender_var,
            value="Male",
        )
        gender_male.grid(row=2, column=1, sticky="w", pady=10)
        gender_female = ttk.Radiobutton(
            self.bmr_tab,
            text="Female",
            variable=self.bmr_gender_var,
            value="Female",
        )
        gender_female.grid(row=2, column=1, sticky="e", pady=10)

        # Input variables
        self.bmr_weight_label = ttk.Label(self.bmr_tab, text="Weight (kg):")
        self.bmr_weight_label.grid(row=3, column=0, sticky="w", pady=10)
        self.bmr_weight_entry = ttk.Entry(self.bmr_tab, width=15)
        self.bmr_weight_entry.grid(row=3, column=1, sticky="w", pady=10)

        self.bmr_height_label = ttk.Label(self.bmr_tab, text="Height (cm):")
        self.bmr_height_label.grid(row=4, column=0, sticky="w", pady=10)
        self.bmr_height_entry = ttk.Entry(self.bmr_tab, width=15)
        self.bmr_height_entry.grid(row=4, column=1, sticky="w", pady=10)

        ttk.Label(self.bmr_tab, text="Age (years):").grid(
            row=5, column=0, sticky="w", pady=10
        )
        self.bmr_age_entry = ttk.Entry(self.bmr_tab, width=15)
        self.bmr_age_entry.grid(row=5, column=1, sticky="w", pady=10)

        # Calculate button
        calc_btn = ttk.Button(
            self.bmr_tab,
            text="Calculate BMR",
            style="Calculate.TButton",
            command=self.calculate_bmr,
        )
        calc_btn.grid(row=6, column=0, columnspan=2, pady=20, ipady=5)

        # Result display
        self.bmr_result_frame = ttk.LabelFrame(
            self.bmr_tab,
            text=" Your Results ",
            padding=10,
        )
        self.bmr_result_frame.grid(
            row=7, column=0, columnspan=2, sticky="nsew", pady=10
        )
        self.bmr_tab.rowconfigure(7, weight=1)
        self.bmr_tab.columnconfigure(0, weight=1)
        self.bmr_tab.columnconfigure(1, weight=1)

        self.bmr_val_label = ttk.Label(
            self.bmr_result_frame,
            text="BMR: -- kcal/day",
            style="Result.TLabel",
        )
        self.bmr_val_label.pack(anchor="w", pady=5)

        self.bmr_info_label = ttk.Label(
            self.bmr_result_frame,
            text="BMR represents the minimum energy required to keep your body functioning at rest.",
            wraplength=380,
            justify="left",
            font=("Helvetica", 9, "italic"),
        )
        self.bmr_info_label.pack(anchor="w", pady=(5, 0))

    def update_bmr_labels(self):
        if self.bmr_unit_var.get() == "Metric":
            self.bmr_weight_label.configure(text="Weight (kg):")
            self.bmr_height_label.configure(text="Height (cm):")
        else:
            self.bmr_weight_label.configure(text="Weight (lbs):")
            self.bmr_height_label.configure(text="Height (inches):")

    def calculate_bmr(self):
        try:
            weight = float(self.bmr_weight_entry.get())
            height = float(self.bmr_height_entry.get())
            age = float(self.bmr_age_entry.get())
            if weight <= 0 or height <= 0 or age <= 0:
                raise ValueError("Values must be positive numbers.")
        except ValueError:
            messagebox.showerror(
                "Input Error",
                "Please enter valid positive numbers for weight, height, and age.",
            )
            return

        if self.bmr_unit_var.get() == "Imperial":
            weight_kg = weight * 0.45359237
            height_cm = height * 2.54
        else:
            weight_kg = weight
            height_cm = height

        # Mifflin-St Jeor Equation
        if self.bmr_gender_var.get() == "Male":
            bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
        else:
            bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

        self.bmr_val_label.configure(text=f"BMR: {bmr:.1f} kcal/day")


if __name__ == "__main__":
    root = tk.Tk()
    app = BmiBmrCalculator(root)
    root.mainloop()