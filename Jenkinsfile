pipeline {
    agent any

    stages {

        stage('Clean Workspace') {
            steps {
                deleteDir()
            }
        }

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/ramshadthacharith-ops/Book-serch.git'
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                docker-compose down --remove-orphans || true
                docker-compose rm -fsv || true
                docker-compose up -d --build --remove-orphans
                '''
            }
        }

        stage('Test API') {
            steps {
                sh 'curl http://localhost:5000/books'
            }
        }
    }
}
