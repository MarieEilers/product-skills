# Reference Frameworks

Diese Datei gibt Coach und User **gemeinsames Vokabular**, damit Coaching in
einer kohaerenten Produkt-Philosophie geerdet bleibt — statt zwischen Schulen zu
driften. Der Coach **webt** diese ein, **lehrt** sie nicht vor.

## Operating Models

- **Produktmodell**: Empowered cross-functional Teams loesen Probleme mit
  messbaren Outcomes. Discovery vor Delivery. Output ist nicht das Ziel —
  Outcomes sind es.
- **Projektmodell**: Stakeholder definieren eine Roadmap aus Features. PMs
  schreiben Specs. Designer designen zur Spec. Engineers bauen zur Spec. Output
  ist das Ziel. Cagan nennt das **Feature Factory**.

User coacht sich zum Produktmodell unter strukturellem Druck zum Projektmodell.
**Beide Realitaeten werden geehrt.** Coaching hilft zu sehen, **wann und wie
unnoetig** in den Projekt-Modus gerutscht wird.

## Four Product Risks (Cagan)

Jede signifikante Produktentscheidung wird gegen diese vier gepruefte:

- **Value Risk** — Werden Kunden es kaufen / nutzen / wollen?
- **Usability Risk** — Koennen Nutzer es bedienen?
- **Feasibility Risk** — Kann Engineering es in Constraints bauen?
- **Viability Risk** — Funktioniert es fuers Business (Legal, Finanz, Brand,
  Sales, Support, Compliance)?

Compliance-schwere Domaenen erheben Viability Risk legitim — aber es darf die
anderen drei nicht verdraengen.

## Build to Learn vs Build to Earn (Jeff Patton / Cagan)

- **Discovery** = build to learn. Cheap, disposable Artefakte, die Risiken
  reduzieren.
- **Delivery** = build to earn. Production-Code.

**Beide verwechseln** — Production-Grade-Sachen bauen, um zu lernen — ist ein
verbreitetes Anti-Pattern.

**Tempo vs Sicherheit** (@produxtmanager, 01.10.2026): Beides zugleich gibt es selten. Wer zu
schnell baut, baut womoeglich das Falsche. Coaching-Frage: Wie viel Sicherheit braucht
diese Entscheidung, und was ist der kleinste Test, der sie liefert, bevor gebaut wird?

## Strategic Context (Cagan)

Ein Produkt-Team braucht vier Dinge, um im Produktmodell zu funktionieren:

1. **Product Vision** — wo will das Team in 3-10 Jahren sein?
2. **Product Strategy** — welche Insights, welche Bets?
3. **Team Topology** — wie sind die Verantwortlichkeiten geschnitten?
4. **Team Objectives** — welche Outcomes (nicht Outputs) treiben das Team?

Wenn der User nicht zeigen kann, wo jedes davon fuer seinen Scope **lebt** —
ist das ein Coaching-Thema.

## Product Sense Dimensionen

Starke Product-People entwickeln Wissen in:

- Users / Customers
- Industrie / Markt
- Competitive Landscape
- Domaene (Fachwissen)
- Sales / Marketing
- Financials (Cost, Monetization, Unit Economics)
- Compliance / Legal / Privacy
- Key Health Metrics
- Technology
- Cross-Team-Relationships

In jeder Session: implizit pruefen, wo der User **stark** ist, wo **Wachstum**
liegt — und passend coachen.

## Mary Parker Follett — Integrative Lens

Follett (1868-1933) entwickelte ein Management-Verstaendnis, das im SVPG-Geist
nuetzlich ist:

- **"Power-with" statt "Power-over"** — kollaborative Macht statt
  hierarchischer Macht.
- **Integration vs Compromise vs Domination** — drei Wege, Konflikt zu loesen.
  Integration ist das Ziel: eine Loesung finden, in der beide Seiten das
  Wesentliche behalten.
- **"The situation as the authority"** — die Fakten der Situation, nicht
  persoenliche Autoritaet, treiben die Entscheidung.

Diese Linsen mappen auf Stakeholder-Dynamiken (z.B. konkurrierende
Nutzerbeduerfnisse) und Cross-Team-Koordination.

## Team Topologies (Skelton / Pais)

Wenn das Coaching-Thema Cross-Team- oder Plattform-Fragen beruehrt:

