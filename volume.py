from pycaw.pycaw import AudioUtilities


devices = AudioUtilities.GetSpeakers()
volume = devices.EndpointVolume


def volume_up():
    current_volume = volume.GetMasterVolumeLevelScalar()
    new_volume = min(current_volume + 0.1, 1.0)
    volume.SetMasterVolumeLevelScalar(new_volume, None)


def volume_down():
    current_volume = volume.GetMasterVolumeLevelScalar()
    new_volume = max(current_volume - 0.1, 0.0)
    volume.SetMasterVolumeLevelScalar(new_volume, None)


def mute():
    volume.SetMute(1, None)


def unmute():
    volume.SetMute(0, None)

def get_volume():
    return int(volume.GetMasterVolumeLevelScalar() * 100)