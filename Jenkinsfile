pipeline {
    agent any

    environment {
        PATH  = "/usr/local/bin:/opt/homebrew/bin:${env.PATH}"
        IMAGE = "katef20/urfu-isd"
    }

    triggers {
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Lint') {
            steps {
                sh '''
                  docker run --rm -v "$PWD":/app -w /app python:3.12-slim sh -c "
                    pip install -q flake8 &&
                    flake8 --exclude=.venv,.git,__pycache__,.idea --max-line-length=120 .
                  "
                '''
            }
        }
        stage('Unit tests') {
            steps {
                sh '''
                  docker run --rm -v "$PWD":/app -w /app python:3.12-slim sh -c "
                    pip install -q -r requirements.txt &&
                    python -m pytest -v
                  "
                '''
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE:$BUILD_NUMBER -t $IMAGE:latest .'
            }
        }
        stage('Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub',
                                                  usernameVariable: 'DH_USER',
                                                  passwordVariable: 'DH_TOKEN')]) {
                    sh 'echo "$DH_TOKEN" | docker login -u "$DH_USER" --password-stdin'
                    sh 'docker push $IMAGE:$BUILD_NUMBER'
                    sh 'docker push $IMAGE:latest'
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker rm -f urfu-isd-app || true'
                sh 'docker run -d --name urfu-isd-app -p 8000:8000 $IMAGE:latest'
            }
        }
    }

    post {
        always {
            sh 'docker logout || true'
        }
    }
}
