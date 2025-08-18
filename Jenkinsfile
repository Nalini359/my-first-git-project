pipeline {
    agent any

    stages {
        stage('Pull Docker Image') {
            steps {
                sh 'docker pull nalini35/my-python-app:latest'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                    if [ "$(docker ps -q -f name=my-python-container)" ]; then
                        docker stop my-python-container
                        docker rm my-python-container
                    fi
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name my-python-container nalini35/my-python-app:latest'
            }
        }
    }
}
