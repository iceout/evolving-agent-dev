# Implementation Style Draft

## Intent

Implementation should be simple, direct, and maintainable. Avoid code that exists only because an agent is trying to look careful.

## Defaults

Prefer:

- direct control flow
- clear names
- small functions with real purpose
- existing project patterns
- explicit boundary validation
- natural errors when extra wrapping adds no value

Avoid:

- speculative defensive programming
- speculative abstractions
- unused extension points
- repeated internal validation
- catch-and-rethrow wrappers with no added context
- logging that does not help debugging or operations
- options and fallbacks not required by the current task

## Defensive Programming Boundary

Validate at untrusted boundaries:

- user input
- configuration files
- filesystem
- network
- database
- subprocesses
- model/tool calls
- external plugin APIs

Inside trusted internal calls, do not repeat checks already guaranteed by the boundary, type system, or schema validation.

## Review Questions

1. Which branches handle realistic situations?
2. Which checks are duplicated from an earlier boundary?
3. Which abstractions are needed now rather than imagined for later?
4. Can this be shorter without losing clarity?
5. Did the implementation become awkward only to satisfy a brittle test?

## Escape Hatch

Extra validation is acceptable when it improves:

- user-facing error messages
- security
- data corruption prevention
- diagnosis of external system failures
- compatibility with weakly typed or unreliable callers

The reason should be visible in code structure, test names, or review notes.
