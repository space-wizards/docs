
# Development

This section isn't finished yet, hence this PR is a draft. TODO:

* subcommands (if any exist, all must be subcommands)
* type signature restrictions 
  * (name, pipedType) tuple must be unique.
  * TakesPipedTypeAsGenericAttribute limitations 
* example implementations
  * optional & params args
  * invertible
  * invocation context & variables
* Loc strings
 * subcommand loc keys: "comp:add" -> "comp-add"
 * required descriptions 'command-description-{command name}'
 * optional command help: 'command-help-{command name}'
   * If not specified, auto-generatedmand-arg-hin
 * Optional argument hints 'comt-{command name}-{argument name}'
   * If not specified, defaults to the argument's signature
 * optional argument signature 'command-arg-sig-{command name}-{argument name}'
   * if not specified, autogenerated as <name (type)> or [name (type)] or [name (type)]...
   * used for hints, explain, etc.
* type parsers
  * custom type parsers
  * completion hints
* type arguments
* variable parsing context