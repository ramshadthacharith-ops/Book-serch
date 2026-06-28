pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/ramshadthacharith-ops/Book-serch.git'
            }
        }

        stage('Verify Environment') {
            steps {
                sh '''
                echo "==== Workspace ===="
                pwd
                ls -la

                echo "==== Docker Versions ===="
                docker version
                docker compose version
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                echo "Stopping old containers..."
                docker compose down || true

                echo "Building and starting containers..."
                docker compose up -d --build
                '''
            }
        }

        stage('Wait for Startup (Health Check)') {
            steps {
                sh '''
                set +e

                echo "Waiting for API to be ready..."

                for i in $(seq 1 12); do
                    echo "Attempt $i: checking API..."
                    
                    curl -s -f http://localhost:5000/books && {
                        echo "API is UP!"
                        exit 0
                    }

                    sleep 5
                done

                echo "API failed to start in time"

                echo "==== Docker Logs (library-app) ===="
                docker logs library-app --tail 50 || true

                exit 1
                '''
            }
        }

        stage('Test API') {
            steps {
                sh '''
                echo "Running final API test..."
                curl -s http://localhost:5000/books
                '''
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
