#!/usr/bin/env python3
"""Erzeugt die animierten SVG-Bilder der README in assets/.

    python3 werkzeuge/bilder.py

Stil wie der Blog BLUU: monochrom, Hairlines, Mono-Labels, ein Faden in BLUU-Violett.
GitHub zeigt SVGs als <img>; Web-Fonts laden dort nicht, deshalb System-Schriften.
Die Chat-Texte sind wörtliche Auszüge einer echten Sitzung mit einem erfundenen Fall.
"""

from pathlib import Path
from xml.sax.saxutils import escape

ZIEL = Path(__file__).resolve().parent.parent / "assets"

INK, MUTED, LINE, FADEN = "#100F0D", "#7A7A72", "#E4E4DE", "#4B3BFF"
SANS = "-apple-system, 'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
SERIF = "Georgia, 'Iowan Old Style', 'Times New Roman', serif"
MONO = "ui-monospace, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"

REDUZIERT = "@media (prefers-reduced-motion: reduce) { * { animation: none !important; } .nur-animiert { display: none; } .nur-statisch { display: inline; } }"


def schreibe(name, inhalt):
    ZIEL.mkdir(exist_ok=True)
    (ZIEL / name).write_text(inhalt, encoding="utf-8")
    print("geschrieben:", ZIEL / name)


BV = "4"  # Bildversion: bei Änderungen hochzählen, sonst zeigt GitHub alte Bilder aus dem Cache

