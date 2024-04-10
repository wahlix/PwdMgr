Sure, here is the updated content for your README.md file:

```markdown
# README.md

## PwdMgr.py

This Python script is used to change the password of a user on a Windows system.

### How it works

The script uses the `subprocess` module to run a Powershell command that changes the user's password. The command is constructed using the `net user` command, which is a native Windows command used for managing user accounts.

### Usage

The script prompts the user for a username and a new password. These inputs are then passed to the `change_windows_password` function.

```python
if __name__ == "__main__":
    username = input("Ange användarnamnet för vilket du vill ändra lösenordet: ")
    new_password = input("Ange det nya lösenordet: ")
    
    change_windows_password(username, new_password)
```

### Error Handling

If an error occurs while running the Powershell command, the script will catch the `subprocess.CalledProcessError` exception and print an error message.

```python
try:
    subprocess.run(['powershell.exe', '-Command', powershell_cmd], check=True)
except subprocess.CalledProcessError as e:
    print("Ett fel uppstod:", e)
```

### Note

This script should be run with administrative privileges as changing user passwords is a system-level operation.
```
