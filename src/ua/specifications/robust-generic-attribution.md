# Robust Generic Attribution

Стандарт **RGA** (Robust Generic Attribution) призначений для гнучкого, відкритого і зрозумілого способу <!--Додайте ще кілька вихвалянь, бо в мене фантазія всьо.--> призначення різних метаданих, таких як ліцензування і атрибуція, для довільної кількості файлів різних типів, наприклад, звукових ефектів або прототипів. Файл RGA містить метадані для всіх файлів у тій самій директорії, що й файл RGA (не враховуючи субдиректорії). Записи в RGA-файлі містять специфічні метадані, такі як автор файлу(ів) або опис будь-яких модифікацій, зроблених до них (відповідно до більшості ліцензій Creative Commons).

RGA являє собою YAML-файл з ім'ям `attributions.yml` і містить довільну кількість записів, як зазначено нижче.

Зазвичай, щоразу, з додаванням нових файлів, додається новий запис, оскільки він, ймовірно, не міститиме тих самих метаданих, що є в існуючих записах. Однак, можна додавати файли до вже існуючого запису, якщо метадані в обох ідентичні.

## YAML

Файл RGA повинен мати ім'я `attributions.yml`. Усі значення записів беруться у подвійні лапки (`""`).

YAML може містити довільну кількість записів, що охоплюють усі файли у тій самій директорії, що й RGA файл. Доступні наступні варіанти записів:

Ключ | Що означає
--- | -------
`files` | Масив імен файлів (з розширеннями), до яких застосовується цей запис. Порядок назв файлів є довільним. Підтримується шаблонний запис `*` (тобто `*.ogg` означатиме всі OGG-файли у директорії).
`copyright` | The copyright holder and other relevant info. Any disclosure of modifications to comply with certain licenses should also go in this field.
`license` | A valid [SPDX License Identifier](https://spdx.org/licenses/) applying to all files within an entry. If a license does not have a valid SPDX identifier, `Custom` may be used but a link to the license should be provided in the `copyright` field.
`source` |  A valid URL pointing to a location where the file can be downloaded. If you are the creator of the work and don't have an alternate download location (e.g. bandcamp), provide the link to the pull request that added the file to the game. If this is a derivative work, this should be mentioned in the copyright field. If the file has only been lightly modified, just link to the original file. If the file has been heavily modified, link the modified version but provide links to any original files in the copyright field.

### Приклад YAML

```yaml
- files: ["thunderdome.ogg"]
  license: "CC-BY-NC-SA-3.0"
  copyright: "-Sector11 by MashedByMachines. Converted from MP3 to OGG."
  source: "https://www.newgrounds.com/audio/listen/312622"
- files: ["endless_space.ogg"]
  license: "CC-BY-3.0"
  copyright: "Endless Space by SolusLunes. Converted from MP3 to OGG."
  source: "https://www.newgrounds.com/audio/listen/67583"
```

## Design Goals

* Editing an RGA must be possible without proper tooling. This means no binary metadata.
* It must be easily diffable on GitHub.
* It must not bloat Git history too much when changes are made (prevent large file rewrites).
