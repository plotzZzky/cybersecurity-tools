#!/bin/bash


function system_data() {
  local system="$(uname -a)"

  echo -e "\n--> Sistema" 
  echo "$system"
}

function username() {
  local username="$(whoami)"

  echo -e "\n--> Username "
  echo -e "* $username"
}

function homefolder() {
  local home="$HOME"

  echo -e "\n--> Todas as pastas de usuários" 
  echo "* $home"
}

function all_homefolder() {
  local folders="$(ls /home)"

  echo -e "\n--> Todas as pastas de usuário:" 
  echo -e "$folders"
}

function host_name() {
  local hostname="$(hostname)"
  echo -e "\n--> Hostname" 
  echo -e "* $hostname"
}

function user_ip() {
  local enternet_data="$(ip a)"
  echo -e "\n--> Ips" 
  echo "$enternet_data"
}

function time_date() {
  local time="$(timedatectl)"

  echo -e "\n--> Horários:" 
  echo "$time"
}

function disks() {
  local disks="$(lsblk -fpm)"

  echo -e "\n--> Discos:" 
  echo "$disks"
}

function display_data() {
  local display="$(inxi -G)"

  echo -e "\n--> $display"
}

# Apps
function all_brownsers() {
  local brownsers="$(
    which firefox
    which google-chrome
    which chromium
    which opera
    which brave
  )"

  echo -e "\n--> Navegadores:" 
  echo "$brownsers"
}

function dev_tools() {
  local dev="$(
    which docker 
    which pycharm
    which code
    which codium
    which vim
    which neovim
  )"

  echo -e "\n--> Ferramentas de dev:" 
  echo "$dev"
}


function return_data() {
  echo -e " - - - - - - - - - - - - - - - - - - - Linux System Information - - - - - - - - - - - - - - - - - - - "
  system_data

  username
  homefolder
  all_homefolder

  host_name
  user_ip
  time_date

  disks

  display_data

  all_brownsers
  dev_tools

  echo " "
}

return_data

