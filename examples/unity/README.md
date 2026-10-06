# Unity game example

Typical project evidence:

- runtime: `unity`;
- implementation root: repository/project root containing `Assets/`, `Packages/` and `ProjectSettings/`;
- deterministic validation: compile/import plus available EditMode/PlayMode tests and build check;
- deployment artifact: project-defined player build.

Do not make the generic foundation depend on a specific Unity version or CI provider. Pin those facts in the adopting project's documentation.
