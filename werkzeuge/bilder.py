#!/usr/bin/env python3
"""Erzeugt die animierten SVG-Bilder der README in assets/.

    python3 werkzeuge/bilder.py

Stil wie der Blog „sudo make it simple“: monochrom, Hairlines, Mono-Labels, ein roter Faden.
GitHub zeigt SVGs als <img>; Web-Fonts laden dort nicht, deshalb System-Schriften.
Die Chat-Texte sind wörtliche Auszüge einer echten Sitzung mit einem erfundenen Fall.
"""

from pathlib import Path
from xml.sax.saxutils import escape

ZIEL = Path(__file__).resolve().parent.parent / "assets"

INK, MUTED, LINE, FADEN = "#100F0D", "#7A7A72", "#E4E4DE", "#E5342B"
SANS = "-apple-system, 'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
SERIF = "Georgia, 'Iowan Old Style', 'Times New Roman', serif"
MONO = "ui-monospace, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"

REDUZIERT = "@media (prefers-reduced-motion: reduce) { * { animation: none !important; } .nur-animiert { display: none; } .nur-statisch { display: inline; } }"


def schreibe(name, inhalt):
    ZIEL.mkdir(exist_ok=True)
    (ZIEL / name).write_text(inhalt, encoding="utf-8")
    print("geschrieben:", ZIEL / name)


# ------------------------------------------------------------------ Kopf
def kopf():
    w, h = 1200, 430
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="product-skills: Deine KI nickt alles ab. Diese nicht. Skills für Product Owner – in Claude, Gemini und ChatGPT.">
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
  <text x="{w-48}" y="39" class="mono" font-size="14" letter-spacing="1.4" fill="{MUTED}" text-anchor="end">SKILLS FÜR CLAUDE · GEMINI · CHATGPT · V0.1</text>
  <text x="48" y="122" class="mono" font-size="15" letter-spacing="1.6" fill="{MUTED}">// MARKETPLACE VON MARIE CHRISTIN EILERS</text>
  <text x="46" y="208" font-family="{SANS}" font-size="70" font-weight="700" letter-spacing="-2" fill="{INK}">Deine KI nickt alles ab.</text>
  <text x="46" y="292" font-family="{SANS}" font-size="70" font-weight="700" letter-spacing="-2" fill="{INK}">Diese nicht.</text>
  <path class="faden" pathLength="1" d="M48,312 C120,300 210,318 300,305 C340,300 380,310 410,302"/>
  <text x="48" y="362" font-family="{SANS}" font-size="25" fill="{INK}">Skills für Product Owner – in Claude, Gemini und ChatGPT.</text>
  <text x="{w-48}" y="398" class="mono" font-size="16" fill="{INK}" text-anchor="end">$ sudo make it simple<tspan class="cur">▍</tspan></text>
</svg>
'''


# ------------------------------------------------------------------ Klickpfad
def klickpfad():
    schritte = ["Anpassungen", "Plugins", "Hinzufügen", "Marketplace hinzufügen", "Aus einem Repository hinzufügen", "MarieEilers/product-skills", "Entdecken → product-coach → +"]
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
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{h}" viewBox="0 0 1200 {h}" role="img" aria-label="In der Claude-App: Anpassungen, Plugins, Hinzufügen, Marketplace hinzufügen, Aus einem Repository hinzufügen, MarieEilers/product-skills eintragen, unter Entdecken beim product-coach auf Plus klicken.">
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
  <text x="48" y="62" font-family="{MONO}" font-size="15" letter-spacing="1.6" fill="{MUTED}">// IN DER CLAUDE-APP ODER AUF CLAUDE.AI</text>
  {"".join(teile)}
</svg>
'''


# ------------------------------------------------------------------ Chat
CHAT = [
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
]


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


def chat():
    w = 1200
    y = 92
    t = 0.6
    teile = []
    vorher = None
    for wer, text in CHAT:
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
                teile.append(f'<text class="denkt" x="48" y="{y+14}" style="animation-delay:{t:.2f}s"><tspan fill="#B4583A">✳</tspan> denkt nach …</text>')
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
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Chat mit dem Product Coach in der Claude-App: echte Sitzung mit erfundenem Fall, gekürzt.">
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
  <text x="{w-30}" y="32" font-family="{MONO}" font-size="13" letter-spacing="1.2" fill="#7A776E" text-anchor="end">ECHTE SITZUNG · ERFUNDENER FALL · GEKÜRZT</text>
  {"".join(teile)}
  <rect x="30" y="{h-62}" width="{w-60}" height="44" rx="12" fill="#FFFFFF" stroke="#DEDBD0"/>
  <text x="50" y="{h-34}" font-family="{SANS}" font-size="16" fill="#A8A498">Antworte Claude …</text>
