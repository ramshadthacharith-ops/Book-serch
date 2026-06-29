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
                docker rm -f library-app library-db || true
                docker volume rm book-search-pipeline_pgdata || true
                docker-compose down --remove-orphans || true
                docker-compose up -d --build --remove-orphans
                '''
            }
        }

        stage('Test API') {
            steps {
                sh 'sleep 10 && curl http://192.168.1.7:5000/books'
            }
        }
    }
}
