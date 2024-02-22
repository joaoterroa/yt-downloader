import shlex
import subprocess  # For calling FFmpeg for conversion
import threading  # For running download in a separate thread
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

app = tk.Tk()
app.title("YouTube Downloader")
app.geometry("500x250")  # Adjusted size to accommodate progress bar

# Style configuration
style = ttk.Style(app)
style.theme_use("clam")  # Use the 'clam' theme for a more modern look

# Create frames for better organization
url_frame = ttk.Frame(app, padding="10")
url_frame.pack(fill="x")

download_frame = ttk.Frame(app, padding="10")
download_frame.pack(fill="x", pady=10)

button_frame = ttk.Frame(app, padding="10")
button_frame.pack(fill="x")

progress_frame = ttk.Frame(app, padding="10")  # Frame for progress bar
progress_frame.pack(fill="x", pady=(0, 10))

# URL Entry
ttk.Label(url_frame, text="YouTube URL:").pack(side="left", padx=(0, 10))
url_entry = ttk.Entry(url_frame, width=40)
url_entry.pack(side="left", expand=True, fill="x")

# Download options (MP3/MP4)
format_var = tk.StringVar(value="MP4")
ttk.Radiobutton(download_frame, text="MP4", variable=format_var, value="MP4").pack(
    side="left"
)
ttk.Radiobutton(download_frame, text="MP3", variable=format_var, value="MP3").pack(
    side="left", padx=20
)

# Buttons
download_button = ttk.Button(
    button_frame, text="Download", command=lambda: start_download_thread()
)
download_button.pack(side="left", padx=5)

reset_button = ttk.Button(button_frame, text="Reset", command=lambda: reset_app())
reset_button.pack(side="left", padx=5)

# Progress bar
progress = ttk.Progressbar(progress_frame, mode="indeterminate", length=280)
progress.pack(fill="x", expand=True)


# Start download in a separate thread to keep the UI responsive
def start_download_thread():
    download_thread = threading.Thread(target=start_download)
    download_thread.start()


# Function to download video
# Enhanced download function for highest quality video
def download_video(url, download_folder):
    try:
        # First, get the filename yt-dlp will use
        get_filename_command = f'yt-dlp --get-filename -o "{download_folder}/%(title)s.%(ext)s" --merge-output-format mp4 {url}'
        filename_result = subprocess.run(
            shlex.split(get_filename_command), stdout=subprocess.PIPE, check=True
        )
        filename = filename_result.stdout.strip().decode("utf-8")

        # Now download the video
        download_command = f'yt-dlp -o "{filename}" --merge-output-format mp4 {url}'
        subprocess.run(shlex.split(download_command), check=True)

        # Assuming filename includes the full path
        return filename, filename.split("/")[-1].rsplit(".", 1)[
            0
        ]  # Return the full path and the title
    except subprocess.CalledProcessError as e:
        print(f"Error downloading video: {e}")
        return False, None  # Return False and None if download failed


# Function to download audio and convert to MP3 with FFmpeg
def download_audio(url, download_folder):
    try:
        # Command to download the best quality audio using yt-dlp and convert it to MP3
        download_command = f'yt-dlp --extract-audio --audio-format mp3 --audio-quality 0 -o "{download_folder}/%(title)s.%(ext)s" {url}'
        # Run the command
        subprocess.run(shlex.split(download_command), check=True)

        # Since yt-dlp names files based on the title, we need to get the filename
        get_filename_command = f'yt-dlp --get-filename -o "{download_folder}/%(title)s.%(ext)s" --audio-format mp3 {url}'
        filename_result = subprocess.run(
            shlex.split(get_filename_command), stdout=subprocess.PIPE, check=True
        )
        filename = filename_result.stdout.strip().decode("utf-8")

        # Assuming filename includes the full path
        title = filename.split("/")[-1].rsplit(".", 1)[
            0
        ]  # Extract the title from the filename

        return filename, title  # Return the full path and the title
    except subprocess.CalledProcessError as e:
        print(f"Error downloading audio: {e}")
        return False, None  # Return False and None if download failed


# Start download process
def start_download():
    # Ensure the progress bar is visible when download starts
    progress.pack(fill="x", expand=True)
    progress.start(10)  # Start the progress bar animation

    url = url_entry.get()
    choice = format_var.get()
    download_folder = filedialog.askdirectory()

    if not download_folder:
        progress.stop()  # Stop the progress bar if no folder selected
        progress.pack_forget()  # Hide the progress bar
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
        progress.stop()  # Stop the progress bar on completion or error
        progress.pack_forget()  # Hide the progress bar when done or on error


# Reset application state
def reset_app():
    url_entry.delete(0, tk.END)


app.mainloop()
