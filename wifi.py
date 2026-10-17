import subprocess


def get_wifi_status():
    result = subprocess.run(
        ["powershell", "-Command", "Get-NetAdapter -Name 'Wi-Fi' -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Status"],
        capture_output=True,
        text=True
    )

    if "Up" in result.stdout:
        return True

    return False