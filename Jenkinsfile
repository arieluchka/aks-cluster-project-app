podTemplate(containers: [
    containerTemplate(
        name: 'docker-test', 
        image: 'docker:latest'
        )
  ]) {

    node(POD_LABEL) {
        stage('Get docker version') {
            container('docker') {
                stage('Shell Execution') {
                    sh '''
                    echo "Hello! I am executing shell"
                    '''
                }
            }
        }

    }
}