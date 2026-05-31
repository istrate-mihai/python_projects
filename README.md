# python-projects

A collection of standalone Python applications built from scratch — no AI-generated boilerplate, no tutorial copy-paste. Each project targets a specific skill: GUI programming, data processing, automation, web scraping, APIs, games, and more.

This repo is the hands-on complement to the theory covered in [fundamental_algorithms](https://github.com/your-username/fundamental_algorithms).

---

## Philosophy

Reading books and implementing algorithms teaches you *how* Python works. Building real applications teaches you *what* to do with it. This repo is the second half of that equation.

Every project here is small enough to finish in a sitting or two, but real enough to demonstrate something worth showing.

---

## Projects

### GUI Applications

| Project | Folder | Stack | Description | Status |
|---------|--------|-------|-------------|--------|
| Calculator | `calculator/` | tkinter | Full-featured desktop calculator with keyboard support | ✅ Done |
| Text Editor | `text_editor/` | tkinter | Minimal notepad clone — open, edit, save files | ⏳ Pending |
| Unit Converter | `unit_converter/` | tkinter | Convert between metric/imperial units across categories | ⏳ Pending |
| Pomodoro Timer | `pomodoro_timer/` | tkinter | 25/5 work-break timer with session tracking | ⏳ Pending |
| Password Generator | `password_generator/` | tkinter | Configurable password generator with clipboard copy | ⏳ Pending |

### Data & Automation

| Project | Folder | Stack | Description | Status |
|---------|--------|-------|-------------|--------|
| CSV Analyser | `csv_analyser/` | csv, statistics | Summary stats, column inspector, outlier detection | ⏳ Pending |
| Directory Cleaner | `dir_cleaner/` | os, shutil, pathlib | Sort files into folders by extension, dry-run mode | ⏳ Pending |
| Bulk File Renamer | `bulk_renamer/` | pathlib, re | Pattern-based batch renaming with preview | ⏳ Pending |
| JSON Diff Tool | `json_diff/` | json, difflib | Compare two JSON files, highlight changed keys | ⏳ Pending |
| Log Parser | `log_parser/` | re, collections | Parse access logs, produce summary reports | ⏳ Pending |

### Web & APIs

| Project | Folder | Stack | Description | Status |
|---------|--------|-------|-------------|--------|
| Weather CLI | `weather_cli/` | requests, argparse | Fetch current weather by city via OpenWeatherMap | ⏳ Pending |
| GitHub Repo Stats | `github_stats/` | requests | Fetch stars, forks, issues for any public repo | ⏳ Pending |
| URL Shortener CLI | `url_shortener/` | requests | Shorten URLs via a public API from the terminal | ⏳ Pending |
| Hacker News Digest | `hn_digest/` | requests, BeautifulSoup | Scrape and display top HN stories with scores | ⏳ Pending |

### Games & Simulations

| Project | Folder | Stack | Description | Status |
|---------|--------|-------|-------------|--------|
| Alien Invasion | `alien_invasion/` | pygame | 2D arcade shooter — *Python Crash Course* Part 2 | ⏳ Pending |
| Snake | `snake/` | pygame | Classic snake with score tracking and speed scaling | ⏳ Pending |
| Minesweeper | `minesweeper/` | tkinter | Classic minesweeper with grid generation logic | ⏳ Pending |
| Hangman | `hangman/` | tkinter | Word guessing game with a word bank | ⏳ Pending |

### Data Visualisation

| Project | Folder | Stack | Description | Status |
|---------|--------|-------|-------------|--------|
| Data Visualisation | `data_visualization/` | matplotlib, plotly | Charts, scatter plots, CSV graphing — *PCC* Part 2 | ⏳ Pending |
| Stock Price Chart | `stock_chart/` | matplotlib, requests | Fetch and plot price history for any ticker | ⏳ Pending |
| Sorting Visualiser | `sorting_visualiser/` | matplotlib, animation | Watch bubble/merge/quick sort run step-by-step | ⏳ Pending |

### Web Applications

| Project | Folder | Stack | Description | Status |
|---------|--------|-------|-------------|--------|
| Learning Log | `learning_log/` | Django | CRUD app with user auth — *Python Crash Course* Part 2 | ⏳ Pending |
| Personal Budget Tracker | `budget_tracker/` | Flask, SQLite | Income/expense tracker with category breakdowns | ⏳ Pending |
| Paste Bin Clone | `pastebin_clone/` | Flask | Create, view, and expire text pastes | ⏳ Pending |

### Utilities & Scripts

| Project | Folder | Stack | Description | Status |
|---------|--------|-------|-------------|--------|
| Flashcard CLI | `flashcard_cli/` | json, random | Terminal-based flashcard app, JSON deck format | ⏳ Pending |
| Markdown to HTML | `md_to_html/` | re, pathlib | Convert Markdown files to standalone HTML pages | ⏳ Pending |
| Daily Journal CLI | `journal_cli/` | json, datetime | Append entries to a local JSON journal, search by date | ⏳ Pending |

---

## Stack

- Python 3.10+
- stdlib-first: `tkinter`, `os`, `pathlib`, `re`, `json`, `csv`, `argparse`, `urllib`
- Third-party where it earns its place: `requests`, `pygame`, `matplotlib`, `plotly`, `flask`, `django`, `beautifulsoup4`

---

## Setup

```bash
git clone https://github.com/your-username/python-projects.git
cd python-projects

# Each project has its own requirements.txt where needed
cd calculator
python main.py

# For projects with dependencies
pip install -r requirements.txt
python main.py
```

---

## Related

- [fundamental_algorithms](https://github.com/your-username/fundamental_algorithms) — algorithms and CS theory, book by book

---

## Author

**Mihai** — Full-stack developer, Brașov, Romania.  
Building real things to understand how Python works at depth.
