# # Variables & Imports
import os, subprocess, time, inspect  # Basic imports (do not requires installing modules from pip and like that)
class main:
    # Modules (def, or default variables like SupportedPlatoforms)
    ExtraModulesImported = True
    # Classess
    class version:
        VersionsMap = {
            1.0: 'Cyclizar',
            1.1: 'Combee'
        }
        Version = 1.1  # 11R1 is a fundament
        Codename = VersionsMap.get(Version)
        VersionType = 'Beta'  # Alpha, Release, Beta
        Build = f'{str(Version).replace('.', '')}{VersionType[0]}1-MOBILE'
        all = f'Version: {Version}\nVersion Type: {VersionType}\nVersion Codename: {Codename}\nBuild: {Build}'
    class activities:
        def DeviceInfoBasic(out_model=False):  # out_model only for LogcatWrite() to get a model name
            Model = subprocess.check_output('su -c getprop ro.product.model', shell=True).decode('utf-8').replace('\n', '')
            if out_model == True: return Model
            Manufacter = subprocess.check_output('su -c getprop ro.product.manufacturer', shell=True).decode('utf-8').replace('\n', '')
            AndroidVersion = subprocess.check_output('su -c getprop ro.build.version.release', shell=True).decode('utf-8').replace('\n', '')
            SDK = subprocess.check_output('su -c getprop ro.build.version.sdk', shell=True).decode('utf-8').replace('\n', '')
            DeviceFingerprint = subprocess.check_output('su -c getprop ro.build.fingerprint', shell=True).decode('utf-8').replace('\n', '')
            SerialNumber = subprocess.check_output('su -c getprop ro.serialno', shell=True).decode('utf-8').replace('\n', '')
            print(f'Model: {Model}\nManufacter: {Manufacter}\nFingerprint: {DeviceFingerprint}\nAndroid Version: {AndroidVersion}\nSDK: {SDK}\nSerial Number: {SerialNumber}')
        def Netstat(): print(f'{subprocess.check_output('su -c netstat', shell=True).decode('utf-8')}\n\npress enter to exit')
        def Logcat(): os.system('adb logcat')  # Just adb logcat
        def LogcatWrite():  # Menu 2, option 2: Writes logcat into home dir by file: {model name, ex. Pixel7}.log
            cache = f'/storage/emulated/0/{main.activities.get_dt()}.log'
            print(f'Writing device logcat in {cache}.\nUse CTRL+C to stop')
            os.system(f'su -c logcat > {cache}')
            input('\nProcess ended, press enter to exit')
        def ReturnADB_EXP(): return """import os, subprocess\nversion = '1.1-ArtazonMobile'\ndef cls(): os.system('clear')\nclass AppVariables: ShowInMainInput = 'cd '\ncurrent_dir = '/'\ncomment = '''\n'''\nwhile True:\n    try:\n        ShowInMainInput = f'cd {current_dir}/'\n        cls()\n        try: print(f'''{subprocess.check_output(f'su -c ls "{current_dir}"', shell=True).decode('ascii').replace('''\n''', ' | ')}\n\n\nCurrent Directory: {current_dir}\n{comment}\n''')\n        except: \n            input('No device attached, reconnect it or check adb access to it')\n            raise ValueError\n        cache = input(ShowInMainInput)\n        if comment != '''\n''': comment = '''\n'''\n        if cache == '': pass\n        elif cache[0] == '^': \n            cache = cache.replace('^', '')\n            print('Running the sh command on a device...')\n            os.system(f'su -c sh {cache}')\n        elif cache == '' or cache == ' ': comment = '''\nSymbols entered are not cd'able!\n'''\n        elif current_dir == '/' and cache == '/': comment = "Can't cd into /, when alredy in!" \n        elif int(os.system(f'su -c cd "{current_dir}/{cache}"')) == 512: comment = 'This directory does not exist!' \n        elif cache == '..':\n            cache = str(subprocess.check_output(f'su -c "cd {current_dir}/.. && pwd"', shell=True).decode('ascii').replace('''\n''', ''))\n            if cache == '/' and current_dir == '/': current_dir = '/'\n            elif cache == '//' and current_dir == '/': current_dir = '/'\n            else: current_dir = cache\n        elif cache == '$help': \n            cls()\n            input('''Commands:\n\n$help - Shows this text\n^{zsh command} - It will run zsh command (without ^ on device)\n\npress enter to exit''')\n        else:\n            if current_dir == '/': current_dir = str(subprocess.check_output(f'su -c "cd /{cache} && pwd"', shell=True).decode('ascii').replace('''\n''', ''))\n            else: current_dir = str(subprocess.check_output(f'su -c "cd {current_dir}/{cache} && pwd"', shell=True).decode('ascii').replace('''\n''', ''))\n    except KeyboardInterrupt: \n        cls()\n        break\n    except ValueError: pass\n    except EOFError: comment = 'Got unknown error'"""
        def ListPackages():  # Just listing all packages trough pm
            os.system('su -c pm list packages')
            input('\n\npress enter to exit')
        def Install(apps):  # Simple adb install command
            os.system(f'adb install {apps}')
        def Remove(package):  # Also simple adb remove
            os.system(f'adb uninstall {package}')
        def RecordScreen(): os.system(f'su -c screenrecord /storage/emulated/0/{main.activities.get_dt()}.mp4')
        def MakeScreenshot(): os.system(f'su -c screencap -p /storage/emulated/0/{main.activities.get_dt}.png')
        def Else(cache_prompt):
            if cache_prompt != '': input('Wrong option!')
        def DefExitPrompt(text='Done!'): input(f'{text}\n\npress enter to exit')
        class FunScripts:
            def PixelSimulator():
                for i in reversed(range(101)):
                    time.sleep(0.5)
                    cls()
                    print(f'Current battery procent: {i}')
                    sh(f'su -c dumpsys battery set level {i}')
                cls()
                print('Final killing moment...')
                sh('su -c dumpsys battery set level -1')
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
menu_options = ' 1: Device info\n 2: Logcat\n 3: Terminal explorer\n 4: Apps manager\n 5: Capture\n 6: Shell'
try: import requests  # Extra imports (requires installing moudles trough pip or others)
except: 
    comment = 'Warning: extra modules was not imported'
    print('Warning: extra modules was not imported, read more on GitHub project page')
    main.ExtraModulesImported = False
