# OCEAN Personality Short Scale (.NET 10 Console & Python Tkinter)

## Important Disclaimer: Unofficial & Non-Professional Tool

This project is an unofficial and non-professional implementation of the short scale test regarding to the Big Five personality traits (OCEAN) model, which is intended for educational purposes only and SHOULD NOT be used for clinical, employment, or diagnostic purposes. *__It is not affiliated with, endorsed by, or connected to any commercial psychological assessment company or copyright holder of official personality inventories like the NEO-PI-R.__*

The personality assessment items (questions) used in this project were AI-assisted, based on publicly available descriptions of the Big Five Personality Trait framework **without direct replication of copyrighted items**. The descriptions are commonly found online, in books, and within the broader psychological community. It is challenging to trace a definitive, copyright-free origin for each item due to the widespread dissemination of the Big Five Personality Trait theory.

*__If any content in this repository is determined to be inconsistent with copyright guidelines, please contact me immediately via [GitHub Issues](https://github.com/yourusername/OCEAN.ShortScale/issues) or [benjamin_2001@qq.com](mailto:benjamin_2001@qq.com). I will promptly investigate and remove or properly attribute the content in question.__*

## Project Overview
This project provides two implementations of the OCEAN Personality Short Scale Test:
- **C# Console Application**: A command-line interface for quick testing
- **Python Tkinter Application**: A graphical user interface for a more interactive experience

Both versions feature the same set of 40 questions (8 per personality trait) with proper reverse scoring and detailed result analysis.

## Note on Personality Testing

The Big Five personality traits describe general tendencies and are a good starting point for personal growth. However:
- This test is for educational and self-reflection purposes only
- It should not be used for clinical, employment, or diagnostic purposes
- Every person's personality is unique and developable
- For professional personality assessment, consult a qualified psychologist

## Personality Traits Measured

The test measures the five major dimensions of personality according to the Big Five theory:

1. **Openness to Experience** - Imagination, curiosity, creativity, appreciation for art
2. **Conscientiousness** - Organization, reliability, discipline, goal-setting
3. **Extraversion** - Sociability, energy, assertiveness, enthusiasm
4. **Agreeableness** - Compassion, trust, cooperation, empathy
5. **Neuroticism** - Emotional stability, anxiety, stress tolerance, mood swings

## Features

### Common Features
- **40 Questions**: 8 questions per personality trait with appropriate reverse scoring
- **Detailed Analysis**: Average scores, visual representation (star ratings), and trait interpretations
- **Result Saving**: Option to save results to a timestamped text file
- **English Language**: All content is in English for international accessibility

### C# Console Application
- Lightweight and fast
- Simple command-line interface
- Easy to run on any system with .NET installed

### Python Tkinter Application
- User-friendly graphical interface
- Navigation between questions (next/previous)
- Visual progress through the test
- Interactive results display

## Getting Started

### Prerequisites
#### C# Version
- .NET 10.0 or later installed on your system

#### Python Version
- Python 3.7 or later installed on your system
- Tkinter library (usually included with Python)

### Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Pac-Dessert1436/OCEAN.ShortScale.git
   ```
   You can also download the ZIP archive and extract it.

2. Navigate to the project directory:
   ```bash
   cd OCEAN.ShortScale
   ```

### Running the C# Version

```bash
dotnet run OCEAN.ShortScale.cs
```

### Running the Python Version

```bash
python ocean_shortscale.py
```

## Test Instructions

1. Read each statement carefully
2. Rate how well each statement describes you on a scale of 1-5:
   - 1 = Not at all
   - 2 = Slightly
   - 3 = Moderately
   - 4 = Quite well
   - 5 = Perfectly
3. Answer all 40 questions
4. View your results and interpretation
5. Optionally save your results to a file

## Scoring Methodology

- **Forward Questions**: Scores are used as-is (1-5)
- **Reverse Questions**: Scores are reversed (5-1 becomes 1-5)
- **Averages**: For each trait, average score is calculated from all 8 questions
- **Interpretation**: Scores are categorized as Very High, Moderately High, Moderately Low, or Very Low

## Result Interpretation

### Openness to Experience
- **High**: Imaginative, curious, creative, open to new ideas
- **Low**: Practical, traditional, conservative, prefer routine

### Conscientiousness
- **High**: Organized, reliable, disciplined, goal-oriented
- **Low**: Spontaneous, flexible, casual, prefer flexibility

### Extraversion
- **High**: Sociable, talkative, energetic, outgoing
- **Low**: Quiet, reserved, independent, prefer solitude

### Agreeableness
- **High**: Friendly, compassionate, helpful, cooperative
- **Low**: Critical, competitive, skeptical, assertive

### Neuroticism
- **High**: Emotional, anxious, sensitive, prone to stress
- **Low**: Emotionally stable, calm, resilient, stress-resistant

## Project Structure

```
OCEAN.ShortScale/
├── OCEAN.ShortScale.cs      # C# console application
├── ocean_shortscale.py      # Python Tkinter GUI application
├── LICENSE                  # Project license
└── README.md                # This documentation
```

## Acknowledgments

- Based on the Big Five Personality Trait theory
- Developed for educational and self-awareness purposes

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License


This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
