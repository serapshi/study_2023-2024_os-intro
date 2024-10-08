---
## Front matter
lang: ru-RU
title: Выполнение 12 лабораторной работы
subtitle: Программирование в командном процессоре ОС UNIX. Командные файлы
author:
  - Павлюченков С.В.
institute:
  - Российский университет дружбы народов, Москва, Россия
date: 07 сентября 2024

## i18n babel
babel-lang: russian
babel-otherlangs: english

## Formatting pdf
toc: false
toc-title: Содержание
slide_level: 2
aspectratio: 169
section-titles: true
theme: metropolis
header-includes:
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
---

## Докладчик

:::::::::::::: {.columns align=center}
::: {.column width="70%"}

  * Павлюченков Сергей Витальевич
  * Студент ФФМиЕН
  * Российский университет дружбы народов
  * [1132237372@pfur.ru](mailto:1132237372@pfur.ru)
  * <https://serapshi.github.io/svpavliuchenkov.github.io/>

:::
::: {.column width="30%"}

![](./image/my_photo.jpg)

:::
::::::::::::::

## Цель работы

Изучить основы программирования в оболочке ОС UNIX/Linux. Научиться писать
небольшие командные файлы.

## Задание

1. Написать скрипт, который при запуске будет делать резервную копию самого себя (то
есть файла, в котором содержится его исходный код) в другую директорию backup
в вашем домашнем каталоге. При этом файл должен архивироваться одним из архиваторов на выбор zip, bzip2 или tar. Способ использования команд архивации
необходимо узнать, изучив справку.
2. Написать пример командного файла, обрабатывающего любое произвольное число
аргументов командной строки, в том числе превышающее десять. Например, скрипт
может последовательно распечатывать значения всех переданных аргументов.
3. Написать командный файл — аналог команды ls (без использования самой этой команды и команды dir). Требуется, чтобы он выдавал информацию о нужном каталоге
и выводил информацию о возможностях доступа к файлам этого каталога.
4. Написать командный файл, который получает в качестве аргумента командной строки
формат файла (.txt, .doc, .jpg, .pdf и т.д.) и вычисляет количество таких файлов
в указанной директории. Путь к директории также передаётся в виде аргумента командной строки.


# Выполнение лабораторной работы

## Создание рабочей среды и файла для первого задания

![Создание файла](image/1.png){#fig:001 width=70%}

## Код первой программы 

Написал скрипт, который при запуске будет делать резервную копию самого себя (то
есть файла, в котором содержится его исходный код) в другую директорию backup
в вашем домашнем каталоге. При этом файл архивируется архиватором tar.

![Код программы](image/2.png){#fig:002 width=70%}

## Сделал файл исполняемым

![Меняю права доступа к файлу](image/3.png){#fig:003 width=70%}

## Запуск программы

![Запуск программы](image/4.png){#fig:004 width=70%}

## Создание файла для второго задания

![Создание файла](image/5.png){#fig:005 width=70%}

## Код программы 

Написал командного файла, обрабатывающего любое произвольное число
аргументов командной строки, в том числе превышающее десять. Скрипт
может последовательно распечатывать значения всех переданных аргументов.

![Код программы](image/6.png){#fig:006 width=70%}

## Сделал файл исполняемым

![Меняю права доступа к файлу](image/7.png){#fig:007 width=70%}

## Запуск второй программы

![Запуск программы](image/8.png){#fig:008 width=70%}

## Создание файла для третьего задания

![Создание файла](image/9.png){#fig:009 width=70%}

## Код программы - аналог команды ls (без использования самой этой команды и команды dir). 

![Код программы](image/10.png){#fig:010 width=70%}

## Сделал файл исполняемым

![Меняю права доступа к файлу](image/11.png){#fig:011 width=70%}

## Запуск третьей программы

![Запуск программы](image/12.png){#fig:012 width=70%}

## Создание файла для четвертого задания

![Создание файла](image/13.png){#fig:013 width=70%}

## Код четвертой программы

Написал командный файл, который получает в качестве аргумента командной строки
формат файла (.txt, .doc, .jpg, .pdf и т.д.) и вычисляет количество таких файлов
в указанной директории. Путь к директории также передаётся в виде аргумента командной строки.

![Код программы](image/14.png){#fig:014 width=70%}

## Сделал файл исполняемым

![Меняю права доступа к файлу](image/15.png){#fig:015 width=70%}

## Запуск третьей программы

## ![Запуск программы](image/16.png){#fig:016 width=70%}


## Выводы

Я узнал много нового о bash и программирование в командной строке. Научился создавать командные файлы