import pyzipper
import concurrent.futures
import zlib
from zipfile import ZipFile
from colorama import Fore

poster='''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠃⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠾⢛⠒⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⣄⡈⠓⢄⠠⡀⠀⠀⠀⣄⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣷⠀⠈⠱⡄⠑⣌⠆⠀⠀⡜⢻⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠳⡆⠐⢿⣆⠈⢿⠀⠀⡇⠘⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⡇⠀⠀⠈⢆⠈⠆⢸⠀⠀⢣⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣧⠀⠀⠈⢂⠀⡇⠀⠀⢨⠓⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣦⣤⠖⡏⡸⠀⣀⡴⠋⠀⠈⠢⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠁⣹⣿⣿⣿⣷⣾⠽⠖⠊⢹⣀⠄⠀⠀⠀⠈⢣⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⣇⣰⢫⢻⢉⠉⠀⣿⡆⠀⠀⡸⡏⠀⠀⠀⠀⠀⠀⢇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡇⡇⠈⢸⢸⢸⠀⠀⡇⡇⠀⠀⠁⠻⡄⡠⠂⠀⠀⠀⠘
⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠛⠓⡇⠀⠸⡆⢸⠀⢠⣿⠀⠀⠀⠀⣰⣿⣵⡆⠀⠀⠀⠀
⠈⢻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣦⣀⡇⠀⢧⡇⠀⠀⢺⡟⠀⠀⠀⢰⠉⣰⠟⠊⣠⠂⠀⡸
⠀⠀⢻⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢧⡙⠺⠿⡇⠀⠘⠇⠀⠀⢸⣧⠀⠀⢠⠃⣾⣌⠉⠩⠭⠍⣉⡇
⠀⠀⠀⠻⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣋⠀⠈⠀⡳⣧⠀⠀⠀⠀⠀⢸⡏⠀⠀⡞⢰⠉⠉⠉⠉⠉⠓⢻⠃
⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣀⠠⠤⣤⣤⠤⠞⠓⢠⠈⡆⠀⢣⣸⣾⠆⠀⠀⠀⠀⠀⢀⣀⡼⠁⡿⠈⣉⣉⣒⡒⠢⡼⠀
⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣎⣽⣶⣤⡶⢋⣤⠃⣠⡦⢀⡼⢦⣾⡤⠚⣟⣁⣀⣀⣀⣀⠀⣀⣈⣀⣠⣾⣅⠀⠑⠂⠤⠌⣩⡇⠀
⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⣺⢁⣞⣉⡴⠟⡀⠀⠀⠀⠁⠸⡅⠀⠈⢷⠈⠏⠙⠀⢹⡛⠀⢉⠀⠀⠀⣀⣀⣼⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡟⢡⠖⣡⡴⠂⣀⣀⣀⣰⣁⣀⣀⣸⠀⠀⠀⠀⠈⠁⠀⠀⠈⠀⣠⠜⠋⣠⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⢿⣿⣿⣷⡟⢋⣥⣖⣉⠀⠈⢁⡀⠤⠚⠿⣷⡦⢀⣠⣀⠢⣄⣀⡠⠔⠋⠁⠀⣼⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠈⠻⣿⣿⢿⣛⣩⠤⠒⠉⠁⠀⠀⠀⠀⠀⠉⠒⢤⡀⠉⠁⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣤⣤⠴⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⠀⠀⠀⠀⠀⢩⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀
                           ᑕ T ᑭ ᗩ ᙭⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''
def word_list(zip_file, wordlist):
    with open(wordlist, 'r') as f:
        passwords = [line.strip() for line in f]

    for password in passwords:
        try:
            with pyzipper.AESZipFile(zip_file, 'r') as zf:
                zf.extractall(pwd=password.encode('utf-8'))
                print(f'Password found:\n{Fore.GREEN}{password}{Fore.RESET}')
                return
        except RuntimeError as e:
            if "Bad password" in str(e):
                pass
            else:
                print(f'Error: {e}')

    # If none of the passwords match
    print('Password not found in the given word list.')
def print_poster():
    gradient_colors = [Fore.MAGENTA, Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA,Fore.RED,Fore.CYAN,Fore.MAGENTA, Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA,Fore.RED,Fore.CYAN,Fore.MAGENTA, Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA,Fore.RED,Fore.CYAN,Fore.MAGENTA, Fore.RED, Fore.YELLOW, Fore.GREEN]

    # Split the poster into lines
    poster_lines = poster.split('\n')

    for line, color in zip(poster_lines, gradient_colors):
        # Print each line with a different gradient color
        print(color + line)

    # Reset the color to default at the end
    print(Fore.RESET)
def parallel_crack_password1(zip_file, min_length, max_length, executor, password_type):
    files_inside_folder = []
    result = None  # Initialize result here
    
    if mod == 1:
        with ZipFile(zip_file, 'r') as zf:
            # Skip the first folder and get the files inside it
            files_inside_folder = [name for name in zf.namelist() if '/' in name and not name.endswith('/')]

    with pyzipper.AESZipFile(zip_file, 'r') as zf:
        for file_name in files_inside_folder:
            for length in range(min_length, max_length + 1):
                charset = get_charset(password_type)
                result = brute_force1(zf, file_name, length, executor, charset)
                if result:
                    return result

    return None
def get_charset(password_type):
    if password_type == '1':
        return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elif password_type == '2':
        return '0123456789'
    elif password_type == '3':
        return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    elif password_type == '4':
        return '!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    elif password_type == '5':
        return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    elif password_type == '6':
        return '0123456789!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    elif password_type == '7':
        return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    else:
        print('Invalid password type. Using default charset.')
        return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def brute_force1(zf, file_name, length, executor, charset):
    password_chars = [''] * length
    current_attempt = [''] * length

    print(f"CHECKING FILE: {file_name} ... PLEASE WAIT (PATIENCE IS IMPORTANT FOR PASSWORD CRACKING)")

    return brute_force_helper1(zf, file_name, password_chars, current_attempt, 0, length, charset)

def brute_force_helper1(zf, file_name, password_chars, current_attempt, position, length, charset):
    if position == length:
        attempt = ''.join(current_attempt)
        try:
            # Try to extract the specified file in the zip file using the current attempt as the password
            with zf.open(file_name, pwd=attempt.encode('utf-8')) as f:
                content = f.read()
               
                return attempt
        except (RuntimeError, zlib.error, pyzipper.zipfile.BadZipFile) as e:
           
            pass  # Suppress the error details and continue with the next attempt
    else:
        for char in charset:
            current_attempt[position] = char
            result = brute_force_helper1(zf, file_name, password_chars, current_attempt.copy(), position + 1, length, charset)
            if result:
                return result

    return None
def parallel_crack_password(zip_file, min_length, max_length, executor, password_type):
    result = None  # Initialize result here
    if mod == 2:
        with pyzipper.AESZipFile(zip_file, 'r') as zf:
            for length in range(min_length, max_length + 1):
                charset = get_charset(password_type)
                result = brute_force(zf, length, executor, charset)
                if result:
                    return result

    return None


    return None

def brute_force(zf, length, executor, charset):
    password_chars = [''] * length
    current_attempt = [''] * length

    print("CHECKING...PLEASE WAIT (PATIENCE IS IMPORTANT FOR PASSWORD CRACKING)")

    return brute_force_helper(zf, password_chars, current_attempt, 0, length, charset)

def brute_force_helper(zf, password_chars, current_attempt, position, length, charset):
    if position == length:
        attempt = ''.join(current_attempt)
        try:
            # Try to extract each item in the zip file using the current attempt as the password
            for file_info in zf.infolist():
                with zf.open(file_info.filename, pwd=attempt.encode('utf-8')) as f:
                    try:
                        content = f.read()
                        # Continue processing the content here if needed
                        return attempt
                    except (RuntimeError, zlib.error, pyzipper.zipfile.BadZipFile) as e:
                      pass
                        # Continue with the next file
        except (RuntimeError, zlib.error, pyzipper.zipfile.BadZipFile) as e:
            pass
            # Continue with the next attempt
    else:
        for char in charset:
            current_attempt[position] = char
            result = brute_force_helper(zf, password_chars, current_attempt.copy(), position + 1, length, charset)
            if result is not None:
                return result

    return None

if __name__ == '__main__':
    print_poster()
    zip_file = input("Enter the correct and full file path: ")
    
    choice=input("1---->Brute force attack\n2--->Word list attack\n")

if choice=='1':
    min_password_length = int(input("Enter the minimum password length: "))
    max_password_length = int(input("Enter the maximum password length: "))
    
    print("Choose password type:")
    print("1. Alphabets")
    print("2. Numbers")
    print("3. Alphanumeric (Alphabets and numbers)")
    print("4. Special Characters")
    print("5. Alphabets with Special Characters")
    print("6. Numbers with Special Characters")
    print("7. All Three (Alphabets, Numbers, Special Characters)")
    print("<----PRESS ANY OTHER KEYS FOR EXIT---->")
    
    password_type = input("Enter the number corresponding to the password type: ")
    if password_type not in ['1', '2', '3', '4', '5', '6', '7']:
         print("Exited")
         exit(0)
    
    try:
        mod = int(input("\nZIP TYPE(This is important to know the type)\n1 for zipped from folder\n2 for zipped file\n<----PRESS ANY OTHER KEYS FOR EXIT---->\n"))
        
        if mod == 1:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                result = parallel_crack_password1(zip_file, min_password_length, max_password_length, executor, password_type)
        elif mod == 2:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                result = parallel_crack_password(zip_file, min_password_length, max_password_length, executor, password_type)
                
        else:
            print("Invalid input. Exiting.")
            exit(0)
        
        if result:
            print(f'Found password:\n{Fore.GREEN}{result}{Fore.RESET}')
        else:
              print(f'\t\t\t\n{Fore.RED}! ! ! NOTE:     1--> IF PASSWORD IS WRONG or UNABLE TO FIND, YOU ENTERED THE WRONG ZIP TYPE (Try the rest of one to get the correct password)\n\t\t2-->Try all password type one by one\n\t\t3--> Still wrong try MAX length of password (eg.min:1 and max:10 or more) and choose remain password type ! ! !')
              print(f'{Fore.CYAN}Unable to find password{Fore.RESET}')
    except ValueError:
        print("Exited")
elif choice=='2':
    wordlist=input("Enter the full and correct path of word list file :")
    word_list(zip_file, wordlist)
else:
    print("Invalid input")
    exit(0)