- **Stream-aligned Team** — bedient einen kontinuierlichen Wertstrom.
- **Enabling Team** — hilft anderen Teams, Capabilities aufzubauen.
- **Complicated-Subsystem Team** — kuemmert sich um spezialisierte Subsysteme.
- **Platform Team** — bietet eine self-service Plattform.

Plus **3 Interaction Modes**: Collaboration, X-as-a-Service, Facilitating.

## Continuous Discovery Habits (Teresa Torres)

- **Woechentliche Customer-Touchpoints**: nicht "wann wir Zeit haben", sondern
  fest in der Kadenz.
- **Opportunity-Solution-Tree**: Outcomes → Opportunities → Solutions →
  Assumptions zu testen.
- **Assumption Tests**: vor Build, kleinster Test, der eine Annahme prueft.

## Intent & Craft im KI-Bauboom (Katie Dill, Stripe)

Ausgangsbild: der Bauboom nach dem Zweiten Weltkrieg. Der Modernismus hatte eine
Haltung, die Kopien danach nur noch das Muster. Ergebnis: austauschbare
"Zombie-Gebaeude". Mit KI kann heute jeder bauen, und es droht dasselbe in
Software: **Zombie UI**, also eintoenig, leer oder vernachlaessigt.

Drei Beobachtungspunkte:

- **LLMs liefern das Wahrscheinlichste.** Gut fuer "was funktioniert hat", schwach
  bei "was ist eigen, was passt zu unserer Marke und dem Kontext unserer Nutzer".
- **Burrito-Dilemma.** Die Geschwindigkeit fasziniert so sehr, dass man grobe
  Maengel uebersieht. Ein poliert wirkender Erstentwurf taeuscht Fertigkeit vor.
- **Wegwerf-Haltung.** Was schnell gebaut ist, wird als entbehrlich behandelt.
  Verantwortung fuer Entscheidungen und Langzeitfolgen faellt weg.

Vier Empfehlungen, als Coaching-Fragen nutzbar:

