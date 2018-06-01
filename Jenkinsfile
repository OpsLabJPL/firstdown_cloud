node('CAE-Jenkins2-DH-Agents-Linux') {
    checkout scm
    def customImage = docker.build("my-image:${env.BUILD_ID}")
    customImage.inside {
        sh 'python setup.py test'{
    }
}
