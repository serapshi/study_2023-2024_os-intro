---
## Front matter
title: "Отчёт по 4 этапу индивидуального проекта"
subtitle: "Добавление к сайту ссылок на научные и библиометрические ресурсы."
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

Дополнить свой сайт ссылками на научные и библиометрические ресурсы и пополнить блог новым материалом.


# Задание


Зарегистрироваться на соответствующих ресурсах и разместить на них ссылки на сайте:
eLibrary : https://elibrary.ru/;
Google Scholar : https://scholar.google.com/;
ORCID : https://orcid.org/;
Mendeley : https://www.mendeley.com/;
ResearchGate : https://www.researchgate.net/;
Academia.edu : https://www.academia.edu/;
arXiv : https://arxiv.org/;
github : https://github.com/.
Сделать пост по прошедшей неделе.
Добавить пост на тему по выбору:
Оформление отчёта.
Создание презентаций.
Работа с библиографией.

# Выполнение лабораторной работы

После успешной регистрации на каждом из сервисов, я добавил каждую ссылку в свой профиль в файле index.md директории admin.

![Редактирование информации](image/1.png){#fig:001 width=70%}

После загрузки новых данных, успешно собираю сайт на сервере.

![сборка сайта ](image/2.png){#fig:002 width=70%}

Проверяю, как выглядят добавленные ссылки на разные ресурсы.

![Новый вид профиля](image/3.png){#fig:003 width=70%}

Аналогично прошлым этапам, создаю два поста: первый о прошедшей недели, а второй о создании отчетов. Также загружаю все на гитхаб и проверяю, как все отображается на сайте.

![Проверка новых постов](image/4.png){#fig:004 width=70%}

# Выводы

Я зарегистрировался на разных платформах, где в последующем можно будет отмечать свои будущие статьи. Также улучшил навык создания постов на основу Hugo blox.


