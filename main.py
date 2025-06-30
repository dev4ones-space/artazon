# # Variables & Imports
import os, platform, subprocess, time, inspect  # Basic imports (do not requires installing modules from pip and like that)
class main:
    # Modules (def, or default variables like SupportedPlatoforms)
    SupportedPlatoforms = ['Darwin', 'Linux']
    UnsupportedOS = False
    IsPixel = False
    # Classess
    class version:
        VersionsMap = {
            1.0: 'Cyclizar'
        }
        Version = 1.0
        Codename = VersionsMap.get(Version)
        VersionType = 'Release'  # Alpha, Release, Beta
        Build = f'{str(Version).replace('.', '')}{VersionType[0]}1'
        all = f'Version: {Version}\nVersion Type: {VersionType}\nVersion Codename: {Codename}\nBuild: {Build}'
    class activities:
        def UnsupportedOS():  # not supported OS prompt
            if input('Warning: This "app" was made for Unix-like systems (Linux, macOS), and not supported on your OS. \n  Enter "continue" to proceed with current OS (this can cause your device to not work properly)\n\n>>> ') == 'continue': main.UnsupportedOS = True
            else: raise RuntimeError('Unsupported OS')
        def CheckDevice():  # checks for any device; returns 0 if device/s is attached, -1 if not any
            cache = str(subprocess.check_output('adb devices', shell=True).decode('utf-8'))
            if cache.replace('\n', '') == 'List of devices attached': return -1
            else: return 0
        def DeviceInfoBasic(out_model=False):  # out_model only for LogcatWrite() to get a model name
            Model = subprocess.check_output('adb shell getprop ro.product.model', shell=True).decode('utf-8').replace('\n', '')
            if out_model == True: return Model
            Manufacter = subprocess.check_output('adb shell getprop ro.product.manufacturer', shell=True).decode('utf-8').replace('\n', '')
            AndroidVersion = subprocess.check_output('adb shell getprop ro.build.version.release', shell=True).decode('utf-8').replace('\n', '')
            SDK = subprocess.check_output('adb shell getprop ro.build.version.sdk', shell=True).decode('utf-8').replace('\n', '')
            DeviceFingerprint = subprocess.check_output('adb shell getprop ro.build.fingerprint', shell=True).decode('utf-8').replace('\n', '')
            SerialNumber = subprocess.check_output('adb shell getprop ro.serialno', shell=True).decode('utf-8').replace('\n', '')
            print(f'Model: {Model}\nManufacter: {Manufacter}\nFingerprint: {DeviceFingerprint}\nAndroid Version: {AndroidVersion}\nSDK: {SDK}\nSerial Number: {SerialNumber}')
        def NoDevice(): print('No device attached, press enter to exit')  # No device message
        def Netstat(): print(f'{subprocess.check_output('adb shell netstat', shell=True).decode('utf-8')}\n\npress enter to exit')
        def Logcat(): os.system('adb logcat')  # Just adb logcat
        def LogcatWrite():  # Menu 2, option 2: Writes logcat into home dir by file: {model name, ex. Pixel7}.log
            WhereToWrite = subprocess.check_output('cd ~/ && pwd', shell=True).decode('utf-8').replace('\n', '')
            cache = f'{WhereToWrite}/{subprocess.check_output('adb shell getprop ro.product.model', shell=True).decode('utf-8').replace('\n', '').replace(' ', '')}.log'
            print(f'Writing device logcat in {cache}.\nUse CTRL+C to stop')
            os.system(f'adb logcat > {cache}')
            input('\nProcess ended, press enter to exit')
        def DetectGooglePixel():  # Very simple Google Pixel check, but can by easly broken by spoffing model name or fingerprint (fingerprints is not checking, may be added in newer versions, also mb spoofed trough MagiskHide Props or like that)
            print('Detecting if device Google Pixel or not...')
            if main.activities.DeviceInfoBasic(True).find('Pixel') != -1: 
                print('Detected Google Pixel')
                return 1
            else: 
                print('Not detected any Pixel phone, proceeding with default flash')
                return 0
        class help:
            def menu4(): input('Shorcuts: \n  ## - will change for /storage/emulated/0\n  ##d - will change for /storage/emulated/0/Download\n\npress enter to exit')  # Push/Pull help prompt
        def __GetAllActivities__(): # First ChatGPT func
            funcs = [name for name, func in inspect.getmembers(main.activities, inspect.isfunction)]
            funcs.append('__GetAllActivities__')
            return funcs
        def __RunActivity__(name, *args, **kwargs): # Second ChatGPT func
            funcs = dict(inspect.getmembers(main.activities, inspect.isfunction))
            if name not in funcs:
                raise ValueError(f"Activity '{name}' not found.")
            return funcs[name](*args, **kwargs)
