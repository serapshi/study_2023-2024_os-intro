---
## Front matter
title: "Отчёт по лабораторной работе №3"
subtitle: "Markdown"
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


Научиться оформлять отчёты с помощью легковесного языка разметки Markdown.

# Задание


– Сделайте отчёт по предыдущей лабораторной работе в формате Markdown.
– В качестве отчёта просьба предоставить отчёты в 3 форматах: pdf, docx и md (в архиве,
поскольку он должен содержать скриншоты, Makefile и т.д.)

# Выполнение лабораторной работы

Указываю номер лабораторной работы, которую я выполнил, человека, который ее выполнил(себя) и название данной лабораторной работы.

![Редактирование начала отчета](image/1.png){#fig:001 width=70%}

Из файла посвященного первой лабораторной работе копирую и вставляю цель данной работы. 

![Цель работы](image/2.png){#fig:002 width=70%}

Добавляю список задач, который мне нужно было выполнить.

![Заполнение важной информации](image/3.png){#fig:003 width=70%}

Вставляю в отчет все полезные скриншоты иллюстрирующие выполнение работы и подписываю их.

![Заполнения тела отчета](image/4.png){#fig:004 width=70%}

Написал вывод данной работы и ответил на контрольные вопросы 1-ой лабораторной работы.

![Конец отчета](image/5.png){#fig:005 width=70%}

Применил make-филе на свой отчет (report.md) и получил 2 отчетных файла в разных форматах - pdf и docx.

![Создание отчета в pdf и docx](image/6.png){#fig:006 width=70%}


# Выводы

Выполнив эту лабораторную работу я научился составлять отчеты с помощью языка markdown.


