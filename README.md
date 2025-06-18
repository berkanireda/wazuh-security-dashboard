# wazuh-security-dashboard
Tableau de bord web interactif pour la visualisation des alertes et de l'état du SIEM Wazuh. Conçu pour une surveillance de sécurité intuitive et en temps réel.

# Wazuh Security Dashboard

![License](https://img.shields.io/badge/license-MIT-blue.svg)


Tableau de bord web interactif pour la visualisation des alertes et de l'état du SIEM Wazuh. Conçu pour une surveillance de sécurité intuitive et en temps réel.

---

### Aperçu

**(IMPORTANT : Remplacez l'image ci-dessous par une vraie capture d'écran de votre dashboard ! C'est l'élément le plus vendeur.)**


Ce projet a pour but de fournir une interface claire et réactive pour interagir avec l'API de Wazuh. Que vous soyez un analyste de sécurité, un administrateur système ou simplement un passionné de cybersécurité, ce tableau de bord vous aidera à obtenir des informations exploitables à partir de vos données Wazuh.

### ✨ Fonctionnalités

* **Vue d'Ensemble en Temps Réel :** Visualisez les dernières alertes de sécurité dès leur apparition.
* **Santé des Agents :** Surveillez le statut de tous vos agents Wazuh (Actif, Déconnecté, Jamais connecté).
* **Top 5 des Alertes :** Identifiez rapidement les règles de sécurité les plus fréquemment déclenchées.
* **Filtrage et Recherche :** Recherchez des alertes spécifiques par niveau, par groupe d'agents ou par description.
* **Design Responsive :** Accessible sur ordinateur de bureau et appareils mobiles.
* **Configuration Facile :** Connexion à votre API Wazuh via un simple fichier de configuration.

### 🔧 Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants :

* Une instance de **Wazuh Manager** (v4.x ou supérieure) fonctionnelle.
* Un accès à l'**API de Wazuh** avec un utilisateur et un mot de passe.
* **Node.js** (v18.x ou supérieure) et **npm** installés sur votre machine.
* **Git** pour cloner le dépôt.

### 🚀 Installation

Suivez ces étapes pour mettre en place le projet localement :

1.  **Clonez le dépôt :**
    ```bash
    git clone [https://github.com/VOTRE_NOM_UTILISATEUR/wazuh-security-dashboard.git](https://github.com/VOTRE_NOM_UTILISATEUR/wazuh-security-dashboard.git)
    cd wazuh-security-dashboard
    ```

2.  **Installez les dépendances :**
    ```bash
    npm install
    ```

3.  **Configurez l'environnement :**
    Copiez le fichier d'exemple `.env.example` et renommez-le en `.env`.
    ```bash
    cp .env.example .env
    ```
    Modifiez ensuite le fichier `.env` avec les informations de votre API Wazuh :
    ```ini
    # URL de votre API Wazuh
    WAZUH_API_URL=https://votre-adresse-wazuh:55000

    # Identifiants de l'utilisateur de l'API
    WAZUH_API_USER=votre_user
    WAZUH_API_PASSWORD=votre_mot_de_passe
    ```

### ▶️ Utilisation

Une fois la configuration terminée, lancez le serveur de développement :

```bash
npm start
