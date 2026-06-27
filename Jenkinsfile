pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/ramshadthacharith-ops/Book-serch.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t library-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop library-app || true'
                sh 'docker rm library-app || true'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d --name library-app -p 5000:5000 library-app'
            }
        }
    }
}
