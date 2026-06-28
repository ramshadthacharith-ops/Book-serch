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

                echo "==== docker-compose ===="
                docker-compose
                docker-compose version
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                set -e

                echo "Stopping old containers..."
                docker-compose down || true

                echo "Building and starting containers..."
                docker-compose up -d --build
                '''
            }
        }

        stage('Wait for Startup (Health Check)') {
            steps {
                sh '''
                echo "Waiting for API to be ready..."

                for i in $(seq 1 15); do
                    echo "Attempt $i..."

                    if curl -s -f http://localhost:5000/books; then
                        echo "API is UP ✔"
                        exit 0
                    fi

                    sleep 5
                done

                echo "API failed to start"
                docker logs library-app --tail 50 || true
                exit 1
                '''
            }
        }

        stage('Test API') {
            steps {
                sh '''
                echo "Final API validation..."

                STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5000/books)

                if [ "$STATUS" = "200" ]; then
                    echo "API Working ✔"
                    curl http://localhost:5000/books
                else
                    echo "API Failed ❌ HTTP $STATUS"
                    docker logs library-app --tail 50
                    exit 1
                fi
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Deployment Successful"
        }
        failure {
            echo "❌ Deployment Failed"
        }
    }
}
