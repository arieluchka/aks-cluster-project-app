pipeline {
    agent {
        kubernetes {
        label 'promo-app'
        idleMinutes 5
        yamlFile 'build-pod.yaml'
        defaultContainer 'ez-docker-helm-build'
        }
    }
    stages {
        stage('Build image') {
            steps {
                echo 'Starting to build docker image'
                sh "docker build -t test-python ."
            }
        }
    }
}
