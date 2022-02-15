from os import system, path
from functions import CLoc_bot, formater


clones_folder = './clones'  # Clones folder's path [Files that were used only for testing, credits to the original authors]
output_folder = './output'  # .csv files folder's path
CLoc_path = path.dirname(path.abspath("cloc.exe"))  # CLoc.exe path
system(f'cd {CLoc_path}')  # Finding CLoc

CLoc_bot(clones_folder, output_folder)
formater(output_folder)
