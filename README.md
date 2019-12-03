# GAFF
Generateur Automatique de Fotes de Français

Ce projet est dans le cadre de la réalisation d'un générateur de "fotes" de français

## Projets connexes

Dans le répertoire "Papiers" se trouve des papiers de recherches sur l'orthographe français
* *Des corpus d'erreurs pour TRACE*
* *Typologie des modifications dans les révisions de Wikipédia*
* *Comparaison de types d erreurs orthographiques en FLM et FLE*
* *Identifier les erreurs : une typologie des erreurs* & *Typologie erreurs CATACH*
    * A partir du chapitre 6, la fin n'est pas la même
* *Quelle typologie adopter pour l analyse des erreurs orthographiques des apprenants du FLE*

Plus sur ce qui est du Seq2Seq :
* *Sequence to Sequence Learning with Neural Networks*
* *Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation*

Autre :
* *Liste orthographique de base*

## Corpus

Des travaux sur la langue française existe déjà, notamment :

* [Wikipedia Correction and Paraphrase Corpus (WiCoPaCo)]()
    * Corpus extrait de la totalité des sites [Wikimedia Foundation, Inc](https://wikimediafoundation.org/) (Wikipédia, Wikilivres, Wikinews, etc...)

* [Corpus LARA](https://github.com/fauconnier/corpus-LARA)

* [frWac](https://corpora.dipintra.it/public/run.cgi/corp_info?corpname=frwac_full)
    * Le corpus frWaC est un corpus de textes français collectés dans le domaine *.fr* avec l'utilisation de mots de moyenne fréquence du corpus Le Monde Diplomatique et de listes de vocabulaire français de base comme la sémantique. Le corpus se compose de sites Web français d'une taille totale de 1,3 milliard de mots.
    * [autre source](https://www.sketchengine.eu/frwac-french-corpus/)

## Générateur de fautes (béta)

### Prérequis

```
pip install numpy spacy jupyterlab
```
- Pour lancer le *.ipynb*, executer : ```jupyter-lab```

### Avancement des types de fautes prisent en compte

| **Type de fautes** | **Non géré** | **En cours** | **En partie** | **Géré** |
|:---|:---:|:---:|:---:|:---:|
| Omission de lettre |  |  |  | X|
| Inversion de lettre |  |  | X | X |
| Ajout de lettre |  | X |  |  |
| Confusion |  |  | X | X |
| Erreur phonétique |  |  | X | X |
| Morphogramme |  |  | X |  |
| Erreur logrammique |  |  | X | X |
| Erreur non fonctionnelle |  |  |  | X |

**Résultats :**
- Test generation de fautes versus Grammelect :
    - toutes les fautes sont trouvés hormis celle qui produise d'autre mots existant dans la langue française ;
    - Lorsqu'on demande la correction du mot par Grammelect, celui-ci donnes en premier lieux les mots originaux.

### Ressources pour le dévellopement :

 - [DCODE](https://www.dcode.fr/permutations-avec-repetition), permutations avec repetition

 - [Notice](https://rtemis.hypotheses.org/r-temis-pas-a-pas) d'utilisation pour traitement de corpus avec R

### Ressources pour tous les types de fautes :

 - [Article](https://www.trucsdeblogueuse.com/fautes-orthographe-coulissesdublog-3) sans prétention, sur les fautes d'orthographe dans les blog

 - Article Wikipédia sur la fréquence d'apparition des lettres de l'alphabet : [ici](https://fr.wikipedia.org/wiki/Analyse_fr%C3%A9quentielle) et [là](https://fr.wikipedia.org/wiki/Analyse_fr%C3%A9quentielle) ainsi que l'étude

 - [Liste](https://www.francaisfacile.com/exercices/exercice-francais-2/exercice-francais-95684.php) exaustive de suffixisation

 - [Liste](http://ameliorersonfrancais.com/grammaire/homophone) des différents homophones

 - [Liste](https://www.etudes-litteraires.com/bac-francais/fautes-orthographe.php) de fautes courantes

 - [Etude](http://jetou2013.free.fr/documents/JeTou2013-Actes-p64-69-Katoozian.pdf) comparative de types d’erreurs orthographiques en FLM et FLE

 - [Etude](https://halshs.archives-ouvertes.fr/tel-01226159) sur la normalisation orthographique de corpus dit "bruités"

 - [Liste](https://halshs.archives-ouvertes.fr/search/index/q/*/keyword_t/traitement%20automatique%20du%20langage%20naturel) d'archive sur le traitement automatique du langage naturel

 - [Liste](https://halshs.archives-ouvertes.fr/search/index/q/*/keyword_t/dictionnaires%20%C3%A9lectroniques) d'archive sur les dictionnaires électroniques

 - [Etude/Liste](http://www.ia94.ac-creteil.fr/maitrise-langue/marathon_accompagnement/07_Liste_Ortho_Base_Catach.pdf) des "400" mots les plus utilisés de la langue Française [Annexe](http://ien-saverne.site.ac-strasbourg.fr/marathon/wp-content/uploads/2014/10/8_Typologie_erreurs_CATACH.pdf)

 - [Evaluation](http://www.education.gouv.fr/cid23433/les-performances-en-orthographe-des-eleves-en-fin-d-ecole-primaire-1987-2007-2015.html) gouvernementale sur les performances en orthographe des élèves en fin d'école primaire

 - WiCoPaCo :
	- <a href="https://www.limsi.fr/fr/plateformes-et-ressources/corpus"> Corpus </a>

	- <a href="https://anrtrace.limsi.fr/SpellingCorpus.pdf"> Etude 1 </a>

	- <a href="https://wicopaco.limsi.fr/pub/taln10.pdf"> Etude 2 </a>

	- <a href="https://wicopaco.limsi.fr/pub/typologie-modifications-wikipedia.pdf"> Etude 3 </a>

	- <a href="https://www.limsi.fr/en/laboratory/platforms-and-resources"> Plateforme de ressources </a>


 - Corpus SMS avec fautes :

	- <a href="http://88milsms.huma-num.fr/data4science/corpusdisponible.html"> Corpus </a>

	- <a href="http://www.sms4science.org/userfiles/le%20langage%20SMS%20r%C3%A9v%C3%A9lateur%20d%271comp%C3%A9tence.pdf"> Etude </a>

	- <a href="https://www.huma-num.fr/sites/default/files/lettre_infoinshs_31_partage_experience.pdf"> Article </a>

	- <a href="http://www.sms4science.org/?q=en"> Lien </a>

	- <a href="http://www.smspourlascience.be/"> Lien </a>

## Recherche, code & developpement

### Recherches

Les debuts de tests et d'appropriation de Keras se sont fait principalement à l'aide du code en exemple dans la documentation Keras.
Plus précisement la partie qui concerne le [Seq2Ses d'entrainement Keras](https://keras.io/examples/lstm_seq2seq/) et le [Seq2Seq prédictif](https://keras.io/examples/lstm_seq2seq_restore/).
J'ai pu aussi tester la [génération de texte par LSTM](https://keras.io/examples/lstm_text_generation/) en changeant le dataset par du contenu venant du dataset Wikiquote.

### Developpement

#### Prérequis

Avant de pouvoir utiliser certains fichiers, il faut disposer des librairies suivantes :
[ ! ] *L'utilisation d'un venv est fortement conseillé*

* Pip
```
sudo apt install python3-pip
```

* LXML
```
pip3 install lxml
```

* Scipy

```
pip3 install numpy scipy matplotlib ipython jupyter pandas sympy nose
```

#### Enumération des fichiers utilitaires

Après avoir utilisé différents corpus, différents fichiers de développement ont été développés, notamment :

* **XML strainer**. Permet d'extraire le contenu des balises "modif" dans le corpus v1 ou v2 de WiCoPaCo en un fichier .csv ou .txt. *Si extraction en .txt, alors utilisation possible du corpus_breaker.py à l'issue*

* **Corpus breaker**. Permet de diviser un gros corpus en des "corpus" plus petits. Le corpus en entrée doit être extrait au préalable et doit respecter un format bien spécifique pour être segmenté en fichiers de n lignes souhaitées.

## Outils

* [Grammalecte](https://grammalecte.net/)
