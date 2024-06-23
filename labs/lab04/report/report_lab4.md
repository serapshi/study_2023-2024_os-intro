---
## Front matter
title: "Отчёт по лабораторной работе № 4"
subtitle: "Продвинутое использование git"
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


Получение навыков правильной работы с репозиториями git.

# Задание

Выполнить работу для тестового репозитория.
Преобразовать рабочий репозиторий в репозиторий с git-flow и conventional commits.



# Выполнение лабораторной работы

Устанавливаю git-flow из коллекции репозиториев Copr.

![Установка git-flow](image/1.png){#fig:001 width=70%}

![Установка git-flow](image/2.png){#fig:002 width=70%}

Устанавливаю Node.js.

![Установка Node.js](image/3.png){#fig:003 width=70%}

Устанавливаю pnpm.

![Установка pnpm](image/4.png){#fig:004 width=70%}

Для работы с Node.js добавил каталог с исполняемыми файлами, устанавливаемыми yarn, в переменную PATH.

![Настройка Node.js](image/5.png){#fig:005 width=70%}

Добавляю программу для помощи в форматировании коммитов.

![Общепринятые коммиты](image/6.png){#fig:006 width=70%}

Добавляю программу для помощи в создании логов.

![Общепринятые коммиты](image/7.png){#fig:007 width=70%}

Делаю первый коммит и выкладываем на github.

![Создание репозитория git](image/8.png){#fig:008 width=70%}

Открываю конфигурация для пакетов Node.js

![Конфигурация общепринятых коммитов](image/9.png){#fig:009 width=70%}

Заполняю несколько параметров пакета. Таким образом, файл package.json приобретает такой вид:

![Конфигурация общепринятых коммитов](image/10.png){#fig:010 width=70%}

Выполняю коммит (git cz).

![Выполнение коммита](image/11.png){#fig:011 width=70%}

Отправляю на github.

![git push](image/12.png){#fig:012 width=70%}

Инициализирую git-flow.

![Конфигурация git-flow](image/13.png){#fig:013 width=70%}

Проверяю, что я на ветке develop

![Конфигурация git-flow](image/14.png){#fig:014 width=70%}

Загружаю весь репозиторий в хранилище.

![Конфигурация git-flow](image/15.png){#fig:015 width=70%}

Установите внешнюю ветку как вышестоящую для этой ветки.

![Название](image/16.png){#fig:016 width=70%}

Создаю релиз с версией 1.0.0.

![Конфигурация git-flow](image/17.png){#fig:017 width=70%}

Создаю журнал изменений. Добавляю журнал изменений в индекс.

![Конфигурация git-flow](image/18.png){#fig:018 width=70%}

Заливаю релизную ветку в основную ветку

![Конфигурация git-flow](image/19.png){#fig:019 width=70%}

Отправляю данные на github.

![Конфигурация git-flow](image/20.png){#fig:020 width=70%}

Создаю релиз на github. Для этого использую утилиты работы с github:

![Конфигурация git-flow](image/21.png){#fig:021 width=70%}

Создаю ветку для новой функциональности.

![Разработка новой функциональности](image/22.png){#fig:022 width=70%}

Создадим релиз с версией 1.2.3.

![Создание релиза git-flow](image/23.png){#fig:023 width=70%}

Обновляю номер версии в файле package.json. Ставлю её в 1.2.3.

![Создание релиза git-flow](image/24.png){#fig:024 width=70%}

Добавляю журнал изменений в индекс.

![Создание релиза git-flow](image/25.png){#fig:025 width=70%}

Заливаю релизную ветку в основную ветку

![Создание релиза git-flow](image/26.png){#fig:026 width=70%}

Отправляю данные на github.

![Создание релиза git-flow](image/27.png){#fig:027 width=70%}

Создаю релиз на github с комментарием из журнала изменений.

![Релиз](image/28.png){#fig:028 width=70%}



# Выводы

Я научился использовать продвинутые функции git, ознакомился со способами создания и changelog'a и добавления комитов с комментариями из него. 

# Список литературы{.unnumbered}

Лабораторная работа № 4
