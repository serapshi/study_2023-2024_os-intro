---
## Front matter
title: "Отчёт по 1 этапу индивидуального проекта"
subtitle: "Размещение на Github pages заготовки для персонального сайта."
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

Разместить заготовку для индивидуального проекта на Github Pages.


# Задание

Установить необходимое программное обеспечение.
Скачать шаблон темы сайта.
Разместить его на хостинге git.
Установить параметр для URLs сайта.
Разместить заготовку сайта на Github pages.



# Выполнение лабораторной работы

Клонирую репозитой, чтобы работать с шаблоном индивидуального проектаю.

![Клонирование репозитория](image/1.png){#fig:001 width=70%}

Устанавливаю расширенную версию Hugo.

![Установка ПО](image/2.png){#fig:002 width=70%}

Распаковываю расширенную версию hugo на своей виртуальной машине. 

![Подготовка ПО](image/3.png){#fig:003 width=70%}

Переношу исполняемый файл hugo в директорию с шаблоном индивидуального проекта.

![Перенос исполняемоговайла](image/4.png){#fig:004 width=70%}

Запускаю исполняемый файл hugo

![Развертывание сайта](image/5.png){#fig:005 width=70%}

Запускаю локальный сервер hugo.

![Запуск сервера](image/6.png){#fig:006 width=70%}

Локальный сервер с шаблоном запустился, его можно просмотреть по адресу localhost:1313

![Запущенный сервер](image/7.png){#fig:007 width=70%}

Открываю сайт, чтобы удостовериться,что все сработало.

![Запущенный сервер](image/8.png){#fig:008 width=70%}

Успешно разместил заготовку сайта на Github pages.

![Сборка сайта на Github pages](image/9.png){#fig:009 width=70%}
# Выводы

Мне удалось разместить шаблон индивидуального проекта на сервесе github pages.


