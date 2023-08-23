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
        IMAGE_VERSION = ""
        TAGNAME = "production-version" //change later to the branch name and then name the tags like "<branch>-release"
        TAGDESCRIPTION = ""
    }

    stages {
        stage('setup image tag') {
            steps{
                script {
                	sh "git config --global --add safe.directory ${sh(script: "pwd", returnStdout: true)}"
                    TAGDESCRIPTION = sh(script: "git tag -l -n99 --format='%(contents)' ${env.TAGNAME}", returnStdout: true).trim()
                    IMAGE_VERSION = "${TAGDESCRIPTION}-dev"
                }
            }
        }
        stage('Build image') {
            steps {
                echo 'Starting to build docker image'
                sh "docker build -t $DOCKERHUB_CREDENTIALS_USR/aks-app-jenkins-test:${IMAGE_VERSION} ."
            }
        }
        stage('login to dockerhub') {
            steps{
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('push') {
            steps{
                sh "docker push $DOCKERHUB_CREDENTIALS_USR/aks-app-jenkins-test:${IMAGE_VERSION}"
            }
        }
    }
    post {
        always {
            sh 'docker logout'
        }
    }
}