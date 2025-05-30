# Fluent & Localization
The localization system is what pulls up human-readable text strings so that they can be translated by other servers if they so choose. Mainline SS14 only supports English, but other servers are free to add additional language support.

Localization is done with [Project Fluent](https://www.projectfluent.org/) (from now on just 'Fluent'). It's a project for a better localization system invented by Mozilla for Firefox. It's relatively new but has notable improvements over older systems like `gettext`. With old systems like gettext, the code still contains the "english" version of the string. This however does not work well in practice because English lacks (for better or worse) many nuances other languages might have. Fluent solves this by not even having English in the code.

## Basic Overview

The basic idea is that the code and prototypes themselves contains no human-presented text strings. All actual text presented to humans is instead specified in `.ftl` files inside `Resources/Locale/<language code>`. So for (US) English it'd be `space-station-14/Resources/Locale/en-US/`, French would be `.../fr-FR/`, etc... 

An example of a real localization directory can be found [here](https://github.com/space-wizards/space-station-14/tree/master/Resources/Locale/en-US), SS14's English (US/Default) localization.

These localized text strings can be retrieved in-game with the `Loc.GetString()` method (and similar).

Note that you can find a complete overview of Fluent's markup syntax, with examples and live playground, on [its website](https://www.projectfluent.org/) (see "syntax guide" on the top).

## Practical Examples.

#### Example 1 (A simple message):
```
comp-stack-already-full = Stack is already full.
```
This example defines a message called `comp-stack-already-full`, with the value `"Stack is already full."`.
Using this messageId in C# code, as follows:
```csharp=
Loc.GetString("comp-stack-already-full")
```

Will return the string `"Stack is already full."` which you can then use for popup messages, UI, and so on.


#### Example 2 (A message with variables):

```
traitor-user-was-a-traitor = {$user} was a traitor.
```
Not all text is as straight forward as `"Stack is already full."`, often you'll need part of the text to change. Unfortunately, given that languages have different grammars ([SVO](https://en.wikipedia.org/wiki/Subject%E2%80%93verb%E2%80%93object), [SOV](https://en.wikipedia.org/wiki/Subject%E2%80%93object%E2%80%93verb), etc.) you can't just do 
```csharp=
var text = "Bob" + Loc.GetString("traitor-user-was-a-traitor");
```

```admonish warning
Remember, the above is what *not* to do!
```

and hope to get `"Bob was a traitor."`, this might work for english (an SVO language), but it won't work for many others (including other SVO languages!)

Fortunately, Fluent was built to handle this (and many more problems).
Messages can contain variables that can be used within the localized text in whatever position is appropriate for the language. The `{$user}` portion is a Fluent '[placeable](https://www.projectfluent.org/fluent/guide/placeables.html)' being used to insert the [variable](https://www.projectfluent.org/fluent/guide/variables.html) `$user` into the text.

Requesting a localized string with variables is done slightly differently than requesting a message without:
```csharp=
Loc.GetString("traitor-user-was-a-traitor", ("user", traitor.Mind.Session.Name));
```
After the messageId, `"traitor-user-was-a-traitor"`, we have a tuple `(..., ...)` composed of a string followed by a value, `traitor.Mind.Session.Name`, which is the traitor's name.
Defining variables in a `Loc.GetString()` call like this allows the name defined in the tuple to be placed into the localized text to paste in the value.
```csharp=
Loc.GetString("traitor-user-was-a-traitor", ("user", "Bob"));
```
This gets us `"Bob was a traitor."`

#### Example 3 (Plurals, gender, and other language-specific problems)
```
humanoid-character-profile-summary = 
    This is {$ent}. {GENDER($ent) ->
    [male] He is
    [female] She is
    *[other] They are
} {$age} years old. 
```
You probably know of atleast 1 language that varies the structure of a sentence or word depending on the amount, gender or other feature of an object. If you're reading this document then the easiest example is going to be English!

The `humanoid-character-profile-summary` message is used in the lobby character selection screen and describes your character's name, gender, and age, so obviously it needs to change depending on the character's **name**, **gender**, and **age**! 

**name** and **age** are easy as they don't change the structure of the sentence. Name is assumed when you pass an `EntityUid` in as a parameter, and you can get grammatical gender using the `GENDER()` function. We pass the age in here manually.

However, with **gender** it gets tricky. In english a person's gender affects what pronouns are used in sentences that refer to them; We need 'He', 'She' or 'They' to be chosen appropriately.
Thankfully Fluent supports '[selectors](https://www.projectfluent.org/fluent/guide/selectors.html)' which should look familiar to anyone who's ever used a `switch/case` or `match` statement in other programming languages. A variable is switched or matched against a series of branches and if a match is found that branch is executed.
Fluent's selectors are no different, depending on the variable switched the sentence is changed to match the most appropriate branch.
- String variables are matched against string branches `[male], [female], etc`
- Numerical variables are matched against numbers `[1], [2], etc` and the special `[zero], [one], [two], [few], [many]` categories which represent the 'CLDR plural category' of the number. 
    - This is used to handle pluralizations:
        -  1 minute, 2+ minutes (english plurals)
        -  1 minuta, 2-4 minuty and 5+ minut (czech plurals)

#### Example 4 (Fluent Functions)

Obviously, the above with gender is a little annoying to write and is especially annoying to have to call in C#. Thankfully, we have some fluent functions that make it easier. Fluent functions are called inside the curly braces `{}` just like with variables, and are called with the variables as arguments. Functions are often used multiple times in a row, on the results of other functions.

Using functions, the above example code simply looks like:

```
humanoid-character-profile-summary = This is {$ent}. {SUBJECT($ent)} {CONJUGATE-BE($ent)} {$age} years old.
```

##### Function rundown

The easiest to understand is `CAPITALIZE`, which just capitalizes the first letter of whatever is passed in. This is most often used to modify the results returned by other functions.

The functions `GENDER()` and `PROPER()` return the grammatical gender (masculine, feminine, epicene, neuter) and the proper-ness of an entity respectively.

Functions also exist for determining the definite and indefinite articles that an entity should have--These functions are `THE`, which returns 'the' if the entity is proper and nothing otherwise, and `INDEFINITE`, which return either 'a' or 'an' depending on some complex rules.

```
hugging-success-generic = You hug {THE($target)}.
hugging-success-generic-others = { CAPITALIZE(THE($user)) } hugs {THE($target)}.
```

Other functions exist for automatically determining various pronouns based on grammatical gender of the entity passed in--masculine, feminine, epicene (they), or neuter (it). These include:
- `SUBJECT($ent)` -- he, she, they, it
- `OBJECT($ent)` -- him, her, them, it
- `POSS-PRONOUN($ent)` -- his, hers, theirs, its
- `POSS-ADJ($ent)` -- his, her, their, its
- `REFLEXIVE($ent)` -- himself, herself, themselves, itself

Finally, there are functions for conjugating certain special verbs based on gender; these are:
- `CONJUGATE-BE($ent)` -- (they) are, (he/she/it) is
- `CONJUGATE-HAVE($ent)` -- (they) have, (he/she/it) has
- `CONJUGATE-BASIC($ent, first, second)` -- (they) {$first}, (he/she/it) {$second} e.g. `CONJUGATE-BASIC($ent, "run", "runs")` (they run, he/she/it runs)

These functions add up to create some complicated FTL strings, but they're going to read perfectly every time no matter which entity is being used.

For example, in `hands-system.ftl`:

```
# Examine text after when they're holding something (in-hand)
comp-hands-examine = { CAPITALIZE(THE(SUBJECT($user))) } { CONJUGATE-BE($user) } holding { INDEFINITE($item) } { $item }.
```

The only unique word in this string is 'holding!' But, in any case, this will always result in a correct looking string, no matter what the user or item are:

```
# Example output strings
Sarah Collins is holding a wrench.
The corgi is holding an apple.
The rats are holding a piece of cheese.
```

You should seek to use these functions whenever possible to make dynamic and 100% correct strings. If you're localizing in a different language, consider what analogues to these functions exist and implement them yourself, since these are obviously very English-specific.

## Localizing Prototypes

```admonish warning
This is not for use upstream. If you're making upstream content please use the name/description fields.
This is to make it easier for translations to override things without editing the main game's data.
```

```yaml
- type: entity
  id: RedOxygenTank
  name: oxygen tank
  description: A tank of oxygen. This one is red.
```

So you know how to localize C# code, but how do you localize YAML?
In general, it's going to be as simple as:
```yaml
  someYaml: some-message-id
```

But for entities we have code in place to allow localizations to be easier to read and write.

```yaml
- type: entity
  id: RedOxygenTank
  name: red-oxygen-tank-name
  description: red-oxygen-tank-desc
```

```
red-oxygen-tank-name = oxygen tank
red-oxygen-tank-desc = A tank of oxygen. This one is red.
```
While you could do something like the above, it's a bit repetitive, we know we're localizing the red oxygen tank entity so why specify it again in each message?

### Enter: Attributes
Fluent allows you to add extra information on to messages, you can use these to describe properties of the text, such as a word's gender or plurality.
We use the attribute system to attach messages... to messages! on the C#     side an entity prototype's id, e.g. `RedOxygenTank` is converted into a messageId `ent-RedOxygenTank`, this messageId gets used for the name of the entity, and has a `.desc` attribute that's used for the entity's description.
```yaml
- type: entity
  id: RedOxygenTank
```
```
ent-RedOxygenTank = oxygen tank
  .desc = A tank of oxygen. This one is red.
```
Look! no YAML definition for name or desc!

## Advice
- ***INDENT WITH SPACES, NOT TABS***
    - Fluent treats tabs literally, so they can't be used for indentation
- Fluent's [Syntax Guide.](https://www.projectfluent.org/fluent/guide/)
- Fluent's [Good Practices.](https://github.com/projectfluent/fluent/wiki/Good-Practices-for-Developers)
- SS14-specific, we recommend prefixing all messages with something relevant to the context they're used in, this helps keep the messageIds unique (a requiement) and also serves to "namespace" messages.
e.g. messages defined for the `StackComponent` should begin with `comp-stack-`
- To apply the language language pack to the game you just have to edit [Shared/EntryPoint.cs](https://github.com/space-wizards/space-station-14/blob/master/Content.Shared/EntryPoint.cs#L18).
- We recommend searching for `Loc.GetString` in the code to find all the translatable text