T = {
    "de": {
        "kopf_label": "product-skills: Deine KI nickt alles ab. Diese nicht. Skills für Product Owner – in Claude, Gemini und ChatGPT.",
        "kopf_meta": "SKILLS FÜR CLAUDE · GEMINI · CHATGPT · V0.2",
        "kopf_eyebrow": "// MARKETPLACE VON MARIE CHRISTIN EILERS",
        "kopf_z1": "Deine KI nickt alles ab.", "kopf_z2": "Diese nicht.", "kopf_faden": 410,
        "kopf_lede": "Skills für Product Owner – in Claude, Gemini und ChatGPT. Deutsch und Englisch.",
        "klick": ["Anpassungen", "Plugins", "Hinzufügen", "Marketplace hinzufügen", "Aus einem Repository hinzufügen", "MarieEilers/product-skills", "Entdecken → product-coach → +"],
        "klick_titel": "// IN DER CLAUDE-APP ODER AUF CLAUDE.AI",
        "klick_label": "In der Claude-App: Anpassungen, Plugins, Hinzufügen, Marketplace hinzufügen, Aus einem Repository hinzufügen, MarieEilers/product-skills eintragen, unter Entdecken beim product-coach auf Plus klicken.",
        "chat_label": "Chat mit dem Product Engineering Coach in der Claude-App: echte Sitzung mit erfundenem Fall, gekürzt.",
        "chat_rechts": "ECHTE SITZUNG · ERFUNDENER FALL · GEKÜRZT", "chat_denkt": "denkt nach …", "chat_eingabe": "Antworte Claude …",
        "chat": [
            ("du", "Coach mich auf eine Situation. Das Management war direkt beim Team. Die bauen jetzt den Export, den der Vertrieb einem Großkunden bis März versprochen hat. Unsere Kundenprio #1 liegt damit auf Eis."),
            ("claude", "**Du nennst eine Lösung, aber kein Problem.** Welches Problem hat der Großkunde, das der Export lösen soll? Weiß das im Team jemand?"),
            ("claude", "**„Liegt auf Eis“ ist eine Annahme.** Hat jemand entschieden, dass ihr nur eines von beiden machen könnt? Oder ist das so gekommen, weil niemand entschieden hat?"),
            ("claude", "Was hast du den fünf Pilot-Hofläden für November zugesagt – und weiß im Management jemand von dieser Zusage?"),
            ("du", "Den Start im November. Das Management weiß davon nichts. Ich habe die Kundenprio nie mit Zahlen vorgestellt."),
            ("claude", "**Das Management hat deine Priorität nicht übergangen. Aus seiner Sicht gab es sie gar nicht.** Ihr habt beide Zusagen nach außen gegeben, ohne sie intern abzustimmen. Der Vertrieb war nur schneller beim Team."),
            ("du", "Autsch. Was mache ich bis Freitag – konkret?"),
            ("claude", "**Montag:** den Export verstehen. Geh zuerst zum Vertrieb, nicht zum Management."),
            ("claude", "**Bis Mittwoch:** aus den Zitaten Belege machen. Zitate kannst du zählen."),
            ("claude", "**Freitag:** Termin beim Management. Bitte um eine Entscheidung, statt dich zu beschweren – mit zwei oder drei Optionen."),
        ],
        "wege_titel": "// SO KOMMT EIN SKILL IN DEINE KI", "wege_badge": "EMPFOHLEN",
        "wege_label": "Vier Wege, einen Skill in deine KI zu bringen: Claude-App über den Marketplace (empfohlen), Claude-App per ZIP, Gemini mit demselben ZIP, ChatGPT als Projekt mit der Kurzfassung.",
        "wege": [
            ("CLAUDE-APP · MARKETPLACE", "Einmal einrichten, alle Skills", ["Anpassungen → Plugins → Hinzufügen", "Marketplace hinzufügen → Aus einem Repository", "MarieEilers/product-skills eintragen", "Unter „Entdecken“ beim Skill auf „+“"], True, "Pro, Max, Team, Enterprise · auch in Cowork"),
            ("CLAUDE-APP · ZIP", "Ein Skill, auch im Gratis-Tarif", ["ZIP laden – nicht entpacken", "Anpassungen → Skills → Hinzufügen", "„Skill hochladen“ → ZIP wählen"], False, "Code-Ausführung muss eingeschaltet sein"),
            ("GEMINI · SKILL", "Dasselbe ZIP, kein Abo nötig", ["ZIP laden – nicht entpacken", "In Gemini die Skills öffnen", "Hochladen → ZIP wählen"], False, "neu seit Oktober 2026, kommt nach und nach"),
            ("CHATGPT · PROJEKT", "Mit der Kurzfassung", ["Neues Projekt anlegen", "Kurzfassung in die Projektanweisungen", "Vorlagen als Dateien dazulegen"], False, "Business und Enterprise: Skill-Upload"),
        ],
    },
    "en": {
        "kopf_label": "product-skills: Your AI nods along. These skills don't. Skills for product owners – in Claude, Gemini and ChatGPT.",
        "kopf_meta": "SKILLS FOR CLAUDE · GEMINI · CHATGPT · V0.2",
        "kopf_eyebrow": "// MARKETPLACE BY MARIE CHRISTIN EILERS",
        "kopf_z1": "Your AI nods along.", "kopf_z2": "These skills don't.", "kopf_faden": 690,
        "kopf_lede": "Skills for product owners – in Claude, Gemini and ChatGPT. English and German.",
        "klick": ["Customize", "Plugins", "Add", "Add marketplace", "Add from a repository", "MarieEilers/product-skills", "Discover → product-coach → +"],
        "klick_titel": "// IN THE CLAUDE APP OR ON CLAUDE.AI",
        "klick_label": "In the Claude app: Customize, Plugins, Add, Add marketplace, Add from a repository, enter MarieEilers/product-skills, then in Discover click plus on product-coach.",
        "chat_label": "Chat with the Product Engineering Coach in the Claude app: real session with a fictional case, shortened, translated from German.",
        "chat_rechts": "REAL SESSION · FICTIONAL CASE · SHORTENED · TRANSLATED", "chat_denkt": "thinking …", "chat_eingabe": "Reply to Claude …",
        "chat": [
            ("du", "Coach me on a situation. Management went straight to the team. They're now building the export that sales promised a key account by March. Our customer priority #1 is on hold."),
            ("claude", "**You're naming a solution, not a problem.** What problem does the key account want the export to solve? Does anyone on the team know?"),
            ("claude", "**“On hold” is an assumption.** Did anyone decide that you can only do one of the two? Or did it just happen because nobody decided?"),
            ("claude", "What did you promise the five pilot farm shops for November – and does anyone in management know about that promise?"),
            ("du", "A start in November. Management doesn't know. I never presented the customer priority with numbers."),
            ("claude", "**Management didn't override your priority. From their point of view, it didn't exist.** You both made promises to the outside without aligning internally. Sales just got to the team faster."),
            ("du", "Ouch. What do I do by Friday – concretely?"),
            ("claude", "**Monday:** understand the export. Go to sales first, not to management."),
            ("claude", "**By Wednesday:** turn the quotes into evidence. Quotes can be counted."),
            ("claude", "**Friday:** meeting with management. Ask for a decision instead of complaining – with two or three options."),
        ],
        "wege_titel": "// HOW TO GET A SKILL INTO YOUR AI", "wege_badge": "RECOMMENDED",
        "wege_label": "Four ways to get a skill into your AI: Claude app via the marketplace (recommended), Claude app via ZIP, Gemini with the same ZIP, ChatGPT as a project with the short version.",
        "wege": [
            ("CLAUDE APP · MARKETPLACE", "Set up once, get every skill", ["Customize → Plugins → Add", "Add marketplace → Add from a repository", "Enter MarieEilers/product-skills", "In “Discover”, click “+” on the skill"], True, "Pro, Max, Team, Enterprise · also in Cowork"),
            ("CLAUDE APP · ZIP", "One skill, free plan too", ["Download the ZIP – don’t unzip", "Customize → Skills → Add", "“Upload a skill” → pick the ZIP"], False, "Code execution must be turned on"),
            ("GEMINI · SKILL", "Same ZIP, no subscription", ["Download the ZIP – don’t unzip", "Open Skills in Gemini", "Upload → pick the ZIP"], False, "new since October 2026, rolling out"),
            ("CHATGPT · PROJECT", "With the short version", ["Create a new project", "Paste the short version as instructions", "Add the templates as files"], False, "Business & Enterprise: skill upload"),
        ],
    },
}


