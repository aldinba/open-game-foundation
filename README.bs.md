# Open Game Foundation

Runtime-agnostički temelj za razvoj igara u malim i srednjim timovima koji rade sa ljudima i coding agentima.

Daje repozitoriju trajni operativni okvir za:

- identitet projekta i release evidenciju;
- rad više agenata bez gaženja promjena;
- determinističku validaciju;
- playtest evidenciju i lifecycle bugova/nalaza;
- živu tehničku i produktnu dokumentaciju;
- sigurniji deploy i razvoj podrške za platforme.

Ne propisuje engine. Web igre, Godot, Unity i drugi runtime-i koriste isti operativni ugovor, dok engine-specifične stvari ostaju lokalne projektu.

## Brzi početak

Najbrže:

```bash
python3 scripts/init_foundation.py ../moja-igra \
  --slug moja-igra \
  --title "Moja igra" \
  --runtime browser \
  --implementation-root src
```

Zatim:

1. Pročitaj `ADOPTION.md`.
2. Zamijeni generičku dokumentaciju stvarnim činjenicama iz svog repoa.
3. Definiši jednu determinističku validation komandu za svoj engine/runtime.
4. Pokreni `python3 scripts/validate_foundation.py ../moja-igra`.
5. Ako nemaš jači `AGENTS.md`, uzmi `AGENTS.template.md` kao početak.

## Glavna ideja

Repo, a ne chat historija, treba biti projektna memorija.

Ako novi developer ili agent sutra uđe u projekat, iz repoa treba moći zaključiti:

- šta gradimo;
- kako je sistem podijeljen;
- šta je trenutno podržano;
- kako se projekat validira;
- šta automatika ne može dokazati;
- kako ide release/deploy;
- koje su važne odluke ranije donesene i zašto.

## Pravila koja su se pokazala vrijednim

- Jedan writer po fajlu ili jako spojenom subsystemu.
- Paralelni rad ide kroz nezavisne scopeove ili branch/worktree.
- `FIXED` nije isto što i `VERIFIED`.
- Build koji prolazi ne znači da je igra zabavna ili razumljiva.
- Deploy nije implicitno dozvoljen samo zato što je build spreman.
- Za veće odluke koristi ADR umjesto da razlog ostane samo u chatu.
- Svaki veći task mora provjeriti documentation impact.

## Koliko procesa je dovoljno

Za mali prototip ne treba sve odmah. Počni sa:

- `.game/project.json`
- jednom `validate` komandom
- `AGENTS.md`
- `docs/BUILD_AND_TESTING.md`
- jednim release zapisom

Ostalo dodaj kad projekat počne imati više ljudi, više agenata, više platformi ili redovne playtestove.

Kompletan mali primjer je u `examples/minimal-game/`.
