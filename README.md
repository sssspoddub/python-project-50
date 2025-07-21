# ⚡️ GendiffX

> **GendiffX** — утилита-«дифф» для конфигурационных файлов JSON и YAML.  
> Она строит различия между двумя файлами и выводит результат в одном из трёх форматов: **stylish**, **plain**, **json**.

![Actions Status](https://github.com/sssspoddub/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)
![SonarCloud Coverage](https://sonarcloud.io/api/project_badges/measure?project=sssspoddub_python-project-50&metric=coverage)
[![asciicast](https://asciinema.org/a/8qkPEhB2FT2F0TjcWvtiMxe.svg)](https://asciinema.org/a/8qkPEhB2FT2F0TjcWvtiMxe)

---

## ✨ Возможности
- Сравнение **JSON** и **YAML** файлов любой вложенности.  
- Форматы вывода:
  - **stylish** — человекочитаемое дерево;
  - **plain** — плоский текст (удобно для логов);
  - **json** — машинно-читаемый вывод.  
- CLI-интерфейс и программный API.  
- Покрытие тестами > 90 % и строгий линтинг `ruff`.

## 🔧 Установка

```bash
pip install --user -r requirements.txt
make install            # для локальной разработки
