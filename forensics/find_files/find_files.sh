#!/bin/bash
# Script que faz a varedura no sistema por arquivos com determinado nome ou extensão


logs_path="logs"
find_path="/home" 


function find_file() {
  # Função que busca o arquivo
  local filename="$1"
  
  # retorna os resultados da busca de arquivos a partir do path(incluindo links)
  # - contendo filename no nome ou extensão
  # - sem os erros de permissão negada
  local results=$(find -L "$find_path" -type f -name "$filename" 2>/dev/null || true)

  if [ -n "$results" ]; then
    local clean_filename=$(echo "$filename" | tr -d '*' | tr -d '.') # nome do log
    echo "$results" >> "$logs_path/$clean_filename.log"
  fi
}

function open_list_and_files_all_files() {

  rm -f $logs_path/* # Limpa a pasta de logs a cada nova execução
  mkdir -p $logs_path  # Cria a pasta de logs

  echo -e "Buscando os arquivos da lista a partir de $find_path\n"

   while IFS= read -r file; do # Abre a lista de arquivos e le linha por linha
      find_file "$file" "$find_path"
  done < files.txt

  echo "Terminado! Logs salvos na pasta"
}


open_list_and_files_all_files

