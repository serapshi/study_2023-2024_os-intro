---
## Front matter
title: "Отчёт по 3 этапу индивидуально проекта"
subtitle: "Добавление к сайту достижения."
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

Добавить больше информации обо мне, и создать материал для сайта.


# Задание

Добавить информацию о навыках (Skills).
Добавить информацию об опыте (Experience).
Добавить информацию о достижениях (Accomplishments).
Сделать пост по прошедшей неделе.
Добавить пост на тему по выбору:
Легковесные языки разметки.
Языки разметки. LaTeX.
Язык разметки Markdown.


# Выполнение лабораторной работы

Добавил информацию о некоторых своих навыках в файл index.md директории admin.

![Добавление информации](image/1.png){#fig:001 width=70%}

Добавляю информацию о своих достижения в конце файла index.md директории admin. 

![Добавление информации](image/2.png){#fig:002 width=70%}

Аналогично добавил информацию о своем опыте.

![Добавление информации](image/3.png){#fig:003 width=70%}

Загружаю файл с обновленной информацией на сервер.

![Загрузка на сервер](image/4.png){#fig:004 width=70%}

Ожидаю, пока сайт успешно соберется.

![Сборка сайта](image/5.png){#fig:005 width=70%}

Открываю на сайте информацию о своих навыках.

![Демонстрация изменений](image/6.png){#fig:006 width=70%}

Создаю пост о прошедшец недели и загружаю его на сервер.

![Загрузка файла](image/7.png){#fig:007 width=70%}

После успешной сборки сайта, открываю пост о прошедшей недели.

![Новый пост](image/8.png){#fig:008 width=70%}

Написал новый пост о языке разметки Markdown.

![Написание нового поста](image/9.png){#fig:009 width=70%}

После чего аналогично прошлому посту загрузил его на сервер, и просмотрел его после успешной сборки сайта.
# Выводы


Я успешно расширил количество информации обо мне на сайте, также пополнил блог двумя новыми постами.

