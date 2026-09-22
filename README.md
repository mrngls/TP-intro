# Bac à sable — Prise en main OpenCode

Exercice de prise en main d'OpenCode (phase 2 du TP, ~20-25 min). Pas d'enjeu de compréhension
d'un vrai dépôt : l'objectif est uniquement de se familiariser avec les mécaniques de l'outil.

## Déroulé

1. **Prise de contexte** : `cd bac-a-sable`, `opencode`, puis `/init` — vérifier que l'`AGENTS.md`
   généré décrit correctement le projet.

2. **Diagnostiquer et corriger un bug connu** : lancer `pytest` (un test échoue), puis demander
   « Le test `test_is_palindrome_with_spaces` échoue, explique pourquoi et corrige `is_palindrome`. »
   — observer le diff, l'accepter, relancer `pytest` pour confirmer.

3. **Écrire une fonction à partir d'une spec** : « Implémente `word_frequency(text)` : dictionnaire
   {mot: occurrences}, insensible à la casse, en ignorant la ponctuation. » — vérifier le résultat
   à la main sur un exemple avant d'accepter.

4. **Écrire les tests correspondants** : « Ajoute des tests pytest pour `word_frequency`, y compris
   un texte vide et un texte avec ponctuation. » — lancer `pytest` et juger si les cas limites sont
   vraiment couverts, pas seulement le cas trivial.

5. **Tester l'annulation** : demander une modification volontairement sous-spécifiée
   (« rends `is_palindrome` plus rapide », sans autre précision) — observer ce que l'IA décide
   d'elle-même, puis `/undo` si le résultat ne convient pas.

6. **(Optionnel)** Comparer deux modèles : `/models`, changer de modèle Aristote, redemander
   `celsius_to_fahrenheit` avec le même prompt, comparer les deux résultats.

## Lancer les tests

```bash
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate sous Windows
pip install pytest
pytest
```
