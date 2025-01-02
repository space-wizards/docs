
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
 * required descriptions 'command-description-<command>'
 * optional command help: 'command-help-{name}'
   * If not specified, auto-generated
 * Optional argument hints 'command-arg-hint-{name}-{argument}'
   * If not specified, auto-generated
* type parsers
  * custom type parsers
  * completion hints
* type arguments
* variable parsing context
