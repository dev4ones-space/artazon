# # Variables & Imports
import os, platform, subprocess, time, inspect  # Basic imports (do not requires installing modules from pip and like that)
class main:
    # Modules (def, or default variables like SupportedPlatoforms)
    SupportedPlatforms = ['Darwin', 'Linux']
    IsPixel = False
    ExtraModulesImported = True
    # Classess
    class version:
        VersionsMap = {
            1.0: 'Cyclizar',
            1.1: 'Combee'
        }
        Version = 1.1
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
        def ReturnADB_EXP(): return """import os, subprocess\nversion = '1.1-adb_ver'\ndef cls(): os.system('clear')\nclass AppVariables: ShowInMainInput = 'cd '\ncurrent_dir = '/'\ncomment = '''\n'''\nwhile True:\n    try:\n        ShowInMainInput = f'cd {current_dir}/'\n        cls()\n        try: print(f'''{subprocess.check_output(f'adb shell ls "{current_dir}"', shell=True).decode('ascii').replace('''\n''', ' | ')}\n\n\nCurrent Directory: {current_dir}\n{comment}\n''')\n        except: \n            input('No device attached, reconnect it or check adb access to it')\n            raise ValueError\n        cache = input(ShowInMainInput)\n        if comment != '''\n''': comment = '''\n'''\n        if cache == '': pass\n        elif cache[0] == '^': \n            cache = cache.replace('^', '')\n            print('Running the sh command on a device...')\n            os.system(f'adb shell sh {cache}')\n        elif cache == '' or cache == ' ': comment = '''\nSymbols entered are not cd'able!\n'''\n        elif current_dir == '/' and cache == '/': comment = "Can't cd into /, when alredy in!" \n        elif int(os.system(f'adb shell cd "{current_dir}/{cache}"')) == 512: comment = 'This directory does not exist!' \n        elif cache == '..':\n            cache = str(subprocess.check_output(f'adb shell "cd {current_dir}/.. && pwd"', shell=True).decode('ascii').replace('''\n''', ''))\n            if cache == '/' and current_dir == '/': current_dir = '/'\n            elif cache == '//' and current_dir == '/': current_dir = '/'\n            else: current_dir = cache\n        elif cache == '$help': \n            cls()\n            input('''Commands:\n\n$help - Shows this text\n^{zsh command} - It will run zsh command (without ^ on device)\n\npress enter to exit''')\n        else:\n            if current_dir == '/': current_dir = str(subprocess.check_output(f'adb shell "cd /{cache} && pwd"', shell=True).decode('ascii').replace('''\n''', ''))\n            else: current_dir = str(subprocess.check_output(f'adb shell "cd {current_dir}/{cache} && pwd"', shell=True).decode('ascii').replace('''\n''', ''))\n    except KeyboardInterrupt: \n        cls()\n        break\n    except ValueError: pass\n    except EOFError: comment = 'Got unknown error'"""
        def DetectGooglePixel():  # Very simple Google Pixel check, but can by easly broken by spoffing model name or fingerprint (fingerprints is not checking, may be added in newer versions, also mb spoofed trough MagiskHide Props or like that)
            print('Detecting if device Google Pixel or not...')
            if main.activities.DeviceInfoBasic(True).find('Pixel') != -1:  # Does find it by searching a "Pixel" in model
                print('Detected Google Pixel')
                return 1
            else: 
                print('Not detected any Pixel phone, proceeding with default flash')
                return 0
        def ListPackages():  # Just listing all packages trough pm
            os.system('adb shell pm list packages')
            input('\n\npress enter to exit')
        def Install(apps):  # Simple adb install command
            os.system(f'adb install {apps}')
        def Remove(package):  # Also simple adb remove
            os.system(f'adb uninstall {package}')
        def RecordScreen():  # Will return 0 if record successful, 1 if fail (any other result that exit code 2 from adb). 2 if screen is off (will fail and give adb res 55808)
            cache = int(os.system('adb shell screenrecord /storage/emulated/0/.TempScreenRecording.mp4'))  # Gives 2 if recording was aborted trough ctrl+c, any other - fail
            if cache == 2: return 0
            elif cache == 55808: return 2
            else: return 1
        def MakeScreenshot():  # Has 0 res'ts (out) except basic sh/adb errors
            os.system('adb shell screencap -p /storage/emulated/0/.TempScreenshot.png')
        def Else(cache_prompt):
            if cache_prompt != '': input('Wrong option!')
        def DefExitPrompt(text='Done!'): input(f'{text}\n\npress enter to exit')
        class FunScripts:
            def PixelSimulator():
                for i in reversed(range(101)):
                    time.sleep(0.5)
                    cls()
                    print(f'Current battery procent: {i}')
                    sh(f'adb shell dumpsys battery set level {i}')
                cls()
                print('Final killing moment...')
                sh('adb shell dumpsys battery set level -1')
                main.activities.DefExitPrompt()
        def get_dt(): return f'{time.localtime().tm_year}-{time.localtime().tm_mon}-{time.localtime().tm_mday}_{time.localtime().tm_hour}-{time.localtime().tm_min}'
        
        def __GetAllActivities__():  # First ChatGPT func
            funcs = [name for name, func in inspect.getmembers(main.activities, inspect.isfunction)]
            funcs.append('__GetAllActivities__')
            return funcs
        def __RunActivity__(name, *args, **kwargs):  # Second ChatGPT func
            funcs = dict(inspect.getmembers(main.activities, inspect.isfunction))
            if name not in funcs:
                raise ValueError(f"Activity '{name}' not found.")
            return funcs[name](*args, **kwargs)
