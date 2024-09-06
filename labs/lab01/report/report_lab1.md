---
## Front matter
title: "Oтчёт по лабораторной работе № 1"
subtitle: "Установка и конфигурация операционной системы на виртуальную машину"
author: "Сергей Витальевич Павлюченков"

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы


Целью данной работы является приобретение практических навыков установки операционной системы на виртуальную машину, настройки минимально необходимых для дальнейшей работы сервисов.

# Задание

Скачать ОС Linux Fedora Sway.
Установить ее в виртуальной машине.
Установить доп ПО.




# Выполнение лабораторной работы

Скачиваю Fedora Sway с их сайта.

![Сайт дистрибутива](image/0.png){#fig:001 width=70%}

Устанавливаю хост клавишу, для меня это rctrl.

![host key](image/1.png){#fig:002 width=70%}

Выбираю нужный графический контроллер  - VMVSGA

![Настройка графики](image/2.png){#fig:003 width=70%}
 
Включаю общий буфер обмена и функцию переноса файлов с виртуальной машины на основную.

![Доп настройки](image/3.png){#fig:004 width=70%}

Впервые запустил виртуальную машину, после того как подлючил установленный .iso файл.
Ввожу команду запуска установщика - liveinst

![Первый запуск](image/4.png){#fig:005 width=70%}

Выбираю язык интерфейса

![Выбор языка интерфейса](image/5.png){#fig:006 width=70%}

Настраиваю раскладку, пароль, жесткий диск, часовой пояс, имя узла и учетную запись root

![Финальные настройки перед установкой](image/6.png){#fig:007 width=70%}


Устанавливаю дистрибутив.

![Установка](image/7.png){#fig:008 width=70%}

После установки отключаю вторичное устройство IDE.

![Отключаю установочный файл](image/8.png){#fig:009 width=70%}

Захожу в режим супер-пользователя.

![Захожу в root](image/9.png){#fig:010 width=70%}

Обновляю все пакеты командой dnf -y update.

![Обновление всех пакетов](image/10.png){#fig:011 width=70%}

Устанавливаю программы для удобства работы в консоли:

![Установка ПО](image/11.png){#fig:012 width=70%}

Запускаю таймер автообновления.

![Подготовка ОС](image/12.png){#fig:013 width=70%}

Устанавливаю mc и tmux.

![Установка ПО](image/13.png){#fig:014 width=70%}

Перехожу в директорию SELinux используя mc.

![Работа в mc](image/14.png){#fig:015 width=70%}


Заменяю значение SELinux с enforcing на permissive.

![Отключение SELinux](image/15.png){#fig:016 width=70%}

Перезагружаю систему и опять захожу в роль супер-пользователя

![Второй запуск ВМ](image/16.png){#fig:017 width=70%}

Устанавливаю средства разработки командой dnf -y group install "Development Tools"

![Установка ПО](image/17.png){#fig:018 width=70%}

Уставаливаю DKMS командой dnf -y install dkms

![Установка ПО](image/18.png){#fig:019 width=70%}

Подключаю образ диска доп гостевой ОС

![Подключение образа диска](image/19.png){#fig:020 width=70%}

Проверяю подключение образа.

![Подключение образа диска](image/20.png){#fig:021 width=70%}

Подмонтирую диск командой mount /dev/sr0 /media.

![Подмонтирование диска](image/21.png){#fig:022 width=70%}

Устанавливаю драйвера.

![Установка драйверов](image/22.png){#fig:023 width=70%}

Создаю конфигурационный файл раскладки и редактирую его.

![Настройка раскладки клавиатуры](image/23.png){#fig:024 width=70%}

Внутри виртуальной машины добавляю своего пользователя в группу vboxsf. 

![Подключение общей папки](image/24.png){#fig:025 width=70%}

Устанавливаю Pandoc

![Установка ПО](image/26.png){#fig:026 width=70%}

Устанавливаю дистрибутив TeXlive.

![Установка ПО](image/27.png){#fig:027 width=70%}

# Домашние задание
Использую dmesg | grep -i "то, что ищем"  во всех случаях.

![Искомая информация ](image/h1.png){#fig:028 width=70%}

![Искомая информация ](image/h2.png){#fig:029 width=70%}

![Искомая информация ](image/h3.png){#fig:030 width=70%}



# Выводы

Я установил дистрибутив Linux Fedora Sway на свой компьютер вместе с основным ПО, что я буду использовать по мере прохождения этого курса.


# Контрольные вопросы


Какую информацию содержит учётная запись пользователя?
- login, имя, фамилия, отчество, псевдоним, пол, Фотографии или аватар пользователя, давность последнего входа в систему, продолжительность последнего пребывания в системе, адрес использованного при подключении компьютера etc.
Укажите команды терминала и приведите примеры:

для получения справки по команде; 
- man help

для перемещения по файловой системе; 
- cd ~

для просмотра содержимого каталога;
- ls /home

для определения объёма каталога;
- du /home

для создания / удаления каталогов / файлов;
- mkdir dir, rmdir dir, rm file, touch file

для задания определённых прав на файл / каталог;
- chmod +x file

для просмотра истории команд.
- history

Что такое файловая система? Приведите примеры с краткой характеристикой.
- порядок, определяющий способ организации, хранения и именования данных на носителях информации в компьютерах.
Например, жесткий диск или CD-диски. Краткие характеристики - размещение и упорядочивание на носителе данных в виде файлов, создание, чтение и удаление файлов.

Как посмотреть, какие файловые системы подмонтированы в ОС?
- Можно использовать dmesg в связке с grep.

Как удалить зависший процесс?
- можно прописать kill номер процесса.

# Список литературы{.unnumbered}

1. Dash, P. Getting Started with Oracle VM VirtualBox / P. Dash. – Packt Publishing Ltd, 2013. – 86 сс.

2. Colvin, H. VirtualBox: An Ultimate Guide Book on Virtualization with VirtualBox. VirtualBox / H. Colvin. – CreateSpace Independent Publishing Platform, 2015. – 70 сс.

3. Vugt, S. van. Red Hat RHCSA/RHCE 7 cert guide : Red Hat Enterprise Linux 7 (EX200 and EX300) : Certification Guide. Red Hat RHCSA/RHCE 7 cert guide / S. van Vugt. – Pearson IT Certification, 2016. – 1008 сс.

4. Робачевский, А. Операционная система UNIX / А. Робачевский, С. Немнюгин, О. Стесик. – 2-е изд. – Санкт-Петербург : БХВ-Петербург, 2010. – 656 сс.

5. Немет, Э. Unix и Linux: руководство системного администратора. Unix и Linux / Э. Немет, Г. Снайдер, Т.Р. Хейн, Б. Уэйли. – 4-е изд. – Вильямс, 2014. – 1312 сс.

6. Колисниченко, Д.Н. Самоучитель системного администратора Linux : Системный администратор / Д.Н. Колисниченко. – Санкт-Петербург : БХВ-Петербург, 2011. – 544 сс.

7. Robbins, A. Bash Pocket Reference / A. Robbins. – O’Reilly Media, 2016. – 156 сс.
