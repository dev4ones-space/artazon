import os, subprocess
version = '1.0-r_mod'
def cls(): os.system('clear')
class AppVariables: ShowInMainInput = 'cd '
current_dir = '/'
comment = '''
'''
while True:
    try:
        ShowInMainInput = f'cd {current_dir}/'
        cls()
        try: print(f'''{subprocess.check_output(f'su -c ls "{current_dir}"', shell=True).decode('ascii').replace('''
''', ' | ')}


Current Directory: {current_dir}
{comment}
''')
        except: 
            input('No device attached, reconnect it or check adb access to it')
            raise ValueError
        cache = input(ShowInMainInput)
        if comment != '''
''': comment = '''
'''
        if cache == '': pass
        elif cache[0] == '^': 
            cache = cache.replace('^', '')
            print('Running the sh command on a device...')
            os.system(f'su -c sh {cache}')
        elif cache == '' or cache == ' ': comment = '''
Symbols entered are not cd'able!
'''
        elif current_dir == '/' and cache == '/': comment = "Can't cd into /, when alredy in!" 
        elif int(os.system(f'su -c cd "{current_dir}/{cache}"')) == 512: comment = 'This directory does not exist!' 
        elif cache == '..':
            cache = str(subprocess.check_output(f'su -c "cd {current_dir}/.. && pwd"', shell=True).decode('ascii').replace('''
''', ''))
            if cache == '/' and current_dir == '/': current_dir = '/'
            elif cache == '//' and current_dir == '/': current_dir = '/'
            else: current_dir = cache
        elif cache == '$help': 
            cls()
            input('''Commands:

$help - Shows this text
^{zsh command} - It will run zsh command (without ^ on device)

press enter to exit''')
        else:
            if current_dir == '/': current_dir = str(subprocess.check_output(f'su -c "cd /{cache} && pwd"', shell=True).decode('ascii').replace('''
''', ''))
            else: current_dir = str(subprocess.check_output(f'su -c "cd {current_dir}/{cache} && pwd"', shell=True).decode('ascii').replace('''
''', ''))
    except KeyboardInterrupt: 
        cls()
        break
    except ValueError: pass
    except EOFError: comment = 'Got unknown error'