
# Mein LLM-Projekt

Dieses Repository enthält den Quellcode für ein Local Language Learning Model (LLM) basierend auf der `transformers`-Bibliothek von Hugging Face. Es umfasst Funktionen zum Stellen von Fragen, zur Dateianalyse sowie zum Fine-Tuning des Modells mit neuen Daten.

## Projektstruktur

```
model/
    wolfram.gguf  # Das vortrainierte Language Model
src/
    fileanalyser.py  # Modul zur Analyse von Textdateien
    logger.py        # Modul für verbesserte Logging-Funktionen
    question.py      # Modul zur Verarbeitung und Beantwortung von Fragen
    trainer.py       # Modul zum Fine-Tuning des Language Models
main.py  # Hauptskript zum Ausführen des Programms
```

## Voraussetzungen

Bevor Sie beginnen, stellen Sie sicher, dass Sie die folgenden Anforderungen erfüllt haben:

- Python 3.8 oder höher
- Pip und Virtualenv

## Installation

Klonen Sie das Repository und navigieren Sie in das Hauptverzeichnis:

```bash
git clone <URL_zu_Ihrem_Repository>
cd <Name_des_geklonten_Verzeichnisses>
```

Erstellen Sie ein virtuelles Umfeld und aktivieren Sie es:

```bash
python -m venv venv
source venv/bin/activate  # Unter Windows verwenden Sie `venv\Scripts\activate`
```

Installieren Sie die erforderlichen Abhängigkeiten:

```bash
pip install -r requirements.txt
```

## Benutzung

Um das Programm zu starten, führen Sie:

```bash
python main.py
```

Folgen Sie den Anweisungen im Terminal, um zwischen verschiedenen Modi zu wählen und Aktionen durchzuführen.

## Beiträge

Beiträge sind willkommen! Für größere Änderungen öffnen Sie bitte zuerst ein Issue, um zu diskutieren, was Sie ändern möchten.

## Lizenz

[MIT](https://choosealicense.com/licenses/mit/)
