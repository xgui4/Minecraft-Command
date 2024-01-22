import webbrowser
import subprocess
import config as Config

print("Java ou Bedrock (Windows 10/11 Seulement) ?")
 
user_input = input()

if (user_input == "Bedrock"):
    webbrowser.open("minecraft:")

Config.LAUNCHER_PATH = "C:\Program Files\Modrinth App\Modrinth App.exe"

if (user_input == "Java"):
    subprocess.run(Config.LAUNCHER_PATH)