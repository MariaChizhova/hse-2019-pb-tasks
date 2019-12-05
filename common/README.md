# Общее
## Содержание
1. [Содержание](#содержание)
1. [Требования к коду на Python](#требования-к-коду-на-python)
    1. [Разумная попытка](#разумная-попытка)
    1. [Блокирующее](#блокирующее)
    1. [Блокирующее, если иное не оговорено в задании](#блокирующее-если-иное-не-оговорено-в-задании)
1. [Сдача задания через git](#сдача-задания-через-git)
    1. [Начало процесса](#начало-процесса)
	1. [Исправление замечаний](#исправление-замечаний)
    1. [Последующие попытки](#последующие-попытки)
1. [Git troubleshooting](#git-troubleshooting)
    1. [В PR есть лишние коммиты](#в-pr-есть-лишние-коммиты)

## Требования к коду на Python
### Разумная попытка
1. Все присланные файлы не имеют синтаксических ошибок.
1. Предоставленные в задании тесты проходят без их изменений при запуске команды `pytest`.
### Блокирующее
1. Попытка является "разумной" (смотри выше)
1. Команда `flake8 --max-line-length=100` (с установленными `pep8-naming` и `flake8-quotes`) не выдаёт ошибок ни в одном из файлов.
1. Команда `pylint --max-line-length=100 --disable=invalid-name,missing-docstring,global-statement,too-many-lines,R --enable=simplifiable-if-statement,redefined-variable-type` не выдаёт ошибок ни в одном из файлов.
   Это требование можно ослабить, если вы предоставите практику пример, где это команда выдаёт неразумную, на ваш взгляд, рекомендацию.
1. Команда `mypy --ignore-missing-imports` не выдаёт ошибок ни в одном из файлов.
1. Все ваши тесты запускаются командой `pytest` и проходят под Windows, Linux и Mac (используйте `/` вместо `\` для разделения папок в путях, а в Python можно использовать `pathlib`).
1. В качестве shebang в Python используется `#!/usr/bin/env python3`.
1. В неисполняемых файлах shebang отсутствует.

### Блокирующее, если иное не оговорено в задании
1. Каждая содержательная команда в коде (не обработка ошибки и не вызов `main(sys.argv[1:])` должна вызываться
   хотя бы в одном тесте (неважно, юнит- или интеграционном).
   Проверяйте при помощи `pytest-cov`.
1. Должны быть указаны типы всех параметров всех функций (кроме параметров тестов `test_*`) и типы их возвращаемых значений для команды `mypy`.
1. Для каждой процедуры должен быть написан хотя бы один нетривиальный юнит-тест.

## Сдача задания через git
### Начало процесса
1. Сделайте форк этого репозитория `*-tasks`. В дальнейшем вы будете работать с ним.
1. Склонируйте форк к себе на компьютер
    ```
    $ git clone <your-fork-url>
    ```
1. Выберите задание над которым вы собираетесь работать (если у вас уже был форк, сначала убедитесь, что вы на последней версии в ветке `master` по инструкции [ниже](#последующие-попытки)):
    ```
    $ git checkout -b <your-assignment-branch>
    ```
    Конкретное название ветки указано в условии задания.
1. Сделайте задание. Для этого перейдите в директорию с заданием и напишите свой код в предоставленных файлах. "Чистая история" очень рекомендуется, но по умолчанию она не требуется.
1. Не должно быть коммитов, изменяющих какие-либо файлы, кроме явно указанных в задании, например, добавляющие папку `.idea`, файлы `*.iml` или `*.pyc`. Используйте `.gitignore` в корне репозитория.
1. После того, как вы закоммитили все изменения, отправьте их на сервер.
    * Для первой отправки ветки на сервер используйте команду:
      ```
      $ git push -u origin <your-assignment-branch>
      ```
    * В следующие используйте:
      ```
      $ git push
      ```
1. Создайте Pull Request в ветку `master` этого репозитория с нужным заголовком, указанным в условии задания.
    * В названии Pull Request не допускаются сокращения, перестановка слов, отсутствие запятой, пробелов, лишние пробелы,
      неверный регистр, написание имени транслитом, неверный порядок имени и фамилии.
    * О том, как сделать Pull Request, написано [здесь](https://help.github.com/articles/creating-a-pull-request/).
1. Убедитесь, что `@yeputons-bot` добавил к вашему PR метки, соответствующие
   номеру задания, номеру группы, а также `needs-grading` и назначил review
   на вашего преподавателя.

### Исправление замечаний
1. Не помечайте комментарии преподавателя как `Resolved`, если об этом
   нет явной договорённости.
1. При желании ответьте на замечания преподавателя индивидуально.
1. Оставьте в PR отдельное сообщение, начинающееся со строчки
   `@yeputons-bot, исправлено.`
1. Убедитесь, что `@yeputons-bot` добавил к вашему PR метку `needs-grading`
   и назначил review на вашего преподавателя.

### Последующие попытки
1. У вас уже должен быть форк и клон форка на комьютере. Если нет, то воспользуйтесь инструкцией выше.
2. Переключитесь на ветку `master`.
    ```
    $ git checkout master
    ```
3. Проверьте, что git настроен на синхронизацию с этим репозиторием:
    ```
    $ git remote -v
    ```
    Если вывод этой команды содержит `upstream https://github.com/yeputons/hse-2019-pb-tasks`, то пропустите
    следующий шаг (4).
4. Настройте git на синхронизацию с этим репозиторием:
    ```
    $ git remote add upstream https://github.com/yeputons/hse-2019-pb-tasks
    ```
5. Обновите свой форк:
    ```
    $ git fetch upstream
    ```
6. Сделайте так, чтобы ваша ветка `master` полностью совпадала с веткой `master` из этого репозитория.
    ```
    $ git merge --ff-only upstream/master
    ```
    Если это команда выдаёт ошибку, значит, вы как-то поменяли свою ветку `master` и Pull Request гарантированно не будет чистым.
7. Выполните шаги, начиная с третьего, [из инструкции выше](#начало-процесса).

## Git troubleshooting
Первым делом запустите команду `git log --branches --graph --oneline --decorate`, которая
покажет полное состояние вашего репозитория.

Также сохраните куда-нибудь все файлы в состояниях `untracked`, `modifed`, `staged`
(все, кроме `unmodified+committed`):
можно либо в отдельную папку, либо добавить их всех в `staged` и сделать `git stash`
(см. [главу 7.3 Инструменты Git - Прибережение и очистка](https://git-scm.com/book/ru/v2/%D0%98%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B-Git-%D0%9F%D1%80%D0%B8%D0%B1%D0%B5%D1%80%D0%B5%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B8-%D0%BE%D1%87%D0%B8%D1%81%D1%82%D0%BA%D0%B0)).

### В PR есть лишние коммиты
1. Скорее всего, вы увидите похожую картину:
   ```
   * 64875a6 (HEAD -> task01-grep-solution, origin/task01-grep-solution) Add unit tests for process_file
   * bced7f9 Implement grep.py
   * 38c7441 (origin/task02-git-solution, task02-git-solution) largest_heads_run.py: minor reorder of computations
   * 8daaf24 largest_heads_run.py: get_max_run: simplify calculations
   * d145832 largest_heads_run.py: get rid of unnecessary variables
   * 6a15237 largest_heads_run.py: extract get_max_run(flips) function
   * 0e60d9b largest_heads_run.py: generate list of flips in advance
   * ada2229 largest_heads_run.py: simplify update of sum of runs
   *   6a69958 (origin/master, origin/HEAD, master) Merge pull request #84 from yeputons/fix-git-push
   |\  
   | * d62596e (origin/fix-git-push) common/README: add -u flag for the first 'git push'
   |/  
   * 159f19b .travis.yml: add python3-tk
   ```
1. Убедитесь, что `HEAD` указывает на ветку, из которой вы делаете Pull Request.
   Назовём её `<new-branch>` (в примере — `task01-grep-solution`).
   Если это не так — переключитесь на эту ветку командой `git checkout <new-branch>` или `git switch <new-branch>`.
1. Убедитесь, что `<new-branch>` растёт из ветки `master`, и что в `<new-branch>` есть все нужные коммиты.
   Лишние коммиты, скорее всего, будут в начале ветки и лежать в ветке `<old-branch>` (в примере — `task02-git-solution`),
   которая будет префиксом `<new-branch>`.
1. Убедитесь, что в `master` последний коммит — не ваш, а из основного репозитория.
1. Теперь надо взять коммиты, лежащие в ветке `<new-branch>`, и не лежащие в ветке `<old-branch>`, и перебазировать
   их поверх `master` в ветку `<new-branch>`.
   Это разбирается в [3.6 Ветвление в Git - Перебазирование](https://git-scm.com/book/ru/v2/Ветвление-в-Git-Перебазирование),
   секция "более интересные перемещения".
   Есть два способа:
    * `git rebase --interactive master` и удалить строчки, соответствующие ненужным коммитам.
    * `git rebase --onto master <old-branch> <new-branch>`.
1. После этого история должна выглядеть так:
   ```
   * 165d1be (HEAD -> task01-grep-solution) Add unit tests for process_file
   * c009030 Implement grep.py
   | * 38c7441 (origin/task02-git-solution, task02-git-solution) largest_heads_run.py: minor reorder of computations
   | * 8daaf24 largest_heads_run.py: get_max_run: simplify calculations
   | * d145832 largest_heads_run.py: get rid of unnecessary variables
   | * 6a15237 largest_heads_run.py: extract get_max_run(flips) function
   | * 0e60d9b largest_heads_run.py: generate list of flips in advance
   | * ada2229 largest_heads_run.py: simplify update of sum of runs
   |/  
   *   6a69958 (origin/master, origin/HEAD, master) Merge pull request #84 from yeputons/fix-git-push
   |\  
   | * d62596e (origin/fix-git-push) common/README: add -u flag for the first 'git push'
   |/  
   * 159f19b .travis.yml: add python3-tk
   ```
1. Теперь требуется запушить ветку `task01-grep-solution`.
   Это будет переписывание истории, так как мы стёрли из неё какие-то коммиты.
   Другими словами, она уже не является надмножеством `origin/task01-grep-solution` иfast-forward не сработает.
   Для переписывания истории вызовите команду `git push --force`.