1. **Point of View haben.** Ohne eigene Haltung liefert die KI eine, und die ist
   generisch und rueckwaertsgewandt. *Frage:* Wer wollt ihr fuer eure Nutzer
   sein, und woran sieht man das im Detail? Qualitaetsmassstab ist das Ergebnis
   fuer den Nutzer, nicht der Herstellungsweg ("Warum soll es zaehlen, wie es
   gemacht wurde?"). Ziel ist nicht Perfektion, sondern eine Ebene tiefer gehen,
   als der Kunde sieht. Geschmack entsteht durch genaues Hinschauen: was Nutzer
   brauchen (nicht nur sagen), was in Produkten, Kunst und Alltag gut wirkt.
2. **Standards in die Maschine codieren.** Entscheidungen fallen zunehmend ohne
   Designer im Raum (verteiltes Bauen, Agenten, generative UI). Das Designobjekt
   ist nicht mehr der Screen, sondern das System. Das alte System skalierte
   Konsistenz, das neue muss **Intent** skalieren: ganze Muster und Flows statt
   nur Komponenten, meinungsstark und zum richtigen Zeitpunkt in den Kontext
   geladen. *Frage:* Wo steht euer Massstab so, dass ein Agent ihn anwenden kann?
3. **"Fertig" nicht mit "gut" verwechseln.** Frueher filterte die Knappheit
   (20 Ideen, eine wird gebaut). Heute entsteht alles, und der Filter muss nach
   dem Bauen kommen, wo Nein-Sagen schwerer faellt. Dafuer braucht es die Rolle
   des **Editors**, die das Ganze von Anfang bis Ende verantwortet. Ein System
   kann jede Regel erfuellen und trotzdem tot sein (Christopher Alexander).
   *Fragen:* Loest es das Problem wirklich? Entspricht es dem Denken des Nutzers?
   Ist es als Ganzes stimmig oder nur in Einzelteilen? Ist es ueberhaupt
   ausgeformt? Beispiel: eine KI-gestuetzte Animation brauchte 56 Iterationen bis
   zur Qualitaet; die KI oeffnete den Moeglichkeitsraum, ersetzte aber nicht das
   pruefende Auge.
4. **Kreativitaet freisetzen.** KI senkt die Kosten des Erschaffens; einen Teil der
   Ersparnis in Eigenes investieren. Wenn alle bauen, wird Differenzierung
   wichtiger. KI soll die Decke anheben, nicht nur den Boden. Taktik: Inputs mit
   eigenem Massstab und Quellmaterial anreichern, Outputs nie beim ersten Wurf
   belassen, Gegen-Agenten zur Kritik einsetzen. Fuehrung: Raum zum Erkunden
   geben, "das Seltsame schuetzen".

Ergaenzend: **Vier Dimensionen von Ambition mit KI** (Felix Rieseberg, Anthropic, hier aus
einer Zusammenfassung auf Instagram, nicht aus dem Original): **Speed** (schneller erledigen, der
offensichtliche Teil) · **Altitude** (Ergebnisse statt Einzelaufgaben vorgeben, etwa "die
Anwendung bleibt absturzfrei" statt "behebe diesen Fehler") · **Depth** (aussergewoehnliche
Qualitaet verlangen: Expertenmethoden, Rohdaten, unabhaengige Pruefung) · **Range** (Disziplinen
kombinieren). *Frage:* Nutzt du KI gerade nur fuer Speed, und welches Ergebnis haettest du dir
ohne sie nicht vorgenommen?

Im Coaching einsetzen, wenn der User mit KI baut oder bauen laesst und die Frage
nach Qualitaet, Differenzierung oder Abnahme offen ist. Verbindet sich mit
**Build to Learn**: schnelle KI-Prototypen sind Discovery, aber die Editor-Frage
muss gestellt werden, bevor daraus Delivery wird.

## Gewohnheits-Check: woran PMs scheitern (@produxtmanager)

Kein Framework, sondern eine Diagnose-Liste. Die These: PMs scheitern selten an
fehlendem Koennen, sondern an Gewohnheiten, die sich produktiv anfuehlen und das
Produkt nicht voranbringen. Der Coach nutzt die Liste, um ein Verhalten zu benennen,
und fragt dann nach dem konkreten Fall. Ein Urteil ueber die Person faellt er nicht.

| Gewohnheit | Kern | Verbindung |
|---|---|---|
| Ja sagen, weil Nein unangenehm ist | Jedes unnoetige Ja zerstreut den Fokus | Nein als Entscheidung, Follett |
| Bauen, bevor das Problem verstanden ist | Schnelle Loesung fuers falsche Problem bleibt falsch | Problem-Modus, Discovery |
| Jede Stakeholder-Anfrage als Prioritaet | Druck ist nicht gleich Wirkung | Feature Factory |
| Lautester Stakeholder formt die Roadmap | Lautstaerke ist kein Beleg | Situation als Autoritaet |
| Jedes Meeting besuchen aus Angst, etwas zu verpassen | Ueberall sein heisst nicht Wert stiften | Fokus, Team Topologies |
| Daten nutzen, um die eigene Meinung zu verteidigen | Nur bestaetigende Belege suchen ist keine Discovery | Assumption Tests |
| Features ausliefern mit Wert verwechseln | Ausgeliefert ist Output, Nutzerverhalten danach ist Outcome | Outcome vs Output |
| Entscheidungen bei jedem Widerspruch neu oeffnen | Widerspruch heisst nicht, dass die Entscheidung falsch war | Festgelegtes stabil halten |
| Nutzer nach Wuenschen fragen statt nach ihrem Ziel | Nutzer beschreiben Loesungen, PMs untersuchen Probleme | Continuous Discovery, JTBD |
| Produktivitaet an Beschaeftigung messen | Voller Kalender, leere Roadmap | Outcome vs Output |
| Schwierigen Gespraechen ausweichen | Kurzfristige Ruhe, langfristige Produktprobleme | Wahrheit vor Affirmation |

Zusammenfassung: Die schlimmste Gewohnheit ist, das zu tun, was sich produktiv
anfuehlt, statt das, was das Produkt voranbringt. Gutes Produktmanagement heisst
nicht mehr tun, sondern konsequent entscheiden, was Zeit, Aufmerksamkeit und
Entscheidungen verdient.

*Coaching-Fragen:* Welche Gewohnheit davon hat dich diese Woche Zeit gekostet? Was
hast du zugesagt, das du eigentlich ablehnen wolltest, und was hat dich abgehalten?
Welche Entscheidung hast du wieder aufgemacht, und gab es dafuer neue Fakten oder
nur neuen Widerspruch?

## Ungeschriebene Regeln als Push-back-Fragen (@produxtmanager)

Ergaenzung zum Gewohnheits-Check. Hier geht es nicht um eigene Gewohnheiten,
sondern um typische Saetze von aussen und die Gegenfrage, die der Coach dem User
an die Hand gibt.

| Wenn jemand sagt ... | Gegenfrage |
|---|---|
| "Das ist nur ein kleines Feature." | Was haengt alles daran (Support, Randfaelle, Pflege)? Klein ist es selten. |
| Der CEO will es. | Welches Problem steckt hinter der Anfrage? Auch eine CEO-Anfrage ist eine Anfrage. |
| Etwas soll noch auf die Roadmap. | Was faellt dafuer runter? Je voller die Roadmap, desto weniger sagt sie aus. Sie ist eine Sammlung von Wetten, keine To-do-Liste. |
| "Die Nutzer haben danach gefragt." | Warum haben sie gefragt? Der Wunsch allein ist kein Grund zu bauen. |
| Das Feature ist live. | Was tun die Nutzer jetzt anders? Erst ihr Verhalten zeigt den Erfolg. |
| Engineering schaetzt drei Monate. | Was macht es drei Monate? Erst verstehen, dann ueber den Zeitplan reden. |
| Sales sagt, ein Kunde braucht es. | Wie viele andere Kunden haben dasselbe Problem? Ein Kunde ist noch kein Markt. |
| Viele Kennzahlen im Dashboard. | Welche eine Kennzahl zeigt, ob das Produkt funktioniert? |

Passt zu: Feature Factory, Roadmap als Hypothese, Outcome vs Output, Four Product
Risks (Viability bei Sales-Anfragen), Follett ("die Situation als Autoritaet"
statt Rang des Anfragenden).

## Anti-Patterns, die der Coach beobachtet

- Stakeholder-Wuensche als Anforderungen behandeln, ohne das zugrundeliegende
  Problem zu pruefen.
- Proxy-Kunden (interne SMEs als Stellvertreter fuer Endnutzer) als validierte
  User-Voice behandeln.
- Lieferung von Features ohne Discovery — "wir kommen aus der Loesung, nicht
  aus dem Problem".
- Produkt-Konsolidierung ohne Pruefung, ob es **Integration** oder nur
  **Kompromiss** zwischen widerstreitenden Zielgruppen ist.
- "Build to earn" fuer Discovery-Artefakte.
- Roadmap als Commitment statt als Hypothese.
- **Broken Trust Loop**: unvalidiertes Feature → negatives Stakeholder-Feedback
  → engere Top-down-Kontrolle → mehr unvalidierte Features.
- **Zombie UI**: KI-Erstentwurf als fertig ausgeliefert, weil er poliert wirkt —
  ohne Editor, ohne eigenen Massstab, ohne Blick aufs Ganze.

## Coach-Vokabular (haeufig benutzte Begriffe)

Behalte als loanword im Deutschen: Discovery, Outcome, Output, Stakeholder,
Persona, Insight, Assumption, Hypothesis, Pilot, Roadmap, Feature Factory.

Bei deutschen Begriffen wenn praeziser: **Produkt-Sinn** (Product Sense),
**Auftrags-Modus** (Project Mode), **Loesungs-Modus**, **Problem-Modus**.

## Quellen

- **Marty Cagan / SVPG** — *Inspired*, *Empowered*, *Transformed*.
- **Jeff Patton** — *User Story Mapping*.
- **Teresa Torres** — *Continuous Discovery Habits*.
- **Mary Parker Follett** — *Dynamic Administration* (1941, posthumes Sammelband).
- **Skelton / Pais** — *Team Topologies*.
- **Katie Dill (Stripe)** — "How to scale intent, quality, and artistry with AI",
  Lenny and Friends Summit, San Francisco, 10.09.2026 (YouTube: GLvFTMtw4Jk).
- **@produxtmanager** — Instagram-Carousel "Most PMs don't fail because...",
  25.09.2026. Praxis-Beitrag, keine Primaerquelle; Folien 01 und 13 fehlen in der
  Vorlage.
- **@produxtmanager** — Instagram-Carousel "The Unwritten Rules of Product
  Management", 21.09.2026. Praxis-Beitrag; Folie 03 fehlt in der Vorlage.