# ------------------------------------------------------------------ Kopf
def kopf(t):
    w, h = 1200, 430
    f = t["kopf_faden"]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(t['kopf_label'])}">
  <style>
    .mono {{ font-family: {MONO}; }}
    .faden {{ fill: none; stroke: {FADEN}; stroke-width: 6; stroke-linecap: round; stroke-dasharray: 1; stroke-dashoffset: 1; animation: zeichnen 1.3s cubic-bezier(.5,0,.2,1) .4s forwards; }}
    @keyframes zeichnen {{ to {{ stroke-dashoffset: 0; }} }}
    .cur {{ animation: blink 1.1s steps(1) infinite; }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .faden {{ animation: none; stroke-dashoffset: 0; }} .cur {{ animation: none; }} }}
  </style>
  <rect x="1" y="1" width="{w-2}" height="{h-2}" rx="16" fill="#FFFFFF" stroke="{LINE}" stroke-width="2"/>
  <line x1="1" y1="62" x2="{w-1}" y2="62" stroke="{LINE}" stroke-width="2"/>
  <text x="48" y="39" class="mono" font-size="14" letter-spacing="1.4" fill="{MUTED}">// PRODUCT-SKILLS</text>
  <text x="{w-48}" y="39" class="mono" font-size="14" letter-spacing="1.4" fill="{MUTED}" text-anchor="end">{escape(t['kopf_meta'])}</text>
  <text x="48" y="122" class="mono" font-size="15" letter-spacing="1.6" fill="{MUTED}">{escape(t['kopf_eyebrow'])}</text>
  <text x="46" y="208" font-family="{SANS}" font-size="70" font-weight="700" letter-spacing="-2" fill="{INK}">{escape(t['kopf_z1'])}</text>
  <text x="46" y="292" font-family="{SANS}" font-size="70" font-weight="700" letter-spacing="-2" fill="{INK}">{escape(t['kopf_z2'])}</text>
  <path class="faden" pathLength="1" d="M48,312 C{48+(f-48)*.2:.0f},300 {48+(f-48)*.45:.0f},318 {48+(f-48)*.7:.0f},305 C{48+(f-48)*.8:.0f},300 {48+(f-48)*.92:.0f},310 {f},302"/>
  <text x="48" y="362" font-family="{SANS}" font-size="25" fill="{INK}">{escape(t['kopf_lede'])}</text>
  <text x="{w-48}" y="398" class="mono" font-size="16" fill="{INK}" text-anchor="end">BLUU · Build less. Understand users.<tspan class="cur">▍</tspan></text>
