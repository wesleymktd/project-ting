def exists_word(word, instance):
    results = []

    for index in range(len(instance)):
        file_data = instance.search(index)
        file_name = file_data.get("nome_do_arquivo")
        lines = file_data.get("linhas_do_arquivo")
        findOk = []

        for i, line in enumerate(lines, 1):
            if word.lower() in line.lower():
                findOk.append({"linha": i})

        if findOk:
            result = {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": findOk
            }
            results.append(result)

    return results


def search_by_word(word, instance):
    results = []

    for index in range(len(instance)):
        file_data = instance.search(index)
        file_name = file_data.get("nome_do_arquivo")
        lines = file_data.get("linhas_do_arquivo")
        findOk = []

        for i, line in enumerate(lines, 1):
            if word.lower() in line.lower():
                findOk.append({"linha": i, "conteudo": line})

        if findOk:
            result = {
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": findOk
            }
            results.append(result)

    return results
