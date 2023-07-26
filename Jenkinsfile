podTemplate(containers: [
    containerTemplate(
        name: 'docker-test', 
        image: 'docker:dind',
	command: 'sleep',
	args: '999999',
        securityContext: [privileged: true]
        )
  ]) {

    node(POD_LABEL) {
        stage('Get docker version') {
            container('docker-test') {
                stage('Shell Execution') {
                    sh "docker --version"
		    sh "sudo service docker status"
		    sh "sudo service docker start"
		    echo 'Starting to build docker image'
                    sh "docker build -t test-of-build ."
                }
            }
        }

    }
}