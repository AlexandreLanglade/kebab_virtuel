utiliser ppilot5 v3.2
---------------------

ppilot permet d’utiliser des systèmes de synthèse vocale compatibles SAPI5.

Lancement
ppilot5 -b 127.255.255.255:2010 -r Hortense -o "Microsoft Hortense"
Sans arguments, ppilot5 utilise l'adresse de bus 127.255.255.255:2010 avec la première TTS trouvée sur le système

  -b adresse_IP:port
  -r nom sous lequel apparaîtra l’agent sous ivy
  -o nom du moteur de synthèse utilisé (ici, la TTS "Microsoft Hortense", TTS par défaut sous windows)

Commandes
  * Synthèse
    - ppilot5 Say="hello" ppilot5 prononce "hello" et renvoie ppilot5 Answer=Finished quand le buffer est vide
	- ppilot5 SaySSML=<sequence_SSML>* ppilot5 prononce la séquence SSML et renvoie ppilot5 Answer=Finished quand le buffer est vides

	* Les balises <speak> et </speak> sont automatiquement ajoutées au flux 

Exemple de séquence SSML : 
	ppilot5 SaySSML=Je peux parler <emphasis level="strong">très fort</emphasis> si je veux !	

  * Commandes
    - ppilot5 Command=Stop la synthèse vocale devrait être stoppée.
    - ppilot5 Command=Pause la synthèse vocale est mise en pause. ppilot5 renvoie ppilot5 Answer=Paused
    - ppilot5 Command=Resume la synthèse vocale est relancée si elle était en pause précédemment. ppilot5 renvoie ppilot5 Answer=Resumed
    - ppilot5 Command=Quit l’application se ferme

  * Paramètres
    - ppilot5 Param=Pitch:value le pitch devrait être changé par la valeur donnée. (ne fonctionne pas !)
    - ppilot5 Param=Speed:value la vitesse est changée par la valeur donnée. ppilot5 renvoie ppilot5 Answer=SpeedValueSet:value
    - ppilot5 Param=Volume:value le volume est changé par la valeur donnée. ppilot5 renvoie ppilot5 Answer=VolumeValueSet:value

    