runtime = True
def sh(cmd): return int(os.system(cmd))  # Run a sh cmd, just a shorcut for os.system()
def cls(): os.system('clear')  # Clears the screen, by now only for Unix-like systems
# # Some pre-run things (like check for platform)
if __name__ != '__main__': raise RuntimeError('Running in import mode is not supported')  # To protect from launching trough from or import
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
            cache = input(f'Artazon Mobile\n\n\n{menu_options}\n\n{comment}\ni: advanced menu\nSelect: ')
            cls()
            if comment != '': comment = ''  # To remove comment text if it exists
            
            if cache.find('1') != -1: # Function last update: 11B4; Last small update: no-yet
                cache = input(f'Device Info\n\n\n 1: Default Info\n 2: Netstat (Active Internet Connections)\n\nSelect: ')
                cls()
                if cache.find('1') != -1:
                    main.activities.DeviceInfoBasic()
                    main.activities.DefExitPrompt('')
                elif cache.find('2') != -1:
                    main.activities.Netstat()
                    main.activities.DefExitPrompt('')
                else: main.activities.Else(cache)
            
            elif cache.find('2') != -1:  # Function last minor/fix update: 10R1; Last small update: 11B4
                cache = input(f'Logcat\n\n\n 1: Live logcat\n 2: Write logcat output\n\nSelect: ')
                cls()
                if cache.find('1') != -1: main.activities.Logcat()
                elif cache.find('2') != -1: main.activities.LogcatWrite()
                else: main.activities.Else(cache)
            
            elif cache.find('3') != -1:
                print('Writing app...')
                open('adb-term-e-mobile.py', 'w').write(main.activities.ReturnADB_EXP)
                os.system('python3 adb-term-e-mobile.py')
            
            elif cache.find('4') != -1:  # Function last minor/fix update: 11B1; Last small update: no-yet
                input('Sorry, this this function still in development')
                raise ConnectionAbortedError()
                cache = input('Apps manager\n\n\n 1: List all packages\n 2: Install app/s\n 3: Remove app/package\n\nSelect: ')
                cls()
                if cache.find('1') != -1: main.activities.ListPackages()
                elif cache.find('2') != -1:
                    cache = input('App/s to install: ')
                    cls()
                    main.activities.Install(cache)
                elif cache.find('3') != -1:
                    cache = input('Package/s to uninstall: ')
                    cls()
                    main.activities.Install(cache)
                else: main.activities.Else(cache)
            
            elif cache.find('5') != -1:  # Function last minor/fix update: 11B3; Last small update: no-yet
                cache = input('Capture\n\n\n 1: Record screen\n 2: Make screenshot\n\nSelect: ')
                cls()
                if cache.find('1') != -1:
                    print('Recording screen...')
                    main.activities.RecordScreen()
                    main.activities.DefExitPrompt()
                elif cache.find('2') != -1: 
                    print('Making screenshot...')
                    main.activities.MakeScreenshot()
                    main.activities.DefExitPrompt()
                else: main.activities.Else(cache)
            
            elif cache.find('6') != -1:  # Function last minor/fix update: 11B3; Last small update: no-yet
                cache = input('Shell\n\n\n 1: Launch shell on device as root\n 2: Run pre-included commands\n\nSelect: ')
                cls()
                if cache.find('1') != -1: os.system('su')
                elif cache.find('2') != -1:
                    cache = input('Shell/Pre-included commands\n\n\n 1: Set battery level\n 2: Reset battery level(%, back to normal)\n 3: Fun scripts (may break android!)\n\nSelect: ')
                    cls()
                    if cache.find('1') != -1:
                        cache = input('Battery level (%, can be higher than 100): ')
                        cls()
                        print('Setting battery level...')
                        os.system(f'su -c dumpsys battery set level {cache}')
                        main.activities.DefExitPrompt()
                    elif cache.find('2') != -1:
                        print('Reseting battery level...')
                        os.system('su -c dumpsys battery reset level')
                        main.activities.DefExitPrompt()
                    elif cache.find('3') != -1:
                        cache = input('Fun scripts\n\n\n 1: Google Pixel simulator (may break android!)\n\nSelect: ')
                        if cache.find('1') != -1:
                            print('Starting script...')
                            main.activities.FunScripts.PixelSimulator()
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
    except ConnectionAbortedError: pass  # A exception for passing to main menu of func or any like that
    except KeyboardInterrupt: 
        cls()
        exit()
    except EOFError: # Turned off for debugging if beta or alpha (means adds EOFError), release - just except for basic errors
        cls() 
        comment = ''
        input('An unknown error occured, press enter to get back to main menu')