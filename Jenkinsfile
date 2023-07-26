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
                    git "https://github.com/arieluchka/aks-cluster-project-app"
                    '''; ls
                }
            }
        }

    }
}