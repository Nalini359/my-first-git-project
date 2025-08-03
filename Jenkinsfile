pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/Nalini359/my-first-git-project'
            }
        }

        stage('Docker Version Test') {
            steps {
                sh 'docker version'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-python-app .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run --rm my-python-app'
            }
        }
    }
}