</svg>
'''
# ------------------------------------------------------------------ Klickpfad
def klickpfad(t):
    schritte = t["klick"]
    zeichen, hoehe, luft, pfeil = 9.3, 46, 26, 34   # Monospace 15.5px ≈ 9.3px je Zeichen
    x, y, zeile = 48, 108, 0
    teile = []
    takt = 0.7
    for i, s in enumerate(schritte):
        breite = len(s) * zeichen + 2 * luft
        if i > 0:
            if x + pfeil + breite > 1152:
                x, y = 48, y + hoehe + 26
            teile.append(f'<text class="pfeil" x="{x+pfeil/2:.0f}" y="{y+29}" text-anchor="middle">→</text>')
            x += pfeil
        eingabe = "eingabe" if "/" in s else ""
        teile.append(f'''<g class="chip {eingabe}" style="animation-delay:{i*takt:.1f}s">
      <rect x="{x}" y="{y}" width="{breite:.0f}" height="{hoehe}" rx="10"/>
      <text x="{x+luft}" y="{y+29}">{escape(s)}</text></g>''')
        x += breite
    gesamt = len(schritte) * takt + 2.5
    h = y + hoehe + 70
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{h}" viewBox="0 0 1200 {h}" role="img" aria-label="{escape(t['klick_label'])}">
  <style>
    .chip rect {{ fill: #FFFFFF; stroke: {INK}; stroke-width: 1.6; }}
    .chip text {{ font: 400 15.5px {MONO}; fill: {INK}; }}
    .chip.eingabe rect {{ fill: {INK}; }}
    .chip.eingabe text {{ fill: #FFFFFF; }}
    .chip {{ animation: an {gesamt:.1f}s steps(1) infinite; }}
    @keyframes an {{ 0% {{ opacity: .28; }} 6% {{ opacity: 1; }} 100% {{ opacity: 1; }} }}
    .pfeil {{ font: 400 18px {MONO}; fill: {MUTED}; }}
    {REDUZIERT}
  </style>
  <rect x="1" y="1" width="1198" height="{h-2}" rx="16" fill="#FFFFFF" stroke="{LINE}" stroke-width="2"/>
  <text x="48" y="62" font-family="{MONO}" font-size="15" letter-spacing="1.6" fill="{MUTED}">{escape(t['klick_titel'])}</text>
  {"".join(teile)}
</svg>
'''


# ------------------------------------------------------------------ Chat


def woerter(text):
    """Zerlegt **fett** markierten Text in (wort, fett)-Paare."""
    erg, fett = [], False
    for teil in text.split("**"):
        for w in teil.split():
            erg.append((w, fett))
        fett = not fett
    return erg


def umbrechen(paare, max_zeichen):
    zeilen, akt, laenge = [], [], 0
    for w, f in paare:
        if akt and laenge + 1 + len(w) > max_zeichen:
            zeilen.append(akt)
            akt, laenge = [], 0
        akt.append((w, f))
        laenge += len(w) + (1 if laenge else 0)
    if akt:
        zeilen.append(akt)
    return zeilen


def zeile_svg(zeile):
    teile = []
    for i, (w, f) in enumerate(zeile):
        t = escape(w) + (" " if i < len(zeile) - 1 else "")
        teile.append(f'<tspan font-weight="700">{t}</tspan>' if f else t)
    return "".join(teile)


