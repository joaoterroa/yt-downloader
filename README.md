# YouTube Downloader

A simple, user-friendly application to download YouTube videos as MP4 or just the audio as MP3, built with Python and `tkinter`.

## Prerequisites

Before running the application, ensure you have Python installed on your system. This application has been tested with Python 3.8 and above.

### Dependencies

- **yt-dlp**: A command-line program to download videos from YouTube and other video hosting sites.
- **ffmpeg**: Required for processing video and audio files.

## Installation

1. **Install ffmpeg**:

   - Download the `ffmpeg` package from the official [ffmpeg website](https://ffmpeg.org/download.html).
   - Extract the contents of the downloaded file to `C:\ffmpeg`.
   - Ensure the `bin` folder within `C:\ffmpeg` is added to your system's PATH environment variable. This step is crucial for allowing the command line to recognize `ffmpeg` commands.

2. **Download yt-dlp**:

   - Visit the [yt-dlp release page](https://github.com/yt-dlp/yt-dlp/releases) and download the recommended release file for your platform.
   - Place the `yt-dlp` executable inside the `C:\ffmpeg\bin` folder. This setup allows `yt-dlp` to utilize `ffmpeg` for processing video and audio.

3. **Verify Installation**:

   - Open your terminal or command prompt and run the following command to check if `yt-dlp` is correctly installed:
     ```
     yt-dlp --version
     ```
   - If you see the version number of `yt-dlp`, the installation is successful.

4. **Download the Application**:

   - Clone this repository or download the application code to your local machine.

## Running the Application

1. Navigate to the directory where you downloaded the application files.

2. **Running from the Command Line**:

   - Run the application using Python by executing the following command in your terminal or command prompt:
     ```
     python yt-downloader.py
     ```
   - Replace `yt-downloader.py` with the path to the application script if you're in a different directory.

3. **Running by Double-Clicking**:

   - Alternatively, if your system is configured to execute Python scripts, you can run the application by double-clicking on the `yt-downloader.py` file. This method bypasses the need for command line interaction.

4. The application window will open. Enter the YouTube URL you wish to download, select the desired format (MP4 or MP3), and click "Download".

5. You will be prompted to select a download directory. Choose your desired location, and the download will begin.

6. Once the download is complete, a success message will appear.

## Features

- **Simple GUI**: Easy-to-use graphical interface for downloading videos.
- **MP4 and MP3 Downloads**: Option to download videos as MP4 files or just the audio as MP3 files.
- 
## Troubleshooting

If you encounter any issues with `yt-dlp`, ensure you have the latest version by downloading the latest release from the `yt-dlp` GitHub page. For issues related to `ffmpeg`, verify that it is correctly installed and added to your system's PATH. For other issues, refer to the `yt-dlp` documentation or submit an issue on this repository.

## License

This project is open-source and available under the [MIT License](LICENSE.md).