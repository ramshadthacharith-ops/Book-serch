pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/ramshadthacharith-ops/Book-serch.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker compose build
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                docker compose down -v --remove-orphans || true
                docker compose up -d --build
                '''
            }
        }

    }

    post {
        success {
            echo 'Deployment Successful'
        }
        failure {
            echo 'Deployment Failed'
        }
    }
}
