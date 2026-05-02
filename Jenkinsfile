pipeline {
    agent any

    environment {
        APP_CONTAINER = "flask-todo-app"
        TEST_IMAGE = "flask-todo-tests"
        APP_PORT = "5000"
    }

    stages {

        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/mhaseebhassan/td.git'
            }
        }

        stage('Start App') {
            steps {
                sh '''
                    docker stop flask-todo-app || true
                    docker rm flask-todo-app || true
                    docker build -t flask-todo-app .
                    docker run -d --name flask-todo-app -p 5000:5000 flask-todo-app
                    sleep 5
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    docker build -f Dockerfile.test -t flask-todo-tests .
                    docker run --rm --network host flask-todo-tests
                '''
            }
        }

        stage('Teardown') {
            steps {
                sh '''
                    docker stop flask-todo-app || true
                    docker rm flask-todo-app || true
                '''
            }
        }
    }

    post {
        always {
            script {
                def recipient = env.GIT_COMMITTER_EMAIL ?: 'qasimalik@gmail.com'
                mail(
                    to: recipient,
                    subject: "Test Results: ${currentBuild.fullDisplayName}",
                    body: "Build: ${env.BUILD_URL}\nStatus: ${currentBuild.currentResult}\nBranch: ${env.GIT_BRANCH}\nCommit: ${env.GIT_COMMIT}"
                )
            }
        }
    }
}