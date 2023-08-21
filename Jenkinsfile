pipeline {
    agent {
        kubernetes {
        label 'docker-image-build'
        idleMinutes 5
        yamlFile 'build-pod.yaml'
        defaultContainer 'dind'
        }
    }
    environment{
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
        VERSION = "${env.BUILD_ID}-${env.GIT_COMMIT}"
    }

    stages {
        stage('Build image') {
            steps {
                echo 'Starting to build docker image'
                echo "${env.VERSION} test"                
                sh "docker build -t arieluchka/aks-app-jenkins-test:test ."
            }
        }
        stage('login to dockerhub') {
            steps{
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('push') {
            steps{
                sh 'docker push arieluchka/aks-app-jenkins-test:test'
            }
        }
    }
    post {
        always {
            sh 'docker logout'
        }
    }
}