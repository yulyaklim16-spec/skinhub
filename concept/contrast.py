"""Контраст текста и фона по WCAG 2.1 для пар из concept/tokens.css.

Запуск: python concept/contrast.py
Печатает таблицу в Markdown и вписывает её в concept.md и concept.html между метками
<!-- contrast:start --> и <!-- contrast:end -->.

AA: обычный текст ≥ 4.5:1, крупный (≥ 24px или ≥ 18.66px жирный) ≥ 3:1.
"""
import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent
TOKENS = dict(re.findall(r'(--c-[\w-]+):\s*(#[0-9a-fA-F]{6})', (ROOT / 'tokens.css').read_text(encoding='utf-8')))


def rgb(h):
    h = h.lstrip('#')
    return [int(h[i:i + 2], 16) for i in (0, 2, 4)]


def mix(a, b, p):
    """color-mix(in srgb, a p%, b)"""
    ca, cb = rgb(a), rgb(b)
    return '#' + ''.join(f'{round(x * p + y * (1 - p)):02x}' for x, y in zip(ca, cb))


def lum(h):
    def ch(c):
        c /= 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(c) for c in rgb(h))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg, bg):
    l1, l2 = sorted((lum(fg), lum(bg)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def t(name):
    return TOKENS[name]


# (текст, фон, где встречается, крупный текст?)
PAIRS = [
    ('--c-text', '--c-bg', 'Основной текст и цены на фоне', False),
    ('--c-text', '--c-surface', 'Цены и заголовки в карточках', False),
    ('--c-text-muted', '--c-bg', 'Подписи, FAQ, футер', False),
    ('--c-text-muted', '--c-surface', 'Названия кейсов в карточках', False),
    ('--c-text-muted', '--c-surface-2', 'Подписи в панелях', False),
    ('--c-text-muted', '--c-surface-3', 'Подписи в нижнем меню', False),
    ('--c-text-muted', '--c-surface-2', 'Неактивный таб «Top today»', False),
    ('--c-neutral-200', '--c-bg', 'Текст на чипах оплаты', False),
    ('--c-on-accent', '--c-accent', 'Кнопка действия: Sign in', False),
    ('--c-bg', '--c-text', 'Белая кнопка, плашка EVENT', False),
    ('--c-accent', '--c-bg', 'Заголовки баннеров лаймом', True),
    ('--c-accent', '--c-surface', 'Лайм на карточке', False),
    ('--c-success', '--c-bg', 'Текст успеха', False),
    ('--c-error', '--c-bg', 'Текст ошибки', False),
    ('--c-on-state', '--c-success', 'Плашка успеха', False),
    ('--c-on-state', '--c-error', 'Плашка ошибки', False),
    ('--c-rarity-covert-text', '--c-surface', 'Бейдж Covert', False),
    ('--c-rarity-classified-text', '--c-surface', 'Бейдж Classified', False),
    ('--c-rarity-gold-text', '--c-surface', 'Бейдж Fade · FN', False),
]
# карточка дропа: белое название на фоне, смешанном из цвета редкости (34%) и поверхности
for r in ['milspec', 'restricted', 'classified', 'covert', 'gold']:
    PAIRS.append(('--c-text', ('mix', f'--c-rarity-{r}'), f'Название на плитке дропа: {r}', False))

# вайрфрейм страницы кейса (wireframes/case.html)
PAIRS += [
    ('--c-text', '--c-bg-deep', 'Кейс: текст страницы', False),
    ('--c-text-muted', '--c-bg-deep', 'Кейс: лид, подписи, заметки', False),
    ('--c-accent', '--c-bg-deep', 'Кейс: ссылки', False),
    ('--c-success', '--c-bg-deep', 'Кейс: метка версии v1.x', False),
    ('--c-live', '--c-bg', 'Кейс: подпись «fold · 844 px»', False),
    ('--c-bg', '--c-text', 'Кейс и главная: счётчик Battles в нижнем меню', False),
    ('--c-info', '--c-bg', 'Иконка смены языка (не текст, ≥ 3)', True),
    ('--c-neutral-200', '--c-surface-well', 'Кейс: бейдж +XP', False),
    ('--c-neutral-200', '--c-surface', 'Кейс: бейдж DEMO', False),
    ('--c-text-muted', '--c-surface', 'Кейс: неактивный сегмент Real', False),
    ('--c-error', ('mix', '--c-error', 0.14, '--c-surface-2'), 'Кейс: метка «НЕТ»', False),
]
for r in ['milspec', 'restricted', 'classified', 'covert', 'gold']:
    PAIRS.append(('--c-neutral-200', ('mix', f'--c-rarity-{r}'), f'Кейс: подпись и шанс на плитке скина: {r}', False))


def rows():
    out = []
    for fg, bg, where, large in PAIRS:
        fgv = t(fg)
        if isinstance(bg, tuple):
            tok, p, base = (bg[1], 0.34, '--c-surface') if len(bg) == 2 else bg[1:]
            bgv = mix(t(tok), t(base), p)
            bgname = f'{tok} {round(p * 100)}% + {base}'
            bgcss = f'color-mix(in srgb,var({tok}) {round(p * 100)}%,var({base}))'
        else:
            bgv, bgname, bgcss = t(bg), bg, f'var({bg})'
        r = ratio(fgv, bgv)
        need = 3.0 if large else 4.5
        out.append((fg, fgv, bgname, bgv, r, need, r >= need, where, bgcss))
    return out


def markdown(rs):
    lines = ['| Текст | Фон | Коэффициент | AA | Где |', '|---|---|---|---|---|']
    for fg, fgv, bg, bgv, r, need, ok, where, _ in rs:
        lines.append(f'| `{fg}` {fgv} | `{bg}` {bgv} | {r:.2f}:1 | {"проходит" if ok else "НЕ проходит"} (≥ {need:g}) | {where} |')
    return '\n'.join(lines)


def html(rs):
    body = ''.join(
        f'<tr><td><span class="sw" style="background:var({fg})"></span><code>{fg}</code> {fgv}</td>'
        f'<td><span class="sw" style="background:{bgcss}"></span><code>{bg}</code> {bgv}</td>'
        f'<td class="r"><span class="smp" style="color:var({fg});background:{bgcss}">Aa $3.10</span></td>'
        f'<td class="r">{r:.2f}:1</td><td class="{"ok" if ok else "no"}">{"проходит" if ok else "не проходит"} <small>≥ {need:g}</small></td><td>{where}</td></tr>'
        for fg, fgv, bg, bgv, r, need, ok, where, bgcss in rs)
    return ('<div class="tw"><table class="ct"><thead><tr><th>Текст</th><th>Фон</th><th>Образец</th><th>Коэффициент</th><th>AA</th><th>Где</th></tr></thead>'
            f'<tbody>{body}</tbody></table></div>')


def inject(path, text):
    p = ROOT / path
    s = p.read_text(encoding='utf-8')
    s2, n = re.subn(r'(<!-- contrast:start -->).*?(<!-- contrast:end -->)', lambda m: m[1] + '\n' + text + '\n' + m[2], s, flags=re.S)
    if n:
        p.write_text(s2, encoding='utf-8')
    return n


if __name__ == '__main__':
    rs = rows()
    md = markdown(rs)
    print(md)
    print('\nне проходят:', sum(not r[6] for r in rs), 'из', len(rs))
    inject('concept.md', md)
    inject('concept.html', html(rs))
