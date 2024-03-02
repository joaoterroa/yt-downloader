import shlex
import subprocess
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

app = tk.Tk()
app.title("YouTube Downloader")
app.geometry("500x250")

style = ttk.Style(app)
style.theme_use("clam")

url_frame = ttk.Frame(app, padding="10")
url_frame.pack(fill="x")

download_frame = ttk.Frame(app, padding="10")
download_frame.pack(fill="x", pady=10)

button_frame = ttk.Frame(app, padding="10")
button_frame.pack(fill="x")

progress_frame = ttk.Frame(app, padding="10")
progress_frame.pack(fill="x", pady=(0, 10))

ttk.Label(url_frame, text="YouTube URL:").pack(side="left", padx=(0, 10))
url_entry = ttk.Entry(url_frame, width=40)
url_entry.pack(side="left", expand=True, fill="x")

format_var = tk.StringVar(value="MP4")
ttk.Radiobutton(download_frame, text="MP4", variable=format_var, value="MP4").pack(
    side="left"
)
ttk.Radiobutton(download_frame, text="MP3", variable=format_var, value="MP3").pack(
    side="left", padx=20
)

download_button = ttk.Button(
    button_frame, text="Download", command=lambda: start_download_thread()
)
download_button.pack(side="left", padx=5)

reset_button = ttk.Button(button_frame, text="Reset", command=lambda: reset_app())
reset_button.pack(side="left", padx=5)

progress = ttk.Progressbar(progress_frame, mode="indeterminate", length=280)
progress.pack(fill="x", expand=True)


def start_download_thread():
    download_thread = threading.Thread(target=start_download)
    download_thread.start()


def download_video(url, download_folder):
    try:
        get_filename_command = f'yt-dlp --get-filename -o "{download_folder}/%(title)s.%(ext)s" --merge-output-format mp4 {url}'
        filename_result = subprocess.run(
            shlex.split(get_filename_command), stdout=subprocess.PIPE, check=True
        )
        filename = filename_result.stdout.strip().decode("utf-8", errors="replace")

        download_command = f'yt-dlp -o "{filename}" --merge-output-format mp4 {url}'
        subprocess.run(shlex.split(download_command), check=True)

        return filename, filename.split("/")[-1].rsplit(".", 1)[0]
    except subprocess.CalledProcessError as e:
        print(f"Error downloading video: {e}")
        return False, None


def download_audio(url, download_folder):
    try:
        download_command = f'yt-dlp --extract-audio --audio-format mp3 --audio-quality 0 -o "{download_folder}/%(title)s.%(ext)s" {url}'
        subprocess.run(shlex.split(download_command), check=True)

        get_filename_command = f'yt-dlp --get-filename -o "{download_folder}/%(title)s.%(ext)s" --audio-format mp3 {url}'
        filename_result = subprocess.run(
            shlex.split(get_filename_command), stdout=subprocess.PIPE, check=True
        )
        filename = filename_result.stdout.strip().decode("utf-8", errors="replace")

        title = filename.split("/")[-1].rsplit(".", 1)[0]

        return filename, title
    except subprocess.CalledProcessError as e:
        print(f"Error downloading audio: {e}")
        return False, None


def start_download():
    progress.pack(fill="x", expand=True)
    progress.start(10)
    url = url_entry.get()
    choice = format_var.get()
    download_folder = filedialog.askdirectory()

    if not download_folder:
        progress.stop()
        progress.pack_forget()
        messagebox.showerror("Error", "Please select a folder!")
        return

    try:
        if choice == "MP4":
            file_path, title = download_video(url, download_folder)
        else:
            file_path, title = download_audio(url, download_folder)
        messagebox.showinfo("Success", f"'{title}' has been downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

    finally:
        url_entry.delete(0, tk.END)
        progress.stop()
        progress.pack_forget()


def reset_app():
    url_entry.delete(0, tk.END)


app.mainloop()
