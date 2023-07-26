podTemplate(containers: [
    containerTemplate(
        name: 'docker-test', 
        image: 'docker:latest',
	command: 'sleep',
	args: '999999'
        )
  ]) {

    node(docker) {
        stage('Get docker version') {
            container('docker-test') {
                stage('Shell Execution') {
                    sh '''
                    echo "Hello! I am executing shell"
                    '''
                }
            }
        }

    }
}