</svg>
'''


# ------------------------------------------------------------------ Wege in die KI
WEGE = [
    ("CLAUDE-APP · MARKETPLACE", "Einmal einrichten, alle Skills", [
        "Anpassungen → Plugins → Hinzufügen",
        "Marketplace hinzufügen → Aus einem Repository",
        "MarieEilers/product-skills eintragen",
        "Unter „Entdecken“ beim Skill auf „+“",
    ], True, "Pro, Max, Team, Enterprise · auch in Cowork"),
    ("CLAUDE-APP · ZIP", "Ein Skill, auch im Gratis-Tarif", [
        "ZIP laden – nicht entpacken",
        "Anpassungen → Skills → Hinzufügen",
        "„Skill hochladen“ → ZIP wählen",
    ], False, "Code-Ausführung muss eingeschaltet sein"),
    ("GEMINI · SKILL", "Dasselbe ZIP, kein Abo nötig", [
        "ZIP laden – nicht entpacken",
        "In Gemini die Skills öffnen",
        "Hochladen → ZIP wählen",
    ], False, "neu seit Oktober 2026, kommt nach und nach"),
    ("CHATGPT · PROJEKT", "Mit der Kurzfassung", [
        "Neues Projekt anlegen",
        "Kurzfassung in die Projektanweisungen",
        "Vorlagen als Dateien dazulegen",
    ], False, "Business und Enterprise: Skill-Upload"),
]


def wege():
    w, kb, kh, luft = 1200, 540, 268, 24
    teile = []
    for i, (kopf_, titel, schritte, empfohlen, hinweis) in enumerate(WEGE):
        x = 48 + (i % 2) * (kb + luft)
        y = 92 + (i // 2) * (kh + luft)
        rahmen = INK if empfohlen else LINE
        teile.append(f'<rect x="{x}" y="{y}" width="{kb}" height="{kh}" rx="12" fill="#FFFFFF" stroke="{rahmen}" stroke-width="{2 if empfohlen else 1.6}"/>')
        teile.append(f'<text x="{x+26}" y="{y+38}" font-family="{MONO}" font-size="13" letter-spacing="1.3" fill="{MUTED}">{escape(kopf_)}</text>')
        if empfohlen:
            teile.append(f'<rect x="{x+kb-136}" y="{y+20}" width="112" height="26" rx="6" fill="{INK}"/><text x="{x+kb-80}" y="{y+38}" font-family="{MONO}" font-size="12" fill="#FFFFFF" text-anchor="middle" letter-spacing="1">EMPFOHLEN</text>')
        teile.append(f'<text x="{x+26}" y="{y+76}" font-family="{SANS}" font-size="24" font-weight="700" fill="{INK}">{escape(titel)}</text>')
        for j, st in enumerate(schritte):
            yy = y + 118 + j * 32
            teile.append(f'<text x="{x+26}" y="{yy}" font-family="{MONO}" font-size="14" font-weight="700" fill="{INK}">0{j+1}</text>')
            teile.append(f'<text x="{x+62}" y="{yy}" font-family="{SANS}" font-size="17" fill="{INK}">{escape(st)}</text>')
        teile.append(f'<text x="{x+26}" y="{y+kh-22}" font-family="{MONO}" font-size="12" letter-spacing=".6" fill="{MUTED}">{escape(hinweis)}</text>')
    h = 92 + 2 * kh + luft + 44
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Vier Wege, einen Skill in deine KI zu bringen: Claude-App über den Marketplace (empfohlen), Claude-App per ZIP, Gemini mit demselben ZIP, ChatGPT als Projekt mit der Kurzfassung.">
  <rect x="1" y="1" width="{w-2}" height="{h-2}" rx="16" fill="#FFFFFF" stroke="{LINE}" stroke-width="2"/>
  <text x="48" y="58" font-family="{MONO}" font-size="15" letter-spacing="1.6" fill="{MUTED}">// SO KOMMT EIN SKILL IN DEINE KI</text>
  {"".join(teile)}
</svg>
'''


if __name__ == "__main__":
    schreibe("kopf-v3.svg", kopf())
    schreibe("klickpfad.svg", klickpfad())
    schreibe("wege.svg", wege())
    schreibe("product-coach-chat.svg", chat())
