from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    name_file = path_file.split("/")[-1]

    for i in range(len(instance)):
        file_processed = instance.search(i)
        if file_processed.get("nome_do_arquivo") == path_file:
            print(f"Arquivo {name_file} já foi processado. Ignorando.")
            return

    lines = txt_importer(path_file)

    info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }

    instance.enqueue(info)

    print(f'Arquivo {name_file} processado com sucesso:')
    print(info)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
