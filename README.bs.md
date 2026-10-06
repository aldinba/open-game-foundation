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

## Šta ovo znači ako krećeš od nule

OGF ti ne daje game engine niti gotovu igru. Daje novom game projektu mali operativni sistem, tako da ne moraš izmišljati kako ćeš voditi projekat dok istovremeno pokušavaš napraviti igru.

Od prvog playable prototipa dobiješ jasno mjesto gdje možeš odgovoriti:

- Šta je ovaj projekat trenutno?
- Koji build/verziju upravo testiramo?
- Kako znamo da je repo mehanički zdrav?
- Šta još mora provjeriti čovjek kroz playtest?
- Koji bug je samo popravljen, a koji je stvarno ponovo provjeren?
- Zašto smo donijeli važnu tehničku ili produktnu odluku?
- Šta Claude, Codex, drugi agent ili novi developer treba pročitati prije izmjene?

Praktično:

- engine/runtime pravi igru;
- Git čuva historiju koda;
- OGF čuva smisao projekta, validaciju, playtest evidence, odluke i release stanje razumljivim kroz vrijeme.

Najmanji koristan setup je namjerno mali: identitet projekta, jedna validation komanda, repository/agent pravila, minimalna build/testing dokumentacija i jedan release zapis. Advanced review, experiment, risk, benchmark i retro moduli uključuju se tek kada projekat dovoljno naraste.

Ako radiš sam, OGF prvenstveno smanjuje gubitak konteksta. Kada uključiš drugog developera, coding agente, više buildova ili vanjske playtestere, vrijednost brzo raste jer svi rade iz iste projektne istine u repou umjesto iz rekonstruisane chat historije.

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

Za veće ili neizvjesnije projekte postoji i opcionalni advanced layer: assumptions, risks, experiments, specijalizovane review perspektive, performance benchmark, milestone retro i `AGENT_INDEX.md` za brže snalaženje ljudi i agenata. Pogledaj `docs/OPTIONAL_MODULES.md`.
