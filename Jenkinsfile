pipeline {
    agent {
        kubernetes {
        label 'docker-image-build'
        idleMinutes 5
        yamlFile 'build-pod.yaml'
        defaultContainer 'dind'
        }
    }
    // options { skipDefaultCheckout() }
    environment{
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
        IMAGE_VERSION = ""
        VERSION = "${env.BUILD_ID}-${env.GIT_COMMIT}"
        TAGNAME = "main_release"
        TAGDESCRIPTION = ""
        GIT_URL_TEST = "${REPO_URL}"
        PWD = ""
    }

    stages {
        // stage('Checkout') {
        //     steps {
        //         script{
        //             def repoUrl = env.
        //         }
        //     }
        // }
        stage('setup image tag') {
            // agent {
            //     kubernetes {
            //     label 'git-tag-build'
            //     idleMinutes 5
            //     yamlFile 'git-pod.yaml'
            //     defaultContainer 'git-tags'
            //     }
            // }
            // options { skipDefaultCheckout() }
            steps{
                script {
                    // PWD = sh(script: "pwd", returnStdout: true)
                	sh "git config --global --add safe.directory ${sh(script: "pwd", returnStdout: true)}"
                    TAGDESCRIPTION = sh(script: "git tag -l -n99 --format='%(contents)' ${env.TAGNAME}", returnStdout: true).trim()
                    IMAGE_VERSION = "${TAGDESCRIPTION}.0.0"
                    echo "${IMAGE_VERSION}"
                    // sh "git config --global --add safe.directory /home/jenkins/agent/workspace/aks-pipeline_main"
                    // sh "git tag -l -n99 --format='%(contents)' ${env.TAGNAME}"
                    // echo "git tag -l -n99 --format='%(contents)' ${env.TAGNAME}"
                    // TAGDESCRIPTION = sh(script: "git tag -l -n99 --format='%(contents)' ${env.TAGNAME}", returnStdout: true).trim()
                }
            }
        }



        stage('Build image') {
            steps {
                checkout scm
                echo 'Starting to build docker image'
                echo "${env.VERSION} test"  
                echo "${GIT_URL}"              
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