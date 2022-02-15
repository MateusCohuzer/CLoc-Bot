from os import path, listdir, system
from csv import reader, writer


def CLoc_bot(clones_folder='./clones', output_folder='./output'):
    """ Use CLoc to create a .csv file with the --by-file-by-lang filter """
    for file in listdir(clones_folder):
        file_name = path.join(file)
        if path.exists(f'output/{file_name}.csv'):
            print(f"O arquivo {file_name}.csv já existe \n")
        else:
            system(f'cloc --by-file-by-lang --csv --out {output_folder}/{file_name}.csv {clones_folder}/{file_name}')
            print(f'\n Arquivo {file_name}.csv criado \n')


def formater(output_folder='./output'):
    """ Format the .csv file with a project variable, and delete the SUM data """
    for file in listdir(output_folder):
        with open(f'{output_folder}/{file}', 'r') as arquivo:
            arquivo_csv = reader(arquivo, delimiter=',')
            lista_csv = list(arquivo_csv)
            for i, linha in enumerate(lista_csv):
                if len(linha) == 6 and linha[0] != "project" and linha[0] != file[:-4]:
                    linha.insert(0, "project")
                elif len(linha) == 5 and linha[0] != file[:-4]:
                    linha.insert(0, f'{file[:-4]}')
                if len(linha) == 7:
                    lista_csv[i].remove(linha[-1])
                if linha[1] == 'SUM' and linha[2] == '':
                    del lista_csv[i:]
        arquivo.close()
        with open(f'{output_folder}/{file}', 'w', newline='') as arquivo:
            writer_ = writer(arquivo)
            writer_.writerows(lista_csv)
            print(f'\nO Arquivo {file} foi formatado com sucesso \n')
