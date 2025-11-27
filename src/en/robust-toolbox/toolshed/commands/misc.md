# Miscellanious

## Misc
{{#template 
    ../../../templates/toolshed-command-head.md
    name=explain &lt;command run&gt;
    typesig=[none] -> [none]
}}
Prints a breakdown of the flow of the input command run to the console.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=stopwatch &lt;command run&gt;
    typesig=[none] -> [none]
}}
Prints the execution time of the input command run to the console.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=search &lt;query&gt;
    typesig=IEnumerable<T> -> IEnumerable<FormattedMessage>
}}
Performs a simple string search over the input, highlighting matches.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=help
    typesig=[none] -> [none]
}}
Prints the help text to the console.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=more
    typesig=[none] -> object?
}}
Returns the contents of the `$more` variable. `$more` is automatically assigned by the shell when it has to cut off a message for being too long.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=buildinfo
    typesig=[none] -> [none]
}}
Prints info about the game's build (game name, engine version, build commit, manifest hash) to the console.

{{#template 
    ../../../templates/toolshed-command-head.md
    name=cmd:moo
    typesig=[none] -> string
}}
The most important command.