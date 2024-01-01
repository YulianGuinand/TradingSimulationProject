De l'Utilisation du Web Scraping à yfinance :

L'accès à des données financières fiables et à jour est crucial pour toute analyse ou stratégie de trading. J’ai essayé d’obtenir ces données de la manière la plus efficace et la plus précise possible. J’ai conclu que finance est le meilleur choix.

1. Le Web Scraping Initial avec Selenium :

Au début de mes recherches, j'ai exploré le web scraping avec Selenium. Cette bibliothèque Python est puissante et offre la capacité d'automatiser les navigateurs web pour extraire des données à partir de sites web, même ceux qui nécessitent une interaction JavaScript. J’ai créé un programme avec Selenium afin de recueillir les données du site https://fr.finance.yahoo.com/.

Le web scraping avec Selenium ait été efficace pour extraire des données mais plusieurs inconvénients sont rapidement apparus :

**Fiabilité** : Certains sites web changent leur structure fréquemment, ce qui nécessite des ajustements constants du code de scraping.

**Performance** : L'automatisation d'un navigateur peut être lente, surtout si l'on souhaite récupérer des données pour de nombreux actifs ou sur une longue période.

**Driver** : Selenium a besoin d’avoir accès au chromedriver.exe devant être installé et mis dans un dossier spécifique. Ce driver doit être de la même version que le chrome installé dans l’ordinateur. Ce choix est donc définitivement mauvais si nous souhaitons partager ce programme.

2. La Transition vers yfinance :

Face aux défis du web scraping, j'ai commencé à rechercher des alternatives plus efficaces. C'est alors que j'ai découvert yfinance, une bibliothèque Python qui offre un accès direct et simple aux données financières via l'API Yahoo Finance.

Voici quelques-uns des points positifs qui m'ont convaincu d'adopter yfinance :

**Fiabilité** : yfinance se connecte directement à une source de données établie et fiable (Yahoo Finance), réduisant ainsi le risque d'erreurs ou d'incohérences dans les données. **Rapidité** : En utilisant une API dédiée, yfinance est significativement plus rapide que le web scraping pour récupérer des données sur plusieurs actifs ou pour des intervalles de temps étendus.

**Facilité d'Utilisation** : yfinance est simple à mettre en place et à utiliser, avec des fonctions claires pour extraire une variété de données financières.

**Mais** en contrepartie il y a un délai entre le temps réel et l’api qui correspond à quelques secondes. Mais comme nous développons un programme de simulation afin d'entraîner l’utilisateur au trading cela ne dérange pas du tout

De plus, yfinance propose de télécharger des données historiques avec un début et une fin ce qui est très pratique si la bourse est fermé et que nous souhaitons quand même tester des stratégie sur celle là.

**En Conclusion** :

Bien que le web scraping avec Selenium soit une technique puissante, les défis liés à sa mise en œuvre et à sa maintenance m'ont conduit à rechercher des solutions alternatives. yfinance s'est avéré être la réponse idéale, offrant fiabilité, rapidité et facilité d'utilisation. Ainsi, nous allons utiliser la bibliothèque yfinance.
