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
                    docker stop $APP_CONTAINER || true
                    docker rm $APP_CONTAINER || true
                    docker build -t flask-todo-app .
                    docker run -d --name $APP_CONTAINER -p $APP_PORT:5000 flask-todo-app
                    sleep 5
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    docker build -f Dockerfile.test -t $TEST_IMAGE .
                    docker run --rm \
                        --network host \
                        -e BASE_URL=http://localhost:5000 \
                        $TEST_IMAGE
                '''
            }
        }

        stage('Teardown') {
            steps {
                sh '''
                    docker stop $APP_CONTAINER || true
                    docker rm $APP_CONTAINER || true
                '''
            }
        }
    }

    post {
        always {
            mail to: "${env.GIT_COMMITTER_EMAIL ?: 'qasimalik@gmail.com'}",
                 subject "Test Results: ${currentBuild.fullDisplayName}",
                 body: """
Build: ${env.BUILD_URL}
Status: ${currentBuild.currentResult}
Branch: ${env.GIT_BRANCH}
Commit: ${env.GIT_COMMIT}
                 """
        }
    }
}
