import subprocess

def change_windows_password(username, new_password):
    try:
        # Konstruera kommandot för att ändra lösenordet med Powershell
        powershell_cmd = f'net user {username} {new_password}'
        
        # Kör Powershell-kommandot med subprocess
        subprocess.run(['powershell.exe', '-Command', powershell_cmd], check=True)
        
        print(f"Lösenordet för användaren {username} har ändrats framgångsrikt!")
    except subprocess.CalledProcessError as e:
        print("Ett fel uppstod:", e)

if __name__ == "__main__":
    username = input("Ange användarnamnet för vilket du vill ändra lösenordet: ")
    new_password = input("Ange det nya lösenordet: ")
    
    change_windows_password(username, new_password)
