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
        stage('Build image') {
            steps {
                sh 'docker build -t $IMAGE:$BUILD_NUMBER -t $IMAGE:latest .'
            }
        }
        stage('Push to Docker Hub') {
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
    }

    post {
        always {
            sh 'docker logout || true'
        }
    }
}
