import os.path

import chromedriver_autoinstaller # selenium과 함께 설치?
import platform


def install_chromedriver():
    """
    실행시키는 파일 기준으로 상대경로가 결정된다.
    예를 들어 ./Darwing/경로 지정후 01_naver_api/04_webtoons.py 에서 실행시
        01_naver_api/Darwin/112/chromedriver 결로에 설치된다.

    :return:
    """
    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split(".")[0]
    print(chrome_ver)

    system = platform.system()
    print(system)

    dir = f'../chromedriver/{system}/{chrome_ver}/'
    path = None
    if os.path.exists(dir):
        print('Chromedriver Already Installed!')
    else:
        try:
            os.makedirs(f'../chromedriver/{system}') # 디렉토리 먼저 생성
            path = chromedriver_autoinstaller.install(False, f'../chromedriver/{system}')  # cwd=False 지정한 디렉토리에 설치 | cwd=True 현재 디렉토리에 설치
            print('Chromedriver Installed Completely!')
        except Exception as e:
            print('Chromedriver Installation Error : ', e)

    return f'{path}'

install_chromedriver() # import시 바로 실행


def get_chromedriver_path():
    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split(".")[0]
    system = platform.system()
    dir = f'../chromedriver/{system}/{chrome_ver}/'
    filename = 'chromedriver.exe' if system == 'Windows' else 'chromedriver'
    return f'{dir}/{filename}'