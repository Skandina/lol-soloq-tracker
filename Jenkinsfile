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

        stage('Test') {
            steps {
                echo 'Running tests'
            }
        }
    }
}