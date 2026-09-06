import json
import urllib.parse
import urllib.request
import tkinter as tk
from tkinter import messagebox, ttk

API_KEY = "cf9fb599cc3b4cc1b00162720261507"


def get_weather(event=None):
    city = city_entry.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    status_label.config(text="Fetching weather...", fg="#666666")
    root.update_idletasks()

    encoded_city = urllib.parse.quote(city)
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={encoded_city}&aqi=no"

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))

        loc = data["location"]
        curr = data["current"]

        city_name = f"{loc['name']}, {loc['country']}"
        condition = curr["condition"]["text"]
        temp_c = curr["temp_c"]
        temp_f = curr["temp_f"]
        humidity = curr["humidity"]
        wind_kph = curr["wind_kph"]
        wind_mph = curr["wind_mph"]
        pressure_mb = curr["pressure_mb"]
        last_updated = curr["last_updated"]

        # Update labels
        location_label.config(text=city_name)
        temp_label.config(text=f"{temp_c}°C / {temp_f}°F")
        condition_label.config(text=f"Condition: {condition}")
        humidity_label.config(text=f"Humidity: {humidity}%")
        wind_label.config(text=f"Wind: {wind_kph} km/h ({wind_mph} mph)")
        pressure_label.config(text=f"Pressure: {pressure_mb} mb")
        updated_label.config(text=f"Last updated: {last_updated}")
        status_label.config(text="")

    except urllib.error.HTTPError as e:
        status_label.config(text="")
        if e.code == 400:
            messagebox.showerror("Not Found", f"City '{city}' not found.")
        else:
            messagebox.showerror("Error", f"HTTP Error {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        status_label.config(text="")
        messagebox.showerror("Network Error", f"Failed to connect: {e.reason}")
    except Exception as e:
        status_label.config(text="")
        messagebox.showerror("Error", f"An unexpected error occurred:\n{e}")


# --- GUI Setup ---
root = tk.Tk()
root.title("Weather App")
root.geometry("420x460")
root.resizable(False, False)
root.configure(bg="#f4f6f9")

# Header Frame
header_frame = tk.Frame(root, bg="#1e3a8a", pady=15)
header_frame.pack(fill="x")

title_label = tk.Label(
    header_frame,
    text="☁ Weather App",
    font=("Helvetica", 18, "bold"),
    bg="#1e3a8a",
    fg="white",
)
title_label.pack()

# Input Frame
input_frame = tk.Frame(root, bg="#f4f6f9", pady=15)
input_frame.pack(padx=20, fill="x")

city_entry = tk.Entry(
    input_frame,
    font=("Helvetica", 13),
    width=22,
    relief="solid",
    bd=1,
)
city_entry.pack(side="left", padx=(0, 8), ipady=4)
city_entry.insert(0, "Melbourne")
city_entry.bind("<Return>", get_weather)

search_btn = tk.Button(
    input_frame,
    text="Search",
    font=("Helvetica", 11, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=12,
    pady=4,
    command=get_weather,
)
search_btn.pack(side="left")

# Status / Loading Label
status_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 10, "italic"),
    bg="#f4f6f9",
)
status_label.pack()

# Results Card
card_frame = tk.Frame(root, bg="white", bd=1, relief="solid")
card_frame.pack(padx=20, pady=5, fill="both", expand=True)

location_label = tk.Label(
    card_frame,
    text="--",
    font=("Helvetica", 16, "bold"),
    bg="white",
    fg="#1f2937",
    pady=8,
)
location_label.pack()

temp_label = tk.Label(
    card_frame,
    text="--°C / --°F",
    font=("Helvetica", 22, "bold"),
    bg="white",
    fg="#2563eb",
)
temp_label.pack(pady=4)

condition_label = tk.Label(
    card_frame,
    text="Condition: --",
    font=("Helvetica", 12),
    bg="white",
    fg="#4b5563",
)
condition_label.pack(pady=2)

details_frame = tk.Frame(card_frame, bg="white", pady=10)
details_frame.pack(fill="x", padx=15)

humidity_label = tk.Label(
    details_frame,
    text="Humidity: --%",
    font=("Helvetica", 11),
    bg="white",
    fg="#374151",
    anchor="w",
)
humidity_label.pack(fill="x", pady=2)

wind_label = tk.Label(
    details_frame,
    text="Wind: --",
    font=("Helvetica", 11),
    bg="white",
    fg="#374151",
    anchor="w",
)
wind_label.pack(fill="x", pady=2)

pressure_label = tk.Label(
    details_frame,
    text="Pressure: --",
    font=("Helvetica", 11),
    bg="white",
    fg="#374151",
    anchor="w",
)
pressure_label.pack(fill="x", pady=2)

updated_label = tk.Label(
    card_frame,
    text="Last updated: --",
    font=("Helvetica", 9, "italic"),
    bg="white",
    fg="#9ca3af",
    pady=8,
)
updated_label.pack(side="bottom")

# Fetch default city on start
root.after(100, get_weather)

root.mainloop()