def chat(tx):
    w = 1200
    y = 92
    t = 0.6
    teile = []
    vorher = None
    for wer, text in tx["chat"]:
        if wer == "du":
            zeilen = umbrechen(woerter(text), 74)
            bh = len(zeilen) * 27 + 26
            bx, bw = w - 48 - 740, 740
            y += 10
            inhalt = "".join(f'<text x="{bx+20}" y="{y+36+i*27}" class="du">{zeile_svg(z)}</text>' for i, z in enumerate(zeilen))
            teile.append(f'<g class="b" style="animation-delay:{t:.2f}s"><rect x="{bx}" y="{y}" width="{bw}" height="{bh}" rx="16" fill="#ECE9DF"/>{inhalt}</g>')
            y += bh + 26
            t += 1.0
        else:
            if vorher == "du":
                teile.append(f'<text class="denkt" x="48" y="{y+14}" style="animation-delay:{t:.2f}s"><tspan fill="#B4583A">✳</tspan> {escape(tx['chat_denkt'])}</text>')
                t += 1.3
                teile.append(f'<text class="b label" x="48" y="{y+14}" style="animation-delay:{t:.2f}s">✳ CLAUDE</text>')
                y += 34
            zeilen = umbrechen(woerter(text), 108)
            inhalt = "".join(f'<text x="48" y="{y+22+i*30}" class="claude">{zeile_svg(z)}</text>' for i, z in enumerate(zeilen))
            teile.append(f'<g class="b" style="animation-delay:{t:.2f}s">{inhalt}</g>')
            y += len(zeilen) * 30 + 18
            t += 0.9
        vorher = wer
    y += 20
    h = y + 70
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(tx['chat_label'])}">
  <style>
    .du {{ font: 400 18px {SANS}; fill: #1F1E1D; }}
    .claude {{ font: 400 19px {SERIF}; fill: #1F1E1D; }}
    .label {{ font: 400 12px {MONO}; fill: #B4583A; letter-spacing: .8px; }}
    .denkt {{ font: 400 14px {MONO}; fill: #9A968B; opacity: 0; animation: denk 1.3s linear forwards; }}
    @keyframes denk {{ 0% {{ opacity: 0; }} 12% {{ opacity: 1; }} 85% {{ opacity: 1; }} 100% {{ opacity: 0; }} }}
    .b {{ animation: ein .45s ease backwards; }}
    @keyframes ein {{ from {{ opacity: 0; transform: translateY(6px); }} to {{ opacity: 1; transform: none; }} }}
    {REDUZIERT}
  </style>
  <rect x="1" y="1" width="{w-2}" height="{h-2}" rx="16" fill="#FAF9F5" stroke="#E4E2DA" stroke-width="2"/>
  <path d="M1 17 A16 16 0 0 1 17 1 H{w-17} A16 16 0 0 1 {w-1} 17 V52 H1 Z" fill="#F0EEE6"/>
  <circle cx="30" cy="27" r="7" fill="#E5645B"/><circle cx="54" cy="27" r="7" fill="#E7C37E"/><circle cx="78" cy="27" r="7" fill="#7FB685"/>
  <text x="108" y="32" font-family="{MONO}" font-size="13" letter-spacing="1.2" fill="#7A776E">CLAUDE · CHAT</text>
  <text x="{w-30}" y="32" font-family="{MONO}" font-size="13" letter-spacing="1.2" fill="#7A776E" text-anchor="end">{escape(tx['chat_rechts'])}</text>
  {"".join(teile)}
  <rect x="30" y="{h-62}" width="{w-60}" height="44" rx="12" fill="#FFFFFF" stroke="#DEDBD0"/>
  <text x="50" y="{h-34}" font-family="{SANS}" font-size="16" fill="#A8A498">{escape(tx['chat_eingabe'])}</text>
</svg>
'''


# ------------------------------------------------------------------ Wege in die KI


def wege(t):
    w, kb, kh, luft = 1200, 540, 268, 24
    teile = []
    for i, (kopf_, titel, schritte, empfohlen, hinweis) in enumerate(t["wege"]):
        x = 48 + (i % 2) * (kb + luft)
        y = 92 + (i // 2) * (kh + luft)
        rahmen = INK if empfohlen else LINE
        teile.append(f'<rect x="{x}" y="{y}" width="{kb}" height="{kh}" rx="12" fill="#FFFFFF" stroke="{rahmen}" stroke-width="{2 if empfohlen else 1.6}"/>')
        teile.append(f'<text x="{x+26}" y="{y+38}" font-family="{MONO}" font-size="13" letter-spacing="1.3" fill="{MUTED}">{escape(kopf_)}</text>')
        if empfohlen:
            teile.append(f'<rect x="{x+kb-136}" y="{y+20}" width="112" height="26" rx="6" fill="{INK}"/><text x="{x+kb-80}" y="{y+38}" font-family="{MONO}" font-size="12" fill="#FFFFFF" text-anchor="middle" letter-spacing="1">{t['wege_badge']}</text>')
        teile.append(f'<text x="{x+26}" y="{y+76}" font-family="{SANS}" font-size="24" font-weight="700" fill="{INK}">{escape(titel)}</text>')
        for j, st in enumerate(schritte):
            yy = y + 118 + j * 32
            teile.append(f'<text x="{x+26}" y="{yy}" font-family="{MONO}" font-size="14" font-weight="700" fill="{INK}">0{j+1}</text>')
            teile.append(f'<text x="{x+62}" y="{yy}" font-family="{SANS}" font-size="17" fill="{INK}">{escape(st)}</text>')
        teile.append(f'<text x="{x+26}" y="{y+kh-22}" font-family="{MONO}" font-size="12" letter-spacing=".6" fill="{MUTED}">{escape(hinweis)}</text>')
    h = 92 + 2 * kh + luft + 44
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(t['wege_label'])}">
  <rect x="1" y="1" width="{w-2}" height="{h-2}" rx="16" fill="#FFFFFF" stroke="{LINE}" stroke-width="2"/>
  <text x="48" y="58" font-family="{MONO}" font-size="15" letter-spacing="1.6" fill="{MUTED}">{escape(t['wege_titel'])}</text>
  {"".join(teile)}
</svg>
'''


if __name__ == "__main__":
    for alt in ZIEL.glob("*.svg"):
        alt.unlink()
    for lang, t in T.items():
        schreibe(f"kopf-{lang}-{BV}.svg", kopf(t))
        schreibe(f"klickpfad-{lang}-{BV}.svg", klickpfad(t))
        schreibe(f"wege-{lang}-{BV}.svg", wege(t))
        schreibe(f"product-coach-chat-{lang}-{BV}.svg", chat(t))
