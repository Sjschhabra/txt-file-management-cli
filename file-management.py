import os
from tabulate import tabulate

def list_txt_files_in_directory(directory):
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    if not txt_files:
        print("\nNo .txt files found in the directory.")
    else:
        txt_files = [{"\033[93m#\033[0m": idx, "\033[93mFile Name\033[0m": txt} for idx, txt in enumerate(txt_files, start=1)]
        table_str = tabulate(txt_files, headers="keys", tablefmt="pretty")
        print("\n\033[1;93mList of .txt files in the directory:\033[0m")
        print(table_str)

def manage_file(project_directory):
    
    while True:
        
        list_txt_files_in_directory(project_directory)
        a = input("\033[31;1mName of the file (or exit): \033[0m")
        

        if a == 'exit':
            return

        file_path = os.path.join(project_directory, f'{a}.txt')

        if os.path.exists(file_path):
            t = open(file_path)
            text = t.read()
            q = input(f"--The file '{a}.txt' already exists.\n--Its Content is: \"{text}\"\nWant to o:overwrite or a:append or d:delete?: ")
            t.close()
            if q.lower() == "o":
                os.remove(file_path)
                f = open(file_path, 'w')
                print(f"file named \033[93m{a}.txt\033[0m has been created")
                f.close()
            elif q.lower() == "a":
                f = open(file_path, 'a')
                f.write(input("Write the Extra Content: "))
                print(f"file named \033[93m{a}.txt\033[0m has been appended")
                f.close()
            elif q.lower()== "d":
                 os.remove(file_path)
                 print(f"File named \033[93m{a}.txt\033[0m has been deleted.")
                 
                 break
            else:
                return

        if not os.path.exists(file_path):
            f = open(file_path, 'w')
            print(f"file named \033[93m{a}.txt\033[0m has been created")
            f.close()
            

        try:
            while True:
                list_txt_files_in_directory(project_directory)
                b = input(f"\n\033[91mInput a Command for the file\033[0m  {a}.txt \U0001F604\n\033[91m(r:read, re:rename a:append, w:write, e:empty, d:delete,  ex:exit):\033[0m ")
                if b == "re":
                    x = input("New Name: ")
                    new_file_path = os.path.join(project_directory, f'{x}.txt')
                    if os.path.exists(new_file_path):
                        t = open(new_file_path)
                        text = t.read()
                        g = input(f"--The file '{x}.txt' already exists.\n--Its Content is: \"{text}\"\nWant to o:overwrite or a:append?: ")
                        t.close()

                        if g.lower() == "o":
                            os.rename(file_path, new_file_path)
                            a = x  # Update 'a' with the new filename
                            file_path = new_file_path  # Update file_path with the new path
                        elif g.lower() == "a":
                            y = open(file_path)
                            sent = y.read()
                            e = open(new_file_path, 'a')
                            e.write(sent)
                            e.close()
                            y.close()
                            os.remove(file_path)
                            a = x  # Update 'a' with the new filename
                            file_path = new_file_path  # Update file_path with the new path
                        else:
                            continue
                    else:
                        os.rename(file_path, new_file_path)
                        a = x  # Update 'a' with the new filename
                        file_path = new_file_path  # Update file_path with the new path
                    print("\033[90m-- Task Completed --\033[0m\n")
                elif b == "a":
                    f = open(file_path, 'a')
                    f.write(input("Write the Extra Content: "))
                    f.close()
                    print("\033[90m-- Task Completed --\033[0m\n")
                elif b == "w":
                    f = open(file_path, 'w')
                    f.write(input("Write the Content: "))
                    f.close()
                    print("\033[90m-- Task Completed --\033[0m\n")
                elif b == "e":
                    f = open(file_path, 'w')
                    f.truncate(0)
                    f.close()
                    print("\033[90m-- Task Completed --\033[0m\n")
                elif b == "r":
                    f = open(file_path, 'r')
                    u = f.read()
                    print(f"Stored Content:\"{u}\"")
                    f.close()
                    print("\033[90m-- Task Completed --\033[0m\n")
                elif b == "d":
                    os.remove(file_path)
                    print(f"\nFile '{a}.txt' has been Deleted.")
                    print("\033[90m-- Task Completed --\033[0m\n")
                    break
                elif b == "ex":
                    print(f"\nFinal File Name is {a}.txt\n\n\n")
                    break
                else:
                    print("\nInvalid command. Please enter a valid command.\n")
                    return
                
        except Exception as e:
            print(f"Error: {e}")

        

project_directory = os.path.dirname(os.path.abspath(__file__))

while True:
    manage_file(project_directory)
