# Lernmodul Texte

Dieses Lernmodul beschäftigt sich mit der Verarbeitung und Analyse von rohen Textdaten, wie sie auf dem sozialen Netzwerk [Twitter](https://twitter.com) in Form von Tweets erzeugt werden. Im Zuge der Sentiment Analysis im Forschungsfeld des Natural Language Processing (NLP) klassifiziert ein Vorhersagemodell einen Tweet anhand seiner (negativen oder positiven) Stimmung. Über die Vorhersage mehrerer Tweets kann so ein Stimmungsbild der Tweets erzeugt werden, welches wiederum von nachfolgenden Entscheidermodellen berücksichtigt werden kann.

## Lernmodul starten

[![myBinder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/git/https%3A%2F%2Fprojectbase.medien.hs-duesseldorf.de%2Feild.nrw-module%2Flernmodul-texte.git/development?filepath=index.ipynb)

Dieses Lernmodul lässt sich über den Online-Dienst [myBinder](https://mybinder.org/v2/git/https%3A%2F%2Fprojectbase.medien.hs-duesseldorf.de%2Feild.nrw-module%2Flernmodul-texte.git/development?filepath=index.ipynb) innerhalb von zwei Minuten starten. 

Alternativ lässt sich dieses Lernmodul lokal in einem Docker Container innerhalb von einer Minute über die folgenden Befehle ausführen:

```
docker build -t lernmodul-texte .
docker run -it -p 8888:8888 --name lernmodul-texte --rm lernmodul-texte
```
