pipeline {
    agent {
        kubernetes {
        label 'docker-image-build'
        idleMinutes 5
        yamlFile 'build-pod.yaml'
        defaultContainer 'dind'
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
