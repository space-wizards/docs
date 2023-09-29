# Robust Station Image

Формат **RSI** (Robust Station Image) призначено для гнучкого, відкритого і зрозумілого способу <!--Додайте ще одне вихваляння, яке би тут підійшло! --> окреслення піктограм всередині листів спрайтів, подібно до формату `.dmi` в BYOND. RSI вважається "пікторамою" і може містити "стани", які є додатковими частинами цієї піктограми. Ці стани можуть визначати користувацькі прапори, кадри анімації та піктограми різних боків спрайту, що може обертатися.

RSI - це папка з назвою, що закінчується на `.rsi`, яка містить файл `meta.json` та один або декілька PNG-файлів відповідно до назв станів.

Метадані зображення (що визначають стани, анімації тощо) зберігаються у форматі JSON, у файлі `meta.json`. Власне спрайти зберігаються на листах спрайтів у вигляді PNG файлів в цій директорії. Кожному унікальному стану відповідає однойменний лист спрайтів.

## JSON

Корінь файлу JSON містить наступні значення:

Ключ | Що означає
--- | -------
`version` | Число типу integer, що відповідає версії формату RSI. Це може бути використано для ідентифікації версії RSI і дозволить коректно використовувати режими зворотної сумісності, коли це необхідно.
`size` | Розміри спрайтів всередині RSI, що зберігаються у вигляді асоціативного списку `{x: ?, y: ?}`. Це _не_ розмір PNG файлів, у яких зберігається лист зі спрайтами. Він використовується для коректного обрізання окремих спрайтів з цілого листа спрайтів.
`states` | Список _станів_, які є безумовно, найважливішою частиною RSI. Подробиці дивіться нижче.
`license` | Можна не вказувати. Дійсний [Ідентифікатор ліцензії SPDX](https://spdx.org/licenses/), що застосовується до цієї роботи.
`copyright` | Можна не вказувати. Інша довільна інформація про авторські права, така як автор, джерело, ...

### Стани

Стан - це контейнер для метаданих певного листа спрайту. У ньому зберігаються дані, пов'язані зі спрайтом, такі як затримки анімації та напрямки. Стан має відповідний лист зі спрайтами.

Стани мають поле, за яким їх можна розрізняти:

Ключ | Що означає
--- | -------
`name` | Назва стану. Може містити лише малі літери, цифри та деякі спеціальні символи (`_-`).

Різні стани не мають мати однаковий ідентифікатор. Два стани з однаковою назвою не можуть існувати.

Окрім ідентифікатора, стан має ще три інші поля, що пов'язані з різними елементами спрайта:

Ключ | Що означає
--- | -------
`flags` | Асоціативний список типу `key: object`, призначений для визначення додаткових даних. Наразі не використовується. Можна не вказувати.
`directions` | Число, що відповідає кількості напрямків, які має стан. Це має бути `1`, `4` або `8`.
`delays` | Можна не вказувати. Якщо визначено, це список зі списків затримок для анімованого стану піктограми. Кожен список у списку відповідає напрямку стану. Затримка є числам типу float і позначає секунди.

Стани завжди впорядковані в алфавітному порядку відповідно до назви їхнього файлу.

#### Directions

There are currently three supported direction types: `1` (no directions), `4` (North South East West), and `8` (North South East West plus diagonals).
These directions are ordered (for layout in the `delays` field and ordering in the sprite sheet) in the following order:

* South
* North
* East
* West
* South East
* South West
* North East
* North West

#### Sprite sheet

The PNG file accompanying a state is always the name of the state. For example, a state with name "hello" would be `hello.png` on disk.

The file contains the individual states resolved with the directions and delays of the state. The size of the file is always a multiple of the RSI's `size`. Sprites are ordered from the top left to the bottom right, always going horizontally first. The amount of sprites per row or column is always made to be as equal as possible, favoring rows to be longer than columns if the amount of states is not able to be divided perfectly.

Sprites are written grouped by direction, then writing each icon in a direction in order, so with 4 directions, ALL south states get written first, then north states, etc...

### Example JSON

Note that in practice the JSON writer probably writes the most compact JSON possible to reduce file size.

```json
{
    "version": 1,

    "license": "CC0-1.0",
    "copyright": "GitHub @PJB3005",

    "size": {
        "x": 32,
        "y": 32
    },
    "states": [
        {
            "name": "hello",
            "flags": {},
            "directions": 4,
            "delays": [
                [1, 1, 1],
                [2, 3, 4],
                [3, 4, 5],
                [4, 5, 6]
            ]
        }
    ]
}
```

## Design Goals

* Editing an RSI must be possible without proper tooling. This means no binary metadata or metadata inside PNG files.
* It must be easily diffable on GitHub.
* It must not bloat Git history too much when changes are made (prevent large file rewrites).
* One PNG One Image