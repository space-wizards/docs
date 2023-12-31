# Поварская книга администратора

## Удаление УЧ и генератора сингулярности
```
    entities named "PA .*" do delete $ID
    deleteewi SingularityGenerator
```
## Снять проклятия со шкафчиков
`entities with CursedEntityStorage do rmcomp $ID CursedEntityStorage; addcomp $ID EntityStorage`
## Удалить все роли призраков
`entities with GhostTakeoverAvailable do rmcomp $ID GhostTakeoverAvailable; rmcomp $ID Mind`
## Очистка от различных частей тела
`entities with MapGrid children with BodyPart do delete $ID`
## Разоружить весь калий на станции
`entities hasreagent Potassium do delete $ID`
## Удалить все изолирующие перчатки выбранного персонажа
`entities with Mind named "NAME GOES HERE" rchildren named "insulated gloves" do delete $ID`

# Роли призраков
## Разумные автоматы
`entities with Advertise do makeghostrole $ID "$NAME" "You're a vending machine, use your speaker to annoy people."; rmcomp $ID Advertise`
## Разумное мыло
`entities with Slippery prototyped SoapOmega do makeghostrole $ID "$NAME" "You're a bar of soap. Slip absolutely everyone."; addcomp $ID MobState; addcomp $ID PlayerMobMover; addcomp $ID PlayerInputMover`
## Пожалуйста, не надо
`entities with Item do makeghostrole $ID "$NAME" "You're a random, talking item. What the fuck?"; addcomp $ID MobState; addcomp $ID PlayerMobMover; addcomp $ID PlayerInputMover`
## Ваше сердце этого больше не выдержит
`entities with Mechanism do makeghostrole $ID "$NAME" "You are some unfortunate soul's $NAME"`
## Призраколярность
`entities with Singularity do makeghostrole $ID "Singularity" "FUCK"; addcomp $ID MobState; addcomp $ID MovementIgnoreGravity; addcomp $ID PlayerInputMover; addcomp $ID PlayerMobMover`

# Сделает всех несчастными
## Абьюз проклятых шкафчиков
### Проклятые шкафчики
`entities with EntityStorage named ".*closet$|^.*locker" do rmcomp $ID EntityStorage; addcomp $ID CursedEntityStorage`
### Ожившие шкафчики
`entities with EntityStorage named ".*closet$|^.*locker" do rmcomp $ID EntityStorage; addcomp $ID CursedEntityStorage; makeghostrole $ID "$NAME" "You're a haunted locker. Consume people."; addcomp $ID MobState; addcomp $ID PlayerMobMover; addcomp $ID PlayerInputMover`
## Баловство с доступами
### День полного доступа
`entities with AccessReader do rmcomp $ID AccessReader`
### Полный доступ к мостику на станции Салтерн
`entities with Airlock named "Bridge" near 6 with Airlock do rmcomp $ID AccessReader`
## Замена работ/костюмов
### День клоунов
`entities with Mind prototyped MobHuman do setoutfit $ID ClownGear; addcomp $ID Clumsy`
### Клоунитизм
`entities with Clumsy near 1 with Body prototyped MobHuman not with Clumsy do setoutfit $ID ClownGear; addcomp $ID Clumsy`
### Все из нас, кроме двух, клоуны - кто оставшиеся
`entities with Mind alive prototyped MobHuman not with Clumsy not select 2 do setoutfit $ID ClownGear; addcomp $ID Clumsy`
### День мима
`entities with Mind prototyped MobHuman do setoutfit $ID MimeGear; rmcomp $ID Speech`
## Контейнеры
### Удалить чьи-то лёгкие
`entities with Body prototyped MobHuman named "NAME GOES HERE" rchildren named "lungs" do delete $ID`
А это выкинет их на пол:
`entities with Body prototyped MobHuman named "NAME GOES HERE" rchildren named "lungs" do rmmechanism $ID`
## Баловство со станцией
### Сделать станцию прозрачной
`entities named ".*wall" do spawn ReinforcedWindow $ID; spawn Grille $ID; spawn CableApcExtension $ID; delete $ID`
### Проспект им. Электрика
`entities named ".*wall" do spawn spawn Grille $ID; spawn CableApcExtension $ID`

# Сделает всех несчастными
## Вызов бога
`entities with Body prototyped MobHuman alive select 1 do addcomp $ID Singularity; addcomp $ID MovementIgnoreGravity; godmode $ID`
## бэнг
`entities with MapGrid rchildren do explode $WX $WY 1 1 1 1`
## бэнг, но веселей
`entities with MapGrid children with Item not anchored do addcomp $ID RoguePointingArrow`