CurrentOS = platform.system()
def cls(): os.system('clear')  # Clears the screen, by now only for Unix-like systems
# # Some pre-run things (like check for platform)
if __name__ != '__main__': raise RuntimeError('Running in import mode is not supported')
if CurrentOS not in main.SupportedPlatoforms: main.activities.UnsupportedOS()
# Main
while True: 
    try:
        cls()
        cache = input(f'Artazon Menu\n\n\n 1: Device info\n 2: Logcat\n 3: Flash\n 4: File/Dir transfer\n\ni: dev settings\n\nSelect: ')
        cls()
        if cache.find('1') != -1:
            cache = input(f'Device Info\n\n\n 1: Default Info\n 2: Netstat (Active Internet Connections)\n\nSelect: ')
            cls()
            if cache.find('1') != -1:
                if main.activities.CheckDevice() == 0: main.activities.DeviceInfoBasic()
                else: main.activities.NoDevice()
                input()
            elif cache.find('2') != -1:
                if main.activities.CheckDevice() == 0: main.activities.Netstat()
                else: main.activities.NoDevice()
                input()
            else: input('Wrong option!')
        elif cache.find('2') != -1:
            cache = input(f'Logcat\n\n\n 1: Live logcat\n 2: Write live logcat into file\n\nSelect: ')
            cls()
            if cache.find('1') != -1:
                if main.activities.CheckDevice() == 0: main.activities.Logcat()
                else: main.activities.NoDevice()
            elif cache.find('2') != -1:
                if main.activities.CheckDevice() == 0: main.activities.LogcatWrite()
                else: main.activities.NoDevice()
            else: input('Wrong option!')
        elif cache.find('3') != -1:
            cache = input(f'Flash\n\n\n 1: Flash boot (for root)\n 2: Flash OS (by-vendor package)\n 3: Flash manually\n\nSelect: ')
            cls()
            if cache.find('1') != -1: # Function last update: 10B1
                if main.activities.DetectGooglePixel() == 1: main.IsPixel = True
                else: main.IsPixel = False
                input('Boot (init_boot if Pixel) image to flash: ')
                cls()
                print('Started flashing...')
                if main.IsPixel == True: cmd = f'init_boot init_boot.img'
                else: cmd = f'boot boot.img'
                if int(os.system(f'fastboot flash {cmd}')) != 0: print('Flash failed...\n\npress enter to exit')
                else: input('Done! Press enter to exit')
            elif cache.find('2') != -1: # Function last update: 10B1
                cache = input('OS Install Package (by-vendor, enter "help", to get more info): ')
                if cache == 'help': 
                    input('By-vendor OS install package must contain "flash-all.sh", which automatically flashes OS.\nThis .zip file is made by manufacter and can non-exist for your phone\n\npress enter to continue')
                    cache = input('OS Install Package: ')
                cache1 = input('Folder name after unpacking (enter "same" to use the same folder name): ')
                cls()
                if main.activities.CheckDevice() != 0: main.activities.NoDevice()
                print('Unzipping package...')
                if int(os.system(f'unzip {cache}')) != 0: input('error: package is corrupted or was not found\n\npress enter to exit')
                else: 
                    print('Unpacked successfuly\nWill proceed in 30 seconds, or do CTRL+C to continue right now\n\nMake sure phone bootloader is unlocked, and it in bootloader/fastboot right now (and connected to machine)')
                    try: time.sleep(30)
                    except KeyboardInterrupt: pass
                    if int(os.system(f'cd {cache1} && sh flash-all.sh')) != 0: input('Script failed, or was not found (if that, check folder unpacked name)\n\npress enter to exit')
                    else: input('Script is done, press enter to exit')
            elif cache.find('3') != -1: # Function last update: 10B1
                boot = input('boot path: ')
                init_boot = input('init_boot path: ')
                vendor = input('vendor path: ')
                recovery = input('recovery path: ')
                dtbo = input('dtbo path: ')
                vbmeta = input('vbmeta path: ')
                system = input('system path: ')
                vendor_boot = input('vendor_boot path: ')
                vendor_kernel_boot = input('vendor_kernel_boot path: ')
                cls()
                print('Flashing all...')
                os.system(f'fastboot flash boot {boot}')
                os.system(f'fastboot flash init_boot {init_boot}')
                os.system(f'fastboot flash vendor {vendor}')
                os.system(f'fastboot flash recovery {recovery}')
                os.system(f'fastboot flash dtbo {dtbo}')
                os.system(f'fastboot flash vbmeta {vbmeta}')
                os.system(f'fastboot flash system {system}')
                os.system(f'fastboot flash vendor_boot {vendor_boot}')
                os.system(f'fastboot flash vendor_kernel_boot {vendor_kernel_boot}')
                input('Done!\n\npress enter to exit')
            else: input('Wrong option!')
        elif cache.find('4') != -1: # Function last update: 10B2
            cache = input('File/Dir transfer\n\n\n 1: Push to device\n 2: Pull from device\n 3: Terminal explorer (term-e with mods) *Will be soon\n\nSelect: ')
            cls()
            if cache.find('1') != -1: 
                cache = input('File/Dir to push: ')
                cache1 = input('Push to (%h for 0/, %d for 0/Download): ')
                if cache1 == '%h': cache1 = '/storage/emulated/0'
                if cache1 == '%d': cache1 = '/storage/emulated/0/Download'
                cls()
                print('Pushing...')
                if main.activities.CheckDevice() != 0: main.activities.NoDevice()
                else: 
                    if int(os.system(f'adb push {cache} {cache1}')) != 0: input('Push failed...\n\npress enter to exit')
                    else: input('Push is done!\n\npress enter to exit')
            elif cache.find('2') != -1:
                cache = input('Pull from device (%h for 0/, %d for 0/Download): ')
                cache1 = input('Pull to: ')
                if cache.find('%h') != -1: cache = cache.replace('%h', '/storage/emulated/0')
                if cache.find('%d') != -1: cache = cache.replace('%d', '/storage/emulated/0/Download')
                cls()
                print('Pulling...')
                if main.activities.CheckDevice() != 0: main.activities.NoDevice()
                else: 
                    if int(os.system(f'adb pull {cache} {cache1}')) != 0: input('Pull failed...\n\npress enter to exit')
                    else: input('Pull is done!\n\npress enter to exit')
        elif cache.find('i') != -1: # Function last update: 10R1
            cache = input('Developer Settings\n\n\n 1: List activities\n 2: Run activity\n 3: App info\n\nSelect: ')
            cls()
            if cache.find('1') != -1: input(f'{'\n'.join(main.activities.__GetAllActivities__()).replace('__GetAllActivities__', '')}press enter to exit')
            elif cache.find('2') != -1: 
                main.activities.__RunActivity__(input('Activity: '))
                input('\n\npress enter to exit')
            elif cache.find('3') != -1: input(f'{main.version.all}\n\npress enter to exit')
        else: input('Wrong option!')
    except KeyboardInterrupt: 
        cls()
        exit()
    except: # Turned off for debugging if beta or alpha, release - just except for basic errors
        cls() 
        input('An unknown error occured, press enter to get back to main menu')