node('CAE-Jenkins2-DH-Agents-Linux') {
    stages {
        stage('Checkout') {
            checkout scm
        }

        def customImage = docker.build("my-image:${env.BUILD_ID}")

        customImage.inside {
            stage('Test') {
                sh 'python setup.py test'{
            }
        }
    }
}
