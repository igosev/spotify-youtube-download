# Spotify and YouTube mp3 download 
Based on [spotdl](https://github.com/spotDL/spotify-downloader). Created and tested on Windows only

## Installation
1. Install [spotdl](https://github.com/spotDL/spotify-downloader)
2. Rename .env.example to .env 
3. In .env change `OUTPUT_DIR` to directory you want
### Optional
For Windows users, you can generate run.bat file, to execute program simpler and faster.
1. In .env `PYTHON_DIR` and `SCRIPT_DIR`. 
   - `PYTHON_DIR` - path where your Python exe is stored\python.exe.
   - `SCRIPT_DIR` - path where your Python script is stored\live.py.
2. Execute `python create_run_bat.py`
## Usage
Run script `python live.py` or execute `run.bat` file.
- You can type song name. It will search in spotify and download mathing song. E.g. `hello`
- You can type multiple song names separated with comma. E.g. `adele hello, what is love`
- You can paste YouTube link to download it directly. `https://www.youtube.com/watch?v=LDU_Txk06tM`

All songs will be saved in `OUTPUT_DIR`. By default, it will be saved in same storage, where script is located.