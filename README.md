# BRAs_VoiceAndVision

## Vue d'ensemble

**BRAs_VoiceAndVision** est un système d'interface avancé conçu pour un exosquelette de bras qui intègre des commandes vocales et une vision par ordinateur afin d'améliorer l'interaction et le contrôle de l'utilisateur. Ce projet utilise des technologies de pointe pour créer une expérience fluide et intuitive. Les composants principaux de ce système sont :

- [**pyzed**](https://www.stereolabs.com/docs/object-detection) : Un wrapper Python pour la caméra stéréo ZED de Stereolabs, offrant une perception de profondeur de haute qualité et une conscience spatiale.
- [**openai-whisper**](https://openai.com/index/whisper/) : Un puissant modèle de reconnaissance vocale développé par OpenAI, permettant une reconnaissance précise des commandes vocales.
- [**yolov8**](https://yolov8.com/) : La dernière itération du modèle de détection d'objets YOLO (You Only Look Once), offrant des capacités de détection d'objets en temps réel et précises.

## Fonctionnalités

- **Reconnaissance des Commandes Vocales** : Utilise `openai-whisper` pour transcrire avec précision les commandes vocales en texte.
- **Détection d'Objets en Temps Réel** : Utilise `yolov8` pour identifier et suivre les objets dans l'environnement.
- **Détection de Profondeur** : Utilise `pyzed` pour la conscience spatiale et les informations de profondeur.

## Prérequis

Assurez-vous d'avoir les exigences logicielles et matérielles suivantes :

- Python 3.7 ou supérieur
- Caméra stéréo ZED (pour `pyzed`)
- GPU compatible pour YOLOv8 et OpenAI Whisper
- Bibliothèques Python requises

## Installation

### 1. Clonez le Répertoire

```bash
git clone https://github.com/your-username/BRAs_VoiceAndVision.git
cd BRAs_VoiceAndVision
