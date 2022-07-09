import os
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()
    runBat = open(os.getcwd() + '/run.bat', 'w')
    runBat.write('@echo off\n' + '"' + os.getenv('python_dir') + '" "' + os.getenv('script_dir') + '"')
    runBat.close()
