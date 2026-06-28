pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/ramshadthacharith-ops/Book-serch.git'
            }
        }

        stage('Verify Workspace') {
            steps {
                sh '''
                pwd
                ls -la
                docker version
                docker compose version
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                docker compose down || true
                docker compose up -d --build
                '''
            }
        }

        stage('Wait for Startup') {
            steps {
                sh 'sleep 20'
            }
        }

        stage('Test API') {
            steps {
                sh 'curl http://localhost:5000/books'
            }
        }
    }

    post {
        success {
            echo '✅ Deployment Successful'
        }
        failure {
            echo '❌ Deployment Failed'
        }
    }
}
