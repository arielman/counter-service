pipeline {
    agent { any } 
    stages {
        stage('Example Build') {
            steps {
                sh 'sudo docker build . -t arielma2304/my-repo:latest'
            }
        }
    }
}
