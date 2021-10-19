utiliser ppilot5 v3.2
---------------------

ppilot permet d�utiliser des syst�mes de synth�se vocale compatibles SAPI5.

Lancement
ppilot5 -b 127.255.255.255:2010 -r Hortense -o "Microsoft Hortense"
Sans arguments, ppilot5 utilise l'adresse de bus 127.255.255.255:2010 avec la premi�re TTS trouv�e sur le syst�me

  -b adresse_IP:port
  -r nom sous lequel appara�tra l�agent sous ivy
  -o nom du moteur de synth�se utilis� (ici, la TTS "Microsoft Hortense", TTS par d�faut sous windows)

Commandes
  * Synth�se
    - ppilot5 Say="hello" ppilot5 prononce "hello" et renvoie ppilot5 Answer=Finished quand le buffer est vide
	- ppilot5 SaySSML=<sequence_SSML>* ppilot5 prononce la s�quence SSML et renvoie ppilot5 Answer=Finished quand le buffer est vides

	* Les balises <speak> et </speak> sont automatiquement ajout�es au flux 

Exemple de s�quence SSML : 
	ppilot5 SaySSML=Je peux parler <emphasis level="strong">tr�s fort</emphasis> si je veux !	

  * Commandes
    - ppilot5 Command=Stop la synth�se vocale devrait �tre stopp�e.
    - ppilot5 Command=Pause la synth�se vocale est mise en pause. ppilot5 renvoie ppilot5 Answer=Paused
    - ppilot5 Command=Resume la synth�se vocale est relanc�e si elle �tait en pause pr�c�demment. ppilot5 renvoie ppilot5 Answer=Resumed
    - ppilot5 Command=Quit l�application se ferme

  * Param�tres
    - ppilot5 Param=Pitch:value le pitch devrait �tre chang� par la valeur donn�e. (ne fonctionne pas !)
    - ppilot5 Param=Speed:value la vitesse est chang�e par la valeur donn�e. ppilot5 renvoie ppilot5 Answer=SpeedValueSet:value
    - ppilot5 Param=Volume:value le volume est chang� par la valeur donn�e. ppilot5 renvoie ppilot5 Answer=VolumeValueSet:value

    