comment = ''
menu_options = ' 1: Device info\n 2: Logcat\n 3: Flash\n 4: File/Dir tools\n 5: Apps manager\n 6: Capture\n 7: Shell'
try: import requests  # Extra imports (requires installing moudles trough pip or others)
except: 
    comment = 'Warning: extra modules was not imported'
    print('Warning: extra modules was not imported, read more on GitHub project page')
    main.ExtraModulesImported = False
CurrentOS = platform.system()  # Finding a platform/OS of machine
runtime = True
def sh(cmd): return int(os.system(cmd))  # Run a sh cmd, just a shorcut for os.system()
def cls(): os.system('clear')  # Clears the screen, by now only for Unix-like systems
# # Some pre-run things (like check for platform)
if __name__ != '__main__': raise RuntimeError('Running in import mode is not supported')  # To protect from launching trough from or import
if CurrentOS not in main.SupportedPlatforms: main.activities.UnsupportedOS()  # Finding up if OS not supported
if main.ExtraModulesImported == True:  # Trying to launch a check version if module "requests" is imported
    print('Checking for lastest version...')
    try: 
        cache = float(requests.get('https://dev4ones.space/artazon/last_version').content.decode('utf-8'))  # Fetching a version from my website. Will get error if version was not fetched successfuly or correctly (like website is down or app to old, and version check link was changed)
        if cache > main.version.Version:  # If int version (like 1.0 or 1.1) is lower than the lastest one
            comment = 'Using older version, please update'
            print(comment)
            input('\n\npress enter to continue.  (1/2)')
            input('\n\npress enter to continue.  (2/2)')
    except:  # Was added because main server (dev4ones.space) can fail, be down, or user has no internet
        print('Failed to obtain last version')  
        comment = 'Failed to obtain last version'
