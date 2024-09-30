```admonish warning "В процессе"
Эта страница находится в стадии разработки! Некоторая информация может быть неполной или неактуальной.
```

# Git для разработчика СС14

Если вы когда-нибудь смотрели халтурно написанное руководство по Git'у или открывали один из множества невероятно раздутых современных графических интерфейсов git'а, таких как GitKraken, вы, вероятно, понимаете, что Git может быть *очень запутанным*. Цель этого руководства - дать вам только ту информацию, которая необходима для правильной разработки для SS14, и предоставить вам ресурсы, чтобы узнать больше, если это необходимо.

Здесь немного ресурсов для изучения гита:
- [Онлайн книга от разработчиков Гита](https://git-scm.com/book/en/v2), очень полезная вещь для начинающих, которая может помочь новичкам.
- [Руководство по Git от Atlassian](https://www.atlassian.com/git/tutorials/setting-up-a-repository). Хорошие гайды для более продвинутых пользователей
- [Ёбанный Git!!!](https://ohshitgit.com/ru), список решений распространенных проблем с git в веселом формате. Может пригодиться.
- [Learn Git Branching](https://learngitbranching.js.org/?locale=ru_RU). Этот курс интерактивный и очень подробный, к его концу вы **выучите Git**. Рекомендуется, если вы уже не новичок но и не профи в Git.

## 1. Настройка самого Гита

```admonish danger "НЕ ИСПОЛЬЗУЙТЕ GITKRAKEN"
Ради всех богов, хостов и сисадминов, не устанавливайте GitKraken или GitHub Desktop. Я не испытывал ничего, кроме бесконечной боли, пытаясь помочь людям, использующим их. Я знаю, что GitKraken выглядит профессионально, а GH Desktop - красиво и просто, но, пожалуйста, не используйте их, если вы не знаете, что делаете.
```

Если вы следовали нашему руководству по **настройке среды разработки**, то, вероятно, у вас уже установлен Git. Если нет, перейдите на [их сайт](https://git-scm.org) и установите его прямо сейчас. Это позволит установить сам Git, а также Git Bash (если вы выберете эту опцию) - один из многих способов использования Git. 

Если вы работаете на Линуксе, то, скорее всего, будете использовать Git через терминал или выбранную вами IDE, и, скорее всего, он у вас уже установлен.

Я настоятельно рекомендую хотя бы попробовать Git Bash, но есть и более дружелюбные альтернативы, которые я также покажу здесь:

- [TortoiseGit](https://tortoisegit.org/) -- старый, но хороший графический визуализатор Git, который отображает информацию в проводнике и делает базовые вещи более простыми.
- [SmartGit](https://www.syntevo.com/smartgit/) -- полнофункциональный графический интерфейс Git, хорошо настраиваемый и простой в использовании.

После того как я написал этот гайд я попробовал еще пару вариантов, и среди них есть и другие очень, очень хорошие программы:

- [Fork](https://git-fork.com/) -- быстрый и чрезвычайно эргономичный графический интерфейс, мой личный фаворит. «Платная», но она такая же „небесплатная“ как WinRAR, так что по сути она бесплатная.
- [Sublime Merge](https://www.sublimemerge.com/) -- очень похож на Fork, выглядит и ощущается отлично, и я получал много рекомендаций по его использованию, хотя и не использовал его так много.

Большинство IDE имеют ту или иную форму интеграции с Git. Интеграция Гита [JetBrains Rider](https://www.jetbrains.com/rider/) действительно хороша (и я лично рекомендую Rider для всего, что связано с разработкой в 14 станции). Я не рекомендую Git в Visual Studio, потому что он... не особо хорош

Пока вы здесь, установите `Python 3.7+`, если у вас его еще нет. Вы можете сделать это [здесь](https://www.python.org/) для Windows и Mac, а если вы на Linux, то у вас почти наверняка уже установлен Python. Если нет, разберись сам, тупой придурок.

<hr>

```admonish danger "Сохранность Email и Имени"
Когда вы [настраиваете свои `user.name` и `user.email`](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup#_your_identity), знайте, что они будут публично отображаться во всех создаваемых вами коммитах. Если вы хотите сохранить конфиденциальность своей информации, вы можете установить `user.name` на ваше имя пользователя вместо вашего настоящего имени, а `user.email` на тот, который предоставляет GitHub, когда в [GitHub Email Settings](https://github.com/settings/emails#primary_email_select_label) установлен флажок [`Keep my email addresses private`](https://github.com/settings/emails#toggle_visibility).
```

Теперь, когда у вас установлен Git, я рекомендую вам сначала немного почитать о его основах и познакомиться с любым git-клиентом, с которым вы работаете, будь то командная строка (Git Bash) или что-то другое.

Мы рассмотрим процесс создания окружения Git для Space Station 14, чтобы вы могли **внести свой вклад в проект через Pull Request, создать собственную кодовую базу** или просто **посмотреть историю развития проекта**.

### 1.1 Почему мы вообще используем Git?

Git - это **программа контроля версий**. По сути, это простой способ отслеживать изменения в коде и управлять этими изменениями без головной боли. Это бесценный инструмент для разработки программного обеспечения, потому что он позволяет легко вносить новые изменения, просматривать различные изменения, видеть, кто внес изменения, и т. д. без необходимости координировать и табулировать все самостоятельно.

GitHub - это онлайн-сервис, на котором размещаются Git **репозитории** (кодовые базы) для удобства совместной работы. Он идеально подходит для такой кодовой базы, как SS14, с большим количеством участников и большой историей. Это также означает, что у нас *открытый код* - любой может зайти на наш GitHub и скачать его!

## 2. Настройка репозитория

Как я уже говорил, репозиторий - это просто кодовая база. Репозитории содержат несколько **ветвей**, а эти ветви содержат различные **коммиты**. Вы, возможно, слышали об этих двух понятиях - я расскажу о них подробнее позже.

**Удалённый** репозиторий - это просто репозиторий, который находится на серверах GitHub. То что он называется удалённым не означает что его выкинули! **Локальный** репозиторий - это тот, который находится на вашем компьютере.

### 2.1 Создание своего удалённого репозитория

Во-первых, давайте создадим наш собственный удаленный репозиторий Space Station 14. Для этого, конечно, вам понадобится учетная запись на GitHub. "Форк"(Fork) таким образом просто означает, что вы копируете всю историю репозитория и изменения в свой собственный удаленный репозиторий, чтобы вы могли свободно вносить изменения в код.

Ваш удаленный репозиторий не будет автоматически синхронизироваться с изменениями из оригинального репозитория SS14 - вам придется делать это самостоятельно, а как это делать я расскажу чуть позже.

Перейдите в [репозиторий Space Station 14](https://github.com/space-wizards/space-station-14) и нажмите на кнопку «Fork», которая помечена на скриншоте:
![](https://i.imgur.com/lAHNHdD.png)

Там вас спросят, где сделать форк и как его назвать - просто зайдите в свой обычный аккаунт и назовите его как угодно! Я бы выбрал `space-station-14`, если вы просто хотите помочь в разработке.

### 2.2 Создание своего локального репозитория

Теперь нам нужно загрузить наш удаленный репозиторий на наш компьютер (это называется **клонирование**), чтобы мы могли добавить ~~20 пар клоунских ботинок в каждый шкафчик~~ некоторые изменения в нем. Технически вы *можете* изменить удаленный репозиторий (на GitHub есть несколько хороших инструментов), но наличие его на вашем компьютере означает, что вы используете IDE вроде Visual Studio или Rider для сборки игры и запуска тестов, а также для удобной работы с Git.
Для каждого шага будут приведены скриншоты и инструкции для Git Bash, SmartGit и TortoiseGit под Windows.

Перейдите в то место на вашем компьютере, где вы хотите разместить локальный репозиторий, и:
<details><summary>TortoiseGit</summary>
<p>

Щелкните правой кнопкой мыши, чтобы увидеть контекстное меню TortoiseGit:

![](https://i.imgur.com/QGmrQmH.png)

</p>
</details>

<details><summary>SmartGit</summary>
<p>

Откройте SmartGit и перейдите в нужное место, затем:

![](https://i.imgur.com/C3JBYR6.png)

</p>
</details>

<details><summary>Git Bash</summary>
<p>

Щелкните правой кнопкой мыши:

![](https://i.imgur.com/kIYnm16.png)

</p>
</details>

<hr>

Затем мы введем команду для клонирования **нашего** удалённого репозитория - не репозитория `space-wizards/space-station-14`.
<details><summary>TortoiseGit</summary>
<p>

![](https://i.imgur.com/3HzCnjm.png)
![](https://i.imgur.com/a7vhKcC.png)


</p>
</details>  

<details><summary>SmartGit</summary>
<p>

![](https://i.imgur.com/YyJm5fx.png)


</p>
</details>

<details><summary>Git Bash</summary>
<p>

![](https://i.imgur.com/Xn4AQLf.png)

Затем переключитесь на папку вашего репозитория, используя:
``cd space-station-14`` 

(Название папки может отличаться, если вы клонировали другой репозиторий, но оно почти всегда совпадает с именем репозитория)

Каждая команда в Git выглядит примерно так - `git` и затем ключевое слово `add`, `commit`, `pull` и т.д.

</p>
</details>

<hr>

После этого у вас будет локальный репозиторий, который теперь можно изменять! Однако вам еще предстоит выполнить некоторые настройки.

### 2.3 Боль с сабмодулями

**Обратите на это внимание!** Если вы не сделаете этого, то при попытке скомпилировать игру вы получите множество странных ошибок.

В Space Station 14 есть *множество* субмодулей - в первую очередь, наш движок RobustToolbox. Субмодули - это просто репозитории внутри репозитория, и их нужно обновлять вручную. Или нет?

У нас есть автоматическая программа обновления подмодулей, так что вам не нужно постоянно запускать `git submodule update --init --recursive` (команда для ручного обновления подмодулей).

Запустите `RUN_THIS.py` внутри репозитория, который вы скачали, с помощью Python(ВЫ же установили Python как я просил в начале этого гайда?). Желательно также из терминала введите `python RUN_THIS.py` или `python3 RUN_THIS.py`. Это должно занять несколько секунд, так что если все мгновенно прекратится, вы, вероятно, не используете Python 3.7+ или что-то в этом роде.

Если вы работаете под Windows и при попытке выполнить приведенную выше комбинацию действий получаете перенаправление в Microsoft Store или сообщение в терминале о том, что Python не установлен, вам нужно отключить ярлык Microsoft, который может вызывать эту проблему. Это можно сделать, найдя в поиске Windows пункт `Manage App Execution Aliases` и отключив две ссылки Python.

Если вы все же хотите модифицировать движок напрямую или обновлять субмодуль вручную (автообновление иногда доставляет неудобства), создайте файл DISABLE_SUBMODULE_AUTOUPDATE в директории BuildChecker/.

Если вам по какой-то причине понадобится вручную обновить RobustToolbox, вы можете использовать `cd RobustToolbox; git checkout v0.4.87` (замените `v0.4.87` на нужную вам версию RobustToolbox), а затем вы можете использовать `cd..\`, чтобы вернуться в репозиторий SS14. Это также пример использования `cd` для навигации по файлам, не выходя из командной строки.

## 3. Настройка удалённых репозиториев
Когда вы клонировали удалённый репозиторий, в ваш локальный репозиторий автоматически был добавлен **ремоут**. **Ремоуты** - это именованные URL-адреса удалённых репозиториев, которые Git отслеживает, чтобы вы могли делать такие вещи, как скачивать (pull) новые изменения в коде или загружать (push) код в ваш форкнутый репозиторий. 

В этом случае автоматически добавляемый удалённый репозиторий называется `origin` и указывает на `https://github.com/[имя пользователя-здесь]/space-station-14` (или как вы назвали удаленное хранилище).

Одна проблема: у нас нигде нет ссылки на оригинальный удаленный репозиторий `space-wizards/space-station-14`! Как же мы сможем обновить наш локальный репозиторий без неё? Поэтому давайте убедимся, что мы перешли в папку нашего локального репозитория, и добавим новый ремоут:

<details><summary>TortoiseGit</summary>
<p>

![](https://i.imgur.com/yANaYWI.png)
![](https://i.imgur.com/cjbhMEN.png)


</p>
</details>

<details><summary>SmartGit</summary>
<p>

![](https://i.imgur.com/LXCpgVo.png)
![](https://i.imgur.com/ZHIHPJC.png)


</p>
</details>

<details><summary>Git Bash</summary>
<p>

![](https://i.imgur.com/00ETpii.png)

</p>
</details>

<hr>

Все, что это делает, - добавляет новый удаленый репозиторий с именем `upstream`, который указывает на исходный репозиторий `space-wizards/space-station-14`. Теперь мы можем получать обновления из основного репозитория, когда захотим! (о том, как это сделать, читайте ниже). 

Принято называть удалённый репозиторий, указывающий на исходный репозиторий, как `upstream`, но технически вы можете называть его как угодно. Однако я буду ссылаться на него как на «upstream», и это терминология, которую также используют руководства Git.

**Дополнение для разработчиков форков:** Если репозиторий, в который вы хотите внести вклад, настроен как прямой форк (IE: GitHub показывает метку «forked from» под именем репозитория), то вам дополнительно нужно добавить этот форк в качестве удаленного (но если форк не настроен таким образом, вы можете проигнорировать это). Вы можете сделать это аналогично тому, как вы добавили upstream в качестве remote (просто используйте ссылку на GitHub форка в качестве URL remote), но не забудьте заменить имя remote `upstream` на любое имя, которое вы считаете подходящим. Для этого ваш собственный форк не обязательно должен быть форком форка; важно лишь, чтобы история коммитов в отдельных ветках, которые вы отправляете на свой собственный удалённый ресурс, совпадала с историей коммитов того, куда вы собираетесь добавлять свои изменения.

```admonish warning title="Перед тем как приступить к работе над своим первым PR в репозитории space-wizards"
Убедитесь, что вы прочитали [Freezes & Restrictions](https://github.com/space-wizards/space-station-14/issues/8524) и удостоверились, что ваша идея не попадает под заморозку, или что для вашего PR требуется какое-то предварительное условие. 
```

## 4. Ветвление и коммиты

Ветви и коммиты - две самые важные концепции в Git, и большая часть вашей работы будет вращаться вокруг них.

### 4.1 Что такое этот ваш коммит?


Как я уже говорил, **коммиты** - это просто упакованные изменения в коде. Как разработчик, вы выбираете, какие изменения войдут в коммит и когда их фиксировать.

Коммиты имеют автора, временную метку создания, сообщение и некоторые изменения кода. У них также есть длинный «хэш коммита», уникальный идентификатор, используемый для ссылки на разные коммиты.

Коммиты - это то, как строится история. Вы можете просмотреть историю каждого коммита, сделанного в репозитории SS14 с самого начала, что очень здорово:

![](https://i.imgur.com/HQDdw6h.png)

(выполняется с помощью `git log --reverse`)

### 4.2 Что такое это ваша ветка(бранч)?

**Ветки** очень, очень важны. По сути, это просто список изменений в коде (коммитов). По умолчанию используется ветка 'master', и все наши серверы используют эту ветку для компиляции кода. 

Вы практически всегда находитесь "в ветке", когда работаете с кодом, и вы можете легко переключать ветку, в которой работаете.
Как правило, ветки называются по имени того, над чем вы собираетесь в них работать, но на самом деле не имеет значения, как они называются.

Вы можете создавать столько веток, сколько захотите. Когда вы создаете ветку, она «отходит»  (нифига себе, правда?) от текущей ветки, на которой вы находитесь, и становится полностью независимой, в которую вы можете добавлять коммиты. 

![](https://i.imgur.com/ByMugxu.png=500x300)

На этой диаграмме каждый маленький узел - это отдельный коммит, а каждый цвет - отдельная ветвь.

#### Объединение веток

Ветви важны, потому что они могут быть **слиты** вместе. Процесс слияния также называется мердж (от англ. merge). Именно так функции интегрируются в основную ветку `master`. **Слияние** означает «взять коммиты с новыми изменениями кода из этой ветки и применить их к другой ветке с другой версией кода».  Вы можете объединить две любые ветки.

Иногда это не проходит гладко, потому что обе ветки изменяют одну и ту же часть файла противоречивыми способами, и в этом случае вы получите **мердж конфликт** - подробнее об этом в дополнениях.

Pull Requests(в русском сообществе их обычно называют ПРы) от GitHub на самом деле является «запросом на мердж» - вы говорите, что хотите объединить коммиты в вашей ветке с другой веткой, обычно `master`. Подробнее об этом позже.
ПРы очень хорошо отображают всю эту информацию:

![](https://i.imgur.com/YAOWX5R.png)
![](https://i.imgur.com/nWWy3J4.png)

В этом пулл реквесте Swept начал с создания новой ветки. Поскольку теперь у него была свежая ветка, свободная от помех, он начал работать над функцией и создавал коммиты для «сохранения прогресса», когда считал это необходимым. Эти коммиты добавлялись в ветку последовательно, и вы можете видеть эволюцию ветки по мере написания кода. Подробнее о запросах на исправление мы поговорим позже.

#### Но почему я должен это все делать?

Технически, конечно, вы можете просто сделать всю свою работу в ветке `master` и отправлять запросы оттуда. Но создание разных веток позволяет легко понять, где вы находитесь, сколько изменений вы внесли, и дает возможность работать над несколькими функциями одновременно.

Также мы закроем ваш PR, если он будет из вашей ветки `master` (это может легко привести к проблемам), так что не делайте этого.

### 4.3 Создание и работа с ветками

Создавать ветки довольно просто. Давайте создадим новую ветку под названием `smeshnoye-izmenenie`:

<details><summary>TortoiseGit</summary>
<p>

![](https://i.imgur.com/OGkblCk.png)
![](https://i.imgur.com/ZPfzFcm.png)

</p>
</details>

<details><summary>SmartGit</summary>
<p>

![](https://i.imgur.com/pK1oyfz.png)
![](https://i.imgur.com/5MZ6Ocv.png)

</p>
</details>

<details><summary>Git Bash</summary>
<p>

![](https://i.imgur.com/kOc9rfe.png)

Вы можете заметить, что название в скобках (master) изменился на (funny-feature)! Невероятно!

`-b` в `git checkout` здесь означает «проверить эту ветку, и создать её, если она не существует».

</p>
</details>

<hr>

Теперь вы можете свободно работать с этой веткой по своему усмотрению, не боясь испортить важную мастер-ветку.

Переключаться между ветками довольно просто: когда вы это делаете, ваши локальные файлы и папки будут изменены в соответствии с веткой, поэтому Git будет кричать на вас, если у вас есть локальные изменения, а вы пытаетесь сменить ветку.

Меняем ветку:

<details><summary>TortoiseGit</summary>
<p>

![](https://i.imgur.com/UThKrCK.png)

</p>
</details>

<details><summary>SmartGit</summary>
<p>

![](https://i.imgur.com/fzC1pVm.png)

</p>
</details>

<details><summary>Git Bash</summary>
<p>

![](https://i.imgur.com/DqWEdY5.png)

</p>
</details>

<hr>

Затем внесите любые локальные изменения! Это не имеет значения. Создайте новый файл, удалите всё, измените одну строку в файле и т. д. Это не повлияет на вашу `master` ветку, потому что теперь вы находитесь на ветке `funny-feature`!

### 4.4 Staging and committing changes to your branch

One more important thing: Before you can `commit` your changes, you have to `add` your changes to the **staging area**. All this means is that you're specifying which files you want to commit. This is helpful, because you *almost never* want to commit submodule changes, so you avoid that by not adding them to the staging area. 

As mentioned before, commits always come with a message, which is just a short, imperative description of what's being done in that commit. Or you can be a chad and name every commit "changes stuff", up to you.

If you want to see what you've currently changed, and what's in the staging area, it's pretty easy:

<details><summary>TortoiseGit</summary>
<p>

![](https://i.imgur.com/xmZKKWJ.png)

TortoiseGit also shows changed files/folders (a red icon in the bottom right) in the Windows Explorer which is really nice and why I have it installed in the first place.

</p>
</details>

<details><summary>SmartGit</summary>
<p>

![](https://i.imgur.com/ROsurs1.png)

This is assuming you installed SmartGit with the option that the main window shows diffs and status. If you didn't, I don't really know where it is.

</p>
</details>

<details><summary>Git Bash</summary>
<p>

![](https://i.imgur.com/UeMjAHj.png)

</p>
</details>

<hr>

Now that you've verified that all of these changes look good, we'll add them to the staging area and commit them (some Git GUIs do this in one step)

<details><summary>TortoiseGit</summary>
<p>

![](https://i.imgur.com/ltIASro.png)
![](https://i.imgur.com/BIa9r6c.png)

</p>
</details>

<details><summary>SmartGit</summary>
<p>

![](https://i.imgur.com/RYUL7u3.png)
![](https://i.imgur.com/Du7HqRV.png)

</p>
</details>

<details><summary>Git Bash</summary>
<p>

![](https://i.imgur.com/mpKk5L1.png)

</p>
</details>

<hr>

Woo, we've committed our changes to a branch! Now that they're committed, they're in the history of the branch forever (sort of). We can do a lot of things now: merge our `funny-feature` into our local `master` branch (if we wanted, for some reason), upload (push) our `funny-feature` branch to our remote repository, or nuke the branch entirely (among other things). We'll opt for pushing the branch and making a pull request now.

## 5. Pushing and making a PR

A **pull request** is a GitHub-specific thing. It just means that you want a codebase to merge your changes on one of your branches into one of their branches--usually to their `master` branch. Before we can do this, our remote GitHub repository (origin) needs to know about the beautiful branches and commits we've created locally, so we upload or **push** those changes to the remote.

### 5.1 Pushing commits

It's pretty easy to push our changes now that we've committed them. Be aware that, when using these commands, Git is probably going to ask for your GitHub credentials so that it can verify that you're allowed to push to that remote.

When pushing changes, we specify the *remote* repository that we're pushing to and the *local* branch that we're pushing. Simple enough.

Pushing our branch to our remote repository (origin):

<details><summary>TortoiseGit</summary>
<p>

![](https://i.imgur.com/bWS5Kdk.png)
![](https://i.imgur.com/Irv1e5k.png)

Selecting 'push all branches' does what it says on the tin. Can be useful.

</p>
</details>

<details><summary>SmartGit</summary>
<p>

![](https://i.imgur.com/s82VnNn.png)
![](https://i.imgur.com/VP8PuCq.png)

</p>
</details>

<details><summary>Git Bash</summary>
<p>

![](https://i.imgur.com/7FJqzkL.png)

</p>
</details>

### 5.2 Making a pull request

Now, the fun part. We'll go to GitHub now and make a pull request for our funny feature.

![](https://i.imgur.com/YNmEMtG.png)

Add a description, a nice title, some screenshots, and hopefully it gets merged.

## 6. Updating our repository

Maybe it's been a while, a week or two, since your last pull request, and you'd like to make another. Before you do anything, you need to download (**pull**) the code changes from the main SS14 repository into your local repository. If you don't, you'll have out-of-date code and your local changes may not be accurate to how the game will actually run--you might even get **merge conflicts** when you try to PR.

There are two ways to update your repository. Both methods assume you have the `upstream` remote set up properly--if not, go back to earlier in the guide. And of course, if you're developing for a downstream, then you'll want to substitute `upstream` for whatever you named the downstream repo in step 4, to make sure that you're working with that downstream's files instead of upstream's. Make sure you *always* go through the update process when switching between contributing to a fork, and contributing to upstream, otherwise you'll inevitably end up either PRing the entire history of a downstream to upstream, or making PRs to downstream that immediately conflict.

The first method, **fetch+merge**, gives you more control but can be confusing. The second method, **pulling**, is simple and easy but doesn't give you much control. However, pulling is usually all you need.

### 6.1 Fetch + merge method

**Fetching** refers to downloading the new branches and commits from a remote repository--but not doing anything with them just yet (nothing locally will be changed). After we fetch changes from our `upstream` remote (the main SS14 repository), we'll merge them into our local `master` branch.

When you fetch a remote, it downloads those branches to your local repository and prepends them with the remotes name and a slash. So, when you fetch `upstream`, it'll make a branch called `upstream/master`. As a bonus, you can checkout this remote branch directly if you'd like, and even create a local branch based off it, which is especially useful if you're working with more than just upstream.


First, let's fetch from our `upstream` remote. It'll take a little bit to complete.

<details><summary>TortoiseGit</summary>
<p>

![](https://i.imgur.com/3cWun8b.png)
![](https://i.imgur.com/XGgXRY0.png)

Make sure you select `upstream` and not origin!

</p>
</details>

<details><summary>SmartGit</summary>
<p>

![](https://i.imgur.com/CNFFJJ8.png)

I think smartgit fetches from all remotes when you click this?????

If it doesn't and it just fetches from origin, go to the bottom left and do this:

![](https://i.imgur.com/8rF0tz5.png)

</p>
</details>

<details><summary>Git Bash</summary>
<p>

![](https://i.imgur.com/aJvW9PX.png)

Here nothing happened because I just fetched, but it'll take a while.

</p>
</details>

<hr>

Now, we'll merge those changes we just downloaded into our `master` branch. You don't have to merge into master here; you can merge into another branch, too. If you just wanted to 'fast-forward' update one of your branches to make sure your PR is up to date, you can merge into that branch instead.

Check out the branch you want to merge to. Then,

<details><summary>TortoiseGit</summary>
<p>

![](https://i.imgur.com/8lUaEFt.png)
![](https://i.imgur.com/7BvBPYY.png)

</p>
</details>

<details><summary>SmartGit</summary>
<p>

![](https://i.imgur.com/n8cc2DN.png)
![](https://i.imgur.com/aRSawAo.png)

</p>
</details>

<details><summary>Git Bash</summary>
<p>

![](https://i.imgur.com/H2L8pOp.png)

You can also `git merge upstream/master [branch-to-merge-to]

</p>
</details>

### 6.2 Pull method

**Pulling** refers to **fetching** (downloading) the new branches and commits from a remote repository, and then merging them into a branch. Pulling is often easier because Git has a nice system for automatically figuring out which remote you want to fetch from (but it doesn't always work cleanly). 

Pulling is usually simpler and a lot easier to do.

We'll **pull** from our `upstream` remote (the main SS14 repo) and tell it to merge into our local `master` branch.

First, checkout your `master` branch. We covered this earlier. Then,

<details><summary>TortoiseGit</summary>
<p>

![](https://i.imgur.com/XMUt6cv.png)
![](https://i.imgur.com/NHVlZ4W.png)

</p>
</details>

<details><summary>SmartGit</summary>
<p>

![](https://i.imgur.com/ANqpcph.png)
![](https://i.imgur.com/kvv058A.png)
![](https://i.imgur.com/k0scDB8.png)

</p>
</details>

<details><summary>Git Bash</summary>
<p>

![](https://i.imgur.com/OfHut9Y.png)

</p>
</details>

<hr>

If either method went well, you've successfully updated your master branch (or whichever branch you chose to update)! Do this regularly, and always before you start work on a new branch.

# Addendums

## 1. Things to keep in mind

You've more or less learned the workflow for developing features for SS14 Git-wise, but here's some things I'd really like to hammer into your mind:
- When creating a new feature, *always always always* create a new branch off of `master` before committing anything. If you accidentally commit your physics changes to your bike horn branch, you're not in for a fun time, but it is fixable (see Oh Shit, Git?! above)
- **Never, ever commit RobustToolbox or any submodules like Lidgren.Network** unless you know what you're doing. In the top-level local repository, these submodules are considered 'files', so it's easy to accidentally stage and commit them. Do not do this. See below for how to fix your fuckups if it happens.
- If you need further help with Git, feel free to ask in the SS14 Discord in #howdoicode.

## 2. A quick example workflow

To get everything in your head and to summarize it all, here's an example workflow for making several pull requests using Git Bash commands.

```python
git checkout master # Before we create a new branch, we should be on master.
git fetch upstream # We'll fetch any new changes from the SS14 repo..
git merge upstream/master # ..and merge them into our master branch.

git checkout -b my-new-feature # Make a new branch for the feature
...local changes later...
git add -A # Add all of our local changes to the staging area
git commit -m "Fix spaghetti explosions" # Commit them
git push origin my-new-feature # and push them to our remote

# Now, I want to work on a different pull request.

git checkout master

# It hasn't been too long, and nothing important was merged,
# so I won't fetch and merge changes again--just a new branch.

git checkout -b another-feature
...local changes later...
git add -A
git commit -m "Deletes nuclear operatives"

# I committed, but then I realized my commit was entirely wrong 
# and i'll take it up later.

git revert HEAD
git checkout master

...a week later...

# A lot of new stuff was merged, so let's update our branch.

git fetch upstream
git merge upstream/master master
git checkout another-feature
git merge master

# Now we'll make changes and push again, this time correctly.

...local changes later...
git add -A
git commit -m "Adds Highlander gamemode"
git push origin another-feature

# Made both PRs, both were merged, so we're done here

git checkout master
git branch -d my-new-feature # Delete both old branches
git branch -d another-feature

```

# Glossary: The Inner Machinations of Git

Just for reference, here's a little glossary of Git concepts and terms explained in a little more detail, all in one place.

- **'Branches'** are self-contained versions of the codebase that you can add commits to. The default branch is **master**, but you can make as many as you like.
- **'Repositories'** are essentially just folders where you can use Git to make changes and keep track of changes made. Local repositories are repositories you have on your computer, and remote repositories are repositories that live on websites like [GitHub](https://github.com/space-wizards/space-station-14). Repositories are made up of a lot of branches.
- **'Remotes'** are names for and links to remote repositories that your local repository can use.
- **'Submodules'** are repositories that are located inside another repository.
- **'Forks'** are repositories that are based on another repository. If you're going to make a pull request to the SS14 repo, you need to fork it first.
- **'The working tree'** is just every file and folder and what not that's in the repository.
- **'Staging'** means adding (with `git add`) changes from your working tree into the 'staging area', where  some actions can be performed on it
- **'Commits'** are snapshots of the repository's working tree at a given time. Basically a save point. A 'commit' is just a list of files that have been changed from the last commit, and the changes that are 'committed' are the changes that you've 'staged'.
- **'Checking out'** is the act of switching to another branch so you can mess with it or look at its changes locally.
- **'Merging'** is the act of integrating the changes from one branch into another branch.
- **'Merge conflicts'** occur when integrating the changes from one branch into another can't be done automatically because they both change the same area in a file, or their changes are mutually exclusive in some other way.
- **'Fetching'** means getting the branches and commits of a remote repository, but not actually.. doing anything with them yet. You'll just have them updated for if you want to checkout or merge them later.
- **'Pulling'** is the act of integrating changes from a remote repository's branch into your local branch.
- **'Pull requests'** are a GitHub-specific action that allow you to request that your local branch and all of its changes is merged into another repository's branch.
- **'Pushing'** is the act of integrating your local changes into a remote repository.

There are way more commands and concepts than this, but this is all you *really* need to know for basic development work.


# Appendix A: Helpful tips and tricks

There's some stuff I didn't cover, but you'll almost inevitably have to do at some point. I'll cover these all **exclusively as git commands in Git Bash** quickly, but they're not too hard to figure out in the other programs (same keywords, just look for those). I recommend using their specific guides because I don't know TortoiseGit / SmartGit / GitKraken / Github Desktop well enough to help you with more advanced stuff.

One note since it comes up a lot here: **`HEAD` is a fancy name for the commit that you're currently on**. Nothing more than that. Branches are also technically fancy names for commits, but you don't need to know that yet.

A lot of these can be found probably more eloquently in Oh Shit, Git?! (see resources above)


## Resolving merge conflicts

*WIP i'll write a better guide for this later because it's important*

A nasty little maintainer has told you to 'resolve conflicts' or your PR 'wont be merged'. What an asshole! Thankfully, it's not too hard.

First, you're going to want to update your local `master branch`. See above for how to do that.

When you run `git merge master [local branch]`, it'll either do it cleanly (woohoo) or tell you you have to resolve conflicts (wahhhh). 

All you need to do to resolve conflicts manually is go into the files that are conflicting, remove all the `>>>>HEAD` and `===== <<<<master` nonsense (just notates where the changes originated) and then edit the file so that it properly integrates both sets of changes. Sometimes this is easy, sometimes it's hard. If it's hard, you probably know what you're doing. After that, just `git commit`.

Atlassian has a really good guide for this [here](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts)

## Checking history

`git log --oneline` is your friend. It shows short commit hashes (unique IDs for commits), their messages, and their branches and tags.

## Getting rid of local changes

You might have accidentally made changes you didn't want to, and you don't want to bother with making an entirely new branch or something--but you haven't committed those changes yet.

```
git reset --hard HEAD
```

This just means 'change the working tree to the current commit, before any local changes. Or else.' **You can't retrieve those local changes if you do this, so be wary.**

## Unstaging changes

Ah shit, I just staged RobustToolbox by accident. No fear!

```
git reset HEAD [file]
```

Alternatively, to unstage everything:

```
git reset HEAD
```

## Reverting a commit you made

Oh shit, your xenomorph erotica made its way into a commit/you accidentally committed a submodule! What now? Well, there's two solutions:

```
git revert HEAD
```

This makes a new commit undoing the current commit, and then commits it. Hehe commit. 

If you want to undo a different commit, you can check its hash in `git log --oneline` and then call `git revert [commit hash]`. Git has a more robust system for doing this; you can do `git revert HEAD~1` to undo the commit before your current one or `git revert HEAD~2` to revert the one before that. The `~1` just means '1 commit before HEAD'.

Alternatively,

```
git reset --hard HEAD~1
```

**I don't recommend doing this unless you're fully aware of what you're doing.**

For when you REALLY don't want anyone to know about that xenomorph erotica you just made. This method rewrites history, so it isn't the best for a collaborative environment. If you do this, you'll need to force push (`git push origin [branch] --force`) or else it won't work. Force pushing can be dangerous, so again, be sure you know what you're doing.


## Checking out a PR's changes locally

Ok, this one is a little difficult. There's a couple ways to do this:

### Github CLI

Install github's fancy CLI and do this:

```
gh pr checkout [pr number]
```

Neat.

### Changing .git/config

Go into your .git folder (hidden by default--may need to enable showing hidden folders in Windows), and open up the 'config' file. There should be a bit that looks something like:

```
[remote "upstream"]
	url = https://github.com/space-wizards/space-station-14
	fetch = +refs/heads/*:refs/remotes/upstream/*
```

Add a line to this that reads `fetch = +refs/pull/*/head:refs/remotes/upstream/pr/*`, so that section should now look like:

```
[remote "upstream"]
        url = https://github.com/space-wizards/space-station-14
        fetch = +refs/heads/*:refs/remotes/upstream/*
        fetch = +refs/pull/*/head:refs/remotes/upstream/pr/*
```

Now, `git fetch upstream`. This method is great if you're a maintainer, but it also.. fetches every branch that's still up from every PR that's been opened, so not fantastic if you just wanted one thing. From here, you can `git checkout upstream/pr/[pr number]` to check out their branch. This is basically what GitHub CLI does but less sophisticated.

### Adding a new remote

This method kinda sucks because it takes a while but if you want to check out someone else's fork of the game and their branches it's pretty nice.

Not actually that hard but its confusing if you don't know Git very well. Set up a remote to the user's remote repository, fetch their branches, and then checkout their branch:

```
git remote add [username] https://github.com/[username]/space-station-14
git fetch [username]
git checkout [username]/[branch name]
```

This also lets you make PRs to their remote branch, if you so desired.
