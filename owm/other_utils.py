import platform


def isWindowsSystem():
    return 'Windows' in platform.system()


def isLinuxSystem():
    return 'Linux' in platform.system()


if __name__ == '__main__':
    print(isWindowsSystem())
    print(isLinuxSystem())