else: print('Skipped checking for lastest version (because extra modules was not imported)')
# Main app
while runtime: 
    try:
        while runtime:  # Was added in 11B2/1 to decrease consumption
            cls()
            cache = input(f'Artazon Menu\n\n\n{menu_options}\n\n{comment}\ni: advanced menu\nSelect: ')
            cls()
            if comment != '': comment = ''  # To remove comment text if it exists
            
            if cache.find('1') != -1: # Function last update: 11B4; Last small update: no-yet
                cache = input(f'Device Info\n\n\n 1: Default Info\n 2: Netstat (Active Internet Connections)\n\nSelect: ')
                cls()
                if cache.find('1') != -1:
                    if main.activities.CheckDevice() == 0: main.activities.DeviceInfoBasic()
                    else: main.activities.NoDevice()
                    main.activities.DefExitPrompt('')
                elif cache.find('2') != -1:
                    if main.activities.CheckDevice() == 0: main.activities.Netstat()
                    else: main.activities.NoDevice()
                    main.activities.DefExitPrompt('')
                else: main.activities.Else(cache)
            
            elif cache.find('2') != -1:  # Function last minor/fix update: 10R1; Last small update: 11B4
                cache = input(f'Logcat\n\n\n 1: Live logcat\n 2: Write logcat output\n\nSelect: ')
                cls()
                if cache.find('1') != -1:
                    if main.activities.CheckDevice() == 0: main.activities.Logcat()
                    else: main.activities.NoDevice()
                elif cache.find('2') != -1:
                    if main.activities.CheckDevice() == 0: main.activities.LogcatWrite()
                    else: main.activities.NoDevice()
                else: main.activities.Else(cache)
            
            elif cache.find('3') != -1:  # Function last minor update: 11B1; Last small update: 11B4
                cache = input(f'Flash\n\n\n 1: Flash boot (for root)\n 2: Flash all (by-vendor package)\n\nSelect: ')
                cls()
                if cache.find('1') != -1: 
                    if main.activities.DetectGooglePixel() == 1: main.IsPixel = True
                    else: main.IsPixel = False
                    cache = input('Boot (init_boot if Pixel) image to flash: ')
                    cls()
                    print('Started flashing...')
                    if main.IsPixel == True: cmd = f'init_boot {cache}'  # Changing boot to init_boot for Pixel phones
                    else: cmd = f'boot {cache}'
                    if int(os.system(f'fastboot flash {cmd}')) != 0: print('Flash failed...\n\npress enter to exit')
                    else: input('Done! Press enter to exit')
                elif cache.find('2') != -1: 
                    cache = input('OS Install Package (by-vendor, enter "help", to get more info): ')
                    if cache == 'help': 
                        input('By-vendor OS install package must contain "flash-all.sh", which automatically flashes OS.\nThis .zip file is made by manufacter and can non-exist for your phone\n\npress enter to continue')
                        cache = input('OS Install Package: ')
                    cache1 = input('Folder name after unpacking (enter "same" to use the same folder name): ')
                    cls()
                    if main.activities.CheckDevice() != 0: main.activities.NoDevice()
                    else: 
                        print('Unzipping package...')
                        if int(os.system(f'unzip {cache}')) != 0: input('error: package is corrupted or was not found\n\npress enter to exit')
                        else: 
                            print('Unpacked successfuly\nWill proceed in 30 seconds, or do CTRL+C to continue right now\n\nMake sure phone bootloader is unlocked, and it in bootloader/fastboot right now (and connected to machine)')
                            try: time.sleep(30)
                            except KeyboardInterrupt: pass
                            if int(os.system(f'cd {cache1} && sh flash-all.sh')) != 0: input('Script failed, or was not found (if that, check folder unpacked name)\n\npress enter to exit')
                            else: input('Script is done, press enter to exit')
                else: main.activities.Else(cache)
            
            elif cache.find('4') != -1:  # Function last minor/fix update: 11B2; Last small update: 11B4
                cache = input('File/Dir transfer\n\n\n 1: Push to device\n 2: Pull from device\n 3: File explorer (on device)\n\nSelect: ')
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
                        if int(os.system(f'adb push {cache} {cache1}')) != 0: main.activities.DefExitPrompt('Push failed...')
                        else: main.activities.DefExitPrompt('Push is done!')
                elif cache.find('2') != -1:
                    cache = input('Pull from device (%h for 0/, %d for 0/Download): ')
                    cache1 = input('Pull to: ')
                    if cache.find('%h') != -1: cache = cache.replace('%h', '/storage/emulated/0')
                    if cache.find('%d') != -1: cache = cache.replace('%d', '/storage/emulated/0/Download')
                    cls()
                    print('Pulling...')
                    if main.activities.CheckDevice() != 0: main.activities.NoDevice()
                    else: 
                        if int(os.system(f'adb pull {cache} {cache1}')) != 0: main.activities.DefExitPrompt('Pull failed...')
                        else: main.activities.DefExitPrompt('Pull is done!')
                elif cache.find('3') != -1: 
                    print('Writing adb-term-e.py')
                    open('adb-term-e.py', 'w').write(main.activities.ReturnADB_EXP())
                    os.system('python3 adb-term-e.py')
                else: main.activities.Else(cache)
            
            elif cache.find('5') != -1:  # Function last minor/fix update: 11B1; Last small update: no-yet
                cache = input('Apps manager\n\n\n 1: List all packages\n 2: Install app/s\n 3: Remove app/package\n\nSelect: ')
                cls()
                if cache.find('1') != -1: 
                    if main.activities.CheckDevice() != 0: main.activities.NoDevice()
                    else: main.activities.ListPackages()
                elif cache.find('2') != -1:
                    cache = input('App/s to install: ')
                    cls()
                    if main.activities.CheckDevice() != 0: main.activities.NoDevice()
                    else: main.activities.Install(cache)
                elif cache.find('3') != -1:
                    cache = input('Package/s to uninstall: ')
                    cls()
                    if main.activities.CheckDevice() != 0: main.activities.NoDevice()
                    else: main.activities.Install(cache)
                else: main.activities.Else(cache)
            
            elif cache.find('6') != -1:  # Function last minor/fix update: 11B3; Last small update: no-yet
                cache = input('Capture\n\n\n 1: Record screen\n 2: Make screenshot\n\nSelect: ')
                cls()
                if cache.find('1') != -1:
                    print('Recording screen...')
                    if main.activities.CheckDevice() != 0: main.activities.NoDevice()
                    else:
                        cache = main.activities.RecordScreen()
                        if cache == 0: 
                            print('Recorded, moving .mp4 to home folder...')
                            os.system(f'adb pull /storage/emulated/0/.TempScreenRecording.mp4 ~/{main.activities.get_dt()}.mp4')  # Pulling video to home
                            os.system('adb shell rm /storage/emulated/0/.TempScreenRecording.mp4')  # Removing temp screen record from device
                            input('\nRecord successful! Recording was moved to home folder.\n\npress enter to exit')
                        elif cache == 1: 
                            os.system('adb shell rm /storage/emulated/0/.TempScreenRecording.mp4')  # Removing temp screen record from device
                            input('Record failed...\n\npress enter to exit')
                        elif cache == 2: input('Recording failed, it was caused by having screen off (in AOD counts too)\n\npress enter to exit')
                elif cache.find('2') != -1: 
                    print('Making screenshot...')
                    if main.activities.CheckDevice() != 0: main.activities.NoDevice()
                    else:
                        main.activities.MakeScreenshot()
                        print('Moving screenshot to home folder...')
                        os.system(f'adb pull /storage/emulated/0/.TempScreenshot.png ~/{main.activities.get_dt()}.png')
                        print('Deleting temp screenshot on device...')
                        os.system('adb shell rm /storage/emulated/0/.TempScreenshot.png')
                        input('Done!\n\npress enter to exit')
                else: main.activities.Else(cache)
            
            elif cache.find('7') != -1:  # Function last minor/fix update: 11B3; Last small update: no-yet
                cache = input('Shell\n\n\n 1: Launch shell on devicen\n 2: Launch shell on device as root\n 3: Run pre-included commands\n\nSelect: ')
                cls()
                if cache.find('1') != -1:
                    os.system('adb shell')
                elif cache.find('2') != -1:
                    print('Use ctrl+c to exit')
                    while True:
                        try:
                            while True:
                                cmdp = input('integrated-root-shell: ')
                                os.system(f'adb shell su -c {cmdp}')
                        except: break
                elif cache.find('3') != -1:
                    cache = input('Shell/Pre-included commands\n\n\n 1: Set battery level\n 2: Reset battery level(%, back to normal)\n 3: Fun scripts (may break android!)\n\nSelect: ')
                    cls()
                    if cache.find('1') != -1:
                        cache = input('Battery level (%, can be higher than 100): ')
                        cls()
                        print('Setting battery level...')
                        if main.activities.CheckDevice() != 0: main.activities.NoDevice()
                        else: 
                            os.system(f'adb shell dumpsys battery set level {cache}')
                            main.activities.DefExitPrompt()
                    elif cache.find('2') != -1:
                        print('Reseting battery level...')
                        if main.activities.CheckDevice() != 0: main.activities.NoDevice()
                        else: 
                            os.system('adb shell dumpsys battery reset level')
                            main.activities.DefExitPrompt()
                    elif cache.find('3') != -1:
                        cache = input('Fun scripts\n\n\n 1: Google Pixel simulator (may break android!)\n\nSelect: ')
                        if cache.find('1') != -1:
                            print('Starting script...')
                            if main.activities.CheckDevice() != 0: main.activities.NoDevice()
                            else: main.activities.FunScripts.PixelSimulator()
                        else: main.activities.Else(cache)
                    else: main.activities.Else(cache)
                else: main.activities.Else(cache)
            
            elif cache.find('i') != -1:  # Function last minor/fix update: 10R1; Last small update: 11R1
                cache = input('Advanced Menu\n\n\n 1: List activities\n 2: Run activity\n 3: App info\n\nSelect: ')
                cls()
                if cache.find('1') != -1: 
                    cls()
                    main.activities.DefExitPrompt('\n'.join(main.activities.__GetAllActivities__()).replace('__GetAllActivities__', ''))
                elif cache.find('2') != -1:
                    cls()
                    cache = input('Activity: ')
                    cache1 = input('Arg ($N to use without args): ')
                    if cache.find('$N') != -1: cache = main.activities.__RunActivity__(cache)
                    else: cache = main.activities.__RunActivity__(cache, cache1)
                    main.activities.DefExitPrompt(f'Activity exit code: {cache}\nDone!')
                elif cache.find('3') != -1: input(f'{main.version.all}\n\npress enter to exit')
                else: input('Wrong option!')
            else: main.activities.Else(cache)
    except KeyboardInterrupt: 
        cls()
        exit()
    except EOFError: # Turned off for debugging if beta or alpha (means adds EOFError), release - just except for basic errors
        cls() 
        comment = ''
        input('An unknown error occured, press enter to get back to main menu')