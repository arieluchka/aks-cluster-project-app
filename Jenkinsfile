podTemplate(containers: [
    containerTemplate(
        name: 'docker-test', 
        image: 'docker:latest',
	command: 'sleep',
	args: '999999'
        )
  ]) {

    node(POD_LABEL) {
        stage('Get docker version') {
            container('docker-test') {
                stage('Shell Execution') {
                    sh '''
                    docker --version
                    '''
                }
            }
        }

    }
}