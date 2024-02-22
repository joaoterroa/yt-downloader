# YouTube Downloader

A simple, user-friendly application to download YouTube videos as MP4 or just the audio as MP3, built with Python and `tkinter`.

## Prerequisites

Before running the application, ensure you have Python installed on your system. This application has been tested with Python 3.8 and above.

### Dependencies

- **yt-dlp**: A command-line program to download videos from YouTube and other video hosting sites.

## Installation

1. **Install yt-dlp**:

   Use pip to install `yt-dlp`. Open your terminal or command prompt and run the following command:

   ```
   pip install yt-dlp
   ```

2. **Download the Application**:

   Clone this repository or download the application code to your local machine.

## Running the Application

1. Navigate to the directory where you downloaded the application files.

2. Run the application using Python by executing the following command in your terminal or command prompt:

   ```
   python yt-downloader.py
   ```

   Replace `yt-downloader.py` with the path to the application script if you're in a different directory.

3. The application window will open. Enter the YouTube URL you wish to download, select the desired format (MP4 or MP3), and click "Download".

4. You will be prompted to select a download directory. Choose your desired location, and the download will begin.

5. Once the download is complete, a success message will appear.

## Features

- **Simple GUI**: Easy-to-use graphical interface for downloading videos.
- **MP4 and MP3 Downloads**: Option to download videos as MP4 files or just the audio as MP3 files.
- **Progress Bar**: Visual progress indication during the download process.

## Troubleshooting

If you encounter any issues with `yt-dlp`, ensure you have the latest version by running `pip install --upgrade yt-dlp`. For other issues, refer to the `yt-dlp` documentation or submit an issue on this repository.

## License

This project is open-source and available under the [MIT License](LICENSE.md).