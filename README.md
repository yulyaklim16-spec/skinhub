# SkinHub

Геймифицированная платформа вокруг скинов Counter-Strike 2. Это дизайн-репозиторий:
исследование, вайрфреймы, концепт, токены, компоненты, дизайн-система и хендоф.

Бриф продукта и рабочие соглашения: [`CLAUDE.md`](./CLAUDE.md).

**Сайт для просмотра:** https://skinhub-topaz.vercel.app — HTML-версии всех этапов. Деплоится на Vercel
автоматически при каждом push в `main`. На сайт попадают только HTML (см. `.vercelignore`).

**Форматы.** У каждого артефакта пара файлов с одним именем: `.md` для Claude (рабочий источник)
и `.html` для человека (просмотреть, показать заказчику, задеплоить). HTML автономный: один файл,
картинки встроены. Чтобы открыть его, скачайте файл и откройте в браузере.

> Этот файл — живой индекс репозитория. Каждый новый артефакт или завершённый этап
> добавляется сюда сразу.

## Статус

| Этап | Папка | Статус | Для Claude | Для человека |
|---|---|---|---|---|
| 1. Исследование | [`research/`](./research/) | ✅ Готово · 2026-10-02 | [`research.md`](./research/research.md) | [`research.html`](./research/research.html) |
| 2. Вайрфреймы | [`wireframes/`](./wireframes/) | 🔄 В работе · главная v12.1, кейс v1.3 | [`home.md`](./wireframes/home.md), [`case.md`](./wireframes/case.md) | [`home.html`](./wireframes/home.html), [`case.html`](./wireframes/case.html) |
| 3. Концепт | [`concept/`](./concept/) | 🟡 Главная v1 | — | — |
| 4. Токены | [`tokens/`](./tokens/) | ⬜ Не начат | — | — |
| 5. Компоненты | [`components/`](./components/) | ⬜ Не начат | — | — |
| 6. Дизайн-система | [`design-system/`](./design-system/) | ⬜ Не начат | — | — |
| 7. Хендоф | [`handoff/`](./handoff/) | ⬜ Не начат | — | — |

## Индекс

### research/
- [`research.md`](./research/research.md) — разбор 7 конкурентов: оценки, воронка первого кейса,
  нижнее меню на мобайле (состав и читабельность), блоки контента на главной, выводы для SkinHub.
- [`research.html`](./research/research.html) — то же для человека: страница со скриншотами,
  один файл (~2,2 МБ). [Опубликованная версия](https://claude.ai/artifact/7ZuPFD7zzDVnxE3rsFewfv).
- [`review-fable.md`](./research/review-fable.md) / [`review-fable.html`](./research/review-fable.html) — независимое UX-ревью
  вайрфреймов агентом на модели Fable: 26 замечаний, чего нет относительно конкурентов, противоречия и недостающие экраны.
- [`screens/`](./research/screens/) — 19 скриншотов: главная, страница кейса и мобильный экран
  Casehug, Hellcase, Skin.club, Rain.gg, Forcedrop, JamSkins, Upgrader.pro.

### wireframes/
- [`home.md`](./wireframes/home.md) / [`home.html`](./wireframes/home.html) — главная v12.1: лента дропов,
  меню, карусель героя без стрелок с выглядывающим следующим слайдом (на десктопе три в ряд), офферы с таймером, промокод в баннере, каталог.
  Журнал решений внутри. [Опубликованная версия](https://claude.ai/artifact/1uap1AuMtoQEx1KNozQQAn).
- [`case.md`](./wireframes/case.md) / [`case.html`](./wireframes/case.html) — страница кейса v1.7:
  гость до открытия, рулетка, результат демо, результат игрока; десктоп. Журнал решений внутри. Журнал решений внутри.
- Следующие экраны: вход, Rewards (миссии и прогресс), апгрейд, инвентарь и вывод.

### concept/
- [`home.md`](./concept/home.md) / [`home.html`](./concept/home.html) — концепт главной v1: мобайл и десктоп,
  [холст в Claude Design](https://claude.ai/artifact/VGpSEgEJ7XKhLT6MGtfWNM).
- [`concept.md`](./concept/concept.md) / [`concept.html`](./concept/concept.html) — концепт: атрибуты, вкус дизайнера
  (Netflix, beton.ua), правила графики для экранов.
- [`references.md`](./concept/references.md) / [`references.html`](./concept/references.html) — референсы из Refero:
  основа — стиль Home (тёмный, один лаймовый акцент), приёмы из Portal и Discord, экраны Home Page Xbox, Epic Games, Twitch.
  У каждого приёма — какое волнение пользователя он снимает.

### tokens/
Пусто.

### components/
Пусто.

### design-system/
Пусто.

### handoff/
Пусто.

## Ключевые выводы исследования

1. Попробовать до входа: демо-открытие без регистрации.
2. Первый экран продаёт ивент: лента дропов, герой с таймером; каталог сразу под ним (решение 2026-10-02).
3. Награда за прогресс (XP) видна на кнопке действия.
4. Ежедневная петля: миссии, бесплатный кейс по уровню, сезоны.
5. Provably Fair и шансы в процентах на каждом открытии.
6. Одна строка режимов, новые режимы открываются по уровню.
