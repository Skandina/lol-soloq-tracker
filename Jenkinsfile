pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out LoL SoloQ Tracker'
            }
        }
    stage('Check Python') {
        steps {
            bat '"C:\\Python311\\python.exe" --version'
            }
        }
        stage('Build') {
            steps {
                echo 'Preparing Python environment'
            }
        }
        stage('Install Dependencies') {
            steps {
                bat '"C:\\Python311\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Python Script') {
            steps {
                withCredentials([
                    string(credentialsId: 'riot-api-key', variable: 'RIOT_API_KEY'),
                    string(credentialsId: 'faker-puuid', variable: 'FAKER_PUUID')
                ]) {
                    bat '"C:\\Python311\\python.exe" src\\main.py'
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests'
            }
        }
    }
}